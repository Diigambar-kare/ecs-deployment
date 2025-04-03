# Use the official Python image from the Docker Hub
#FROM python:3.9-slim

# Set the working directory inside the container
#WORKDIR /app

# Copy your application files into the container
#COPY . /app

# Install the required dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install prometheus_client
#RUN pip install loguru  # Install loguru instead of loki-logger
#RUN pip install requests
# Expose the Prometheus metrics port
#EXPOSE 8000

# Run the Python script
#CMD ["python3", "test.py"]


# Use a specific Python version from the Docker Hub
 FROM python:3.9-alpine


# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker's cache
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies (prometheus_client, loguru, requests)
RUN pip install --no-cache-dir prometheus_client loguru requests

# Copy your application files into the container
COPY . /app/

# Expose the Prometheus metrics port
EXPOSE 8000

# Run the Python script
CMD ["gunicorn", "blue:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--workers", "2"]

