
"""
最小测试用例
"""
print("=== 最小测试 ===\n")

# 1. 先测试一个直接用 @tool 定义的简单工具
from langchain_core.tools import tool
from tools.shell import run_shell_command

@tool
def test_open_browser(input: str) -> str:
    """测试打开浏览器"""
    return run_shell_command(f"start {input}")

# 2. 测试调用这个工具
print("测试直接调用 test_open_browser...")
try:
    result = test_open_browser.invoke({"input": "https://www.baidu.com"})
    print(f"成功! 结果: {result}")
except Exception as e:
    print(f"失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*50)
print("现在测试从 tool_loader 加载的工具...")
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")
if skills:
    loaded_skill = skills[0]
    print(f"已加载: {loaded_skill.name}")
    print(f"类型: {type(loaded_skill).__name__}")
    
    print("\n尝试调用...")
    try:
        result = loaded_skill.invoke({"input": "https://www.baidu.com"})
        print(f"成功! 结果: {result}")
    except Exception as e:
        print(f"失败: {e}")
        import traceback
        traceback.print_exc()
