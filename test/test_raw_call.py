
"""
测试直接调用 open_browser 工具
"""
print("=== 测试直接调用工具 ===\n")

from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")
open_browser = skills[0]

print("工具加载成功:", open_browser.name)

print("\n测试 1: 正常输入（没有反引号）")
try:
    result = open_browser.invoke({"input": "https://www.baidu.com"})
    print("成功！结果:", result)
except Exception as e:
    print("错误:", e)
    import traceback
    traceback.print_exc()

print("\n测试 2: 带反引号的输入（像你遇到的情况）")
try:
    result = open_browser.invoke({"input": " `https://www.baidu.com` "})
    print("成功！结果:", result)
except Exception as e:
    print("错误:", e)
    import traceback
    traceback.print_exc()
