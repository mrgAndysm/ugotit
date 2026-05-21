
"""
深入分析工具调用问题
"""
print("=== 深入分析 ===\n")

# 查看两类工具的实际差异
from tools.file_system import create_file
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")
open_browser = skills[0]

print("1. StructuredTool (create_file):")
print(f"   - 输入模式: {create_file.args_schema if hasattr(create_file, 'args_schema') else 'N/A'}")
print(f"   - 是否结构化: {hasattr(create_file, 'args_schema')}")

print("\n2. Simple Tool (open_browser):")
print(f"   - 输入模式: {open_browser.args_schema if hasattr(open_browser, 'args_schema') else 'N/A'}")
print(f"   - 是否结构化: {hasattr(open_browser, 'args_schema')}")

print("\n3. 测试 invoke 方法:")
print("   - StructuredTool.invoke 应该可以工作")
print("   - 问题可能在于: create_structured_chat_agent 期望所有工具都是 StructuredTool")

print("\n4. 问题根源:")
print("   - 我们混合了两种工具类型:")
print("     * StructuredTool (来自 @tool 装饰器，多输入)")
print("     * Tool (来自 tool_loader.py，单输入)")
print("   - create_structured_chat_agent 可能期望所有工具都是 StructuredTool")

print("\n=== 解决方案思路 ===")
print("让 tool_loader.py 也创建 StructuredTool 而不是简单的 Tool！")
