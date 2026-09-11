# 비교 생성 사전 점검

- 내장 도구: 사용 가능. API: 모델별 추가 생성은 현재 사용자 요청 범위이나 OPENAI_API_KEY 없음(Process/User/Machine 존재 여부만 검사, 값 미출력).
- 공통 프롬프트/마스터 입력4장: 준비 및 이미지 열기 완료. 01구조,02출구,03표현,04세계관. 미승인 생성물 입력 없음.
- same prompt 테스트를 위해 API --no-augment, --n1. 내장 비공개 내부 재작성은 미확인.
- 투영/기단/지붕/출구 상태/입구/윗면/소품/보행 공간은 structure_plan.json에 PLANNED. 실제 이미지 판정은 생성 후 별도.
- 입력 count4는 실제 사용 수이고 도구 최대장수 주장 아님. recent-image max5와 path 입력 한도를 혼동하지 않음.
- 네이티브 결과를 run에 복사하고 outputs/final_manifest.json에 선택본 등록 예정. 마스터 수정/커밋/푸시 없음.

