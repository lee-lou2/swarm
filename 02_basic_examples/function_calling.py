from swarm import Swarm, Agent

# Swarm 클라이언트를 생성합니다.
client = Swarm()


# 특정 위치의 날씨 정보를 반환하는 함수입니다.
def get_weather(location) -> str:
    return "{'temp':67, 'unit':'F'}"  # 임의의 날씨 데이터를 반환합니다.


# 에이전트를 정의합니다. 에이전트는 get_weather 함수를 호출할 수 있습니다.
agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",  # 에이전트의 지시사항을 정의합니다.
    functions=[get_weather],  # 에이전트가 사용할 함수 목록을 추가합니다.
)

# 사용자가 뉴욕의 날씨를 물어보는 메시지를 정의합니다.
messages = [{"role": "user", "content": "What's the weather in NYC?"}]

# Swarm 클라이언트를 사용하여 에이전트와의 대화를 시작합니다.
response = client.run(agent=agent, messages=messages)

# 에이전트의 응답을 출력합니다. 이 응답에는 뉴욕의 날씨 정보가 포함됩니다.
print(response.messages[-1]["content"])
