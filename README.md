## OpenAI Swarm Notes

**OpenAI Swarm Notes** 저장소에 오신 것을 환영합니다! 이 저장소는 OpenAI의 실험적 멀티 에이전트 오케스트레이션 프레임워크인 Swarm을 활용한 다양한 예제를 제공합니다. 여러 에이전트를 조정하고 관리하는 방법에 관심이 있다면, 이 저장소가 좋은 출발점이 될 것입니다.

자세한 설명과 심화된 가이드는 [블로그](https://roughly.kr/)에서 확인하세요.

### 예제 목록

| 예제 폴더 | 설명 |
| -------- | ---- |
| [01_using_different_models](https://github.com/lee-lou2/swarm/tree/main/01_using_different_models) | OpenAI 모델 외에도 Groq, Ollama와 같은 외부 모델과 Swarm을 사용하는 방법을 다룹니다. |

### Swarm 소개

Swarm은 OpenAI에서 제공하는 실험적 프레임워크로, 가벼운 멀티 에이전트 시스템을 탐구할 수 있게 합니다. 이 프레임워크는 교육 목적으로 설계되었으며, 에이전트 간의 **handoff(전달)**와 **routines(루틴)** 패턴을 이해하는 데 도움이 됩니다. 상업적 사용을 위한 것은 아니지만, 멀티 에이전트 오케스트레이션에 관심이 있는 개발자에게 유용한 학습 도구입니다.

### 시작하기

각 예제 폴더에는 Swarm을 설정하고 사용하는 방법이 자세히 설명되어 있습니다. 아래 단계를 통해 원하는 예제의 설정을 따라 해 보세요:

1. 해당 예제 폴더로 이동합니다.
2. `requirements.txt`를 사용해 필요한 패키지를 설치합니다.
3. 폴더 내의 `README` 파일을 참고하여 예제를 실행하세요.

```bash
# 예시: 특정 예제로 이동
cd 01_using_different_models

# 패키지 설치
pip install -r requirements.txt

# 해당 폴더의 README 파일의 지침을 따라 진행하세요.
```

Swarm과 다양한 모델을 활용한 멀티 에이전트 시스템을 탐구해 보세요!

### 제작에 활용된 사이트

- [OpenAI Swarm GitHub Repository](https://github.com/openai/swarm): OpenAI의 Swarm 공식 GitHub
