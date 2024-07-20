import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.1,        # Lower temperature reduces randomness
    "top_p": 1.0,              # Setting top_p to 1 disables nucleus sampling
    "top_k": 0,                # Setting top_k to 0 disables top-k sampling
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(history=[])
ques = """
**
1. RedBoot is a firmware tool developed by which company?
**

**
2. What is the primary purpose of RedBoot?
**

**
3. Which of the following is NOT a feature supported by RedBoot?
**

**
4. What is the main advantage of RedBoot being open source?
**

**
5. What is the role of the HAL in RedBoot?
**

**
6. Which protocol is used for communication with the GNU Debugger (GDB) over serial in RedBoot?
**

**
7. What is the purpose of the "bootp" network standard supported by RedBoot?
**

**
8. What is the main advantage of using RedBoot for flash ROM memory management?
**

**
9. Which of the following operating systems is NOT supported by RedBoot?
**

**
10. What is the purpose of the parameters passed to the Linux kernel upon booting using RedBoot?
**
"""
question = f"""
Evaluate my answers for the below questions.

Questions:

{ques}

"""
ans = """
RedBoot is a firmware tool developed by which company?
Red Hat

What is the primary purpose of RedBoot?
To load and boot an operating system

Which of the following is NOT a feature supported by RedBoot?
Support for only Embedded Linux operating system

What is the main advantage of RedBoot being open source?
It is free to use and modify

What is the role of the HAL in RedBoot?
To abstract the hardware and provide a standard interface

Which protocol is used for communication with the GNU Debugger (GDB) over serial in RedBoot?
X-Modem

What is the purpose of the "bootp" network standard supported by RedBoot?
To obtain network configuration information

What is the main advantage of using RedBoot for flash ROM memory management?
It allows for efficient downloading, updating, and erasing images

Which of the following operating systems is NOT supported by RedBoot?
Windows

What is the purpose of the parameters passed to the Linux kernel upon booting using RedBoot?
To specify the hardware environment and configuration
"""
answer = f"""My answer : 
{ans}

Evaluate my answers for the correctness and give the following details in the following format:

Number of correctly answered questions:
percentage: (number of correctly answered questions / total number of questions * 100):

...
format the response in the below format:
"
##
Question 1:--Incorrect-- RedBoot was developed by MontaVista Software, not Red Hat.
Question 2:--Correct-- RedBoot's primary purpose is to load and boot an operating system.
Question 3:--Incorrect-- RedBoot supports multiple operating systems, not just Embedded Linux. It can boot various operating systems like Linux, VxWorks, and others.
Question 4:--Correct-- Being open source allows for free use, modification, and distribution of RedBoot.
Question 5:--Correct-- The Hardware Abstraction Layer (HAL) in RedBoot provides a standardized interface for interacting with different hardware components.
Question 6:--Incorrect-- The protocol used for communication with GDB over serial in RedBoot is Remote Serial Protocol (RSP), not X-Modem. X-Modem is a file transfer protocol.
Question 7:--Correct-- The "bootp" network standard (Bootstrap Protocol) helps RedBoot obtain network configuration information like IP address, subnet mask, and gateway.
Question 8:--Correct-- RedBoot provides efficient mechanisms for downloading, updating, and erasing images stored in flash ROM memory.
Question 9:--Correct-- RedBoot does not support Windows operating systems. It's primarily designed for embedded systems and Linux-based environments.
Question 10:--Correct-- The parameters passed to the Linux kernel during booting using RedBoot specify the hardware environment, configuration options, and other boot-time settings.

--Explanation of Incorrect Answers:--

Question 1:RedBoot was developed by MontaVista Software, a company specializing in embedded software solutions.
Question 3:RedBoot is designed to be flexible and support various operating systems, not just limited to Embedded Linux.
Question 6:RSP (Remote Serial Protocol) is the standard protocol used for debugging embedded systems over serial connections. It allows GDB to communicate with the target system through RedBoot.

--Key Concepts:

RedBoot:A firmware tool used to boot operating systems on embedded systems. It provides features like network configuration, flash memory management, and debugging capabilities.
Hardware Abstraction Layer (HAL): A layer of software that isolates the operating system from the specific hardware details, providing a standardized interface.
Remote Serial Protocol (RSP): A protocol used for debugging embedded systems over serial connections, allowing GDB to communicate with the target system.
Bootstrap Protocol (BOOTP): A network protocol used to obtain network configuration information for devices during startup.

--Number of correctly answered questions: 7
--percentage: 70%
##
"""
response = (chat_session.send_message(question + answer)).text
# print(question)
print(f"{response}")