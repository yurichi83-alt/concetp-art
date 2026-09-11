# 동일 입력 이미지 모델 비교

- 사용자 원문: ㄱ 자 건물 / 노을 진 저녁 / 도로에 노란 모래로 60% 정도 가려져있다. 오토바이와 자동차. 벽면에는 낙서도 있다. 부러진 전봇대 / 한 장. 현재 설정 한 장 + 2.5 한 장, 같은 프롬프트 비교.
- 마스터 v2.4 / 실행 v1.5. 기본 Salvage Cyberpunk, 장면별 카세트 변형 아님. 평행투영은 현재 마스터 권장 기본 및 최근 오소그래픽 요청에 맞춘 이번 공통 선택.
- 같은 generation_prompt.md와 동일 순서의 원본 레퍼런스 4장. 독립 생성, 상대 모델 결과 입력 없음.
- 비교 목적상 각 경로 첫 출력 1장 보존. 보정/선별/후처리는 비교 표본을 바꾸므로 이번에는 시행하지 않고 오류도 관찰로 기록. 상시 자동 보정 규칙의 이번 비교 한정 적용 예외; 영구 변경 없음.
- A: 내장 image_gen. 공식 제품 문서에 gpt-image-2로 설명됨. 호출 응답의 정확한 모델 스냅샷/quality/internal rewrite는 별도 미확인.
- B: API gpt-image-2.5-sunburst, quality auto, size 1536x1024, n=1, PNG, no-augment. 키 미설정으로 대기.
- 텍스트/원본 순서는 동일하게 통제. 실행 경로/비공개 품질/내부 처리/무작위성은 통제되지 않음. 한 장씩의 결과로 모델 전체 우열을 확정하지 않는다.

| 요구 | 실제 프롬프트 대응 | 검사 |
|---|---|---|
| 전체 정사각형 베이스/단면/공통 XYZ/평행투영 | STRUCTURE: ENTIRE square-footprint; constant depth; same vertical vector; parallel axis edges | C01-C04 |
| 직교 ㄱ자 접촉 외벽/단계 지붕/접지 | STRUCTURE: single joined L; right-angle turns; Stepped LEVEL roofs; visible footing strips | C04/L05/L07 |
| 뒤 두 차단 방향과 출구 두 개/상태/여유/제3 틈 금지 | STRUCTURE: Exactly TWO; wide closed sliding gate; side pocket; No unintended rear gap | L01-L03 |
| 중앙/보행/시야/높이 | STRUCTURE: central combat; continuous routes; no high foreground wall; about 6.5 m | L03-L05, 3D 수치 미검증 |
| 건물 입구/윗면40~80% | CURRENT: human-scale door and service shutter; Approximately60 percent; supported; maintenance gaps | W04/W05 |
| 실내 | CURRENT: no exposed interior | L06 N/A |
| 노을/노란모래60%/차/오토바이/낙서/부러진전봇대 | CURRENT: sunset; THIN yellow; One parked car; one parked motorcycle; graffiti; BROKEN utility pole | R01 |
| Salvage 세계관/LDI 재질/큰 색면/수리 흔적 | ART: recovered advanced technology; broad organized color planes; selective large wear | S01-S04/W01-W03 |
| 녹색CRT/인물/UI 제외; 추상 낙서 예외 | ART: no green CRT; people; UI; Graffiti is abstract painted marks | R01 |
| 4참조 역할 및 카메라 분리 | ART: Image1-4 역할 명시, orthographic camera governs | 참조 검사 |
| 독립 신규 생성 | ART: fresh scene independently; No previous generated image | 입력 검사/R02 |

