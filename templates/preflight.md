# Preflight — masters v2.8 / execution v1.9

사전 준비·불일치 해결 기록이다. [05](../docs/05_GENERATION_RULES.md)의 절차와 brief.md의 파일 계약을 따른다. 시각 조건·프롬프트 대응·적용 여부는 `requirements.json` 한 곳에 작성하며 여기에 복사하지 않는다. 결과는 아직 NOT_REVIEWED이고 PLANNED는 최종 PNG의 PASS가 아니다.

- run_id / 검사 시각:
- requirements.json / brief / 준비된 실제 prompt·tool_arguments 경로:
- 이번 불일치·미해결 변수·충돌과 해결 기록 (원장 ID):

| 준비 관문 | PLANNED / BLOCKED / UNKNOWN / N/A | 현재 파일·원장 ID·구체 불일치/해결 |
|---|---|---|
| 생성/편집 요청과 요청 장수·시안/부모 관계·활성 지시를 기록 | UNKNOWN | |
| 실제 내장 도구 계약·입력 방식·매개변수별 확인 한도를 기록, 미노출 기능은 미확인 유지 | UNKNOWN | |
| 원문→긍정/금지 시각 요건→정확한 실제 prompt 구절→참조/텍스트 이유→검사 연결 완료; 빈칸/구역명만의 대응 없음 | UNKNOWN | |
| 준비된 prompt 파일과 실제 호출 인자 일치, 현재 참조 배열·개수·경로·해시·열람·역할·승인 범위 일치 | UNKNOWN | |
| 구조안에 공통 정사영·베이스·경계/두 출구·동선·기단 가시성과 구체 큰 형태/외벽 깊이를 함께 계획 | UNKNOWN | |
| geometry/art/world/surface/architecture_form 역할별 근거 확인, 보정 시 참조 변경·생략 이유와 유지 근거를 기록 | UNKNOWN | |
| 실제 PNG 전체/확대·대표 선군/상하 대응·표면별 긍정/금지·S04 독립 관찰 및 적용 R02/R03 비교를 준비 | UNKNOWN | |
| 후보 7차원 비교·잔여 후퇴·전체 완료와 정직한 미달 전달·중단 조건을 구분할 준비 완료 | UNKNOWN | |

아트·세계관 참조 일괄 축소를 기본 기하 보정법으로 삼지 않는다. 이전 run 목록 위에 정정 주석을 쌓지 말고 이번 목록·개수·생략 이유를 현재값으로 맞춘다. 과거 자료의 카메라/배치/전체 QA를 승인 속성에 합치지 않는다. 상세 조건은 [현재 참조](../docs/10_CURRENT_REFERENCES.md)와 원장 역할 연결을 따른다.

```sh
python3 scripts/validate_run.py --run outputs/<run> --stage preflight
```

- 기록 검사 결과/파일:
- 남은 BLOCKED/UNKNOWN 및 영향받는 원장 ID:
- 실제 도구 호출 시 전달한 인자가 준비값과 달랐다면 새 현재값·변경 이유:

RECORD PASS는 준비 기록의 일관성만 확인한다. 이미지 품질과 가짜 관찰은 코드가 판독하지 않는다. 호출 뒤 실제 인자와 delivery_status=submitted를 보존하고 PNG를 열어 review 단계로 진행한다. selection은 final_manifest 등록 후 수행한다. 과거 원장 없는 run을 소급 검사·변경하지 않는다.
