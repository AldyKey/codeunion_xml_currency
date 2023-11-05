FROM python:3.11-bullseye

# Install dependencies required for psycopg2 python package
# RUN apk update && apk add libpq
# RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

CMD gunicorn -b 0.0.0.0:$CONTAINER_PORT project.wsgi