from swarm import Swarm, Agent

# Swarm 클라이언트를 생성합니다.
client = Swarm()

# 영어 에이전트를 정의합니다. 이 에이전트는 영어로만 응답하도록 설정됩니다.
english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",  # 에이전트의 지시사항을 정의합니다.
)

# 스페인어 에이전트를 정의합니다. 이 에이전트는 스페인어로만 응답하도록 설정됩니다.
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",  # 에이전트의 지시사항을 정의합니다.
)


# 이 함수는 스페인어 사용자에게서 메시지가 들어올 때,
# 대화를 스페인어 에이전트로 이관합니다.
def transfer_to_spanish_agent():
    """Transfer Spanish-speaking users immediately."""
    return spanish_agent  # 스페인어 에이전트를 반환하여 대화를 이관합니다.


# 영어 에이전트에 이관 기능을 추가합니다.
english_agent.functions.append(transfer_to_spanish_agent)

# 사용자 메시지를 정의합니다. 이 경우, 사용자는 스페인어로 인사합니다.
messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]

# Swarm 클라이언트를 사용하여 영어 에이전트와의 대화를 시작합니다.
# 대화 도중 스페인어 메시지가 감지되면, 스페인어 에이전트로 이관됩니다.
response = client.run(agent=english_agent, messages=messages)

# 최종 응답을 출력합니다. 이 응답은 스페인어 에이전트에서 생성됩니다.
print(response.messages[-1]["content"])
