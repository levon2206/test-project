# Simple Python App

Python simple webserver.

## Project Description

Python code defines a  simple example of a Python project with a PostgreSQL database and a basic interface using the Tkinter library. This example demonstrates a simple address book application that allows you to add, view, and delete contacts.
## Features

- /health - return HEALTHY
- / - main interface
- /metrics -- endpoint for metrics
### Prerequisites

List any prerequisites.

- python3
- docker

### Installation

Run Project Manually.

```bash
pip3 install flask flask_restful requests psycopg2 prometheus_client requests
python3 hello.py
```
Run Project use docker.

```bash
docker build -t simple-app:v1 .
docker run -d -p 5050:5050 simple-app:v1

```
Access App in 127.0.0.1:5050