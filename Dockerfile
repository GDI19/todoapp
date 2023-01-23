FROM python:3.10.6

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./todoapp/ ./

RUN pip3 install -r requir.txt

RUN pip3 install gunicorn