## Simple Q&A Chatbot with LangChain & Ollama (Phi-3)

📌 Project Overview
This project is a functional Large Language Model (LLM) application built using LangChain and Streamlit. It leverages Ollama to run lightweight, open-source models (like Phi-3) locally. This setup provides a private, secure, and cost-effective way to interact with AI without relying on cloud-based APIs.

🛠️ Tech Stack
- Orchestration: LangChain
- Frontend: Streamlit
- LLM Provider: Ollama (Phi-3)
- Observability: LangSmith (for tracing and monitoring)
- Environment Management: Python-dotenv

✨ Key Features
- Local LLM Integration: Uses the Ollama framework to pull and run models locally.
- Interactive Controls: Features a sidebar for real-time adjustments of Temperature and Max Tokens.
- Traceability: Integrated with LangSmith to monitor the prompt-to-output chain, ensuring visibility into the LLM's logic.
- Modular Prompting: Utilizes ChatPromptTemplate for clean and reusable system-level instructions.A Chatbot using Ollama (Phi-3) and Streamlit. Features LangSmith tracing for LLM observability and interactive parameter tuning.
