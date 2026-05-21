
import os
from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_structured_chat_agent, AgentExecutor
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.file_system import (
    create_user_file, read_user_file, update_user_file, delete_user_file,
    create_workspace_file, read_workspace_file, update_workspace_file, delete_workspace_file,
    list_user_files, list_workspace_files,
    create_file, read_file, update_file, delete_file
)
from tools.shell import run_shell_command
from tool_loader import load_markdown_skills
from config import Config

class Agent:
    def __init__(self):
        # 初始化目录
        Config.init_directories()
        
        # 从环境变量中读取 DeepSeek 配置
        api_key = os.getenv("DEEPSEEK_API_KEY")
        model_name = os.getenv("DEEPSEEK_MODEL")
        base_url = os.getenv("DEEPSEEK_API_BASE")

        self.llm = ChatOpenAI(
            model=model_name,
            api_key=api_key,
            base_url=base_url,
            temperature=0
        )
        
        # 加载 Python 定义的工具
        python_tools = [
            create_user_file,
            read_user_file,
            update_user_file,
            delete_user_file,
            list_user_files,
            create_workspace_file,
            read_workspace_file,
            update_workspace_file,
            delete_workspace_file,
            list_workspace_files,
            create_file,
            read_file,
            update_file,
            delete_file,
            run_shell_command,
        ]
        
        # 加载 Markdown 定义的工具
        markdown_tools = load_markdown_skills("skills")
        
        self.tools = python_tools + markdown_tools
        
        # 系统提示词
        system_message = '''Respond to the human as helpfully and accurately as possible.
You are operating on a Windows operating system.
You MUST use Windows-compatible shell commands. For example, to list files, use `dir`, not `ls`.

重要：文件区域划分说明
========================
1. 用户区（user/）
   - 用途：存放用户需要的最终文件、成果文件
   - 何时使用：当用户明确要求创建文件，或创建的文件是给用户的最终产物时
   - 对应工具：create_user_file, read_user_file, update_user_file, delete_user_file, list_user_files

2. 工作区（workspace/）
   - 用途：存放临时文件、中间产物、工作文件
   - 何时使用：需要临时存储、调试、处理中间结果时
   - 对应工具：create_workspace_file, read_workspace_file, update_workspace_file, delete_workspace_file, list_workspace_files

使用原则：
- 先判断文件性质：是用户需要的最终成果，还是临时工作文件
- 用户明确要求的文件 → 用户区
- 临时处理、中间结果 → 工作区
- 不确定时优先使用工作区

You have access to the following tools:
{tools}

Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).

Valid "action" values: "Final Answer" or {tool_names}

Provide only ONE action per $JSON_BLOB.

Follow this format:

Question: input question to answer
Thought: consider previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
Action:
```
{{
    "action": "Final Answer",
    "action_input": "Final response to human"
}}
```

Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate.'''

        # 创建提示模板
        human_template = '''{input}

{agent_scratchpad}

(reminder to respond in a JSON blob no matter what)'''

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_message),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", human_template),
        ])
        
        # 创建记忆
        memory = ConversationBufferWindowMemory(
            k=10,
            memory_key="chat_history",
            return_messages=True
        )
        
        # 创建 agent
        agent = create_structured_chat_agent(self.llm, self.tools, prompt)
        
        # 创建 executor
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            memory=memory,
            verbose=True,
            handle_parsing_errors=True
        )

    def run(self, user_request: str):
        """
        使用给定的用户请求运行 Agent。
        """
        response = self.agent_executor.invoke({"input": user_request})
        return response["output"]
