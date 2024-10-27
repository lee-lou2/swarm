import os

import openai
from swarm import Swarm, Agent

# Groq
model = "llama3-groq-70b-8192-tool-use-preview"

llm_client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
)


swarm_client = Swarm(client=llm_client)

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
    model=model,
    tool_choice="auto",
)

messages = [{"role": "user", "content": "Hi!"}]
response = swarm_client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
