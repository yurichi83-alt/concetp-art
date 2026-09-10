# 실행 전 확인

- PLANNED: 새 독립 생성 1장. 현재 요청 외 이전 장면의 안개·폐차장·쓰레기는 누적하지 않음.
- PLANNED: 내장 image_gen__imagegen, stylized-concept. referenced_image_paths로 원본 4개 실제 전달.
- PLANNED: 원본 4개를 현재 도구로 열어 확인. M02/M01 공간, M03 표현, M04 세계관. A01/A02·review_only·기존 생성물 제외. M03 보강은 기존 대표앵커와 중복을 줄이기 위해 미선택; 도구 제한 때문에 제외한 것이 아님.
- UNKNOWN: referenced_image_paths 최대 개수, 내부 모델명/토큰/가중치/수정 프롬프트. recent images max5와 혼동하지 않음.
- PLANNED: 현재 project.json, manifest, active approvals 확인. validate_project.py PASS(24/2/3), 파일 무결성만 검증.
- PLANNED: structure_plan.md의 카메라·네 모서리·직교/접지·두 전이·동선·지붕·내부 범위를 3개 섹션 프롬프트에 대응. 사용자 층수 예외 기록. 미해결 변수 없음.
- PLANNED: C01~C04/L01~L07의 실제 구조 오류는 standing structural_auto_correction_20260909 승인 범위에서 수정. 미관만으로 변형하지 않음.
- PLANNED: outputs run별 원본·지시·실제 참조·QA 기록. 파일 열기 전 not_reviewed. 가려진 핵심 구조/공통 원근 근거 부족은 UNCERTAIN.
- PLANNED: git 푸시·마스터 갱신·별도3D/UV 작업 없음.

