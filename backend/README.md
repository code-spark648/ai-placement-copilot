# AI Placement Copilot — Backend

FastAPI · PostgreSQL · SQLAlchemy · Alembic · Google Gemini

---

## Backend Folder Structure

```
backend/
├── alembic/                      # Database migrations
│   ├── env.py                    # Alembic environment (reads app settings)
│   ├── script.py.mako            # Migration file template
│   └── versions/
│       └── 001_initial.py        # Initial migration: all 6 tables
├── alembic.ini                   # Alembic configuration
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI app, CORS, router registration
│   ├── api/
│   │   ├── deps.py               # Shared dependencies (active user, pagination)
│   │   └── routes/
│   │       ├── auth.py           # POST /auth/register, /login  GET /auth/me
│   │       ├── resume.py         # POST /resume/upload  GET /resume/latest|all
│   │       ├── job_match.py      # POST /job-match/analyze  GET /job-match/latest
│   │       ├── skills.py         # POST /skills/gap-analysis  GET /skills/roles
│   │       ├── roadmap.py        # POST /roadmap/generate  GET /roadmap/latest|all
│   │       ├── interview.py      # POST /interview/questions|evaluate  GET /sessions
│   │       └── dashboard.py      # GET /dashboard/stats|readiness-history
│   ├── core/
│   │   ├── config.py             # Pydantic settings (reads .env)
│   │   └── security.py           # JWT creation/decode, password hashing, auth dep
│   ├── db/
│   │   ├── base_class.py         # SQLAlchemy declarative Base
│   │   ├── base.py               # Re-exports Base + all models (for Alembic)
│   │   ├── init_db.py            # create_all() helper script
│   │   └── session.py            # Engine + SessionLocal + get_db()
│   ├── models/
│   │   ├── user.py               # users table
│   │   ├── resume.py             # resumes table
│   │   ├── job_match.py          # job_matches table
│   │   ├── roadmap.py            # roadmaps table
│   │   ├── interview.py          # interview_sessions table
│   │   └── readiness.py          # readiness_scores table
│   ├── schemas/
│   │   ├── user.py               # UserCreate, UserLogin, UserResponse, Token
│   │   ├── resume.py             # ResumeAnalysis, ResumeResponse
│   │   └── misc.py               # All other request/response schemas
│   └── services/
│       ├── resume_ai.py          # Gemini: resume analysis
│       ├── job_match_ai.py       # Gemini: job match + skill gap
│       ├── roadmap_ai.py         # Gemini: roadmap generation
│       └── interview_ai.py       # Gemini: question gen + answer eval
├── Dockerfile                    # Production-ready multi-stage image
├── requirements.txt
└── .env.example
```

---

## Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.11+ |
| PostgreSQL | 14+ |
| pip | latest |

---

## 1 — Clone & enter the backend directory

```bash
git clone <repo-url>
cd ai-placement-copilot/backend
```

---

## 2 — Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate          # Linux / macOS
# venv\Scripts\activate           # Windows PowerShell
```

---

## 3 — Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4 — Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in:

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Random 64-char hex string — `python -c "import secrets; print(secrets.token_hex(32))"` |
| `DATABASE_URL` | PostgreSQL connection string |
| `GEMINI_API_KEY` | From https://aistudio.google.com/app/apikey |

---

## 5 — Create PostgreSQL database

```bash
# Option A — psql CLI
psql -U postgres -c "CREATE DATABASE placement_copilot;"

# Option B — createdb helper
createdb -U postgres placement_copilot
```

---

## 6 — Run database migrations

```bash
# Using Alembic (recommended for production)
alembic upgrade head

# Alternative: direct SQLAlchemy create_all (development only)
python -m app.db.init_db
```

Verify tables were created:

```bash
psql -U postgres -d placement_copilot -c "\dt"
```

Expected output — 6 tables:
```
 users
 resumes
 job_matches
 roadmaps
 interview_sessions
 readiness_scores
```

---

## 7 — Start the backend server

```bash
# Development (auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 8 — Verify it's running

```bash
curl http://localhost:8000/health
# → {"status":"healthy"}

# Interactive API docs
open http://localhost:8000/docs
```

---

## Docker (alternative to local setup)

```bash
# From the repo root:
cp backend/.env.example backend/.env   # fill in GEMINI_API_KEY and SECRET_KEY

docker-compose up --build
```

Services:
- Backend → http://localhost:8000
- Frontend → http://localhost:3000
- PostgreSQL → localhost:5432

---

## API Endpoints Summary

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/auth/register` | No | Create account |
| POST | `/auth/login` | No | Login, get JWT |
| GET | `/auth/me` | Yes | Current user |
| PUT | `/auth/me` | Yes | Update profile |
| POST | `/resume/upload` | Yes | Upload PDF, get ATS analysis |
| GET | `/resume/latest` | Yes | Most recent resume analysis |
| GET | `/resume/all` | Yes | All resume analyses |
| POST | `/job-match/analyze` | Yes | Match resume vs JD |
| GET | `/job-match/latest` | Yes | Most recent match result |
| POST | `/skills/gap-analysis` | Yes | Skill gap for target role |
| GET | `/skills/roles` | Yes | Supported roles list |
| POST | `/roadmap/generate` | Yes | Generate learning roadmap |
| GET | `/roadmap/latest` | Yes | Most recent roadmap |
| GET | `/roadmap/all` | Yes | All roadmaps |
| DELETE | `/roadmap/{id}` | Yes | Delete a roadmap |
| POST | `/interview/questions` | Yes | Generate interview questions |
| POST | `/interview/evaluate` | Yes | Evaluate mock answer |
| GET | `/interview/sessions` | Yes | Past interview sessions |
| GET | `/interview/companies` | Yes | Supported companies |
| GET | `/dashboard/stats` | Yes | Full readiness dashboard |
| GET | `/dashboard/readiness-history` | Yes | Historical readiness scores |

---

## Alembic cheat sheet

```bash
# Create a new migration
alembic revision --autogenerate -m "add_column_xyz"

# Apply all pending migrations
alembic upgrade head

# Roll back one migration
alembic downgrade -1

# Show migration history
alembic history --verbose
```

---

## Render.com deployment

1. Create a new **Web Service** pointing to this repo.
2. Set **Root Directory** → `backend`
3. Set **Build Command** → `pip install -r requirements.txt`
4. Set **Start Command** → `alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add all environment variables from `.env.example` under the **Environment** tab.
6. Create a **PostgreSQL** database on Render and copy the internal URL to `DATABASE_URL`.
