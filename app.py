from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
load_dotenv()

app = Flask(__name__)

# Set your Gemini API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")
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

                # Save to local memory
        with open("task_memory.json", "a") as f:
            json.dump({"tasks": tasks}, f)
            f.write("\n")

        # Read previous tasks for context
        memory_text = ""
        try:
            with open("task_memory.json", "r") as f:
                lines = f.readlines()
                memory_text = "\n".join([json.loads(line)["tasks"] for line in lines])
        except Exception as e:
            memory_text = ""

        # Updated prompt with memory context
        prompt = f"""You are a smart planning assistant.

Past tasks:
{memory_text}

New tasks:
{tasks}

Combine both. Avoid duplicate tasks. Sort and prioritize everything. Format:
1. Task name
Priority: High/Medium/Low
Reason: One-line reason

Then add:
Suggested Order: 1, 2, 3...

Use only plain text. No markdown, no emojis, no quotes."""


        response = model.generate_content(prompt)
        return jsonify({"plan": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
