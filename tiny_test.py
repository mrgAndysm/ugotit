
from tool_loader import load_markdown_skills
s = load_markdown_skills('skills')
print('Skills loaded:', len(s))
if s:
    print('First skill:', s[0].name)
    try:
        result = s[0].invoke({'input': 'https://www.baidu.com'})
        print('Skill call result:', result)
    except Exception as e:
        print('Error calling skill:', e)
        import traceback
        traceback.print_exc()
