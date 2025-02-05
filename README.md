# Customized Mail and Cover Letter Generator for Job Application

This is a Apply Assistant website. It takes a URL of job posting and generates customized mail and cover letter for you which aligns with the job description extracted from the URL given. Here are some prerequisites - you should upload some of your previously written cover letter, mail body and finally your cv to get more information about you. It contains a single page,

The only page takes a job URL from you as input. The it performs several steps to give you the customized cover letter and mail body as output. The steps are given below:

 - Whenever the application is started it automatically stores all the provided cover letters and mails into the vector database with their embedding.
 - Extracts the job description from the provided URL and the description passed through the LLM (Llama3.3) to extract only useful informations like skills, experience, role etc in json format.
 - Then the most relevant cover letter and mail are retrieved from the vector database collections.
 - Read the cv of the applicant to get more context about the applicant. Which helps the LLM to generate more contextual outputs.
 - Retrieved cover letter and mail are used as the format to follow by the LLM while generating response.
 - Then the refined job description, cv, relevant cover letter and mail are provided to the LLM to generate custom cover letter and mail for the job description given.


## How to use this website
Just upload all your cover letters and job mails (mail body written while job application) available and a cv. Then run the application and give a URL to the URL input field. Now hit the submit button it will take a while to complete all the steps. Within minutes you will get a customized cover letter and mail to apply for the job post.

## How to install in your local device
`git clone <Clone url link>`

Then go to the folder and open it using VScode. Then open command prompt in VScode and run - `pip install -r requirements.txt`

Now run cd app Then run `streamlit run main.py`

N.B: Don't forget to create an account in Groq-cloud and get your own API KEY and put it in the `.env` file.

## Tech Stack Used
1. Front-End: StreamLit
2. Back-End: Python, LangChain, and Groq-cloud
3. Server-Side: Chromadb as vector database
