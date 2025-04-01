import time
import datetime
import logging
import random
from prometheus_client import start_http_server, Counter
from fastapi import FastApi

app=FastApi()

# Setup logging configuration to log to a file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='/var/log/my_python_app.log')

# Prometheus counters
hai_counter = Counter('hai_prints_total', 'Total number of times "Hai" was printed')
error_counter = Counter('api_errors_total', 'Total number of API errors')


@app.get("/")
def health_check():
    return{"status":"ok"}


def main():
    # Start Prometheus HTTP server on port 8000
    start_http_server(8000)
    logging.info("Prometheus metrics server started on port 8000")
    
    while True:
        current_time = datetime.datetime.now().isoformat()
        message = f"Hai {current_time}"
        logging.info(message)
        
        # Increment "Hai" counter by 20 for each iteration
        hai_counter.inc(20)

        # Random chance of simulating an API error
        if random.random() < 0.3:  # 30% chance of error
            api = random.choice(["API_A", "API_B", "API_C"])
            error_message = f"Error in {api} at {current_time}"
            logging.error(error_message)
            
            # Increment error counter by 1
            error_counter.inc()

        # Sleep for 20 seconds before the next loop
        time.sleep(20)

if __name__ == "__main__":
    main()

