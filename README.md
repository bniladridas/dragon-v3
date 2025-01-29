# Dragon AI: Simple Setup Guide

## Top Priorities

### Git, Bash, Python
- Efficient code management and automation.
- Streamlined workflows and scripting.

### Vercel
- Seamless deployment and scalability.
- Optimized for serverless functions and static sites.

### Markdown and Keyboard Lighting
- Enhanced documentation and user experience.
- Improved typing efficiency and aesthetic appeal.

<!-- Adding icons for HTML, CSS, JS, Python, Run, Stream, Play, Vercel, and Google DeepMind -->
<p align="center">
  <img src="https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/css-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript">
  <img src="https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/run-%2320232a.svg?style=for-the-badge" alt="Run">
  <img src="https://img.shields.io/badge/stream-%23ff0000.svg?style=for-the-badge" alt="Stream">
  <img src="https://img.shields.io/badge/play-%2300d7ff.svg?style=for-the-badge" alt="Play">
  <img src="https://img.shields.io/badge/vercel-%23ffffff.svg?style=for-the-badge&logo=vercel&logoColor=black" alt="Vercel">
  <img src="https://img.shields.io/badge/google_deepmind-gemini_2.0_exp_flash-%23ea4335.svg?style=for-the-badge&logo=google&logoColor=white" alt="Google DeepMind">
</p>

![bts](api/bts.png)

## How to Run Dragon AI

### Step 1: Clone the Repository
```bash
git clone https://github.com/bniladridas/dragon-ai.git
cd dragon-ai
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Configuration
Copy the example environment file and edit it:
```bash
cp .env.example .env
vim .env
```
Ensure you add your Google API key in the `.env` file:
```bash
GOOGLE_API_KEY=your_api_key_here
```

### Step 4: Run the Application
To start the application, use the following command:
```bash
python api/index.py
```

### Step 5: Access the Web Interface
Open your browser and navigate to `http://127.0.0.1:5000` to start interacting with Dragon AI.

## Configuration for Vercel Deployment
The project uses a `vercel.json` file to redirect all routes to the API index. This is useful for serverless deployments on Vercel. Here is the configuration:

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/api/index" }
  ]
}
```

This configuration ensures that all incoming requests are handled by the `/api/index` route.

## Troubleshooting

### Common Issues

1. **Missing Dependencies**:
   Ensure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Make sure the `.env` file is correctly set up with your API key.

3. **Port Conflicts**:
   If port 5000 is already in use, you can change the port by modifying the `app.run()` line in `api/index.py`:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, port=5001)
   ```

4. **API Key Issues**:
   Verify that your Google API key is valid and has the necessary permissions.

5. **Network Issues**:
   Ensure your network allows outgoing connections to the Google API services.

### Getting Help
If you encounter any issues not covered here, please open an issue on the [GitHub repository](https://github.com/bniladridas/dragon-v3/issues).

## How the Python Code Works

The Python code is a Flask application that provides two main functionalities:

1. **Content Generation**:
   - The `/generate` endpoint allows users to send a POST request with a prompt.
   - The prompt is processed by the Google's Gemini 2.0 exp flash model to generate content.
   - The generated content is returned as a JSON response.

2. **Code Execution**:
   - The `/execute-code` endpoint allows users to send a POST request with code to be executed.
   - The code can be either a shell command (starting with `!`) or Python code.
   - The output or error from the execution is returned as a JSON response.

### Mermaid Model

```mermaid
graph TD
    A[Client] --> |POST /generate| B[Flask API]
    B --> |Request with prompt| C[Google Generative AI]
    C --> |Generated content| B
    B --> |Response with content| A

    A --> |POST /execute-code| B
    B --> |Request with code| D[Subprocess Execution]
    D --> |Execution result| B
    B --> |Response with output/error| A
```

## Research Category: Deployment Details

```
Running build in Washington, D.C., USA (East) – iad1
Cloning github.com/bniladridas/dragon-v3 (Branch: main, Commit: 0aa051a)
Cloning completed: 675.000ms
Restored build cache from previous deployment (3bHrrg8haxCEJNbFdM9kF2mLw2zM)
Running "vercel build"
Vercel CLI 39.3.0
Installing required dependencies...
Build Completed in /vercel/output [4m]
Deploying outputs...
▲ Build system report
▲ To always completely log this report, add VERCEL_BUILD_SYSTEM_REPORT=1 as an Environment Variable to your project.
• At least one "Out of Memory" ("OOM") event was detected during the build.
  • This occurs when processes or applications running during the build completely fill up the available memory (RAM) in the build container. When this happens, the build container terminates on[...]
  • Read this troubleshooting guide for more information: https://vercel.link/troubleshoot-build-errors
```

## Google Vertex AI Gemini v2
[Google Vertex AI Gemini v2 Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2)
Google Vertex AI offers an advanced generative AI model, Gemini v2, designed to understand and generate human-like text. This model is highly effective for various applications, including content creation, customer service, and more.

```plaintext
Gemini v2 model is built to provide:
- High-quality text generation
- Seamless integration with other Google AI services
- Robust performance across different tasks
```

For detailed information, visit the official [Google Vertex AI Gemini v2 Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2).

## Gemini API Model Information
[Gemini API Model Documentation](https://ai.google.dev/gemini-api/docs/models/gemini-v2)
The Gemini API provides access to the Gemini v2 model, enabling developers to integrate advanced generative AI capabilities into their applications. The API supports various endpoints for text generation, model management, and more.

```plaintext
Key features of the Gemini API:
- Easy-to-use endpoints for text generation
- Comprehensive documentation and examples
- Support for multiple languages and use cases
```

For more details, visit the official [Gemini API Model Documentation](https://ai.google.dev/gemini-api/docs/models/gemini-v2).

## Google AI Studio
Google AI Studio provides a comprehensive suite for developing, training, and deploying machine learning models. It allows users to choose from pre-built models or create custom models tailored to specific needs.

### How to Get the Code of the Selected Model
1. Navigate to Google AI Studio and select your desired model.
2. Click on the "Export" button to download the model code.
3. Integrate the downloaded code into your project.

### How to Get the API
1. In Google AI Studio, select the model to which you want to get the API access.
2. Click on the "API" tab to get the API endpoint and authentication details.
3. Use the provided API key and endpoint to make requests to the model.

### Configuration from Google Cloud
To configure your project to use Google AI services, follow these steps:

1. **Create a Google Cloud Project**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.

2. **Enable Required APIs**:
   - Enable the "Cloud AI" and "Cloud Functions" APIs from the API library.

3. **Set Up Authentication**:
   - Create a service account and download the JSON key file.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON key file.

4. **Example Configuration**:
   ```json
   {
     "type": "service_account",
     "project_id": "your-project-id",
     "private_key_id": "your-private-key-id",
     "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
     "client_email": "your-service-account-email",
     "client_id": "your-client-id",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email"
   }
   ```

## Model Configuration Examples

### Gemini 1.5 Pro
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Gemini 1.5 Flash
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Gemini 1.5 Flash 8B
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Gemini 2.0 Flash Exp
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Gemini Exp 1206
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-exp-1206",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Gemini 2.0 Flash Thinking Exp 01-21
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-thinking-exp-01-21",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

### Learn LM 1.5 Pro Experimental
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="learnlm-1.5-pro-experimental",
  generation_config=generation_config,
)

chat_session = model.start_chat(history=[])
response = chat_session.send_message("INSERT_INPUT_HERE")
print(response.text)
```

## Invitation to Sign Up for Gemini or Google AI Program
Interested in exploring the capabilities of Gemini or other Google AI programs? Sign up [here](https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2) to get started with Google AI and access cutting-edge AI models for your projects.
```

# 👍
