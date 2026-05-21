
import os
import re
import yaml
from langchain_core.tools import tool
from tools.shell import _run_shell_command_impl

# 使用 @tool 装饰器来创建，这样与 file_system.py 的工具类型完全一致

def load_markdown_skills(directory: str = "skills") -> list:
    """从指定目录加载基于 Markdown 的技能。"""
    tools = []
    if not os.path.isdir(directory):
        return tools

    for filename in os.listdir(directory):
        if not filename.endswith(".md"):
            continue
        
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            # 使用正则表达式从 Markdown 中提取元数据和 shell 命令
            match = re.search(r'---\n(.*?)\n---\s*```shell\n(.*?)\n```', content, re.DOTALL)
            if not match:
                continue

            meta = yaml.safe_load(match.group(1))
            command_template = match.group(2).strip()

            name = meta.get("name")
            description = meta.get("description")

            # 确保 Markdown 文件格式正确
            if not name or not description or '{{input}}' not in command_template:
                print(f"[警告] 跳过格式不正确的 skill 文件: {filename}")
                continue

            # 使用 exec 动态创建函数，避免闭包问题
            # 这样创建的工具与 file_system.py 的 @tool 装饰器方式完全一致
            tool_code = f'''
import re
from tools.shell import _run_shell_command_impl
from langchain_core.tools import tool

@tool("{name}")
def {name}(input: str) -> str:
    """{description} 工具的输入应该是一个字符串。"""
    command = {repr(command_template)}.replace('{{{{input}}}}', input)
    return _run_shell_command_impl(command)
'''
            # 在局部命名空间中执行
            local_vars = {}
            exec(tool_code, globals(), local_vars)
            
            # 获取创建的工具
            new_tool = local_vars[name]
            tools.append(new_tool)
            
        except Exception as e:
            print(f"加载 skill {filename} 时出错: {e}")
            import traceback
            traceback.print_exc()
    
    return tools
