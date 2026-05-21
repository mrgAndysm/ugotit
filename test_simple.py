
"""
简单测试
"""
print("=== 简单测试 1: 工具导入 ===")
from tools.file_system import create_file, read_file
from tools.shell import run_shell_command

print("  create_file 类型:", type(create_file))
print("  create_file 可调用:", callable(create_file))

print("\n=== 简单测试 2: 尝试两种方案 ===")
print("\n方案 A: 使用 langchain_classic + create_structured_chat_agent")
print("  优点: 旧版 API，更稳定，支持多输入工具")
print("  缺点: 有弃用警告，但不会立即失效")

print("\n方案 B: 调试并修复新 create_agent")
print("  优点: 使用最新 API")
print("  缺点: 可能存在兼容性问题")

print("\n=== 结论建议 ===")
print("  先尝试方案 A（使用 langchain_classic），因为:")
print("  1. 它专门设计用于结构化工具")
print("  2. 我们之前已经有接近可用的版本")
print("  3. 可以快速得到一个工作版本")
