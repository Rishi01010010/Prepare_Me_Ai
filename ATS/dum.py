import os
import PyPDF2
import google.generativeai as genai
genai.configure(api_key="AIzaSyAH3nXug262foRug7tPKQHePBXuImgOulM") 
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 10000,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
chat_session = model.start_chat(history=[])

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

pdf_path = r"D:\My_Resume - Standard.pdf"
resume_text = pdf_to_text(pdf_path)
job_descr = """About the job
Greetings,

We have immediate opportunity for Node Js Developer – 5 to 10 years
Synechron– Bangalore, BCIT

Job Role: Node Js Developer
Job Location: Bangalore, BCIT

About Company:

At Synechron, we believe in the power of digital to transform businesses for the better. Our global consulting firm combines creativity and innovative technology to deliver industry-leading digital solutions. Synechron’s progressive technologies and optimization strategies span end-to-end Artificial Intelligence, Consulting, Digital, Cloud & DevOps, Data, and Software Engineering, servicing an array of noteworthy financial services and technology firms. Through research and development initiatives in our FinLabs we develop solutions for modernization, from Artificial Intelligence and Blockchain to Data Science models, Digital Underwriting, mobile-first applications and more. Over the last 20+ years, our company has been honoured with multiple employer awards, recognizing our commitment to our talented teams. With top clients to boast about, Synechron has a global workforce of 14,700+, and has 48 offices in 19 countries within key global markets. For more information on the company, please visit our website or LinkedIn community.

Diversity, Equity, and Inclusion

Diversity & Inclusion are fundamental to our culture, and Synechron is proud to be an equal opportunity workplace and an affirmative-action employer. Our Diversity, Equity, and Inclusion (DEI) initiative ‘Same Difference’ is committed to fostering an inclusive culture – promoting equality, diversity and an environment that is respectful to all. We strongly believe that a diverse workforce helps build stronger, successful businesses as a global company. We encourage applicants from across diverse backgrounds, race, ethnicities, religion, age, marital status, gender, sexual orientations, or disabilities to apply. We empower our global workforce by offering flexible workplace arrangements, mentoring, internal mobility, learning and development programs, and more.
All employment decisions at Synechron are based on business needs, job requirements and individual qualifications, without regard to the applicant’s gender, gender identity, sexual orientation, race, ethnicity, disabled or veteran status, or any other characteristic protected by law.
JOB DESCRIPTION

Excellent knowledge developing scalable and highly-available Restful APIs using NodeJS technologies and unit test cases using jest framework.
Practical experience with GraphQL, Kafka and Redis.
Well versed with CI/CD principles, and actively involved in solving, troubleshooting issues in distributed services ecosystem
Good understanding of Redhat OpenShift (OCP)
Understanding of containerization, experienced in Dockers , Kubernetes.
Exposed to API gateway integrations like 3Scale.
Understanding of Single-Sign-on or token based authentication (Rest, JWT, oAuth)

If you find this this opportunity interesting kindly share your updated profile on bansi.hindocha@syncheron.com


With below details (Mandatory)
Total Experience
Experience in Node Js-
Experience in Express Js -
Experience in Micro Services-
Experience in Kafka-
Experience in Mongo DB-
Current CTC-
Expected CTC-
Notice period-
Current Location-
Ready to relocate to Bangalore-

If you had gone through any interviews in Synechron before? If Yes when

Regards,
Bansi Hindocha
bansi.hindocha@syncheron.com
"""

resume_prompt = f"""
list only the skill sets mentioned in the following resume. Do not include any introductory sentences or additional information.

Resume:\n{resume_text}\nPlease ensure the output includes only the skill sets mentioned in the resume one below the other.

format the output as the below format.
"C Programming Language
Python Programming Language
Java Programming Language
Network Programming using Python
Discrete Mathematics (DSA)
HTML
CSS (Vanilla & Frameworks)
JavaScript
Node.js
Express.js
SQL Database Management System
MongoDB NoSQL Database Management System
React.js JavaScript Library
Microsoft Office Suite (Word, Excel, PowerPoint, Project)"
"""

resume_skill_response = chat_session.send_message(resume_prompt)
resume_skill = resume_skill_response.text
resume_skills_set = set(skill.strip() for skill in resume_skill.split("\n") if skill.strip())
no_resume_skills = len(resume_skills_set)
print(f"Skills in the resume:\n{'\n'.join(resume_skills_set)}\nNumber of skills in resume: {no_resume_skills}")


job_descr_prompt = f"""
go through the below job description and list down all the skills that are mentioned. Do not include any introductory sentences or additional information.

job description: \n{job_descr}\nPlease ensure the output includes only the skill sets mentioned in the job description one below the other.

format the output as the below format.
"C Programming Language
Python Programming Language
Java Programming Language
Network Programming using Python
Discrete Mathematics (DSA)
HTML
CSS (Vanilla & Frameworks)
JavaScript
Node.js
Express.js
SQL Database Management System
MongoDB NoSQL Database Management System
React.js JavaScript Library
Microsoft Office Suite (Word, Excel, PowerPoint, Project)"
"""

job_descr_skill_response = chat_session.send_message(job_descr_prompt)
job_descr_skill = job_descr_skill_response.text
job_descr_skill_set = set(skill.strip() for skill in job_descr_skill.split("\n") if skill.strip())
no_job_descr_skill= len(job_descr_skill_set)
print(f"Skills in the job descr: {'\n'.join(job_descr_skill_set)}\n Number of skills in job descr: {no_job_descr_skill}")

lack_prompt = f"""
compare the skills mentioned in the resume and the job description and list down the skills which are present in the job description but not in the resume.

Resume Skills: \n{resume_skill}
Job Description Skills: \n{job_descr_skill}

Provide the response in the below format:

"C Programming Language
Python Programming Language
Java Programming Language
Network Programming using Python
Discrete Mathematics (DSA)
HTML
CSS (Vanilla & Frameworks)
JavaScript
Node.js
Express.js
SQL Database Management System
MongoDB NoSQL Database Management System
React.js JavaScript Library
Microsoft Office Suite (Word, Excel, PowerPoint, Project)"
"""
lack_skill_response = chat_session.send_message(lack_prompt)
lack_skill = lack_skill_response.text
lack_skills_set = set(skill.strip() for skill in lack_skill.split("\n") if skill.strip())
no_lack_skills = len(lack_skills_set)
print(f"Skills in the lack: {'\n'.join(lack_skills_set)}\n Number of skills in lack: {no_lack_skills}")

extra_prompt = f"""
compare the skills mentioned in the resume and the job description and list down the skills which are present in the resume but not in the job description.

Resume Skills: \n{resume_skill}
Job Description Skills: \n{job_descr_skill}

Provide the response in the below format:

"C Programming Language
Python Programming Language
Java Programming Language
Network Programming using Python
Discrete Mathematics (DSA)
HTML
CSS (Vanilla & Frameworks)
JavaScript
Node.js
Express.js
SQL Database Management System
MongoDB NoSQL Database Management System
React.js JavaScript Library
Microsoft Office Suite (Word, Excel, PowerPoint, Project)"
"""
extra_skill_response = chat_session.send_message(extra_prompt)
extra_skill = extra_skill_response.text
extra_skills_set = set(skill.strip() for skill in extra_skill.split("\n") if skill.strip())
no_extra_skills = len(extra_skills_set)
print(f"Skills in the extra: {'\n'.join(extra_skills_set)}\n Number of skills in extra: {no_extra_skills}")

matched_prompt = f"""
compare the skills mentioned in the resume and the job description and list down the skills which are present in both the resume and also in the job description.

Resume Skills: \n{resume_skill}
Job Description Skills: \n{job_descr_skill}

Provide the response in the below format:

"C Programming Language
Python Programming Language
Java Programming Language
Network Programming using Python
Discrete Mathematics (DSA)
HTML
CSS (Vanilla & Frameworks)
JavaScript
Node.js
Express.js
SQL Database Management System
MongoDB NoSQL Database Management System
React.js JavaScript Library
Microsoft Office Suite (Word, Excel, PowerPoint, Project)"
"""
matched_skill_response = chat_session.send_message(matched_prompt)
matched_skill = matched_skill_response.text
matched_skills_set = set(skill.strip() for skill in matched_skill.split("\n") if skill.strip())
no_matched_skills = len(matched_skills_set)
print(f"Skills in the matched: {'\n'.join(matched_skills_set)}\n Number of skills in matched: {no_matched_skills}")

def compare_skills(matched_skills_set, job_descr_skill_set):
    return (len(matched_skills_set) / len(job_descr_skill_set)) * 100
    
percentage_match = compare_skills(matched_skills_set, job_descr_skill_set)
print(f"ATS score: {percentage_match}")