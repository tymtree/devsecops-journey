from flask import Flask
import psycopg

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Docker App!"

@app.route("/db")
def db_test():
    conn = psycopg.connect(
        host="postgres",
        dbname="postgres",
        user="postgres",
        password="devpass"
    )
    conn.close()
    return "Python app connected to PostgreSQL database!"

app.run(host="0.0.0.0", port=5000)