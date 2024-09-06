# Use the official Python slim image as the base
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Create an output directory inside the container
RUN mkdir -p /app/output

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install  -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Specify the command to run your application
CMD ["python", "GetFiles.py"]
