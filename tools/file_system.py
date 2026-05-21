
import os
from langchain.tools import tool

@tool
def create_file(file_path: str, content: str) -> str:
    """创建一个新文件并写入内容。当你需要创建一个文件时使用此工具。"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"文件已成功创建在 {file_path}"
    except Exception as e:
        return f"创建文件时出错: {e}"

@tool
def read_file(file_path: str) -> str:
    """读取文件的内容。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"错误: 文件 {file_path} 未找到。"
    except Exception as e:
        return f"读取文件时出错: {e}"

@tool
def update_file(file_path: str, content: str) -> str:
    """向现有文件追加内容。"""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"文件 {file_path} 已成功更新。"
    except FileNotFoundError:
        return f"错误: 文件 {file_path} 未找到。"
    except Exception as e:
        return f"更新文件时出错: {e}"

@tool
def delete_file(file_path: str) -> str:
    """删除一个文件。"""
    try:
        os.remove(file_path)
        return f"文件 {file_path} 已成功删除。"
    except FileNotFoundError:
        return f"错误: 文件 {file_path} 未找到。"
    except Exception as e:
        return f"删除文件时出错: {e}"
