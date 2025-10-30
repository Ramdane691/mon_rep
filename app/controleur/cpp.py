from flask import Blueprint, request, jsonify
import subprocess
import uuid
import os

main = Blueprint('cpp', __name__)

@main.route('/compile/', methods=['POST'])
def compile_code():
    code = request.form.get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    uid = uuid.uuid4().hex
    filename = f'/tmp/{uid}.cpp'
    executable = f'/tmp/{uid}'

    with open(filename, 'w') as f:
        f.write(code)

    try:
        compile_result = subprocess.run(['g++', filename, '-o', executable],
                                        capture_output=True, timeout=5)

        if compile_result.returncode != 0:
            return jsonify({
                'error': 'Compilation failed',
                'details': compile_result.stderr.decode()
            }), 400

        run_result = subprocess.run([executable], capture_output=True, timeout=2)
        output = run_result.stdout.decode()

        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filename):
            os.remove(filename)
        if os.path.exists(executable):
            os.remove(executable)
