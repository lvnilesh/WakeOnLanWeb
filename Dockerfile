FROM python:3.9-slim

# Install sshpass and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	sshpass \
	openssh-client \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN groupadd -r cloudgenius && useradd -r -g cloudgenius cloudgenius
RUN mkdir -p /home/cloudgenius/.ssh
RUN chown -R cloudgenius:cloudgenius /home/cloudgenius

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

RUN chown -R cloudgenius:cloudgenius /app

# Switch to the non-root user
USER cloudgenius

# Expose the port the app runs on
EXPOSE 5090

# Set the environment variable for Flask
ENV FLASK_APP=app/__init__.py

# Command to run the application
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:5090", "app:app"]
