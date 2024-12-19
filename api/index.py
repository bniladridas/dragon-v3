from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='../')

# Configure the API key
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    prompt = data.get('prompt', 'Explain how AI works')
    
    # Get the model
    model = genai.GenerativeModel('gemini-pro')
    
    # Generate the response
    response = model.generate_content(prompt)
    
    return jsonify({'response': response.text})

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)