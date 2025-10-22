# Flask Task Manager with MongoDB

A simple Flask web application to manage tasks, integrated with MongoDB.  
Supports AJAX form submission for creating tasks and stores them in a cloud MongoDB Atlas database.

## Features

- Submit tasks with `name`, `email`, `title`, `description`, and `dueDate`.
- Real-time AJAX form submission without page reload.
- MongoDB Atlas integration (cloud-hosted database).
- View database connection status using `/test-db` endpoint.


## Setup


1.Create a virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows
2.Install dependencies:
pip install -r requirements.txt
3.Create a .env file in the root:
MONGO_URI=my_mongodb_connection_string
4.Run the Flask app:
python app.py
5.Open browser: http://localhost:5000/index

