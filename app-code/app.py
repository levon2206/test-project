from flask import Flask, render_template, request, redirect, Response, jsonify
import psycopg2
import os
from prometheus_client import Counter, generate_latest, REGISTRY, Histogram, multiprocess
import configparser

app = Flask(__name__)

# Set the PROMETHEUS_MULTIPROC_DIR environment variable
os.environ['PROMETHEUS_MULTIPROC_DIR'] = '/var/log/'

# Read database connection details from file
config_file_path = "/vault/secret/db_config.ini"

config = configparser.ConfigParser()
config.read(config_file_path)

db_section = config['database']

# Fetch database connection details
db_name = db_section.get('name')
db_user = db_section.get('user')
db_password = db_section.get('password')
db_host = db_section.get('host')
db_port = db_section.get('port')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
cursor = conn.cursor()

# Create a table if not exists
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )'''
)
conn.commit()

# Define Prometheus metrics
try:
    db_query_counter = Counter('flask_app_db_queries_total', 'Total number of database queries')
except ValueError:
    # Metric already registered
    db_query_counter = REGISTRY.get('flask_app_db_queries_total')

try:
    request_duration_histogram = Histogram('flask_app_request_duration_seconds', 'Request duration in seconds')
except ValueError:
    # Metric already registered
    request_duration_histogram = REGISTRY.get('flask_app_request_duration_seconds')

@app.route('/')
def index():
    with request_duration_histogram.time():
        # Retrieve students from the database
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

    db_query_counter.inc()

    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']

    with request_duration_histogram.time():
        # Insert student into the database
        cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()

    db_query_counter.inc()

    return redirect('/')

@app.route("/health")
def health_handler():
    data = {"status": "HEALTHY"}
    return jsonify(data)

@app.route('/metrics')
def metrics():
    # Expose Prometheus metrics
    return Response(generate_latest(REGISTRY), content_type='text/plain')

if __name__ == "__main__":
    app.run(debug=True, port=5050)
