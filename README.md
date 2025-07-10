
<h1 align="center">AI Task Planner 📝🤖</h1>

<p align="center">
  <b>Smartly sort, prioritize, and plan your tasks using Google Gemini AI.</b><br>
  <i>Built with Flask, Gemini API, and a modern web UI.</i>
</p>

---

## ✨ Features

- 🧠 <b>AI-Powered Planning:</b> Uses Google Gemini to combine, deduplicate, sort, and prioritize your tasks.
- 💾 <b>Task Memory:</b> Remembers your previous tasks for better context and smarter planning.
- 🎨 <b>Modern UI:</b> Clean, responsive interface with beautiful styles.
- ⚡ <b>Instant Results:</b> Get your smart plan in seconds.

---

## 🛠️ Tech Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,googlecloud" height="32" />
</p>

- **Backend:** Python, Flask, Google Gemini API  
- **Frontend:** HTML, CSS (custom, responsive)  
- **Other:** dotenv for environment variables  

---

## 📦 Project Structure

```
AI-Task-Planner/
│
├── app.py                # Flask backend, Gemini integration, task memory
├── templates/
│   └── index.html        # Main web UI
├── static/
│   └── styles.css        # Custom styles
├── .gitignore
├── README.md
└── task_memory.json      # (auto-created) Stores task history
```

---

## ⚙️ Setup & Run

1. **Clone the repo:**
   ```sh
   git clone https://github.com/Vaibhavk121/AI-Task-Planner.git
   cd AI-Task-Planner
   ```

2. **Install dependencies:**
   ```sh
   pip install flask python-dotenv google-generativeai
   ```

3. **Set up your environment:**
   - Create a `.env` file in the root directory:
     ```
     GEMINI_API_KEY=your-gemini-api-key-here
     ```

4. **Run the app:**
   ```sh
   python app.py
   ```
   Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🖥️ Usage

1. Enter your tasks (one per line) in the textarea.
2. Click **Generate Plan**.
3. View your smart, prioritized plan instantly!

---

## 📄 Example Output

```
1. Finish project report
Priority: High
Reason: Deadline is tomorrow

2. Buy groceries
Priority: Medium
Reason: Running low on essentials

3. Call mom
Priority: Low
Reason: Regular check-in

Suggested Order: 1, 2, 3
```

---


<p align="center">
  
  <b>Made with ❤️ by Vaibhav</b>
  </p>