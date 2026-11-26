# Use the official Python image as the base image.
FROM python:3.8

# Set the working directory.
WORKDIR /usr/src/app

# Copy the Python script into the container.
COPY memory_usage.py ./

# Run the script when the container starts.
CMD ["python", "./memory_usage.py"]

