from fastapi import FastAPI, UploadFile, File
from que import queue
from worker import convert_pdf_job
import uuid
import tempfile

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
   job_id = str(uuid.uuid4())

   with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
       tmp.write(await file.read())
       pdf_path = tmp.name

   job = queue.enqueue(convert_pdf_job, pdf_path)

   return {
       "job_id": job_id,
       "rq_job_id": job.get_id()
   }
