# backend.py

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/add-face', methods=['POST'])
def add_face():
    student_name = request.json.get('name')
    if not student_name:
        return jsonify({'error': 'Name is required'}), 400

    # Run addData.py script with the provided name
    try:
        subprocess.run(['python', 'addData.py', student_name])
        return jsonify({'message': f'Face added for {student_name}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
