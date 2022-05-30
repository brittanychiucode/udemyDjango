# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN export PYTHONPATH="$PYTHONPATH:/usr/src/app"

# install dependencies (needs internet so commented out)
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
# COPY . .

EXPOSE 3000
EXPOSE 8000

# RUN python3 manage.py migrate
# ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
