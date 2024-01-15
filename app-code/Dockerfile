FROM --platform=linux/amd64 python:3.8
### Use --platform=linux/amd64 if you build image in Macbook M* proccessor
WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    pip install --upgrade pip && \
    pip install Flask psycopg2 prometheus_client flask_restful requests

COPY . .
EXPOSE 5050
CMD ["python3", "/app/app.py"]
