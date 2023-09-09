# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./docker/tests/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
