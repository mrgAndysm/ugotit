
import langchain
import langchain_core
import langchain_classic

print('langchain version:', langchain.__version__)
print('langchain_core version:', langchain_core.__version__)
print('langchain_classic version:', langchain_classic.__version__)

# 检查 create_react_agent 位置
print('\n--- 检查 create_react_agent ---')
try:
    from langchain.agents import create_react_agent
    print('✓ create_react_agent from langchain.agents')
except ImportError:
    print('✗ create_react_agent not in langchain.agents')
    try:
        from langchain_classic.agents import create_react_agent
        print('✓ create_react_agent from langchain_classic.agents')
    except ImportError:
        print('✗ create_react_agent not found')

# 检查 AgentExecutor 位置
print('\n--- 检查 AgentExecutor ---')
try:
    from langchain.agents import AgentExecutor
    print('✓ AgentExecutor from langchain.agents')
except ImportError:
    print('✗ AgentExecutor not in langchain.agents')

# 检查 ChatPromptTemplate
print('\n--- 检查 ChatPromptTemplate ---')
try:
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    print('✓ ChatPromptTemplate and MessagesPlaceholder from langchain_core.prompts')
except ImportError:
    print('✗ ChatPromptTemplate not in langchain_core.prompts')

# 检查 ConversationBufferWindowMemory
print('\n--- 检查 ConversationBufferWindowMemory ---')
try:
    from langchain.memory import ConversationBufferWindowMemory
    print('✓ ConversationBufferWindowMemory from langchain.memory')
except ImportError:
    try:
        from langchain_core.memory import ConversationBufferWindowMemory
        print('✓ ConversationBufferWindowMemory from langchain_core.memory')
    except ImportError:
        try:
            from langchain_classic.memory import ConversationBufferWindowMemory
            print('✓ ConversationBufferWindowMemory from langchain_classic.memory')
        except ImportError:
            print('✗ ConversationBufferWindowMemory not found')
