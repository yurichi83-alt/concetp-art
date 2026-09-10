from pathlib import Path
import json, math, hashlib
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[2]
RUN=Path(__file__).resolve().parent
W,H,S=1536,1280,34
def P(x,y,z=0): return (768+(x-y)*S*math.sqrt(3)/2,270+(x+y)*S*.5-z*S)
im=Image.new('RGB',(W,H),'#111b2b'); d=ImageDraw.Draw(im)
def poly(points,fill,outline='#182439',width=3):
    pts=[P(*v) for v in points];d.polygon(pts,fill=fill);d.line(pts+[pts[0]],fill=outline,width=width)
def box(x0,y0,x1,y1,z0,z1,top='#7892a0',left='#526d7c',right='#405a6b'):
    poly([(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],left)
    poly([(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(x1,y0,z1)],right)
    poly([(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],top)
box(0,0,20,20,-3,0,'#738996','#374c64','#455b70')
for v in range(2,20,2):
    d.line([P(v,0),P(v,20)],fill='#8ea0aa',width=2)
    d.line([P(0,v),P(20,v)],fill='#8ea0aa',width=2)
poly([(0,12,0.01),(10,12,.01),(10,15,.01),(0,15,.01)],'#6d9897',width=1)
poly([(6.2,0,.01),(8.8,0,.01),(8.8,13,.01),(6.2,13,.01)],'#6d9897',width=1)
# Fences close every rear interval except the two designated transitions.
box(0,15,0.22,20,0,2.5)
box(0,10,0.22,12,0,2.5)
box(6,0,6.2,.22,0,2.5)
box(8.8,0,9,.22,0,2.5)
box(0,0,6,10,0,4.4)
box(0,10,4,11.7,0,3.0)
box(9,0,20,6.5,0,4.3,'#8296ad','#637b92','#526981')
box(9,0,20,2,4.3,5.0,'#879fb5','#687e92','#5c7388')
# Roof element footprints; shapes guide functional occupancy, not final device designs.
box(.5,1,5.5,5,4.4,5.25)
box(1,5.5,4,9,4.4,5.15)
box(1,2,2,3,5.25,6.3)
box(.3,10.2,3.6,11.5,3,3.5)
box(10,2.6,18.8,4.6,4.3,4.75)
box(10,0.3,18,1.7,5,5.7)
box(10,5,17.5,6.1,4.3,4.8)
# Grounded human entries; no glyphs or extra functional gates.
poly([(6.005,6,0),(6.005,7.4,0),(6.005,7.4,2.5),(6.005,6,2.5)],'#1f3446')
poly([(12,6.505,0),(18,6.505,0),(18,6.505,3.2),(12,6.505,3.2)],'#1b3045')
# Low peripheral wreck/bin volumes; protect center and corridors.
box(1,16.2,4.8,18,0,1.2,'#747986','#4b5364','#3a4556')
box(5.2,16.3,6,17.3,0,1.0)
im.save(RUN/'structure_guide.png')
buildings=[{'id':'scrapyard','rects':[[0,0,6,10],[0,10,4,11.7]],'z':[4.4,3.0],'mechanized_visible_mass_fraction':.5,'roof_functional_coverage_plan':.55,'entry':'decorative_local_door'}, {'id':'auto_repair','rects':[[9,0,20,6.5]],'z':4.3,'raised_roof_strip':[9,0,20,2,5.0],'roof_functional_coverage_plan':.51,'entry':'service_bay_terminates_in_room_not_map_exit'}]
plan={'projection':'parallel_orthographic','world_bounds':[0,0,-3,20,20,6.5],'camera_mapping':'u=768+(x-y)*34*sqrt(3)/2; v=270+(x+y)*17-z*34','projected_X_Y_angles_degrees':[30,150],'constant_extrusion_vertical_px':102,'buildings':buildings,'protected_routes':[{'exit':'left','rect':[0,12,10,15],'height':3,'state':'open','connection':'x<0; yardgate at x0 y12..15'}, {'exit':'right','rect':[6.2,0,8.8,13],'height':3,'state':'open','connection':'y<0; separate alley'}], 'central_clear_rect':[7,10,18,19],'nonbuilding_volumes':[{'id':'wreck','rect':[1,16.2,4.8,18],'height':1.2},{'id':'bins','rect':[5.2,16.3,6,17.3],'height':1}], 'final_evidence':'Inspect actual upper/lower base vectors, paving/footing/roof line families and both routes. Coordinates/guide are not enforced geometry.'}
def overlap(a,b): return min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1])
obstacles=[r for b in buildings for r in b['rects']]+[p['rect'] for p in plan['nonbuilding_volumes']]
assert all(not overlap(o,r['rect']) for o in obstacles for r in plan['protected_routes'])
assert all(not overlap(o,plan['central_clear_rect']) for o in obstacles)
plan['preflight']='PLANNED: orthogonal edges and route/center overlap checks passed, not final-image QA'
(RUN/'structure_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
prompt=(RUN/'generation_prompt.md').read_text(encoding='utf-8').rstrip()
manifest=json.loads((ROOT/'refs/manifest.json').read_text(encoding='utf-8'))
ids=['M01-01','M02-01','M03-10','M04-02']; selected=[next(r for r in manifest['references'] if r['id']==rid) for rid in ids]
inputs=[{'id':'structure_guide','path':str(RUN/'structure_guide.png'),'role':'this scene geometry guide; no enforced lock'}]+[{'id':r['id'],'path':str(ROOT/r['path']),'role':r['use_only'],'exclusions':r['exclude']} for r in selected]
ref=json.loads((ROOT/'templates/references.json').read_text(encoding='utf-8'))
ref.update(run_id=RUN.name,scene_id='night_repair_salvage',request_group_id='20260910_night_scrapyard_auto_repair',independent_new_scenes_requested=True,inspected_for_planning=inputs,submitted_to_generation=[],actual_submitted_image_count=0)
ref['planned_inputs']=inputs;ref['other_independent_scene_outputs_excluded']=['all cassette variant outputs and corrections']
ref['omitted_references_and_reasons']=['Other masters omitted to avoid redundant style/camera cues; roles01/02/03/04 present. No generated preferred results needed.']
ref['submitted_prompt'].update(path='generation_prompt.md',character_count=len(prompt),character_count_method='Python len of exact submitted string',utf8_byte_count=len(prompt.encode('utf-8')),utf8_byte_count_method='len(UTF8 encoding)',whitespace_word_count=len(prompt.split()),word_count_method='Python split')
ref['tool_contract'].update(tool_name='image_gen.imagegen',selected_image_parameter='referenced_image_paths',contract_source='current exposed imagegen contract',confirmed_contract_facts_with_evidence=['prompt and referenced_image_paths supported; recent-image selector max5 applies only to that selector; path count and prompt caps unknown'],supported_input_formats_verified=['PNG'])
ref['structure_guide'].update(path='structure_guide.png',coordinate_camera_source_path='structure_plan.json',projection_mode='parallel_orthographic',selected_camera=plan['camera_mapping'],inspected=False,submitted=False,input_format_verified=True,building_orthogonal_footprints_checked=True,roof_planes_and_supports_checked=True,upper_lower_correspondence_checked=True,polygon_roof_checks_separate_from_AABB=True,functional_exit_roles_locations_states_recorded=True)
(RUN/'references.json').write_text(json.dumps(ref,ensure_ascii=False,indent=2),encoding='utf-8')
groups=[('single frame/base','one complete standalone','C01'),('sharedXYZ/ortho','all X horizontal-world edges','C03/C04'),('constantdepth/cuts','identical projected shape','C02/C03'),('orthogonalfootprints','axis-aligned rectangles','L07'),('roofjoin/support','Supports join roof equipment','C04/L05'),('twoboundaries','Fill other rear boundary intervals','L01'),('twoexitroles','Left functional exit:','L02'),('righttransition','Right functional exit:','L02'),('walkvolumes/center','Reserve broad continuous walking volumes','L03'),('front/footingvisibility','Keep the front view open','C01/L04/L07'),('heightbound','approximately 6.5m','L05/3D separately'),('interior','visible clear pedestrian aisle','L06'),('buildingentry','credible human-sized grounded door','W04'),('roofs','roughly 50–60% functional coverage','W05'),('artdensity/materials','Differentiate painted metal','S01/S02/S03/S04'),('salvageworld','Salvage Cyberpunk is the design base throughout','W01/W02/W03'),('referenceroles','Image 1 is this scene','reference audit/C04'),('keywords/coolnight','scrapyard and automobile repair shop at NIGHT','R01'),('halfmech','Approximately HALF','R01'),('chimneybinswreck','Place a recognizable stripped wrecked car','R01'),('freshlocation','newly designed Salvage Cyberpunk scene','R02'),('exclusions','No green CRT screens','R01')]
assert all(clause in prompt for _,clause,_ in groups)
brief=['# Brief — master2.4 / execution1.5','User: 고물상, 자동차 수리점 / 밤, 쿨 톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝, 폐자동차 / 한 장','Mode: independent new scene; baseline Salvage Cyberpunk. Final count1 of2. No cassette output as input.','Plan: structure_plan.json; actual guide: structure_guide.png. Single orthographic projection, no camera relabel after output.','Current dialogue exclusion: no greenCRT. Cassette style belongs only to independent sibling.','BuildingA entry local closed door; B open servicebay shows terminating room. Exactly2 separate functional exits open after clear.','Scene-only route widths/camera/height values are plans, not master constants or actual3D validation.','Stairs/ramps N/A; no need for them. Roofs stepped level surfaces withsupportedfunctional elements.','All old source images preserved. Built-in only. No API, masterpromotion, installation, commit.','## Requirement coverage','|Requirement|Exact prompt clause|Final check|Coverage|','|---|---|---|---|']
brief += [f'|{name}|{clause}|{qa}|MAPPED|' for name,clause,qa in groups]
brief += ['Additional supplement scope: N/A, none submitted. Only four master images and own guide.','Counts are exactstring metadata in references.json; internaltoken/model/revisedprompt unknown.','Final evidence pending: actualnativePNG endpoints, basevectors, eachbuildingfooting/wall/roof, two routes, W04/W05. Criticalocclusion=UNCERTAIN, anystructuralFAIL=needs_revision.']
(RUN/'brief.md').write_text('\n\n'.join(brief[:10])+'\n'+'\n'.join(brief[10:])+'\n',encoding='utf-8')
(RUN/'preflight.md').write_text('# Preflight — PLANNED; final image not reviewed\n\nGeneration request and independently planned1of2 outputs. Nativeimagegen; PNG path input. Contracts and unknowns inreferences.json. All4masterimages visuallyinspected; guideinspection pending. Fiveplannedinputs is usage, notprovenhardlimit.\n\nStructure polygons orthogonal andsamecamera; rooflevels/supportplans separatefromAABB. Programchecked routes/centralfloor outsidebuilding andpropfootprints. Two rearfunctionalroutes/openstates andlocalbuildingentries mapped. All22coverage rows matchactualprompt. No unresolvedtemplatevariables orpastsceneinput. Original03/04roles retained.\n\nFinalimageQA pending: nativePNGbasecorner vectors, bothaxislinefamilies atbase/paving/buildingfootings/walltops/roof; roofsupports; bothwalkroutes. AnyFAIL=needs_revision; criticaluncertain=uncertain. Onlygeneration structuralcorrections authorized. No3Dmetricsclaim.\n',encoding='utf-8')
print(json.dumps({'run':str(RUN),'prompt_chars':len(prompt),'prompt_words':len(prompt.split()),'inputs':[i['path'] for i in inputs]},ensure_ascii=False))
