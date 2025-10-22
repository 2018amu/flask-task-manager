from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from db import collection
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.get_database("task_manager")  # change name if needed

# ------------------ ROUTES ------------------


@app.route('/')
def home():
    return jsonify({"message": "Flask + MongoDB connection successful!"})


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        required_fields = ['name', 'email', 'title', 'description', 'dueDate']

        # Validate required fields
        if not all(field in data and data[field] for field in required_fields):
            return jsonify({"message": "Please fill in all fields."}), 400

        # Insert data into MongoDB
        collection.insert_one(data)

        return jsonify({"message": "Task submitted successfully!"}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@app.route('/test-db')
def test_db():
    try:
        collections = db.list_collection_names()
        return jsonify({"status": "connected", "collections": collections}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------ MAIN ENTRY ------------------


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=True  # you can turn this off in production
    )
