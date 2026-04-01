

# AgentForge

**A modern Multi-Agent AI Platform** where users can create custom AI agent teams that work together to complete complex real-world tasks.

Instead of chatting with a single AI, you build a "team" of specialized agents (Researcher, Analyst, Writer, Critic, etc.) that collaborate, use tools, search the web, analyze files, and deliver complete results.

## ✨ Vision
AgentForge turns powerful LLMs into collaborative agent teams — making AI actually useful for real, multi-step work.

### Example Use Cases
- "Research the latest AI trends in India and create a 10-page report with sources"
- "Analyze this uploaded PDF + images and summarize the key insights"
- "Plan my next week: research topics, make a schedule, and generate content ideas"

## 🗺️ Project Roadmap

### Phase 0: Foundation (Current)
- Basic single AI agent with web search tool
- Powered by **Groq + Llama 3.3 70B**
- Clean agent architecture using LangChain

### Phase 1: Memory & Tools
- Add conversation memory
- More tools (file analysis, calculations, etc.)

### Phase 2: Multi-Agent System
- Multiple specialized agents
- Supervisor agent for task orchestration

### Phase 3: Full Platform
- Beautiful web UI (Next.js)
- File/PDF/Image upload support
- Real-time streaming of agent collaboration
- Dashboard to save and reuse agent teams

## 🚀 Quick Start (Phase 0)

```powershell
# 1. Clone the repo
git clone https://github.com/fathimamina/AgentForge.git
cd AgentForge/Phase0/agentforge-phase0

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup API key
copy .env.example .env
# Edit .env and add your GROQ_API_KEY
