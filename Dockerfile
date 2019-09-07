# Pull the base image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work dir
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile /code/
RUN pipenv install --skip-lock --system --dev

# Copy current dir project and paste into WORKDIR inside the docker
COPY . /code/

