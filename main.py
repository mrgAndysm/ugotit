
from agent import Agent
from dotenv import load_dotenv
import os

def main():
    """主函数，运行 Agent 的命令行界面。"""
    # 从 .env 文件加载环境变量
    load_dotenv()

    # 检查 API 密钥是否已设置
    if not os.getenv("DEEPSEEK_API_KEY"):
        print("错误: 未在环境变量中找到 DEEPSEEK_API_KEY。")
        print("请确保您的 .env 文件包含了 DEEPSEEK_API_KEY, DEEPSEEK_MODEL, 和 DEEPSEEK_API_BASE。")
        return

    my_agent = Agent()
    
    print("欢迎使用 Langchain ReAct Agent!")
    print("您可以输入 'exit' 来退出程序。")
    print("可用工具:")
    for tool in my_agent.tools:
        print(f"  - {tool.name}: {tool.description}")
    
    while True:
        try:
            user_request = input("\n请输入您的指令: ")
            if user_request.lower() == 'exit':
                print("感谢使用，再见!")
                break
            
            if not user_request:
                continue
                
            result = my_agent.run(user_request)
            print(f"\n[最终答案]\n{result}")
            
        except KeyboardInterrupt:
            print("\n检测到中断，正在退出...")
            break
        except Exception as e:
            print(f"发生意外错误: {e}")

if __name__ == "__main__":
    main()
