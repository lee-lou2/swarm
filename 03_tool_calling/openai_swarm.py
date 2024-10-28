from swarm import Swarm, Agent


swarm_client = Swarm()


def translate_kor_to_en_tool(text: str):
    """한국어를 영어로 번역"""
    return "한국어를 영어로 번역하는 함수입니다"


def translate_en_to_kor_tool(text: str):
    """영어를 한국어로 번역"""
    return "영어를 한국어로 번역하는 함수입니다"


agent = Agent(
    name="Translate Agent",
    instructions="입력된 내용에 맞게 번역해줘.",
    model="gpt-4o-mini",
    functions=[translate_kor_to_en_tool, translate_en_to_kor_tool],
)

messages = [
    {
        "role": "user",
        "content": "'안녕하세요, 제 이름은 장승국입니다. 지금은 도구를 호출하는 여러가지 방법에 대해 소개해드리고 있습니다. 감사합니다.' 를 영어로 번역해줘",
    }
]
response = swarm_client.run(agent=agent, messages=messages, max_turns=1)

translated_text = response.messages[-1]["content"]

# total_tokens: 알 수 없음
# function: "translate_kor_to_en"
# arguments: "안녕하세요, 제 이름은 장승국입니다. 지금은 도구를 호출하는 여러가지 방법에 대해 소개해드리고 있습니다. 감사합니다."
# 도구로부터 얻은 답변을 해줌
print(translated_text)
