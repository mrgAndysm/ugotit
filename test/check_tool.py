
print('--- Checking Tool location ---')
try:
    from langchain.tools import Tool
    print('[OK] Tool from langchain.tools')
except ImportError:
    print('[FAIL] Tool not in langchain.tools')
    try:
        from langchain_core.tools import Tool
        print('[OK] Tool from langchain_core.tools')
    except ImportError:
        print('[FAIL] Tool not found')

print('\n--- Checking @tool decorator ---')
try:
    from langchain.tools import tool
    print('[OK] tool decorator from langchain.tools')
except ImportError:
    print('[FAIL] tool decorator not in langchain.tools')
    try:
        from langchain_core.tools import tool
        print('[OK] tool decorator from langchain_core.tools')
    except ImportError:
        print('[FAIL] tool decorator not found')
