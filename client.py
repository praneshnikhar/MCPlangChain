from langchain_mcp_adapters import MCPToolkit
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather":{
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            },
        }
    )
    import os
    os.environ["Groq_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(
        model, tools
    )