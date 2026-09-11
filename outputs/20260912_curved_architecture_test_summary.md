# 지상 곡면 건축 — 두 장 시험 결과

요청: 슬럼 골목 / 밤, 쿨 톤 / A 1층40%·2층20% 기계 / B 고철상과 평면 절반 크기의 상층 주택 / C 단층과 옆 기계 / 두 장.

지상 보행 경계에 곡선을 허용하되, 직교 컬리전으로 막았을 때 넓은 빈 모서리를 지나갈 수 없는 것처럼 보이지 않는 방향을 시험했다. 임의의 비스듬한 건물 회전은 추가하지 않았다. LDI 건축·재질·빛·색 표현과 Salvage Cyberpunk 세계관은 유지했고, 직전 첨부 건축 이미지는 형태 참고에만 사용했다.

| 시안 | 형태 차이 | 출구 계획과 관찰 |
|---|---|---|
| 01 | 뒤쪽 A의 둥근 기계 외피와 돌출 창, B의 외부 계단·작은 경사 지붕 주택, C의 반원형 지붕 | B 닫힌 셔터 겸용 출구 + 오른쪽 지하 진입부. 우측 접근 일부 가림 |
| 02 | 왼쪽 A의 둥근 모서리와 상층 돌출, 후방 B의 후퇴 주택·작업 테라스, C의 톱니 지붕과 옆 수직 설비 | 왼쪽 계단 전환 + 오른쪽 기계 아래 열린 통로. 통로를 가로막던 펜스/드럼통 제거 완료. 계단 끝과 일부 접근은 가림 |

두 결과 모두 곡면이 지상 외벽까지 이어지고 받침/설비와 연결돼 곡면 허용 시험에 사용할 수 있다. 실제 직교 콜라이더는 제작하지 않았으므로 충돌 적합성을 검증했다고 주장하지 않는다. A의 정확한40/20, B 정확한 절반 면적도 계획값이며 결과는 관찰 추정이다.

최초 2장 뒤 입체 구조 가이드로 각1회 전체 보정했고, 02는 새로 생긴 출구 차단을 국소 보정했다. 총5개 생성 run을 보존하고 최종 전달은2장으로 제한했다.

**최종 검수: 두 장 모두 needs_revision.** 건축 상층의 일부 수평 테라스 선이 기단과 다른 기울기를 가지는 C04 정사영 오류가 재구성 후에도 남았다. 이는 곡면이나 경사 지붕을 잘못 비교한 판정이 아니다. 새로 검증된 기하 제어 전략 없이 같은 전체 생성 지시를 반복하지 않는 실행 기준에 따라 전역 재생성을 중단했다. 구조 완전 통과나 마스터 승인으로 기록하지 않았다.

## 파일과 재현 기록

- [시안01 PNG](20260912_030800_slum_curved_architecture_01_rebuild/image.png) · [실제 생성 지시](20260912_030800_slum_curved_architecture_01_rebuild/generation_prompt.md) · [참조 목록](20260912_030800_slum_curved_architecture_01_rebuild/references.json) · [원본 이미지 검수](20260912_030800_slum_curved_architecture_01_rebuild/review.md)
- [시안02 PNG](20260912_031500_slum_curved_architecture_02_exit_clearance/image.png) · [전체 생성 지시](20260912_030800_slum_curved_architecture_02_rebuild/generation_prompt.md) · [국소 보정 지시](20260912_031500_slum_curved_architecture_02_exit_clearance/generation_prompt.md) · [전체 생성 참조](20260912_030800_slum_curved_architecture_02_rebuild/references.json) · [실제 편집 입력](20260912_031500_slum_curved_architecture_02_exit_clearance/references.json) · [원본 이미지 검수](20260912_031500_slum_curved_architecture_02_exit_clearance/review.md)
- 최종 복사본: outputs/final/20260912_030800__slum_curved_architecture_01.png 및 outputs/final/20260912_031500__slum_curved_architecture_02.png

내장 image_gen.imagegen 사용. 원본 생성 이미지와 모든 보정 이력을 보존했다. 외부 과금 API·추가 설치·전역 설정·Git 작업은 수행하지 않았다. 내부 모델명·토큰·수정 프롬프트는 반환 정보가 없어 미확인이다.

기존 마스터/규칙/프로젝트/승인/템플릿17개 파일의 기준 해시와 현재 해시가 같다. **곡면 허용을 마스터에 추가하지 않았다.** 사용자가 결과를 평가한 뒤 명시적으로 갱신하는 범위만 추후 적용한다.
