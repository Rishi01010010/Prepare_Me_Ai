const express = require('express');
const fileUpload = require('express-fileupload');
const { spawn } = require('child_process');
const path = require('path');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');
const app = express();
const os = require('os');
const fs = require('fs');

app.use(fileUpload());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'frontend')));
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true })); // Middleware to parse JSON bodies

app.post('/upload', (req, res) => {
    if (!req.files || !req.files.pdfFile) {
        return res.status(400).send('No file uploaded.');
    }

    const pdfFile = req.files.pdfFile;
    const uploadPath = path.join(__dirname, 'backend', pdfFile.name);

    pdfFile.mv(uploadPath, (err) => {
        if (err) return res.status(500).send(err);

        const process = spawn('python', ['backend/imp_concepts.py', uploadPath]);
        let output = '';

        process.stdout.on('data', (data) => {
            output += data.toString();
        });

        process.on('close', (code) => {
            try {
                const result = JSON.parse(output);
                res.json(result);
            } catch (error) {
                res.status(500).send('Error processing the PDF.');
            }
        });
    });
});



// Endpoint to get the explanation of a concept
app.post('/explain', (req, res) => {
    const { concept, concatenated_text } = req.body;
    console.log('Received concept:', concept);
    console.log('Received concatenated_text length:', concatenated_text.length);

    // Create a temporary file for the concatenated text
    const tempFilePath = path.join(os.tmpdir(), `concatenated_text_${Date.now()}.txt`);
    fs.writeFileSync(tempFilePath, concatenated_text);

    const process = spawn('python', ['backend/topicexplain.py', concept, tempFilePath]);
    let output = '';
    let errorOutput = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });

    process.on('close', (code) => {
        fs.unlinkSync(tempFilePath); // Clean up the temporary file

        if (errorOutput) {
            console.error('Python script error:', errorOutput);
            res.status(500).json({ error: errorOutput });
        } else {
            // console.log('Python script output:', output);
            const cleanedOutput = output.replace(/\*\*/g, '');
            res.json({ explanation: cleanedOutput });
        }
    });

    process.on('error', (err) => {
        console.error('Failed to start subprocess.', err);
        res.status(500).json({ error: 'Failed to start subprocess.' });
    });
});

app.post('/chat', (req, res) => {
    const { question, concept, text, explanation, conversationHistory } = req.body;

    // Create a temporary file for the concatenated text
    const tempFilePath = path.join(os.tmpdir(), `concatenated_text_${Date.now()}.txt`);
    fs.writeFileSync(tempFilePath, text);

    const process = spawn('python', ['backend/doubtchat.py', question, concept, tempFilePath, explanation, conversationHistory]);
    let output = '';
    let errorOutput = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.stderr.on('data', (data) => {
        errorOutput += data.toString();
    });

    process.on('close', (code) => {
        fs.unlinkSync(tempFilePath); // Clean up the temporary file
        res.json({ answer: output });
    });
});

app.post('/test', (req, res) => {
    const { numQuestions, type, level, concept } = req.body;

    if (!numQuestions || !type || !level || !concept) {
        return res.status(400).json({ error: 'Missing required fields' });
    }

    // Validate numQuestions as a positive integer
    if (isNaN(numQuestions) || numQuestions <= 0) {
        return res.status(400).json({ error: 'Invalid number of questions' });
    }

    const process = spawn('python', ['backend/qanda.py', numQuestions, type, level, concept]);
    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    process.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: 'Python script failed' });
        }

        res.json({ questions: output.split('\n').filter(q => q) });
    });
});

app.post('/evaluate', (req, res) => {
    const { concept, answers } = req.body;

    // Format questions and answers
    const questionText = answers.map(a => a.question).join('\n');
    const answerText = answers.map(a => `${a.question}\n${a.answer}`).join('\n\n');

    const fullPrompt = `Evaluate my answers for the below questions.\n\nQuestions:\n\n${questionText}\n\nAnswers:\n\n${answerText}\n\nEvaluate my answers for the correctness and give the following details in the following format:\n\nNumber of correctly answered questions:\nPercentage: (number of correctly answered questions / total number of questions * 100):\n\n...format the response in the below format:\n\n**\n##\n`;

    const process = spawn('python', ['backend/evaluate.py'], {
        stdio: ['pipe', 'pipe', 'pipe']
    });

    process.stdin.write(JSON.stringify({ prompt: fullPrompt }));
    process.stdin.end();

    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.on('close', (code) => {
        res.json({ evaluation: output });
    });
});

app.post('/translate', async (req, res) => {
    console.log("POST /translate route accessed");

    const { input_code: inputCode, input_language: inputLanguage, output_language: outputLanguage } = req.body;

    console.log('Received data:', { inputCode, inputLanguage, outputLanguage });

    const scriptPath = "D:\\Code Translator\\translate.py";

    const options = {
        mode: 'text',
        pythonOptions: ['-u'], // Disable output buffering
        pythonPath: 'python', // Example path to Python executable, adjust as needed
        args: [inputCode, inputLanguage, outputLanguage]
    };

    console.log("start");

    try {
        let results = await PythonShell.run(scriptPath, options);

        if (!results || results.length === 0) {
            console.error('No output received from Python script');
            return res.status(500).send('No output received from Python script');
        }
    
        const translatedCode = results.join('\n').trim();
        console.log('Python script output:', translatedCode);
        res.send(translatedCode);
    } catch (err) {
        console.error('Error executing Python script:', err);
        res.status(500).send('Error during translation');
    }

    console.log("end");
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});



