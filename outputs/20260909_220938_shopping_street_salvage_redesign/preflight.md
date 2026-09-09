# 생성 전 확인

- game-env-art와 공식 imagegen 스킬 적용.
- docs/05_GENERATION_RULES.md, project.json, refs/manifest.json, state/approvals.json 확인.
- 원본 마스터 01~04 유지: Little Devil Inside 건축 표현 + Salvage Cyberpunk 세계관.
- scripts/validate_project.py: PASS (원본 19, 선호 2, review_only 3).
- 입력 5장 모두 view_image로 실제 열람; 파일 경로는 도구 referenced_image_paths에 전달 예정.
- 대상 1장 + 세계관 2장 + 스타일 2장으로 실제 도구 입력 한도 5장 준수.
- 내장 이미지 도구 사용. 별도 API·추가 설치·전역 설정 변경 없음.
- 사용자 승인 범위는 이전 분석안의 이번 이미지 편집. 영구 마스터 갱신 아님.
- 생성 1장, 자동 재생성 없음. 정확한 높이·통로 폭은 이미지로 수치 검증 불가.

