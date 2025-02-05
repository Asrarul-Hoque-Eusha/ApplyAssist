import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

from dotenv import load_dotenv
load_dotenv()
import os
os.environ["USER_AGENT"]

from chains import Chain
from portfolio import Portfolio
from text_cleaning import clean_text
from mail_cv_letter import Profile


def create_streamlit_app(llm, profile, clean_text):
    st.title("📧 Mail and Cover Letter Generator")
    url_input = st.text_input("Enter a Job Post URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            #portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            #st.code(jobs, language='markdown')
            #st.code(len(jobs))
            for job in jobs:
                skills = job.get('skills', [])
                #links = portfolio.query_links(skills)

                email, coverletter = llm.write_mail(job, profile.mail_body, profile.cover_letter, profile.cv)
                st.code(email, language='markdown')
                st.code(coverletter, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    #portfolio = Portfolio()
    profile = Profile()
    create_streamlit_app(chain, profile, clean_text)

