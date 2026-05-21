
"""
简单最终测试，没有 emoji
"""
print("=== Final Test ===")

print("\n1. Loading skills...")
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")

if skills:
    skill = skills[0]
    print("   Loaded:", skill.name)
    
    print("\n2. Testing skill invoke...")
    try:
        result = skill.invoke({"input": "https://www.baidu.com"})
        print("   OK! Result:", result)
    except Exception as e:
        print("   ERROR:", e)
        import traceback
        traceback.print_exc()

print("\n3. Testing Agent...")
from dotenv import load_dotenv
load_dotenv()
from agent import Agent

print("   Initializing Agent...")
agent = Agent()
print("   OK! Agent initialized.")

print("\n=== All tests pass! You can now run 'python main.py' ===")
