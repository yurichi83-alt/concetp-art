from pathlib import Path
import json
run=Path(__file__).resolve().parent
p=(run/'generation_prompt.md').read_text(encoding='utf-8')
(run/'generation_prompt_before_limit_retry.md').write_text(p,encoding='utf-8')
p=p.replace('Image2 (M01) gives full diorama framing and two cut-face presentation only, not its neon theme/buildings/pipe pattern. Image3 (M02)', 'Image2 (M02)')
p=p.replace('Image4 (M03-10)','Image3 (M03-10)').replace('Image5 (M04-02)','Image4 (M04-02)').replace('Image6 is','Image5 is')
(run/'generation_prompt.md').write_text(p,encoding='utf-8')
r=json.loads((run/'references.json').read_text(encoding='utf-8'))
r['planned_referenced_image_paths']=[x for x in r['planned_referenced_image_paths'] if not x.endswith('composition_cutaway.png')]
r['planned_image_count']=5
r['contract']['referenced_image_paths']='runtime error directly confirmed at most5 paths on 2026-09-10; not inferred from recent-image option'
r['omitted_references_and_reasons']=[{'id':'M01-01','reason':'runtime confirmed5pathlimit; actually inspected and its full framing/two cuts retained in own guide and explicit prompt; M02, art, world, user machine reference kept'}]
r['input_prevalidation_error']='referenced_image_paths must contain at most5 paths; no image produced'
r['prompt_metadata']={'characters':len(p),'utf8_bytes':len(p.encode()),'whitespace_words':len(p.split()),'counts_are_not_capacity_estimates':True}
(run/'references.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
with (run/'preflight.md').open('a',encoding='utf-8') as f:f.write('\n실제 호출 입력 검증에서 referenced_image_paths 최대5장이 확인됨. M01이미지 입력을 생략하되 실제 열어본 구도/단면조건은 가이드와 프롬프트에 유지. 최종 입력5장, 가이드 실제 열어 봄.\n')
print('Adjusted to five actual runtime-supported inputs; no generated image from rejected prevalidation.')
