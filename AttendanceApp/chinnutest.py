import subprocess
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

script_path = os.path.join(curr_dir, 'akhiltest.py')

print('hi')
subprocess.run(['python', script_path])
print('bye')
#
# print(result.stdout)
# print(result.stderr)