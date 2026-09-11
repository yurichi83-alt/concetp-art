# 공식 기능 문서와 적용 범위

확인일: 2026-09-09. 아래는 Codex 운영 기능의 출처이며 아트 마스터 원본의 출처가 아니다.
마스터의 내용과 시각 참조는 사용자가 이 대화에 제공한 자료와 명시적으로 보완·승인한 규칙에서 정리했다.

| 주제 | 공식 출처 | 이 패키지에 적용한 내용 |
|---|---|---|
| AGENTS.md | https://learn.chatgpt.com/docs/agent-configuration/agents-md | 작업 루트의 짧은 진입 지침, 세부 문서 별도 참조, 범위/override 확인 |
| 로컬 스킬 | https://learn.chatgpt.com/docs/build-skills | .agents/skills/<name>/SKILL.md, name·description, 선택/직접 읽기 |
| 이미지 생성 | https://learn.chatgpt.com/docs/image-generation | 내장 이미지 생성, imagegen 호출, 실제 이미지 참조, API 경로 구분 |
| Codex 작업 모범 사례 | https://developers.openai.com/codex/learn/best-practices | 짧고 구체적인 지속 지침과 반복 절차의 재사용 |
| ChatGPT 이미지 가용성 | https://help.openai.com/en/articles/11084440-images-in-chatgpt | Codex에서 이미지 생성/편집 안내, 버전/환경 확인 필요 |

제품 안내는 개정될 수 있다. 내장 이미지 모델의 이름·속도·가격을 이 패키지에서 고정하지 않는다.
AGENTS.md와 스킬은 작업 지침을 적용하기 위한 수단이며 이미지의 출구 수/카메라를 기술적으로 잠그지 않는다.
별도 API를 사용하지 않는 기본 경로로 설계했지만, 사용자의 현재 계정·앱에서 실제 도구를 확인해야 한다.
