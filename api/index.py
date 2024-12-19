from flask import Flask, request, jsonify, send_from_directory
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='../')

# Configure the API key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get('prompt', 'Explain how AI works')
    response = client.models.generate_content(
        model='gemini-2.0-flash-exp', contents=prompt
    )
    return jsonify({'response': response.text})

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)