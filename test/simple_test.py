
"""
简单测试
"""
print("Testing tool_loader...")
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")

print(f"Loaded {len(skills)} skills")
if skills:
    skill = skills[0]
    print(f"Skill name: {skill.name}")
    print(f"Skill type: {type(skill).__name__}")

print("\nTesting Agent import...")
from dotenv import load_dotenv
load_dotenv()
from agent import Agent

print("Creating Agent...")
agent = Agent()
print("OK!")

print(f"\nTotal tools: {len(agent.tools)}")
print("All tools:")
for t in agent.tools:
    print(f"  - {t.name} [{type(t).__name__}]")
