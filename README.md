# IntraVue v1 🎯  
AI-Powered Interview Evaluation System

IntraVue is an AI-driven interview intelligence platform that evaluates a candidate’s answer to a single interview question and provides **structured, unbiased, and actionable feedback** in real time.

This repository contains **IntraVue v1**, the **foundational version** of the system, focused on **prompt-engineered GenAI evaluation with a polished frontend experience**.

---

## 🚀 What is IntraVue v1?

**IntraVue v1** is a single-question interview evaluator that:

- Accepts job context and candidate answers
- Uses a Large Language Model (LLM) with strict prompt formatting
- Produces structured interview feedback
- Visualizes results with confidence scoring and UX polish

> ⚠️ This version is **not RAG-based** and does **not use agents**.  
> Those are planned for **v2 and v3** respectively.

---

## 🧠 Key Features (v1)

- 📌 Expected Knowledge analysis  
- 🧠 Demonstrated Understanding breakdown  
- ⚠️ Identified knowledge gaps  
- 📊 Interview Risk Assessment  
- 🎯 Confidence Score (0–100)  
- 🚀 Improvement Suggestions  
- ✅ Final Evaluation Summary  
- ✨ Smooth UI animations & loading state  

---

## 🏗️ Tech Stack

### Backend
- **FastAPI** – API framework
- **Python** – Core logic
- **Groq LLM API** – Model inference
- **Prompt Engineering** – Controlled outputs

### Frontend
- **HTML / CSS / JavaScript**
- Custom animations & transitions
- Sticky confidence score
- Loading spinner for evaluations

## 📁 Project Structure
```text
IntraVue-v1/
│
├── backend/
│   ├── app.py                 # FastAPI entry point
│   ├── config.py              # Model & prompt configuration
│   ├── prompts/               # Prompt templates
│   │   ├── system_prompt.txt
│   │   ├── user_prompt.txt
│   │   └── output_format.txt
│   └── services/
│       ├── evaluator.py       # Orchestrates evaluation
│       ├── prompt_builder.py  # Builds structured prompts
│       └── llm_client.py      # Groq LLM client
│
├── frontend/
│   ├── index.html             # UI structure
│   ├── styles.css             # Styling & animations
│   └── script.js              # Client-side logic
│
├── .gitignore
└── README.md
```

## 🧩 Project Architecture
## ⚙️ How IntraVue Works (v1 Flow)

1. The user enters:
   - Job role
   - Experience level
   - Job description
   - Interview question
   - Candidate answer

2. The frontend sends the data to the backend endpoint:
   - Post / Evaluate

3. The backend:
   - Builds a structured prompt using job and candidate context
   - Enforces strict output formatting rules
   - Sends the request to the LLM

4. The LLM responds with:
   - Sectioned interview feedback
   - A numeric confidence score

5. The frontend:
   - Parses each section from the response
   - Animates and displays results
   - Visualizes the confidence score

---

## 📊 Evaluation Output Format

The LLM is forced to respond in the following structure:
Expected Knowledge:

...

Demonstrated Understanding:

...

Identified Gaps:

...

Interview Risk Assessment:

...

Confidence Score:
<number between 0 and 100>

Improvement Suggestions:

...

Evaluation Summary:
...

This guarantees consistent parsing and UX stability.

---

## ▶️ Running the Project Locally

### Backend Setup

  - cd backend
  - pip install -r requirements.txt
  - export GROQ_API_KEY=your_api_key
  - uvicorn app:app --reload

Backend runs at:

 - http://127.0.0.1:8000

### Frontend

Open the following file directly in your browser:

frontend/index.html

---

## 🧪 Example Use Case

Interview Question:
What is HTML?

Evaluation Result:
- Knowledge depth assessed
- Missing concepts highlighted
- Interview risk inferred
- Confidence score generated

This simulates a real interview evaluation scenario.

---

## 🛣️ Roadmap

### v2 (Planned)
- Retrieval-Augmented Generation (RAG)
- Domain-specific evaluation
- Resume and JD grounding

### v3 (Planned)
- Agentic AI interviewers
- Multi-question interviews
- Skill-wise scoring
- Decision explanations

---


## ⭐ Final Note

IntraVue v1 is designed to be:
- Interview-ready
- Extendable
- Cleanly versioned
- Product-oriented

If you like this project, feel free to star the repository.
