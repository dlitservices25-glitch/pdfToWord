from fastapi import FastAPI
from rq.job import Job
from redis import Redis

app = FastAPI()

redis_conn = Redis()

@app.get("/status/{job_id}")
def status(job_id: str):
    try:
        job = Job.fetch(job_id, connection=redis_conn)

        return {
            "status": job.get_status(),
            "result": job.result
        }

    except Exception as e:
        return {
            "status": "not_found",
            "error": str(e)
        }