# ⚕️ Diabeta AI (Diabetes RAG Screening)

A Retrieval-Augmented Generation assistant that answers Indonesian Type 2 Diabetes guideline questions with cited sources, plus a rule-based diabetes risk screening calculator.

> ⚠️ For research/learning only. Not clinically validated, not medical advice.

## 🔗 Links to Demo
- Video: https://drive.google.com/file/d/1fbyIJCNMSc0xGx2Fu-lJQJzUd0y-szQe/view?usp=sharing
- Live app: https://diabeta-ai-01bd8.containers.snapdeploy.app

## 📚 Tech stack
- Python 
- FastAPI
- LangChain 
- FAISS 
- Groq (gpt-oss-120b) 
- OpenAI SDK 
- Docker
- HTML/CSS/JS

## 👩🏻‍💻 My Role
Team of 3 (development happened outside GitHub, so this repo shows a single contributor). My role: AI/ML Engineer: built the RAG pipeline (PDF ingestion, chunking, embedding, FAISS retrieval, grounded bilingual prompting) and the rule-based risk-screening calculator, and migrated LLM providers with zero impact to retrieval.

## 🚀 Features
- **Guideline Q&A (RAG):** answers diabetes questions with citations (source doc, page, snippet) in English or Bahasa Indonesia.
- **Risk Screening:** rule-based score from age, BMI, family history, and symptoms → Low/Moderate/High risk.
- **Prompt-engineered chatbot:** handles general diabetes questions.

## Quick Start
```bash
cd diabeta-backend
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key_here" > .env
uvicorn app:app --reload --host 0.0.0.0 --port 7860
```
Open http://127.0.0.1:7860/ : the vector DB builds automatically on first run.

Full architecture, project layout, Docker instructions, and known gotchas: [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)
