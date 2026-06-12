# AI Placement Copilot 🚀

AI Placement Copilot is a full-stack career preparation platform designed to help students prepare for internships and placements through AI-powered career guidance tools.

## Features

### 📄 Resume Analyzer

* Upload PDF resumes
* ATS score analysis
* Skill extraction
* Strengths and weaknesses identification
* Personalized recommendations

### 🎯 Job Match Analyzer

* Compare resume against job descriptions
* Match score calculation
* Missing skills identification
* Missing keyword detection
* Improvement suggestions

### 📈 Skill Gap Analysis

* Analyze current skills against target roles
* Identify missing competencies
* Generate learning priorities
* Career readiness assessment

### 🛣 Personalized Learning Roadmap

* Generate structured 8-week learning plans
* Customized based on target role
* Weekly goals and milestones
* Project recommendations
* Interview preparation guidance

### 🎤 Interview Preparation

* Generate technical interview questions
* Behavioral interview questions
* HR interview questions
* Answer evaluation and feedback

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Axios

### Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### Deployment

* Frontend: Vercel
* Backend: Render

### AI Integration

* Google Gemini API

---

## Project Structure

```bash
AI-Placement-Copilot/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   └── db/
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/code-spark648/ai-placement-copilot.git

cd ai-placement-copilot
```

---

### Backend Setup

```bash
python -m venv venv

source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=your_database_url

GEMINI_API_KEY=your_api_key
```

Run backend:

```bash
uvicorn app.main:app --reload
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```


## Future Enhancements

* Real-time interview simulation
* Voice-based mock interviews
* Company-specific preparation tracks
* Placement analytics dashboard
* Resume version tracking
* AI career mentor chatbot

---

##

---

## License

This project is developed for educational and learning purposes.
