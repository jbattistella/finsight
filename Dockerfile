# Use a base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script(s) into the container
COPY . .

# Install any dependencies required by your Python script(s)
# Uncomment and modify this line if you have a requirements.txt file
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your Python script
CMD ["python", "jobs/app.py"]

