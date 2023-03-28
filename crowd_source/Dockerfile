FROM python:3.10.0-alpine

RUN pip install --upgrade pip

COPY ./crowd_server /app

WORKDIR /app

RUN pip install -r ./requirements/local.txt

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

