
"""
最终测试
"""
from dotenv import load_dotenv
load_dotenv()

print("Importing Agent...")
from agent import Agent

print("Initializing Agent...")
my_agent = Agent()

print("OK - Agent initialized successfully!")
print(f"Loaded {len(my_agent.tools)} tools")
print("\nTool list:")
for tool in my_agent.tools:
    print(f"  - {tool.name}")

print("\nDone! You can now run 'python main.py'")
