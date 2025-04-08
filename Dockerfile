# Use an official Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy all project files to container
COPY . .

# Set default command to run your app
CMD ["python", "main.py"]

