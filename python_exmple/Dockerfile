FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY rest_app.py /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8181 available to the world outside this container
EXPOSE 8181

# Run app.py when the container launches
CMD ["python", "rest_app.py"]
