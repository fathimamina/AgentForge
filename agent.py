import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from ddgs import DDGS
from langchain.agents import create_agent


# 🔐 Load API Key

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("api key is not available")
    exit()

print("Groq key loaded!")


# 🧠 LLM Setup

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.5,
)


# 🔧 Web Search Tool

@tool
def web_search(query: str) -> str:
    
    print(f"🔍 Searching web for: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return "WEB RESULTS: No relevant results found."

        output = ""
        for i, r in enumerate(results, 1):
            output += f"{i}. {r.get('title', 'No title')}\n"
            output += f"   {r.get('body', 'No summary')[:200]}...\n\n"

        return f"WEB RESULTS:\n{output.strip()}"

    except Exception:
        return "WEB RESULTS: Search temporarily unavailable."

# 🧠 System Prompt

system_prompt = """You are a helpful assistant.

Rules:
- If the question is about latest news, current events, or recent updates,
  you MUST use the web_search tool.
- After using the tool, summarize the results clearly.
- Do NOT answer from your own knowledge for current information.
- Keep answers short and clear.
"""

# 🤖 Create Agent

agent = create_agent(
    model=llm,
    tools=[web_search],
    system_prompt=system_prompt,
)

print("\n🎉 Stable Agent Ready!")
print("Try:\n- capital of kerala\n- latest news in kozhikode\n")

# 🔁 Chat Loop

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Exiting...")
        break

    print("\n🤖 Thinking...")

    try:
        response = agent.invoke({
            "messages": user_input
        })

        # Get final response from agent
        print("\n✅ Agent:", response["messages"][-1].content)
        print("-" * 80)

    except Exception:
        print("⚠️ Error, fallback...\n")
        fallback = llm.invoke(user_input)
        print("✅ Fallback:", fallback.content)