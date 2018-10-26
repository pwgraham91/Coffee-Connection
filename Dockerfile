FROM python:3.7-alpine

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt && \
 apk --purge del .build-deps
#RUN pip install -r requirements.txt  (for python:3.7-slim)
ENV FLASK_ENV="docker"
EXPOSE 5000
ENTRYPOINT ["python", "run.py"]
