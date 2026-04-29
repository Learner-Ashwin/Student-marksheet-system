from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# DB connection function
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MYSQL1259@@3211python",
        database="marksheet_db"
    )

@app.route("/")
def home():
    return "API Running"

# ADD STUDENT API
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    name = data["name"]
    student_class = data["class"]
    roll = data["roll"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, class, roll) VALUES (%s, %s, %s)",
        (name, student_class, roll)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully"})

@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return jsonify(students)