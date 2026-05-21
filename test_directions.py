
"""
测试不同的修复方向
"""
import sys
print("=== 测试 1: 检查工具导入和类型 ===\n")

# 检查当前工具的导入
try:
    from tools.file_system import create_file, read_file, update_file, delete_file
    from tools.shell import run_shell_command
    
    print("✓ 工具导入成功")
    print(f"  create_file 类型: {type(create_file)}")
    print(f"  create_file 是否可调用: {callable(create_file)}")
    
    # 测试直接调用工具
    try:
        result = read_file("requirements.txt")
        print(f"✓ 工具直接调用成功: {result[:50]}...")
    except Exception as e:
        print(f"✗ 工具直接调用失败: {e}")
        
except Exception as e:
    print(f"✗ 工具导入失败: {e}")
    import traceback
    traceback.print_exc()


print("\n=== 测试 2: 检查 langchain_classic 的 create_structured_chat_agent ===\n")

try:
    from langchain_classic.agents import create_structured_chat_agent, AgentExecutor
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_openai import ChatOpenAI
    from langchain_core.tools import tool
    
    print("✓ 导入成功")
    
    # 创建简单的测试工具
    @tool
    def test_tool(input: str) -> str:
        """测试工具"""
        return f"测试结果: {input}"
    
    @tool
    def multi_input_tool(a: int, b: int) -> str:
        """多输入工具，测试加法"""
        return str(a + b)
    
    tools = [test_tool, multi_input_tool]
    
    print(f"✓ 创建工具成功，工具数量: {len(tools)}")
    
    # 创建简单的 LLM（不需要真实 API 密钥）
    llm = ChatOpenAI(model="fake-model", api_key="fake-key", base_url="http://localhost:0")
    
    # 创建提示模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    print("✓ 创建提示模板成功")
    
    # 尝试创建 agent
    agent = create_structured_chat_agent(llm, tools, prompt)
    print("✓ create_structured_chat_agent 调用成功")
    
    # 创建 executor
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    print("✓ AgentExecutor 创建成功")
    
    print("\n结论: create_structured_chat_agent 看起来支持多输入工具！")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()


print("\n=== 测试 3: 检查新 create_agent 的工具兼容性 ===\n")

try:
    from langchain.agents import create_agent
    from langgraph.checkpoint.memory import InMemorySaver
    from langchain_openai import ChatOpenAI
    from langchain_core.tools import tool
    
    print("✓ 导入成功")
    
    # 创建测试工具
    @tool
    def simple_tool(input: str) -> str:
        """简单工具"""
        return f"处理了: {input}"
    
    @tool
    def complex_tool(name: str, value: int) -> str:
        """复杂工具，多输入"""
        return f"{name}: {value}"
    
    tools = [simple_tool, complex_tool]
    
    print(f"✓ 创建工具成功")
    print(f"  工具 1 类型: {type(tools[0])}")
    print(f"  工具 2 类型: {type(tools[1])}")
    
    # 创建 LLM
    llm = ChatOpenAI(model="test", api_key="test", base_url="http://test")
    
    # 创建 agent
    checkpointer = InMemorySaver()
    agent = create_agent(
        llm,
        tools=tools,
        system_prompt="You are helpful.",
        checkpointer=checkpointer
    )
    
    print("✓ create_agent 创建成功")
    print("\n结论: 新 create_agent 也接受用 @tool 装饰的工具！")
    
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()


print("\n=== 测试 4: 检查 tool_loader.py 中的工具 ===\n")

try:
    from tool_loader import load_markdown_skills
    
    skills = load_markdown_skills("skills")
    print(f"✓ 加载了 {len(skills)} 个 skill")
    
    if skills:
        skill = skills[0]
        print(f"  Skill 类型: {type(skill)}")
        print(f"  Skill 名称: {skill.name}")
        print(f"  Skill 是否可调用: {callable(skill)}")
        
except Exception as e:
    print(f"✗ 测试失败: {e}")
    import traceback
    traceback.print_exc()


print("\n" + "="*60)
print("验证完成！")
