
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.tools import tool
import os

# 创建一个简单的测试工具
@tool
def test_tool(input: str) -> str:
    """测试工具"""
    return f"工具执行结果: {input}"

tools = [test_tool]

# 查看 create_react_agent 的文档
import inspect
print("create_react_agent signature:")
print(inspect.signature(create_react_agent))
print("\n---")

# 尝试创建一个简单的 Agent
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key="test", base_url="https://example.com")

# 尝试不同的 prompt 模板
# 方法1: 标准的 langchain_classic ReAct 模板
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentType, initialize_agent

print("\nTrying initialize_agent...")
try:
    memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)
    agent_executor = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True
    )
    print("[OK] initialize_agent works")
except Exception as e:
    print(f"[FAIL] initialize_agent error: {e}")
    import traceback
    traceback.print_exc()
