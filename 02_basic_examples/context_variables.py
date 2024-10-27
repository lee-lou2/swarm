from swarm import Swarm, Agent

# Swarm 클라이언트를 생성합니다.
client = Swarm()


# 지시사항을 정의하는 함수입니다. 사용자 이름을 참조하여 맞춤형 인사말을 생성합니다.
def instructions(context_variables):
    name = context_variables.get(
        "name", "User"
    )  # context_variables에서 사용자 이름을 가져옵니다.
    return f"You are a helpful agent. Greet the user by name ({name})."


# 사용자 계정 정보를 출력하는 함수입니다.
def print_account_details(context_variables: dict):
    user_id = context_variables.get(
        "user_id", None
    )  # context_variables에서 사용자 ID를 가져옵니다.
    name = context_variables.get(
        "name", None
    )  # context_variables에서 사용자 이름을 가져옵니다.
    print(f"Account Details: {name} {user_id}")  # 계정 정보를 출력합니다.
    return "Success"  # 함수 호출 결과를 반환합니다.


# 에이전트를 정의합니다. 지시사항과 함께 사용자 계정 정보를 출력하는 기능을 포함합니다.
agent = Agent(
    name="Agent",
    instructions=instructions,  # 지시사항 함수를 설정합니다.
    functions=[print_account_details],  # 에이전트가 호출할 수 있는 함수를 등록합니다.
)

# 사용자 정보를 담은 컨텍스트 변수를 정의합니다.
context_variables = {"name": "James", "user_id": 123}

# Swarm 클라이언트를 사용하여 사용자 인사 메시지에 대한 응답을 생성합니다.
response = client.run(
    messages=[{"role": "user", "content": "Hi!"}],
    agent=agent,
    context_variables=context_variables,  # 컨텍스트 변수를 전달합니다.
)
# 에이전트의 인사 응답을 출력합니다.
print(response.messages[-1]["content"])

# 사용자 요청에 따라 계정 정보를 출력하는 명령을 실행합니다.
response = client.run(
    messages=[{"role": "user", "content": "Print my account details!"}],
    agent=agent,
    context_variables=context_variables,
)
# 에이전트의 응답을 출력합니다.
print(response.messages[-1]["content"])
