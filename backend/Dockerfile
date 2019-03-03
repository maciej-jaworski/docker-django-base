FROM python:3.7.2-alpine3.9

RUN apk update && apk add --upgrade --no-cache \
    # To install psycopg2 from source properly
    postgresql-client \
    postgresql-dev \
    gcc \
    libc-dev \
    libffi-dev \
    # Bash just for convenience
    bash \
    # To install Pillow
    jpeg-dev \
    zlib-dev \
    make

RUN easy_install pip

ADD . /code/
WORKDIR /code/
RUN pip install --upgrade pip && pip install -r requirements.pip

CMD python manage.py runserver 0.0.0.0:8000
