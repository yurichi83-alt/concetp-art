# 사전 점검

- docs/05_GENERATION_RULES.md, docs/08_COMMANDS.md, project.json, refs/manifest.json, state/approvals.json 재확인.
- game-env-art / 공식 imagegen 스킬 사용. 내장 image_gen 도구 사용 가능.
- validate_project.py: PASS. 원본19/선호2/review_only3. 파일 무결성 검사이며 시각적 결과 보증 아님.
- 입력5장 모두 세션에서 실제 열람됨. 재사용 원본의 SHA256이 직전 열람 시점과 일치함을 확인. M03-10/사용자 LDI01은 이번 턴에서도 재열람.
- 한 장 생성, 자동 재생성 없음. 별도 API·설치·전역 설정 변경 없음.
- 골목의 좁음과 연속 중앙공간, 두 출구, 전체외곽 여백을 함께 지정.
- 바닥 쓰레기는 개별 낮은 물체로 표현; 미세 노이즈와 구별.
- 테스트 후 사용자 평가를 기다리는 조건부 마스터 정리 의사이며 현재 마스터 갱신 권한으로 실행하지 않음.
