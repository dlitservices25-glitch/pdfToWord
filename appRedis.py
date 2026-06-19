import streamlit as st
import requests

st.title("📄 PDF → DOCX (RQ + Redis)")

file = st.file_uploader("Upload PDF")

if file and st.button("Submit"):

   res = requests.post(
       "http://localhost:8000/upload",
       files={"file": file.getvalue()}
   )

   data = res.json()

   st.write(data)

   if "rq_job_id" in data:
        st.success(f"Job submitted: {data['rq_job_id']}")
        job_id = data["rq_job_id"]
   else:
        st.error("rq_job_id not found")

   
   st.write(data)

   if st.button("Check status"):

       status = requests.get(
           f"http://localhost:8000/status/{job_id}"
       ).json()

       st.write(status)
