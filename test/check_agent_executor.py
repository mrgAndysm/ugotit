
print('--- Checking AgentExecutor location ---')
try:
    from langchain.agents import AgentExecutor
    print('[OK] AgentExecutor from langchain.agents')
except ImportError:
    print('[FAIL] AgentExecutor not in langchain.agents')
    try:
        from langchain_classic.agents import AgentExecutor
        print('[OK] AgentExecutor from langchain_classic.agents')
    except ImportError:
        print('[FAIL] AgentExecutor not found in langchain_classic.agents')
        try:
            from langchain_core.agents import AgentExecutor
            print('[OK] AgentExecutor from langchain_core.agents')
        except ImportError:
            print('[FAIL] AgentExecutor not found')
