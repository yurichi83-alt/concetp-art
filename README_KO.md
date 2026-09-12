# GameConcept_Codex

키워드로 게임 배경 컨셉 이미지를 만드는 작업 폴더입니다. [START_HERE_KO.md](START_HERE_KO.md)의 첫 요청으로 시작하고 이후에는 `교역장 / 밤 / 드럼통 / 한 장`처럼 입력합니다.

현재 패키지1.8.0 / 마스터 세트 v2.8 / 실행 v1.9 / 마스터03 본문 v2.3입니다. 세부 기준과 우선순위는 [docs/00_INDEX.md](docs/00_INDEX.md)를 따릅니다.

## 기준과 자료

Little Devil Inside의 건축·재질·빛·색 표현과 Salvage Cyberpunk의 회수·수리·개조 세계관을 결합합니다. 단일 정사영 디오라마와 두 기능 출구를 유지하고, 큰 건축 형태·외벽 깊이와 절제된 표면 붓터치를 각각 설계·검수합니다.

- 마스터27장: 원본19장 + 승인 LDI5장 + 사용자 추가3장.
- 선호 결과 A-01/A-02, 표면 보조 B03-01~04, 건축 형태 F-01~07/비교 F-08~11, 검토용 R-01~03은 역할별로 구분합니다.
- 원본의 카메라·세계관·기하까지 일괄 복사하지 않습니다. 선택 입력/비교 전용 범위는 [참조 목록](docs/10_CURRENT_REFERENCES.md)과 [갤러리](REFERENCE_INDEX.html)를 봅니다.

## 작업 흐름

1. 짧은 요청을 새 장소/독립 시안/기존 장면 편집으로 구분합니다.
2. 구조와 큰 기능 부피·외벽 깊이, 표현·세계관의 참조 역할을 계획합니다.
3. run의 `requirements.json`에 요구사항과 실제 프롬프트 구절·참조를 연결하고 내장 도구로 생성합니다.
4. 전체 이미지와 표면별 확대에서 구조·아트·현재 요청을 별도로 검수합니다. 수정 전후 보존은 R03으로 확인합니다.
5. 명시 기준이 누락되면 자동 보정하고 모든 후보의 품질을 비교합니다. 구조만 개선된 최신본을 자동 최종으로 선택하지 않습니다. 전체 통과와 미달 중단은 구분합니다.

설정은 [project.json](project.json)의 프로젝트 운영 정책입니다. 내장 이미지 모델의 파라미터나 Codex 전역 설정이 아니며, 노출되지 않은 품질·참조 가중치·Ultra 연결을 임의로 설정하지 않습니다. 별도 API·설치는 동의 없이 사용하지 않습니다.

## 주요 파일

| 경로 | 역할 |
|---|---|
| AGENTS.md / .agents/skills/game-env-art/ | 진입 지침과 로컬 작업 스킬 |
| docs/01~04 | 공간·표현·세계관 마스터 |
| docs/05 / docs/06 | 생성 절차·보정·검수·후보 선택 |
| templates/requirements.json | 요구사항·실제 입력·관찰·보존·선택 원장 |
| templates/brief.md / preflight.md / review.md | 원장에 연결하는 기록 양식 |
| refs/manifest.json / state/approvals.json | 참조 역할과 승인 이력 |
| outputs/ | run 원본·실제 입력·검수·전달 사본 |
| state/history/ | 갱신 전 문서 스냅샷 |

## 검사

```bash
python3 scripts/validate_project.py
python3 scripts/validate_run.py --run outputs/<run> --stage preflight
python3 scripts/validate_run.py --run outputs/<run> --stage review
python3 scripts/validate_run.py --run outputs/<run> --stage selection
```

첫 명령은 파일·참조 해시·승인·운영 정책 연결을 확인합니다. 나머지는 새 run의 입력/요구사항/검수/선택 기록을 검사합니다. 이미지의 미적·기하학적 품질을 자동 판정하지 않으며, 기록 검사 PASS는 이미지 PASS와 다릅니다. 과거 run을 새 원장 양식으로 소급 변환하지 않습니다.

원본과 과거 결과/QA는 보존합니다. 이번 장면 예외를 영구 규칙으로 만들거나 결과를 마스터로 승격하려면 사용자의 갱신 지시가 필요합니다. Git 동기화는 사용자가 요청한 범위로 진행합니다.

2026-09-12 갱신: [분석 적용 기록](outputs/20260912_master_v2_8_pipeline_update/implementation_ko.md). 참조 목록 개정 2026-09-12-architecture-form-01과 기존 이미지/역할을 유지했습니다.
