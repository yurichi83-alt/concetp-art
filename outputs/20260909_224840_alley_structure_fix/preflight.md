# 구조 보정 전 확인

- 실행 규칙 v1.1, project.json, refs/manifest.json, 최신 상시 승인 재확인.
- 내장 이미지 도구와 game-env-art/imagegen 스킬 사용. 별도 API/설치/전역 설정 변경 없음.
- 대상 이미지와 M02 도해 이번 턴에 실제 열람. 다른 원본도 세션에서 열람함.
- 5개 실제 이미지 입력 경로 사용. 대상의 배치가 아닌 도해를 구조 우선 기준으로 명시.
- 최종 1장. 구조 실패가 남으면 실제 결과에 근거해 수정·재생성 후 재검수.
- 새 규칙 저장 후 validate_project.py PASS; 원본19/선호2/review_only3 유지. 수정한 game-env-art 스킬 quick_validate PASS.
- 구조 체크: C01/C02/L01/L02/L03/L04/L05. 판정은 출력 이미지 관찰로 수행하며 실제 미터 치수는 3D 검증 대상.
