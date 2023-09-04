# official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the test script into the container
COPY test-app.py /app

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Run the script when the container launches
CMD ["python", "test-app.py"]
