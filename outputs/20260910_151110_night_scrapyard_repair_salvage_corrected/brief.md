# Brief — master2.4 / execution1.5

User: 고물상, 자동차 수리점 / 밤, 쿨 톤 / 고물상 건물의 절반은 기계화, 쓰레기통, 굴뚝, 폐자동차 / 한 장

Mode: own structural correction of the same independent scene; baseline Salvage Cyberpunk. Final count1 of2. No cassette output as input.

Plan: structure_plan.json; actual guide: structure_guide.png. Single orthographic projection, no camera relabel after output.

Current dialogue exclusion: no greenCRT. Cassette style belongs only to independent sibling.

BuildingA entry local closed door; B open servicebay shows terminating room. Exactly2 separate functional exits open after clear.

Scene-only route widths/camera/height values are plans, not master constants or actual3D validation.

Stairs/ramps N/A; no need for them. Roofs stepped level surfaces withsupportedfunctional elements.

All old source images preserved. Built-in only. No API, masterpromotion, installation, commit.

## Requirement coverage
|Requirement|Exact prompt clause|Final check|Coverage|
|---|---|---|---|
|single frame/base|one complete standalone|C01|MAPPED|
|sharedXYZ/ortho|all X horizontal-world edges|C03/C04|MAPPED|
|constantdepth/cuts|identical projected shape|C02/C03|MAPPED|
|orthogonalfootprints|axis-aligned rectangles|L07|MAPPED|
|roofjoin/support|Supports join roof equipment|C04/L05|MAPPED|
|twoboundaries|Fill other rear boundary intervals|L01|MAPPED|
|twoexitroles|Left functional exit:|L02|MAPPED|
|righttransition|Right functional exit:|L02|MAPPED|
|walkvolumes/center|Reserve broad continuous walking volumes|L03|MAPPED|
|front/footingvisibility|Keep the front view open|C01/L04/L07|MAPPED|
|heightbound|approximately 6.5m|L05/3D separately|MAPPED|
|interior|visible clear pedestrian aisle|L06|MAPPED|
|buildingentry|credible human-sized grounded door|W04|MAPPED|
|roofs|roughly 50–60% functional coverage|W05|MAPPED|
|artdensity/materials|Differentiate painted metal|S01/S02/S03/S04|MAPPED|
|salvageworld|Salvage Cyberpunk is the design base throughout|W01/W02/W03|MAPPED|
|referenceroles|Image 1 is this scene|reference audit/C04|MAPPED|
|keywords/coolnight|scrapyard and automobile repair shop at NIGHT|R01|MAPPED|
|halfmech|Approximately HALF|R01|MAPPED|
|chimneybinswreck|Place a recognizable stripped wrecked car|R01|MAPPED|
|freshlocation|newly designed Salvage Cyberpunk scene|R02|MAPPED|
|exclusions|No green CRT screens|R01|MAPPED|
Additional supplement scope: N/A, none submitted. Corrective actual inputs: two art/world masters and own guide; M01/M02 inspected but omitted as images, constraints retained.
Counts are exactstring metadata in references.json; internaltoken/model/revisedprompt unknown.
Final evidence pending: actualnativePNG endpoints, basevectors, eachbuildingfooting/wall/roof, two routes, W04/W05. Criticalocclusion=UNCERTAIN, anystructuralFAIL=needs_revision.


Correction evidence: previous review.json C02/C04FAIL. Revised input roles refer to actual three images; old image NOT input. Geometry plan retained as correct source, actual failed shape not preserved. Prompt strengthened for equal basevectors, same roof/ground axis and open right alley. Final QA pending.
