# official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy your application and data files into the container
COPY app.py seattle-weather.csv /app/

# Install required Python packages
RUN pip install Flask

# Expose the port that your Flask app will run on
EXPOSE 5000

# Command to run your Flask application
CMD ["python", "app.py"]
