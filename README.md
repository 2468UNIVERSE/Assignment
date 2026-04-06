# Task 4: Build a Basic REST API
### Flask + MySQL CRUD REST API
A RESTful API built using Flask and MySQL that supports full CRUD (Create, Read, Update, Delete) operations on tasks.
All API endpoints in this project were tested using cURL commands from the terminal, and the testing steps are documented below so that anyone cloning the repository can reproduce the results.

### Features
1. RESTful API built with Flask
2. MySQL database integration
3. Full CRUD operations
4. JSON-based request and response handling
5. All endpoints tested using cURL

### Tech Stack
1. Backend: Flask (Python)
2. Database: MySQL
3. Testing Tool: cURL (Command Line)
4. Database Connector: mysql-connector-python

### Setup Instructions
1. Install Required Packages
```bash
pip install flask mysql-connector-python
```

2. Create Database and Table
Execute the following SQL commands in MySQL:
```bash
CREATE DATABASE flask_crud_api;

USE flask_crud_api;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
```

3. Run the Application
```bash
python Task_Project_4.py
```
The server will start at:
```bash
http://127.0.0.1:5000
```

### API Endpoints and cURL Testing
All API endpoints listed below were tested using cURL from the command line.
1. Create a Task
Endpoint: POST /tasks
cURL Command:
```bash
curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\": \"Learn Flask\"}"
```
Response:
```bash
{
  "message": "Task created successfully"
}
```

2. Get All Tasks
Endpoint: GET /tasks
cURL Command:
```bash
curl http://127.0.0.1:5000/tasks
```
Response:
```bash
[
  {
    "id": 1,
    "title": "Learn Flask",
    "completed": 0
  }
]
```

3. Get a Single Task
Endpoint: GET /tasks/<id>
cURL Command: 
```bash
curl http://127.0.0.1:5000/tasks/1
```

4. Update a Task
Endpoint: PUT /tasks/<id>
cURL Command:
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
-H "Content-Type: application/json" \
-d "{\"completed\": true}"
```
Response;
```bash
{
  "message": "Task updated successfully"
}
```

5. Delete a Task
Endpoint: DELETE /tasks/<id>
cURL Command:
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```
Response:
```bash
{
  "message": "Task deleted successfully"
}
```

### Bulk Testing Using cURL
Add Multiple Tasks Using a Loop (Windows CMD):
```bash
for /l %i in (3,1,10) do curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"title\": \"Task %i\"}"
```

### Notes:
1. Web browsers support only GET requests by default.
2. POST, PUT, and DELETE requests were tested using cURL( paste the cURL commands in the terminal ).
3. The application runs on Flask’s development server.
4. This project is intended for learning and demonstration purposes, not for production use.
