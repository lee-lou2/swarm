import openai
from swarm import Swarm, Agent

# Ollama
model = "llama3.2"

llm_client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
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
