# 🤖 AI Web Search Agent (LangChain + Groq)

A simple AI agent that can answer questions and fetch real-time information using web search.

## 🚀 Features

* Uses LLM (`llama-3.3-70b-versatile`)
* Automatic tool usage (web search)
* Real-time answers for news & current events
* Clean CLI interface

## 🧠 Tech Stack

* LangChain
* Groq API
* DuckDuckGo Search
* Python

## 📁 Project Structure

```
agentforge-phase0/
│── agent.py
│── .env.example
│── requirements.txt
│── README.md
│── .gitignore
```

## ⚙️ Setup

1. Clone repo:

```
git clone https://github.com/your-username/agentforge-phase0.git
cd agentforge-phase0
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

4. Run:

```
python agent.py
```

## 💬 Example Queries

* capital of kerala
* latest news in kozhikode
* what is machine learning

## ⚠️ Notes

* Do NOT share your `.env` file
* Requires internet connection

## 📌 Future Improvements

* Add memory (chat history)
* Add more tools (calculator, weather)
* Deploy as web app

---

Made with ❤️ using LangChain & Groq
