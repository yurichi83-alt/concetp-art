# 현재 내장 이미지 출력 — 비교 전제 정정

현재 내장 이미지1장을 생성했다. 실제 호출의 모델 버전은 반환되지 않아 **확인된 Image2 결과라고 부를 수 없다.**

- [첫 출력](builtin/builtin_first_output.png):1536×1024, needs_revision. 모델 비교용 첫 출력 그대로 보존.
- [공통 프롬프트](generation_prompt.md), [검수](builtin/review.md), [현재 실행 기록](result.json).
- [모델 표기 정정](MODEL_IDENTITY_CORRECTION.md): 공식 발표는 Codex도 Images2.5 제공 대상임을 명시. 내장 사용을 위한 API키/별도 과금은 필수가 아니다.
- 최종 모음: ../final/20260911_090939__builtin_first_output.png.
- API 호출0회. 이전 API계획은 비교 전제를 정정한 상태에서 보류.

API 명령/키설정 관련 파일은 이전 준비 이력이며 현재 실행 지시가 아니다. 향후 별도 API모델 비교를 선택할 때에만 사용한다. 정정 전 기록은 metadata_before_rollout_correction/에 보존했다.
