FROM python:3.8.2-alpine

WORKDIR /home/akanksha/Desktop/Assignment/BEproject

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
 && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV HOME=/home/akanksha/Desktop/Assignment/BEproject
ENV APP_HOME=/home/akanksha/Desktop/Assignment/BEproject
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/home/akanksha/Desktop/Assignment/BEproject/entrypoint.sh"]
