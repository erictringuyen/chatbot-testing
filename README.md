# AI Chatbot Web Application

A simple Flask-based chatbot web application that integrates with OpenAI's GPT API.

## Features

- Clean, modern web UI
- Real-time chat interface
- Conversation history maintained
- Reset conversation option
- Responsive design with gradient styling
- Error handling and loading states

## Setup

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-...
```

### Running the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Usage

1. Open your browser and navigate to `http://localhost:5000`
2. Type your message in the input field
3. Press Enter or click the Send button
4. The chatbot will respond with AI-generated replies
5. Click "Reset" to clear the conversation history

## API Endpoints

- `GET /` - Serves the main chatbot UI
- `POST /chat` - Sends a message and receives a response
  - Request: `{"message": "your message"}`
  - Response: `{"response": "chatbot response"}`
- `POST /reset` - Resets the conversation history

## Project Structure

```
chatbot/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── README.md             # This file
└── templates/
    └── index.html        # Frontend UI
```

## Notes

- The chatbot uses GPT-3.5-turbo model by default
- Conversation history is stored in memory during the session
- Each conversation resets when the application restarts
