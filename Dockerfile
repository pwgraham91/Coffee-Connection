FROM python:3.7
 
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000
ENTRYPOINT ["python", "run.py"]
 

