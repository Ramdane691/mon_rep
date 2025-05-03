from flask import Flask, request, jsonify
from flask_cors import CORS  #à ajouter
import subprocess
import os
import uuid

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis un autre port

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.form.get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    # Créer un fichier temporaire
    uid = uuid.uuid4().hex
    filename = f'/tmp/{uid}.cpp'
    executable = f'/tmp/{uid}'

    with open(filename, 'w') as f:
        f.write(code)

    try:
        # Compiler le fichier
        compile_result = subprocess.run(['g++', filename, '-o', executable], capture_output=True, timeout=5)

        if compile_result.returncode != 0:
            return jsonify({'error': 'Compilation failed', 'details': compile_result.stderr.decode()}), 400

        # Exécuter le programme
        run_result = subprocess.run([executable], capture_output=True, timeout=2)

        output = run_result.stdout.decode().strip()
        return jsonify({'result': output})

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Execution timed out'}), 408

    finally:
        # Nettoyage des fichiers temporaires
        try:
            os.remove(filename)
            os.remove(executable)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app.run(debug=True, port=5050)



