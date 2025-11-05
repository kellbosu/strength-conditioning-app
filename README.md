# 💪 Strength & Conditioning App
A full-stack **strength and conditioning platform** built with **FastAPI (Python)**, **React (Vite)**, and **MongoDB**. A full-stack foundation for managing workouts, tracking progress, and visualizing performance data.

---

## 💡 Overview
The app combines classic strength programming with modern web technologies to create a dynamic, data-driven training experience.
It currently provides:
- A **FastAPI backend** exposing JSON endpoints (`/api/hello`, `/api/roundtrip`)
- A **React + Vite frontend** that fetches and displays live data from the API
- A **MongoDB database** connected through PyMongo for persistent storage
- A **local development environment** with seamless communication between all components (CORS + proxy)

---

## 🧠 Tech Stack
| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Backend** | Python · FastAPI · Uvicorn | REST API, business logic, data layer integration |
| **Frontend** | React · Vite · Node.js | Interactive UI and API integration |
| **Database** | MongoDB (Community 8.0) | Stores user data, programs, and workout history |
| **Dev Tools** | Homebrew · npm · .venv · python-dotenv | Local environment management |
| **Data Format** | JSON | Templates, program structure, and API responses |

## ⚙️ Current Features
- 🏋️ **Auto-generates training waves** (10s, 8s, 5s, 3s) based on lift maxes  
- 🔢 **Calculates weights and reps dynamically** using `SCHEMES` templates  
- 🧩 **Round-trip MongoDB endpoint** (`/api/roundtrip`) that reads and writes data  
- 🌐 **React frontend** fetches live JSON data from FastAPI using Vite’s dev proxy  
- 🔒 **CORS middleware** configured for smooth frontend↔backend communication  
- ⚙️ **Isolated Python environment** (`.venv`) and environment configuration (`.env`)

---

## 🧱 Architecture Overview
```
Browser (React + Vite)
   ↓  fetch('/api/...') via proxy
Vite Dev Server (localhost:5173)
   ↓
FastAPI (Uvicorn, localhost:8000)
   ↓
MongoDB (localhost:27017)
```
- **Frontend:** Renders UI, fetches `/api/hello` and `/api/roundtrip`  
- **Backend:** Processes requests, returns JSON  
- **Database:** Persists documents (users, lifts, waves, etc.)  
- **Environment:** Managed via `.venv` and `.env` for isolation and secrets

---

## 🚧 Future Roadmap
- 🔜 **Program Templates** stored in Mongo for reusable training blueprints  
- 🔜 **User Management & Authentication** (JWT / OAuth)  
- 🔜 **Workout Logging & Progress Visualization**  
- 🔜 **Responsive Dashboard** (wave history)  
- 🔜 **Deployment Setup** (Docker + production build pipeline)

---

## 🚀 Getting Started (Local Development)
### 1️⃣ Backend
```bash
cd backend
source .venv/bin/activate
uvicorn main:app --reload --port 8000
```
### 2️⃣ Frontend
```bash
cd frontend
npm install
npm run dev
```
### 3️⃣ Database
```bash
brew services start mongodb/brew/mongodb-community@8.0
```
Then open:
- **Frontend:** [http://localhost:5173](http://localhost:5173)  
- **Backend Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🏁 Current Milestone
**Version:** `v0.1.0`  
**Status:** End-to-End Hello World achieved  
**Includes:** FastAPI ↔ MongoDB ↔ React (Vite) integration verified locally.

