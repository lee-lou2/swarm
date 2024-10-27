from swarm import Swarm, Agent

# Swarm 클라이언트를 생성합니다.
client = Swarm()

# 간단한 에이전트를 정의합니다. 이 에이전트는 모든 메시지에 대해 친절하게 응답합니다.
agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",  # 에이전트의 지시사항을 정의합니다.
)

# 사용자 메시지를 정의합니다. 이 경우, 사용자는 "Hi!"라고 인사합니다.
messages = [{"role": "user", "content": "Hi!"}]

# Swarm 클라이언트를 사용하여 에이전트와의 대화를 시작합니다.
response = client.run(agent=agent, messages=messages)

# 에이전트의 응답을 출력합니다. 사용자가 "Hi!"라고 인사했을 때, 에이전트의 응답을 확인할 수 있습니다.
print(response.messages[-1]["content"])
