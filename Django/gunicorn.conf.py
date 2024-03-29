import multiprocessing
import os

DEBUG = os.getenv("DEBUG") == "1"

wsgi_app = "d_party.asgi:application"

bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() * 1 + 1
threads = 2

worker_class = "uvicorn.workers.UvicornWorker"

if DEBUG:
    reload = True
