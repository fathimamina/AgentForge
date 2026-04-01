import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from ddgs import DDGS
from langchain.agents import create_agent

# ====================== CONFIG ======================
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("❌ GROQ_API_KEY not found in .env file")
    print("Please create .env from .env.example and add your key.")
    exit(1)

print("✅ Groq API key loaded successfully!")

# ====================== LLM ======================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.3,          # Lower = more consistent & reliable
    max_tokens=1024,
)

# ====================== TOOLS ======================
@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information using DuckDuckGo.

    Use this tool when the user asks for:
    - Latest news or current events
    - Recent updates, trends, or facts
    - Anything that might have changed since the model's training cutoff

    Args:
        query (str): The search query.

    Returns:
        str: Formatted search results with title and summary.
    """
    print(f"🔍 Searching web for: {query}")

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=4))

        if not results:
            return "No relevant web results found."

        output = "WEB SEARCH RESULTS:\n\n"
        for i, r in enumerate(results, 1):
            title = r.get('title', 'No title')
            body = r.get('body', 'No summary')[:250]
            output += f"{i}. **{title}**\n   {body}...\n\n"

        return output.strip()

    except Exception as e:
        print(f"⚠️ Web search error: {e}")
        return "Web search is temporarily unavailable. Please try again later."


# ====================== SYSTEM PROMPT ======================
system_prompt = """You are a helpful, concise, and accurate AI assistant named AgentForge.

Rules:
- For any question about latest news, current events, recent updates, trends, or time-sensitive information — ALWAYS use the web_search tool.
- After getting tool results, summarize them clearly and professionally.
- Never make up current information from your own knowledge.
- Keep responses short, clear, and to the point unless the user asks for more detail.
- Be friendly and helpful.
"""

# ====================== CREATE AGENT ======================
agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=system_prompt,
)

print("\n🎉 AgentForge Phase 0 is ready!")
print("You can now ask questions like:")
print("   • latest news in kozhikode")
print("   • current weather trends in Kerala")
print("   • capital of kerala")
print("Type 'exit' or 'quit' to stop.\n")

# ====================== CHAT LOOP ======================
while True:
    try:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print("👋 Thank you for using AgentForge. Goodbye!")
            break

        if not user_input:
            continue

        print("\n🤖 Agent is thinking...")

        response = agent.invoke({
            "messages": user_input
        })

        # Extract the final answer
        final_message = response["messages"][-1].content
        print(f"\n✅ AgentForge: {final_message}")
        print("-" * 80)

    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
        break
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        print("Falling back to basic response...\n")
        try:
            fallback = llm.invoke(user_input)
            print(f"✅ AgentForge (basic): {fallback.content}")
        except:
            print("❌ Could not get a response. Please check your API key and internet.")