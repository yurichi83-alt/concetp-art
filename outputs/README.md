# Generated outputs

아직 이 프로젝트에서 생성한 새 이미지는 없습니다.
각 실제 생성 run을 고유한 폴더에 보관합니다. 예시 폴더는 파일명을 설명할 뿐 존재하는 결과물이 아닙니다.

```text
<timestamp>_<scene>/
  brief.md
  preflight.md
  references.json
  image.<actual_format>
  review.md
```

이미지를 실제로 저장할 수 없는 환경에서는 해당 상태를 기록하고 존재하지 않는 파일을 만들었다고 보고하지 않습니다.
이미지 QA는 실제 이미지 열기가 가능한 경우에만 합니다. 검수되지 않은 결과는 `not_reviewed`입니다.
요청 장수보다 많은 자동 재생성은 금지합니다. 실험과 사용자 승인 결과를 구분합니다.
