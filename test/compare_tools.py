
"""
对比两种工具的详细区别
"""
print("=== 详细对比工具 ===\n")

# 1. 获取两种工具
from tools.file_system import read_file
from tool_loader import load_markdown_skills
skills = load_markdown_skills("skills")
open_browser = skills[0]

print("工具 1: read_file (@tool 装饰器)")
print(f"  类型: {type(read_file)}")
print(f"  类名: {read_file.__class__.__name__}")
print(f"  模块: {read_file.__class__.__module__}")

print("\n工具 2: open_browser (StructuredTool.from_function)")
print(f"  类型: {type(open_browser)}")
print(f"  类名: {open_browser.__class__.__name__}")
print(f"  模块: {open_browser.__class__.__module__}")

print("\n=== 检查关键属性 ===")

def check_tool_attrs(tool_obj, name):
    print(f"\n{name}:")
    attrs = ['func', 'args_schema', 'name', 'description', '_run']
    for attr in attrs:
        has_attr = hasattr(tool_obj, attr)
        print(f"  {attr}: {has_attr}", end="")
        if has_attr:
            val = getattr(tool_obj, attr)
            if callable(val):
                print(f" [可调用]", end="")
            print(f" - {type(val).__name__}")

check_tool_attrs(read_file, "read_file (@tool)")
check_tool_attrs(open_browser, "open_browser (from_function)")

print("\n=== 测试直接调用 ===")
print("尝试调用 .invoke(...) 方法...")
try:
    # 用一个安全的测试
    result = read_file.invoke({"file_path": "requirements.txt"})
    print(f"read_file.invoke 成功！返回: {result[:30]}...")
except Exception as e:
    print(f"read_file.invoke 错误: {e}")
    import traceback
    traceback.print_exc()

print("\n尝试调用 open_browser.invoke(...)...")
try:
    # 不实际打开浏览器，只是测试
    # 我们可以检查 invoke 方法是否存在且可调用
    print(f"open_browser.invoke 是否可调用: {callable(getattr(open_browser, 'invoke', None))}")
    # 检查 __call__ 方法
    print(f"open_browser 是否可直接调用: {callable(open_browser)}")
except Exception as e:
    print(f"错误: {e}")

print("\n=== 查看 MRO (方法解析顺序) ===")
print(f"read_file 类 MRO: {[c.__name__ for c in type(read_file).__mro__]}")
print(f"open_browser 类 MRO: {[c.__name__ for c in type(open_browser).__mro__]}")

print("\n=== 结论 ===")
print("让我们尝试另一种方法：直接用 @tool 装饰器来重写 tool_loader！")
