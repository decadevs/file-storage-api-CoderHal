# pulling base image
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY /filestore .
# ensure that latest version of pip is used 
RUN pip install --upgrade pip

# install dependencies from requirement file
ADD requirements.txt .
RUN pip install -r requirements.txt

# to expose port
# EXPOSE 8000

# to specify working directory
# CMD python manage.py runserver 0.0.0.0:8100