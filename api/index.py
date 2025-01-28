from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
from dotenv import load_dotenv
import os
import subprocess

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='../')

# Configure the API key from the environment variable
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get('prompt', 'Explain how AI works')
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    return jsonify({'response': response.text})

@app.route('/execute-code', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data.get('code', '')

    app.logger.info(f"Executing code: {code}")

    try:
        if code.startswith('!'):
            # Execute shell command
            command = code[1:].strip()
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
        else:
            # Execute Python code
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True,
                text=True,
                check=True
            )
        app.logger.info(f"Execution result: {result.stdout}")
        return jsonify({'output': result.stdout})
    except subprocess.CalledProcessError as e:
        error_message = e.stderr
        if "Read-only file system" in error_message:
            error_message = "ERROR: The file system is read-only. Package installations are not allowed."
        app.logger.error(f"Execution error: {error_message}")
        return jsonify({'error': error_message}), 400
    except Exception as e:
        error_message = str(e)
        app.logger.error(f"Execution error: {error_message}")
        return jsonify({'error': error_message}), 400

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
