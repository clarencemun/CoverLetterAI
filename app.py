from openai import OpenAI
import streamlit as st

#OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

with st.form("my_form"):
   st.write("This tool leverages OpenAI's ChatGPT 3.5-Turbo to generate a cover letter, based on your resume and a job description that you paste in.")
   

   col1, col2 = st.columns(2)

   with col1:
      resume = st.text_area("Your resume", max_chars=10000)

   with col2:
      jobDescription = st.text_area("Job description", max_chars=10000)

   submitted = st.form_submit_button("Generate")
   if submitted:
         completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
               {"role": "system", "content": "You are a management consulunt at a top-tier firm, skilled at writing cover letters."},
               {"role": "user", "content": "Based on the following resume:" + resume + ", and the following job desctiption:" + jobDescription + "write me a cover letter of no more than 10 sentences total for the specific role in the job description, leveraging information from my resume."},
            ])         
         st.write(completion.choices[0].message.content)
