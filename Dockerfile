# Use the official Python image from Docker Hub as the base image
FROM python:3.8-slim-buster
# Set working directory
WORKDIR /app
# Copy
COPY app.py .
# run
CMD [ "python", "app.py" ]