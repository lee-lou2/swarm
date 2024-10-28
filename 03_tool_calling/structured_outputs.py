import json
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()


class Tool(BaseModel):
    name: str


tool_info = json.dumps(
    [
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
    ]
)

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "사용자 질문에 맞는 도구를 골라줘. 도구 정보는 아래와 같아."
            + tool_info,
        },
        {
            "role": "user",
            "content": "'안녕하세요, 제 이름은 장승국입니다. 지금은 도구를 호출하는 여러가지 방법에 대해 소개해드리고 있습니다. 감사합니다.' 를 영어로 번역해줘",
        },
    ],
    response_format=Tool,
)

total_tokens = completion.usage.total_tokens
function = completion.choices[0].message.parsed.name

# total_tokens: 361
# function: "translate_kor_to_en"
# arguments: X
print(total_tokens, function)
