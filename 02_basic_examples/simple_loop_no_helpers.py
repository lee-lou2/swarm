from swarm import Swarm, Agent

# Swarm 클라이언트를 생성합니다.
client = Swarm()

# 에이전트를 정의합니다. 사용자가 입력한 메시지에 대해 응답합니다.
my_agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",  # 에이전트의 지시사항을 정의합니다.
)


# 메시지를 출력하는 함수입니다. 각 메시지를 포맷에 맞게 출력합니다.
def pretty_print_messages(messages):
    for message in messages:
        if message["content"] is None:
            continue  # 메시지가 비어 있으면 건너뜁니다.
        print(
            f"{message['sender']}: {message['content']}"
        )  # 메시지의 내용을 출력합니다.


# 사용자와의 대화를 저장할 리스트를 초기화합니다.
messages = []
agent = my_agent  # 초기 에이전트 설정

# 사용자와의 상호작용을 위한 무한 루프를 시작합니다.
while True:
    user_input = input("> ")  # 사용자의 입력을 받습니다.
    messages.append(
        {"role": "user", "content": user_input}
    )  # 사용자의 메시지를 리스트에 추가합니다.

    # Swarm 클라이언트를 사용하여 에이전트와의 대화를 진행합니다.
    response = client.run(agent=agent, messages=messages)
    messages = response.messages  # 최신 메시지 상태를 업데이트합니다.
    agent = response.agent  # 현재 활성화된 에이전트를 업데이트합니다.

    # 대화 내용을 출력합니다.
    pretty_print_messages(messages)
