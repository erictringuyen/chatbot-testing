import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conversation_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            max_tokens=500
        )

        assistant_message = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return jsonify({"response": assistant_message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"message": "Conversation reset"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
