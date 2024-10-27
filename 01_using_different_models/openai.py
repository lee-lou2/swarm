from swarm import Swarm, Agent


swarm_client = Swarm()

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
    model=model,
    tool_choice="auto",
)

messages = [{"role": "user", "content": "Hi!"}]
response = swarm_client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
