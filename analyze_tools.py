
"""
详细分析工具类型问题
"""
print("=== 工具类型分析 ===\n")

# 1. 分析 file_system 工具
print("1. 分析 file_system 工具:")
from tools.file_system import create_file
print(f"   create_file 类型: {type(create_file)}")
print(f"   create_file 类名: {create_file.__class__.__name__}")
print(f"   create_file 是否有 invoke 方法: {hasattr(create_file, 'invoke')}")
print(f"   create_file 是否有 func 属性: {hasattr(create_file, 'func')}")
if hasattr(create_file, 'func'):
    print(f"   create_file.func 类型: {type(create_file.func)}")
    print(f"   create_file.func 是否可调用: {callable(create_file.func)}")

print("\n2. 分析 tool_loader 工具:")
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")
if skills:
    skill = skills[0]
    print(f"   Skill 类型: {type(skill)}")
    print(f"   Skill 类名: {skill.__class__.__name__}")
    print(f"   Skill 是否有 invoke 方法: {hasattr(skill, 'invoke')}")
    print(f"   Skill 是否有 func 属性: {hasattr(skill, 'func')}")
    if hasattr(skill, 'func'):
        print(f"   Skill.func 类型: {type(skill.func)}")
        print(f"   Skill.func 是否可调用: {callable(skill.func)}")

print("\n3. 检查两者是否是同一类型:")
print(f"   类型相同: {type(create_file) == type(skill)}")
print(f"   基类相同: {create_file.__class__.__base__ == skill.__class__.__base__}")

print("\n4. 检查导入来源:")
import langchain.tools
import langchain_core.tools
print(f"   langchain.tools.Tool: {hasattr(langchain.tools, 'Tool')}")
print(f"   langchain_core.tools.Tool: {hasattr(langchain_core.tools, 'Tool')}")
print(f"   langchain_core.tools.StructuredTool: {hasattr(langchain_core.tools, 'StructuredTool')}")

print("\n=== 结论 ===")
print("问题很可能在于: tool_loader.py 使用的 Tool 类与 @tool 装饰器创建的工具类型不一致！")
