import multiprocessing
import os

DEBUG = os.getenv("DEBUG") == "1"

wsgi_app = "d_party.asgi:application"

bind = "0.0.0.0:8000"

workers = multiprocessing.cpu_count() * 2 + 1

worker_class = "uvicorn.workers.UvicornWorker"

if DEBUG:
    reload = True
