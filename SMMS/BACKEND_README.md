
# STUDENT MARKS MANAGEMENT SYSTEM (Flask API)

This is a simple Flask-based REST API for managing student records, including their roll numbers, names, and marks.

It supports basic CRUD operations — Create, Read, Update, and Delete — along with a route to calculate the average marks for each student.
## Features

- Saves student's roll number, name and marks
- Display student records
- Validate unique roll numbers
- update student records
- return average marks of student
- Delete student records
- Stores data locally in a JSON file

## Tech Stack

- Python 3.x

- Flask (Web framework)

- JSON (For local data storage)

- Requests (Optional for testing API endpoints)


## Installation & Usage

Clone repository:

```bash
- git clone https://github.com/yourusername/student-marks-management.git
- cd student-marks-management
```
The App runs locally on:
```bash
- http://localhost:5000
```
All available app routes:
```bash
- /records  #(Display all records)
- /records/add_record   #(Add student record)
- /records/update/<roll number>   #(Update record of student w/ roll number)
- /records/delete/<roll number>  #(Delete record of student w/ roll number)
- /records/average/<roll number>    #(Display average marks of student with roll number)
```
The POST and PUT methods should be entered in the following syntax:
```bash
Example: roll = 1, name = John Doe and marks = [85, 90, 95]
{
  "roll": 1,
  "name": "John Doe",
  "marks": [85, 90, 95]
}
```

## Author

Aditya Kumar Sharma (Spark)
- email: shradi0612@gmail.com
- Github: https://github.com/Sparky-06
