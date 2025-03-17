# Use a lightweight Python image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /DockerApp

# Install system dependencies required for mysqlclient
RUN apk add --no-cache \
    python3-dev \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    libffi-dev \
    pkgconfig

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
COPY . /DockerApp
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
