# Dockerized Python Application

## Overview

This project demonstrates a simple Dockerized Python application using the official Python 3.12 Slim image as the base image.

The application prints:

* The Python version running inside the container
* The current date and time

## Project Structure

docker-python-app/

├── app.py

├── Dockerfile

├── requirements.txt

├── README.md

└── screenshots/

    └── output.png

## Python Script

The Python script uses:

* `sys` module to display the Python version
* `datetime` module to display the current date and time

## Base Image

This project uses:

python:3.12-slim

## Build the Docker Image

Run the following command from the project directory:

```bash
docker build -t python-version-app .
```

## Run the Docker Container

```bash
docker run python-version-app
```

## Sample Output

```text
Python Version: 3.12.12 (main, ...)
Current Date and Time: 2026-06-22 22:15:30
```


## Docker Commands Used

Build Image:

```bash
docker build -t python-version-app .
```

Run Container:

```bash
docker run python-version-app
```

List Images:

```bash
docker images
