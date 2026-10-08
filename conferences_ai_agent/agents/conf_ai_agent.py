from pydantic_ai import Agent 
from tools.conf_tools import getPhotosForLocation, getConferenceDetails, getConferences, searchForNearestItem
from dotenv import load_dotenv 
from prompts.conf_system_prompt import SYSTEM_PROMPT

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = [getConferences, getConferenceDetails, getPhotosForLocation, searchForNearestItem],
    system_prompt = SYSTEM_PROMPT
)

async def recommendConferences(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')