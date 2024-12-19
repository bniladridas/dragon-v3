# Dragon AI Architecture

## Overview
The Dragon AI application is a Flask-based web application that integrates with Google's Generative AI to provide real-time content generation. This document outlines the architecture of the application, including its components, data flow, and technology stack.

## Components

### 1. Frontend
The frontend is responsible for providing a user-friendly interface for interacting with the AI model. It is built using HTML, CSS, and JavaScript, with additional libraries for enhanced functionality.

#### Key Features:
- **Responsive Design:** Ensures a smooth user experience on various devices.
- **Dark Theme:** Uses a dark theme for better readability and aesthetics.
- **Chat History:** Allows users to view and navigate through previous chat sessions.
- **Search Functionality:** Provides a search bar to filter chat sessions by content.
- **Real-time Interaction:** Enables users to send prompts and receive AI-generated responses in real-time.
- **Message Formatting:** Supports bold, italic, and code styles for messages.
- **Voice Input:** Allows users to input prompts using voice commands.
- **Syntax Highlighting:** Highlights code blocks in responses for better readability.
- **Markdown Support:** Supports formatted text using Markdown.

### 2. Backend
The backend is a Flask application that handles API requests, processes user prompts, and interacts with the Google Generative AI service.

#### Key Features:
- **Content Generation API:** Exposes an endpoint (`/generate`) to accept JSON payloads with prompts and return generated content.
- **Environment Variables:** Loads environment variables from a `.env` file for configuration.
- **Debug Mode:** Runs the application in debug mode for easier development and testing.

### 3. Google Generative AI
The application uses Google's Generative AI service to generate content based on user prompts. The service is accessed via API calls with authentication provided by a Google API key.

## Data Flow

1. **User Interaction:**
   - The user interacts with the frontend, sending prompts through the chat interface.
   
2. **Frontend to Backend:**
   - The frontend sends a POST request to the `/generate` endpoint with the user's prompt.
   
3. **Backend to Google Generative AI:**
   - The backend sends the prompt to Google's Generative AI service using the provided Google API key.
   
4. **Google Generative AI to Backend:**
   - The AI service generates content based on the prompt and sends it back to the backend.
   
5. **Backend to Frontend:**
   - The backend sends the generated content back to the frontend, which displays it in the chat interface.

## Technology Stack

### Frontend
- **HTML/CSS/JavaScript:** Core technologies for building the web interface.
- **Font Awesome:** Provides icons for various elements.
- **Marked:** Used for parsing Markdown content.
- **Highlight.js:** Provides syntax highlighting for code blocks.
- **Flask:** Used for serving static files.

### Backend
- **Flask:** Web framework for handling API requests and serving the frontend.
- **Python:** Programming language for backend logic.
- **Environment Variables:** Managed using a `.env` file.
- **Google Generative AI:** Service for generating content.

### Version Control
- **Git:** Used for version control.
- **GitHub:** Repository hosting.