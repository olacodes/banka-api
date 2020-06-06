FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Upgrade pip
RUN pip install --upgrade pip

# Install requirements
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

# create woking directory
RUN mkdir /banka-api
WORKDIR /banka-api

# Copy application to working directory
COPY ./banka ./

CMD [ "bin/bash" ]
