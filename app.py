from flask import Flask
import psycopg

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Docker App!"

@app.route("/health")
def health():
    return "Status Healthy"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)