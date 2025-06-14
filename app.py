from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")  # Fallback for development only
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agent', methods=['POST'])
def task_agent():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        tasks = data.get("tasks", "")
        if not tasks:
            return jsonify({"error": "No tasks provided"}), 400

        prompt = f"""Analyze these tasks and create a concise priority-based plan:
{tasks}

Provide a simple response in plain text format (no markdown, no special characters) with:
1. Task number and name
2. Priority level (High/Medium/Low)
3. A brief one-line reason
4. Finally, list the suggested order of completion

Format example:
1. Task Name
Priority: High
Reason: Brief explanation

(and so on...)

Suggested order: 1, 2, 3...

Keep everything in plain text without any special formatting characters."""

        response = model.generate_content(prompt)
        return jsonify({"plan": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
