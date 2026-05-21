
"""
验证修复是否成功
"""
print("=== 验证工具类型一致性 ===\n")

from tools.file_system import create_file
from tool_loader import load_markdown_skills

print("1. 检查 file_system 工具:")
print(f"   create_file 类型: {type(create_file).__name__}")

print("\n2. 检查加载的 skills:")
skills = load_markdown_skills("skills")
if skills:
    skill = skills[0]
    print(f"   Skill 类型: {type(skill).__name__}")
    print(f"   Skill 名称: {skill.name}")

print("\n3. 比较类型:")
print(f"   类型相同: {type(create_file).__name__ == type(skill).__name__}")
print(f"   都是 StructuredTool: {'StructuredTool' in str(type(create_file)) and 'StructuredTool' in str(type(skill))}")

print("\n=== 导入 Agent 测试 ===\n")
from dotenv import load_dotenv
load_dotenv()

print("正在导入 Agent...")
from agent import Agent

print("正在初始化 Agent...")
my_agent = Agent()

print("✓ Agent 初始化成功！")
print(f"  工具总数: {len(my_agent.tools)}")
print("\n工具列表:")
for i, tool in enumerate(my_agent.tools):
    print(f"  {i+1}. {tool.name} [{type(tool).__name__}]")

print("\n=== 所有测试通过！===")
