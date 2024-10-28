from openai import OpenAI

client = OpenAI()


messages = [
    {
        "role": "user",
        "content": "'안녕하세요, 제 이름은 장승국입니다. 지금은 도구를 호출하는 여러가지 방법에 대해 소개해드리고 있습니다. 감사합니다.' 를 영어로 번역해줘",
    },
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=[
        {
            "type": "function",
            "function": {
                "name": "translate_kor_to_en",
                "description": "한국어를 영어로 번역",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "번역할 한국어 텍스트",
                        },
                    },
                    "required": ["text"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "translate_en_to_kor",
                "description": "영어를 한국어로 번역",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "번역할 영어 텍스트"},
                    },
                    "required": ["text"],
                },
            },
        },
    ],
)

# 총 토큰 수
total_tokens = response.usage.total_tokens
# 함수 및 인자 정보
function = response.choices[0].message.tool_calls[0].function.name
arguments = response.choices[0].message.tool_calls[0].function.arguments

# total_tokens: 178
# function: "translate_kor_to_en"
# arguments: {"text": "안녕하세요, 제 이름은 장승국입니다. 지금은 도구를 호출하는 여러가지 방법에 대해 소개해드리고 있습니다. 감사합니다."}
print(total_tokens, function)
