
import subprocess
from langchain.tools import tool

def _run_shell_command_impl(command: str) -> str:
    """实际执行 shell 命令的内部函数（普通函数，可直接调用）"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        output = result.stdout
        if not output.strip():
            return "命令执行成功，但没有产生输出。"
        return output
    except subprocess.CalledProcessError as e:
        return f"命令执行失败，错误: {e}\nStderr: {e.stderr}"
    except Exception as e:
        return f"执行命令时发生未知错误: {e}"

@tool
def run_shell_command(command: str) -> str:
    """执行一个系统命令并返回其输出。
    用于系统级操作，我是windows系统。
    例如，要列出文件，请使用 'ls -l' 或 'dir'。"""
    return _run_shell_command_impl(command)
