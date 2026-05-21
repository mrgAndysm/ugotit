
"""
测试修复后的代码
"""
from dotenv import load_dotenv
load_dotenv()

print("正在导入 Agent...")
from agent import Agent

print("正在初始化 Agent...")
my_agent = Agent()

print("✓ Agent 初始化成功！")
print(f"  加载了 {len(my_agent.tools)} 个工具")
print("\n工具列表:")
for tool in my_agent.tools:
    print(f"  - {tool.name}: {tool.description[:50]}...")

print("\n✓ 所有测试通过！现在可以运行 main.py 了")
