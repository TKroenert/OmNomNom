FROM python:3.6-alpine

WORKDIR /app

RUN mkdir /app/logs && chown -R nobody /app
RUN apk update && apk add gcc musl-dev poppler-utils
ADD dist dist
RUN pip3 install dist/*

USER nobody
ENTRYPOINT ["python3"]
