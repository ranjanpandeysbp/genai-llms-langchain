locations = [
    'from langgraph.prebuilt import create_react_agent',
    'from langchain.agents import create_react_agent',
    'from langchain.agents.react.agent import create_react_agent',
    'from langchain_core.agents import create_react_agent',
]
for loc in locations:
    try:
        exec(loc)
        print(f'WORKS: {loc}')
    except ImportError as e:
        print(f'FAIL: {loc} => {e}')