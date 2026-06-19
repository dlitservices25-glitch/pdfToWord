from redis import Redis
from rq import Queue
from tasks import test_function

redis_conn = Redis(host="127.0.0.1", port=6379)
queue = Queue("pdf_jobs", connection=redis_conn)


#que and test a job or task
job = queue.enqueue(test_function)

print("JOB ID:", job.id)