# Dragon AI: Simple Setup Guide

## How to Run Dragon AI

### Step 1: Clone the Repository
```bash
git clone https://github.com/bniladridas/dragon-v3.git
cd dragon-v3
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
```
GOOGLE_API_KEY=your_api_key_here
```

### Step 4: Run the Application
To start the application, use the following command:
```bash
python api/index.py
```

### Step 5: Access the Web Interface
Open your browser and navigate to `http://127.0.0.1:5000` to start interacting with Dragon AI.

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
