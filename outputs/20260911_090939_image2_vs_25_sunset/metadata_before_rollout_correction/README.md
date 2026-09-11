# 현재 내장 도구 / GPT Image 2.5 비교

현재 상태: 내장 첫 출력 1장 생성·검수·최종 모음 저장. **2.5는 API 키가 없어 아직 생성하지 않음.**

- A: builtin/builtin_first_output.png (1536×1024), needs_revision. 비교 목적상 첫 출력을 보정 없이 보존.
- B: gpt-image-2.5-sunburst, quality auto, 1536×1024, n=1, 동일 원본 레퍼런스4장. 실행 명령은 api25/command.txt, 오프라인 입력 검증은 api25/dry_run.json.
- 공통 실제 입력: generation_prompt.md. --no-augment를 사용하며 앞뒤 공백을 제거한 텍스트와 원본4장의 경로/순서가 내장 호출과 같음을 확인했다.
- 최종 모음: ../final/20260911_090939__builtin_image2_first_output.png.
- 정확한 모델 스냅샷/내장 quality/내부 재작성은 반환되지 않아 미확인. 입력 동일성만 통제하며 경로/무작위성/공개되지 않은 실행 옵션은 통제 불가. 모델별 한 장은 탐색 비교이며 일반 성능 순위가 아니다.

## 필요한 사용자 설정
1. https://platform.openai.com/api-keys 에서 API 키를 만든다. API 계정의 결제/사용 가능 상태가 필요하며 Codex 구독과 별도 API 과금이다.
2. Windows 시작에서 '환경 변수'를 검색 → '계정의 환경 변수 편집' → 사용자 변수 '새로 만들기' → 이름 OPENAI_API_KEY, 값에 키를 로컬로 입력.
3. 채팅에는 키 값을 보내지 않고 '설정 완료'라고 알려준다. 이 작업은 User 범위의 존재를 다시 확인해 필요 시 실행 프로세스에만 가져올 수 있다. 원본 키는 프롬프트/로그/프로젝트/명령 파일에 저장하지 않는다.

## 실행 환경
작업 전용 가상환경: C:/Users/Yeon Hee Kang/OneDrive/문서/Codex/tmp/image-api-compare-venv
공식 bundled imagegen CLI를 직접 사용한다. 별도 SDK 생성 wrapper나 전역 모델 변경은 하지 않는다.
API 호출 횟수: 0. 모델 접근/결제/권한은 실제 인증 전 미확인.

공식 근거:
- https://learn.chatgpt.com/docs/image-generation (제품 문서상 내장 gpt-image-2)
- https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst (비교 대상)

마스터 레퍼런스, 기존 출력, Git 커밋/원격 상태는 이번 요청으로 갱신하지 않았다.

