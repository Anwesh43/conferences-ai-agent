from agents.conf_ai_agent import recommendConferences
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = sys.argv[1:]
    asyncio.run(recommendConferences(prompt=prompt))
