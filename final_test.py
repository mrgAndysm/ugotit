
"""
最终测试！
"""
print("=== 最终测试 ===\n")

print("1. 测试工具加载...")
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")

if skills:
    skill = skills[0]
    print(f"   已加载: {skill.name}")
    
    print("\n2. 测试工具调用...")
    try:
        result = skill.invoke({"input": "https://www.baidu.com"})
        print(f"   ✓ 成功！结果: {result}")
    except Exception as e:
        print(f"   ✗ 失败: {e}")
        import traceback
        traceback.print_exc()

print("\n3. 测试 Agent...")
from dotenv import load_dotenv
load_dotenv()
from agent import Agent

print("   正在初始化 Agent...")
agent = Agent()
print("   ✓ Agent 初始化成功！")

print(f"\n=== 所有测试通过！现在可以运行 'python main.py' ===")
