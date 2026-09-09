# 생성 전 확인

- docs/05_GENERATION_RULES.md v1.1, project.json, refs/manifest.json, 승인 기록 확인.
- 사용자 선호 속성(단면 기계요소/쓰레기봉투)을 범위 한정해 state/approvals.json에 기록.
- 내장 image_gen/imagegen 및 game-env-art 스킬 사용. 설치/외부 API/전역 설정 변경 없음.
- 대상과 M04-07을 이번 턴에 view_image로 실제 열람. 나머지 원본도 세션에서 열람함.
- 실제 이미지 입력은 대상 포함5개. 이미지를 넘긴 사실과 모델 내부 영향도를 구분해 기록.
- validate_project.py PASS, 원본19/선호2/review_only3 유지.
- 실제 결과에서 단면·봉투 보존, 구조 C01/C02/L01~L05, 건물 장치와 기계식 통을 확인.
- 구조 오류는 자동 수정 대상, 구조 외 취향 차이로 자동 변형하지 않음.
