# Generation brief — masters v2.8 / execution v1.9

이 문서는 현재 장면의 설계안이다. 조건 정의는 [05](../docs/05_GENERATION_RULES.md)·[06](../docs/06_QA.md), 조건별 적용/프롬프트/참조/최종 판정의 단일 원장은 `requirements.json`이다. 여기에는 조건표나 결과 판정을 복사하지 않고 해당 원장 ID를 연결한다.

- run_id / request_group_id / scene_id:
- 현재 사용자 원문과 계속 유효한 지시: requirements.json → request_original 및 해당 요구행
- request_mode: new_location / independent_variant / edit_existing / own_correction
- 요청 최종 장수 / 독립 시안 관계:
- 장소 / 시간·팔레트 / 소재 / 이번만의 가정·예외:
- 편집 대상 / 이전 run / 명시 변경 목표 / 보존할 요구행 ID:
- 실제 도구 / 확인한 비율·해상도·이미지 전달 방식:

## 장면과 구조안

- 구조안 파일 / 구조 가이드 PNG / 카메라·좌표 출처:
- 공통 XYZ·척도·정사각 기본 평면 / 단일 orthographic 카메라의 장면별 선택:
- 기본 베이스·양면 단면 / 위아래 모서리 대응 / 관찰 가능한 기단·선군:
- 새 장소의 기능·동선 폭·건물 인접 관계 / 포장·단면의 설계 차이 (R02):
- 중앙 보행 공간 / 외곽 큰 물체 / 두 후면 차단 방향의 연속성:
- 곡면 경계와 직선 구조축 구분 / 지붕 경사·지지 / 계단·램프 연결:
- 내부가 적용되면 방 깊이·입구→통로→기능 공간; 미적용 이유:
- 온전한 벽·외장·차체의 기본 색면/평면 붓터치, 포장별 여백과 국소 손상의 설계:
- 빛·재질·접지 / 회수·수리·공급 관계 / 장면의 기계 비중과 큰 기능 부피:

| 건물/큰 시설 | 용도·주된 실루엣·층/날개 부피 | 구체 돌출/리세스/기능 깊이·지지 | 사람용 입구 역할·접지 | 건물별 윗면 구성·40~80% 계획 근거 | 원장 ID |
|---|---|---|---|---|---|
| | | | | | |

| 기능 출구 | 뒤쪽 방향·면 안 위치 | 형태·보이는 개폐 상태 | 접근/좁은 부분/회전/전환/개방장치 여유 | 개방 후 연결 계획·보이는 근거 / 입구 겸용 | 원장 ID |
|---|---|---|---|---|---|
| Left (~11시) | | | | | |
| Right (~1시) | | | | | |

기단·모서리·외벽 깊이는 최종 이미지에서 관찰 가능하게 계획한다. 가이드는 큰 기능 부피와 깊이도 나타내며 상자 위치만으로 형태를 대신하지 않는다. 실제3D·콜리전·메시·UV 검증은 이 이미지 작업의 합격 조건이 아니다.

## 요구사항 원장 사용법

`templates/requirements.json`을 현재 run에 복사한다. 예시 행은 범위 설명이며 현재 장면의 건물/표면/요청별로 구체화하고 의미가 다른 조건은 행을 나눈다. 적용 요건은 모두 `positive_visual`(반드시 보일 모습), `forbidden_visual`(금지·후퇴 모습), 실제 프롬프트의 정확한 `prompt_clauses`, 전달 `reference_ids` 또는 현재 `text_only_reason`, `planned_evidence`를 갖는다. `ART` 같은 구역명이나 이전 run의 문장은 대응 근거가 아니다. 장수·승인 같은 실행 조건은 이미지 관찰로 위장하지 않는다.

실제 관찰 상세는 각 `requirements[].observation` 한 곳에 쓴다. `checks[]`의 상태는 연결 요구행의 집계이며 `evidence/positive_evidence/forbidden_evidence/regions`는 구체 요구행 ID와 관찰 위치를 참조한다. 동일한 관찰 문장을 두 곳에 다시 작성하지 않는다. 선쌍·확대·전후 비교처럼 표가 필요한 상세 근거는 review.md에 한 번만 기록하고 관찰 행에서 그 근거 ID/영역을 연결한다. 코드 검사는 이 참조 문자열의 의미적 진실성을 판독하지 않는다.

검사는 C01~C04/L01~L07/S01~S04/W01~W05/R01~R03 전체를 유지한다. R02는 새 장소/독립 시안, R03은 동일 시안 편집/보정이다. N/A는 요구행과 check에 이유를 연결한다. 항상 필수인 C01~C04/L01~L05/S01~S04/W01~W03/R01을 현재 사용자가 예외로 바꾼 경우 check.exception에 실제 지시의 source와 quote를 더한다. 그 원문 해석의 정당성은 사람이 검수하며 코드가 승인 진위를 판정하지 않는다. `critical`은 우선순위를 나타내며 적용 필수 조건을 선택사항으로 바꾸지 않는다. 어떤 FAIL도 needs_revision, 불확실은 uncertain, 미관찰은 not_reviewed이며 모든 적용 항목의 PASS/근거 N/A일 때만 candidate_pass다.

## 파일·인자 계약

- 원장의 `prompt_path/tool_arguments_path/references_path`, `candidate.image_path/result_path`는 run 상대경로다. 참조 `path`, 비교 이미지 `image_path`, `selection.manifest_path`는 프로젝트 루트 상대경로다. 로컬 기록 경로는 `..`/절대경로/루트 밖 심볼릭 링크를 사용하지 않는다. 로컬 파일이 있는 첨부는 run 안에 보존한다. 로컬 경로 없는 실제 대화 이미지는 recent 방식에서 path/sha256=null과 conversation_image_evidence로 식별·열람 근거를 남긴다. 없는 파일/해시를 만들었다고 주장하지 않는다.
- 실제 `tool_arguments.json`의 `referenced_image_paths`는 도구 계약대로 절대경로이며 전달 목록을 해석한 경로·순서와 정확히 같다. 최근 이미지 방식은 각 항목에 conversation_image_evidence를 더하고 두 방식을 동시에 쓰지 않는다. 가능한 로컬 사본 증거와 대화 전용 증거를 구분한다.
- `references.json`의 inspected/submitted 항목은 `id/path/sha256/role/scope/exclusions/inspected`, 전달 항목은 1부터 시작하는 `input_index`를 갖는다. 카탈로그 밖 자료에는 `authorization_kind`(scene_structure_guide / explicit_current_request / own_correction_target)와 실제 `authorization_evidence`가 필요하다. explicit_current_request는 authorization_source와 authorization_quote도 기록한다. 명시 편집 대상은 edit_target과 편집/보정 mode로 구분하며 카탈로그의 비교 전용 이미지도 새 편집본 입력으로 사용할 수 있다. 이는 원본 바이트 변경이나 양성/기하 승격이 아니다. 단순 별칭·사본의 사용 제한은 파일명/해시로 계속 검사한다.
- preflight의 `tool_arguments.json`은 보내려는 정확한 인자이며 `delivery_status=planned`다. 호출 뒤 실제 전달 인자를 보존하고 `submitted`로 바꾼다. 프롬프트 해시/문자·바이트·단어수와 참조 개수는 실제 기록이며 모델 내부 토큰이나 입력 상한 추정이 아니다.
- 반환 모델/토큰/수정 프롬프트는 실제 노출된 경우만 기록한다. `submitted_prompt.returned_metadata_evidence`의 같은 키에 run 상대 `response_path`와 실제 값의 `json_pointer`(예: `/model`)를 연결한다. 미반환은 null이다.
- `candidate`에는 실제 이미지 경로/해시/열람 여부/검수 시각을, `result.json`에는 최소 `status/image_path/sha256`를 일치시킨다. 관찰은 `basis=actual_image`, 실제 영역·긍정/금지 근거를 갖는다. 계획에는 NOT_REVIEWED/basis=planned를 유지한다.
- 편집/보정 `comparison`은 실제 이전 PNG/해시와 구조·큰 형태·외벽 깊이·표면·빛/재질·세계관·요청 7개를 비교하고 후퇴를 R03에 연결한다. `selection.considered_candidates`도 실제 고려 후보마다 같은 7개 근거·QA·해시를 기록한다. 현재 후보를 자기 baseline으로 쓰지 않고 이미 알려진 baseline을 후보 비교에서 누락하지 않는다. 대화 전용 편집 대상은 baseline과 그 후보 항목의 image_path/sha256=null, reference_id, 동일 conversation_image_evidence를 사용해 실제 inspected edit_target에 연결한다. 다른 이미지로 임의 바꾸지 않는다. 코드가 알 수 없는 다른 후보의 완전성은 사람이 확인한다.

## 단계별 기록 검증

```sh
python3 scripts/validate_run.py --run outputs/<run> --stage preflight
python3 scripts/validate_run.py --run outputs/<run> --stage review
python3 scripts/validate_run.py --run outputs/<run> --stage selection
```

선택적으로 `--root /absolute/project/path --json`을 쓴다. preflight는 호출 전 준비, review는 실제 PNG를 열어 기록한 관찰, selection은 final_manifest 등록 후 복사 전의 후보 비교·선택 이유를 검사한다. 이어 `collect_final_images.py`와 `--verify`로 사본을 확인한다. 기록 오류는 exit1, 인자 오류는 exit2다.

검사는 이미지 판독기가 아니다. RECORD PASS는 해시·경로·인자·문장·판정 연결의 일관성이며 형태/붓질/정사영의 참, 인용문의 의미적 충분성, 가짜 관찰 여부를 보증하지 않는다. 이미지 candidate_pass와 구분한다. 과거 원장 없는 run은 자동 탐색·소급 FAIL·변경하지 않는다.

승인 `master_update_20260912_v2_8_pipeline_quality`는 생성/편집 요청의 명시 마스터·현재 요건 FAIL 보정(S/W/R 포함)을 허용한다. 취향 실험과 분석/검수/마스터 갱신만 요청한 경우의 이미지 생성은 제외한다. 미달/미검수 전달은 한계·중단 사유·claims_overall_pass=false를 기록하며 final 보관은 합격이나 마스터 승격이 아니다. 실제 열지 못한 전달본은 opened=false, observation_basis=not_reviewed 및 모든 적용 관찰 NOT_REVIEWED를 일치시키고 7차원에도 미관찰 사실을 적는다.
