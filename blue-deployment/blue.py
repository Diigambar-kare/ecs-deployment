import time
import datetime
import logging
import random
from prometheus_client import start_http_server, Counter
from fastapi import FastAPI

app=FastAPI()

# Setup logging configuration to log to a file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='/var/log/my_python_app.log')

# Prometheus counters
hai_counter = Counter('hai_prints_total', 'Total number of times "Hai" was printed')
error_counter = Counter('api_errors_total', 'Total number of API errors')


@app.get("/")
def health_check():
    return{"status":"ok"}



