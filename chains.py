import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `company name`,role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, mail_body, coverletter, cv):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            #### GUIDELINES:
            If experience in cv don't met the experience in job description say "this is not best fit for you" instead of generating mail as response. 
            ### INSTRUCTION:
            You are Asrarul Hoque Eusha, an aspiring Software Engineer. Who is looking for the opportunity across different software companies in the machine learning, software developer, and data scientiest positions.
            Currently working as a Trainee software engineer (AI/ML) in BJIT a prominent company in bangladesh and gained hand on experience in ML application development. Having knowledge of FastAPI, Springboot, Docker, etc.  
            You can find more information about your cv: {cv}. So find out your strong zones and capabilities to highlight.
            Your job is to write a email to the client regarding the job mentioned above describing the capability of yourself 
            in fulfilling their needs.
            Also see an example how to write the email to the client in between 150-200 words: {email} Follow the structure of the email provided.
            Remember you are Asrarul Hoque Eusha, Trainee Software Engineer (AI/ML) at BJIT. Completed your graduation from Chittagong University of Engineering and Technology in CSE.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )

        prompt_cover_letter = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            ### GUIDELINES:
            If experience in cv don't met the experience in job description say "this is not best fit for you" instead of generating cover letter.
            ### INSTRUCTION:
            You are Asrarul Hoque Eusha, an aspiring Software Engineer. Who is looking for the opportunity across different software companies in the machine learning, software developer, and data scientiest positions.
            Currently working as a Trainee software engineer (AI/ML) in BJIT a prominent company in bangladesh and gained hand on experience in ML application development. Having knowledge of FastAPI, Springboot, Docker, etc.  
            You can find more information about your cv: {cv}. So find out your strong zones and capabilities to highlight.
            Your job is to write a email to the client regarding the job mentioned above describing the capability of yourself 
            in fulfilling their needs.
            Also see an example how to write the cover letter to the client: {coverletter} Don't forget to follow the format structure.
            Remember you are Asrarul Hoque Eusha, Trainee Software Engineer (AI/ML) at BJIT. Completed your graduation from Chittagong University of Engineering and Technology in CSE. 
            "Asrarul Hoque Eusha 	 
            Present Address: Khilgaon, Dhaka-1219
            Email: asrar2860@gmail.com
            Cell Number: +8801831782860

            04, October 2024
            The Head of Human Resources 
            Divine IT
            Dhaka, Bangladesh
            Subject: Application for the Trainee Software Engineer (Java) at Divine IT." These are the information about you to put on the top of the cover letter.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        chain_coverletter = prompt_cover_letter | self.llm
        email = chain_email.invoke({"job_description": str(job), "email": mail_body, "cv": cv})
        cover_letter = chain_coverletter.invoke({"job_description": str(job), "coverletter": coverletter, "cv": cv})
        return email.content, cover_letter.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))