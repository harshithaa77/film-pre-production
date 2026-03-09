Generative AI–Powered Film Pre-Production System

Scriptoria is a premium web application that uses Google Gemini AI to convert simple movie ideas into professional screenplays, character profiles, mood boards, and production plans.

🚀 Features
AI Screenplay Generation: Standard Hollywood format.
Character Profiles: Detailed backstories and arcs.
Mood & Sound Design: AI-suggested scores and ambient sounds.
Production Planning: Budget, cast, and location breakdown.
Premium UI: Dark mode, glassmorphism, and smooth animations.
Export: Download your project as PDF or TXT.

🛠 Tech Stack
Backend: Python (Flask)
Frontend: HTML5, CSS3, Vanilla JavaScript
AI: Google Gemini API
Database: SQLite

📦 Setup & Installation
Clone the repository (if not already done).
Install dependencies:
pip install -r requirements.txt
Set up Environment Variables:
Create a .env file in the root directory.
Add your Gemini API key:
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
Note: If you don't have an API key, the app will automatically run in Mock Mode, generating demo data for testing.
Run the application:
python app.py
Open in Browser:
Navigate to http://localhost:5000

🎨 Architecture
app.py: Main Flask application.
utils/ai.py: Handles Gemini API interactions.
clean/: Contains the premium UI assets.
database: scriptoria.db (created on first run).

