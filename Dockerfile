# base image
FROM python:3.10-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# create and set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project files to working directory
COPY . /app/

# run the application
CMD ["python", "app.py"]
