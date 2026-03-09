Generative AI–Powered Film Pre-Production System

🎬 Core Capabilities
- AI Screenplay Generation: Converts simple movie ideas into professional scripts in Hollywood-standard format.
- Character Profiles: Builds detailed backstories and arcs for each character.
- Mood & Sound Design: Suggests scores and ambient sounds to match the tone.
- Production Planning: Breaks down budget, cast, and locations.
- Export Options: Projects can be downloaded as PDF or TXT.

🛠 Tech Stack
- Backend: Python (Flask)
- Frontend: HTML5, CSS3, Vanilla JavaScript
- AI Engine: Google Gemini API
- Database: SQLite

⚙️ Setup & Installatio
- Clone the repository.
- Install dependencies: pip install -r requirements.txt
- Configure environment variables in .env:
- GEMINI_API_KEY=your_api_key_here
- SECRET_KEY=your_secret_key_here
  (If no API key is provided, it runs in Mock Mode with demo data.)
- Run: python app.py
- Open in browser: http://localhost:5000

🏗 Architecture
- app.py → Main Flask application
- utils/ai.py → Handles Gemini API interactions
- clean/ → Premium UI assets (dark mode, glassmorphism, animations)
- database/ → scriptoria.db auto-created on first run

📝 Usage Flow
- Register/Login
- Go to Dashboard
- Click New Project
- Enter your movie idea
- AI generates screenplay, profiles, mood boards, and production plan
- Explore assets and export

This system essentially acts as a creative assistant for filmmakers, automating the heavy lifting of scriptwriting and pre-production planning.



