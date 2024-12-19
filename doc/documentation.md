# Dragon AI Documentation

## Overview
Dragon AI is an advanced AI platform providing cutting-edge solutions for various industries. The application allows users to interact with the AI model in real-time, generate content based on user prompts, and manage chat sessions.

## Features

### Content Generation API
- **Endpoint:** `/generate`
- **Method:** `POST`
- **Description:** Accepts a JSON payload with a `prompt` field and returns generated content using the gemini-1.5-flash model.
- **Default Prompt:** If no prompt is provided, the system defaults to "Explain how AI works".

### Frontend Features
- **Responsive Design:** The application is designed to be responsive, ensuring a smooth user experience on various devices.
- **Dark Theme:** The interface uses a dark theme for better readability and aesthetics.
- **Chat History:** Users can view and navigate through previous chat sessions.
- **Search Functionality:** A search bar allows users to filter chat sessions by content.
- **Real-time Interaction:** Users can send prompts and receive AI-generated responses in real-time.
- **Message Formatting:** Users can format their messages using bold, italic, and code styles.
- **Voice Input:** Users can use voice commands to input prompts, enhancing accessibility.
- **Syntax Highlighting:** Code blocks in responses are syntax-highlighted for better readability.
- **Markdown Support:** Responses can include formatted text using Markdown.

## Technical Details
- **Framework:** Flask
- **Environment Variables:** The application loads environment variables from a `.env` file, specifically using the `GOOGLE_API_KEY` for authentication with the Google Generative AI service.
- **Debug Mode:** The application runs in debug mode for easier development and testing.

## Setup Instructions

1. **Ensure Python and Flask are Installed:**
   - Install Python from the [official website](https://www.python.org/downloads/).
   - Install Flask using pip:
     ```bash
     pip install Flask
     ```

2. **Create a `.env` File:**
   - Create a `.env` file in the project root and add your Google API key:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```

3. **Run the Application:**
   - Navigate to the project directory and run the application:
     ```bash
     python api/index.py
     ```

4. **Access the Application:**
   - Open a web browser and go to `http://localhost:5000`.

## Known Issues
- **No Known Issues Detected:** As of this release, no significant issues have been detected. The application functions as intended across various devices and browsers.

## Future Enhancements
- **User Authentication:** Implement user authentication for personalized chat sessions.
- **Multilingual Support:** Add support for multiple languages.
- **Advanced Formatting Options:** Introduce more advanced text formatting options.
- **Improved Voice Input:** Enhance voice input capabilities with better accuracy and support for more languages.
- **Integration with Other AI Models:** Allow users to choose from different AI models for content generation.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for more information.

## Contact
For any questions or support, please contact the Dragon AI Team at [support@dragon-ai.com](mailto:support@dragon-ai.com).
