from google.adk.agents import Agent


root_agent = Agent(
    name='todo_assistant',
    model='gemini-2.0-flash',
    description=('Agent to answer questions about my TODO list.'),
    instruction=('You are a helpful agent who can answer user questions their TODO list.'),
    tools=[],
)
