# Use the official Python slim image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install  -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Specify the command to run your application
CMD ["python", "delete-data.py"]