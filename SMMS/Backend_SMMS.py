from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)



DATA_FILE = "data.json"
#__HELPERS__
def get_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def add_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    return "Record successfully updated!"

def avg(data):
    sum1 = sum(data)/3
    return jsonify(f"The average marks of student is {sum1}")




@app.route('/records', methods = ['GET'])
def all_records():
    data = get_data()
    return jsonify(data)



@app.route('/records/add_record', methods = ['POST'])
def add_record():
    data = get_data()
    new_data = request.get_json()

    if not new_data or 'roll' not in new_data:
        return jsonify({'Error' : 'Record must contain roll number of student'}), 400
    
    if any(rec['roll'] == new_data['roll'] for rec in data):
        return jsonify({'Error' : 'Roll number already exists'}), 400
    
    data.append(new_data)
    add_data(data)
    return ({'Message' : 'Record successfully updated'}), 201



@app.route('/records/update/<roll>', methods = ['PUT'])
def update_record(roll):
    data = get_data()
    updated_data = request.get_json()
    
    for row in data:
        if str(row['roll']) == str(roll):
            row.update(updated_data)
            add_data(data)
            return jsonify({'Message' : 'Record successfully updated'}), 200
   
    
    return jsonify({'Error' : 'This roll number does not exist'}), 404





@app.route('/records/delete/<roll>', methods = ['DELETE'])
def delete_data(roll):
    data = get_data()
    new_data = [row for row in data if str(row["roll"])!= str(roll)]
    
    if len(data) == len(new_data):
        return jsonify({"Error" : 'The record was not found'}), 404
    
    add_data(new_data)
    return jsonify({'Message' : 'Record was successfully deleted!'}), 200



@app.route('/records/average/<roll>', methods=['GET'])
def avg_marks(roll):
    data = get_data()

    for row in data:
        if str(row['roll']) == str(roll):
            marks = row.get('marks', [])
            if not marks:
                return jsonify({'Error': 'No marks found for this student'}), 400
            avg_marks = sum(marks) / len(marks)
            return jsonify({'roll': row['roll'],'name' : row['name'], 'average': avg_marks}), 200

    return jsonify({'Error': 'Roll number not found'}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
