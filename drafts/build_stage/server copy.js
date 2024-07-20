const express = require('express');
const fileUpload = require('express-fileupload');
const { spawn } = require('child_process');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();

app.use(fileUpload());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'frontend')));
app.use(bodyParser.json());  // Middleware to parse JSON bodies

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
            res.json({ concepts: output });
        });
    });
});


// Endpoint to get the explanation of a concept
app.get('/explain', (req, res) => {
    const { concept, concatenated_text } = req.query;

    const process = spawn('python', ['backend/topicexplain.py', concept, concatenated_text]);
    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.on('close', (code) => {
        // Remove all instances of "**" from the output
        const cleanedOutput = output.replace(/\*\*/g, '');
        res.json({ explanation: cleanedOutput });
    });
});




app.post('/chat', (req, res) => {
    const { question, concept, text, explanation } = req.body;

    const process = spawn('python', ['backend/doubtchat.py', text, concept, explanation, question]);
    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.on('close', (code) => {
        res.json({ answer: output });
    });
});

app.post('/test', (req, res) => {
    const { numQuestions, type, level, concept } = req.body;

    const process = spawn('python', ['backend/qanda.py', numQuestions, type, level, concept]);
    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.on('close', (code) => {
        res.json({ questions: output.split('\n').filter(q => q) });
    });
});

app.post('/evaluate', (req, res) => {
    const { answers } = req.body;

    const process = spawn('python', ['backend/evaluate.py'], {
        stdio: ['pipe', 'pipe', 'pipe']
    });

    process.stdin.write(JSON.stringify(answers));
    process.stdin.end();

    let output = '';

    process.stdout.on('data', (data) => {
        output += data.toString();
    });

    process.on('close', (code) => {
        res.json({ evaluation: output });
    });
});
app.listen(3001, () => {
    console.log('Server is running on port 3000');
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
