from flask import Flask, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

import subprocess
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(curr_dir, 'addData.py')

python_executable = sys.executable

@app.route('/run-script')
def run_script():
    subprocess.run([python_executable, script_path])
    print('Script executed successfully')
    return jsonify({'message': 'Script executed successfully'})

if __name__ == '__main__':
    app.run(debug=True)