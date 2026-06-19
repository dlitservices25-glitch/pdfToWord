from redis import Redis
from rq import Worker, Queue

redis_conn = Redis(host='localhost', port=6379)

queues = [Queue('default', connection=redis_conn)]

worker = Worker(queues, connection=redis_conn)
worker.work()