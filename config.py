
import os

class Config:
    """项目配置类"""
    
    # 基础目录
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # 用户区目录 - 存放用户需要的文件
    USER_DIR = os.path.join(BASE_DIR, "user")
    
    # 工作区目录 - 存放临时文件和中间产物
    WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")
    
    @classmethod
    def init_directories(cls):
        """初始化必要的目录"""
        os.makedirs(cls.USER_DIR, exist_ok=True)
        os.makedirs(cls.WORKSPACE_DIR, exist_ok=True)
    
    @classmethod
    def get_user_path(cls, filename: str) -> str:
        """获取用户区文件的完整路径"""
        return os.path.join(cls.USER_DIR, filename)
    
    @classmethod
    def get_workspace_path(cls, filename: str) -> str:
        """获取工作区文件的完整路径"""
        return os.path.join(cls.WORKSPACE_DIR, filename)
