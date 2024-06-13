import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage

os.environ["TAVILY_API_KEY"] = "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"

tools = [TavilySearchResults(max_results=1)]


llm = ChatGroq(api_key="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")

prompt = hub.pull("hwchase17/react-chat")

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {
        "input": "我今年幾歲?",
        # Notice that chat_history is a string, since this prompt is aimed at LLMs, not chat models
        "chat_history": "Human: 你好! 我是阮銘福,我今年二十歲\nAI: 你好阮銘福! 很高興認識你!",
    }
)
