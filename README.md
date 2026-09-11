# Portfolio-Myself

Personal portfolio website for Tasnia Haque with an AI chatbot assistant, built with Flask.

## Project structure

```
.
├── app/
│   ├── ai_services/       # Groq chatbot logic
│   ├── core/              # Config and logging
│   ├── data/              # Portfolio content (JSON)
│   ├── routers/           # Flask route blueprints
│   ├── schemas/           # Request/response models
│   ├── services/          # Business logic (email, portfolio data)
│   └── main.py            # Application entry point
├── static/                # CSS, images, resume
├── templates/             # HTML templates
├── requirements.txt
└── vercel.json
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
GMAIL_APP_PASSWORD=your_gmail_app_password
GMAIL_ADDRESS=tasniahaque18@gmail.com
```

## Run locally

```bash
python -m app.main
```

Open **http://127.0.0.1:8000** in your browser (port 8000 avoids macOS AirPlay conflicts on port 5000).

Optional env vars: `FLASK_PORT=8000`, `FLASK_DEBUG=true`

## Deploy

Configured for Vercel via `vercel.json`. Set environment variables in the Vercel dashboard.
