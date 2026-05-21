
import os
from langchain.tools import tool
from config import Config

def _resolve_path(file_path: str, area: str = "auto") -> str:
    """
    解析文件路径
    
    Args:
        file_path: 文件路径
        area: 区域类型，可选值: "user", "workspace", "auto"
              - "user": 强制使用用户区
              - "workspace": 强制使用工作区
              - "auto": 根据路径自动判断（绝对路径直接使用，相对路径默认工作区）
    """
    if os.path.isabs(file_path):
        return file_path
    
    if area == "user":
        return Config.get_user_path(file_path)
    elif area == "workspace":
        return Config.get_workspace_path(file_path)
    else:
        return Config.get_workspace_path(file_path)

def _ensure_dir_exists(file_path: str):
    """确保文件所在目录存在"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

@tool
def create_user_file(file_path: str, content: str) -> str:
    """
    在用户区创建一个新文件并写入内容。当你需要创建用户需要的最终文件时使用此工具。
    文件会被保存到 user/ 目录下。
    """
    try:
        full_path = _resolve_path(file_path, "user")
        _ensure_dir_exists(full_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"用户文件已成功创建在 {full_path}"
    except Exception as e:
        return f"创建用户文件时出错: {e}"

@tool
def create_workspace_file(file_path: str, content: str) -> str:
    """
    在工作区创建一个临时文件并写入内容。当你需要创建临时文件、中间文件或工作文件时使用此工具。
    文件会被保存到 workspace/ 目录下。
    """
    try:
        full_path = _resolve_path(file_path, "workspace")
        _ensure_dir_exists(full_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"工作区文件已成功创建在 {full_path}"
    except Exception as e:
        return f"创建工作区文件时出错: {e}"

@tool
def read_user_file(file_path: str) -> str:
    """读取用户区文件的内容。"""
    try:
        full_path = _resolve_path(file_path, "user")
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"错误: 用户文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'user')}）"
    except Exception as e:
        return f"读取用户文件时出错: {e}"

@tool
def read_workspace_file(file_path: str) -> str:
    """读取工作区文件的内容。"""
    try:
        full_path = _resolve_path(file_path, "workspace")
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"错误: 工作区文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'workspace')}）"
    except Exception as e:
        return f"读取工作区文件时出错: {e}"

@tool
def update_user_file(file_path: str, content: str) -> str:
    """向用户区现有文件追加内容。"""
    try:
        full_path = _resolve_path(file_path, "user")
        _ensure_dir_exists(full_path)
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"用户文件 {full_path} 已成功更新。"
    except FileNotFoundError:
        return f"错误: 用户文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'user')}）"
    except Exception as e:
        return f"更新用户文件时出错: {e}"

@tool
def update_workspace_file(file_path: str, content: str) -> str:
    """向工作区现有文件追加内容。"""
    try:
        full_path = _resolve_path(file_path, "workspace")
        _ensure_dir_exists(full_path)
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"工作区文件 {full_path} 已成功更新。"
    except FileNotFoundError:
        return f"错误: 工作区文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'workspace')}）"
    except Exception as e:
        return f"更新工作区文件时出错: {e}"

@tool
def delete_user_file(file_path: str) -> str:
    """删除用户区的一个文件。"""
    try:
        full_path = _resolve_path(file_path, "user")
        os.remove(full_path)
        return f"用户文件 {full_path} 已成功删除。"
    except FileNotFoundError:
        return f"错误: 用户文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'user')}）"
    except Exception as e:
        return f"删除用户文件时出错: {e}"

@tool
def delete_workspace_file(file_path: str) -> str:
    """删除工作区的一个文件。"""
    try:
        full_path = _resolve_path(file_path, "workspace")
        os.remove(full_path)
        return f"工作区文件 {full_path} 已成功删除。"
    except FileNotFoundError:
        return f"错误: 工作区文件 {file_path} 未找到（完整路径: {_resolve_path(file_path, 'workspace')}）"
    except Exception as e:
        return f"删除工作区文件时出错: {e}"

@tool
def list_user_files(dir_path: str = "") -> str:
    """列出用户区目录下的文件。"""
    try:
        full_path = _resolve_path(dir_path, "user")
        if not os.path.exists(full_path):
            return f"目录不存在: {full_path}"
        files = os.listdir(full_path)
        if not files:
            return f"用户区目录 {full_path} 为空"
        return f"用户区 {full_path} 的文件:\n" + "\n".join(files)
    except Exception as e:
        return f"列出用户文件时出错: {e}"

@tool
def list_workspace_files(dir_path: str = "") -> str:
    """列出工作区目录下的文件。"""
    try:
        full_path = _resolve_path(dir_path, "workspace")
        if not os.path.exists(full_path):
            return f"目录不存在: {full_path}"
        files = os.listdir(full_path)
        if not files:
            return f"工作区目录 {full_path} 为空"
        return f"工作区 {full_path} 的文件:\n" + "\n".join(files)
    except Exception as e:
        return f"列出工作区文件时出错: {e}"

@tool
def create_file(file_path: str, content: str) -> str:
    """
    [已弃用，请使用 create_user_file 或 create_workspace_file]
    创建一个新文件并写入内容。默认创建在工作区。
    """
    return create_workspace_file.invoke({"file_path": file_path, "content": content})

@tool
def read_file(file_path: str) -> str:
    """
    [已弃用，请使用 read_user_file 或 read_workspace_file]
    读取文件的内容。默认从工作区读取。
    """
    return read_workspace_file.invoke({"file_path": file_path})

@tool
def update_file(file_path: str, content: str) -> str:
    """
    [已弃用，请使用 update_user_file 或 update_workspace_file]
    向现有文件追加内容。默认在工作区操作。
    """
    return update_workspace_file.invoke({"file_path": file_path, "content": content})

@tool
def delete_file(file_path: str) -> str:
    """
    [已弃用，请使用 delete_user_file 或 delete_workspace_file]
    删除一个文件。默认在工作区操作。
    """
    return delete_workspace_file.invoke({"file_path": file_path})
