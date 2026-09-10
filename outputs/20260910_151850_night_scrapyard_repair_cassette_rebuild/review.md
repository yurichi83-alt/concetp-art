# 카세트 퓨처리즘 최종 테스트 후보 검수

**needs_revision** — 이미지 생성과 키워드 적용은 완료했으나 공통 정사영 구조 통과를 주장하지 않는다.

실제1377×1142 PNG를 열어 전체와2배 검사 크롭으로 대조했다. 원본 좌표는 좌상단(0,0), 오른쪽+x/아래+y. 선택점은 선명한 선에서 약2px오차, 가려진 베이스 모서리는 더 불확실하다. 각도는 화면각이며 실제3D회전각이 아니다.

|검사|판정|근거|
|---|---|---|
|C01|PASS|one completequarterviewdi orama, fullbase and rearboundaries framed|
|C02|UNCERTAIN|Bothcutfaces visible andstraight. Upperleft/rightcorners are partly covered by rearwall joins; observed displacement estimates84,99,104px differ. They do not prove constantdepth under selectedparallelcamera. No falsePASS.|
|C03|PASS|Visiblelongperimeter edges straight, fourcorner rectangularblock impression without visible bevel orcurve; physical3Dplanarity/curvature unproven.|
|C04|FAIL|SameXfamily localbuilding roof/footing andglobalbase do not fully agree. JunkyardfootingX~26.25deg androofX~27.18deg vsbaseupperX~28.92deg. Shortsegment uncertainty affects exactdifference, butcommoncamera hasnotbeenpreserved reliably. Screenangles arenotphysical3Dyaw.|
|L01|PASS|Rearbarriers connect through two buildings and wallsegments, no unintendedthirdgap.|
|L02|PASS|Exactly two assignedfunctionalclosedgates on rearleft/rearright; closedbuildingdoors decorative. Transitionstate credible, futureopening planned.|
|L03|PASS|Centralfloor clear; bothclosedgateapproaches empty withclearoverhead and openingtrack/roller. Bins peripheralfrontleft outsidegateapproach, car recessedbetweenbuildings. Postclearconnection remains plannednotanimated.|
|L04|PASS|Lowfrontprops do nothidecenter orbothcuts.|
|L05|PASS|Visible walls/plinths grounded, humanthresholds meetpaving; roofhousings/ducts on brackets/rails, no floatingmass. Camera inconsistency separatelyC04.|
|L06|NOT_APPLICABLE|Closedworkshopdoors; noexposedroomrequirescirculationreview.|
|L07|UNCERTAIN|Rebuild exposes maincontactcorners and bothcamera-facingwall directions with no diagonallycutcorner. YetglobalC04 mismatch prevents certifyingcommonXYfootprint; cannot inferactual3Drotation fromroof alone.|
|S01|PASS|Broadwalls/tiles withselectedlargepeelingpatches; lowerdetailthanpreviousattempts, notuniformmicrograin.|
|S02|PASS|Densemachinearea atrear, quietcenter andbarebuildingfoundation strips.|
|S03|PASS|Stylizedvolumes/material planes, no photoDOF orbrushstroke.|
|S04|UNCERTAIN|Majorforms/cassettejunctions readable, butglobalcamera caveat C04remains.|
|W01|PASS|Recoveredmoduleprocessor replacesbuildinghalf, retrofittedcontrolpanel/ducts and workshop compressor functional relationships.|
|W02|PASS|Largepatchedpanels/fadedpaint onbothbuildings andworncar/gates; oldmaintainedworld.|
|W03|PASS|Machinery prominent onjunkbuilding and repairroof, notonlysubsoil.|
|W04|PASS|Junkyardservicehumandoor+closedshutter; repairshutterhas humanwicket, allgroundeddecorativeentries.|
|W05|PASS_visual_estimate|Junkyardcombinedsteppedroof: largeprocessmodules occupyupperhalf pluslowroofvent/crate~50–65%; repairroof: duct/airunit+cylinderbank+cover~45–60%. Notexact3Darea certification.|
|R01|PASS_visual_estimate|Nightcoolbluegray; scrapyard+autorepair; visuallyabouthalfjunkyardmechanized; chimney/2bins/wreckcar. Cassettedials/vents/chunkymodules, nogreenCRT. Percentageisvisualestimate.|
|R02|PASS|Independentplanforautorepairshop andprocessorbuilding/carservicepocket; no siblingoroldscene usedascomposition.|

|선|끝점A|끝점B|화면각|
|---|---|---|---|
|base_X_upper|[31, 629]|[670, 982]|28.917°|
|base_X_lower|[31, 713]|[670, 1081]|29.938°|
|base_Y_upper|[670, 982]|[1354, 627]|-27.43°|
|base_Y_lower|[670, 1081]|[1354, 731]|-27.099°|
|junkyard_footing_X|[350, 494.5]|[499, 568]|26.257°|
|junkyard_footing_Y|[499, 568]|[633, 498.5]|-27.414°|
|junkyard_level_roof_X|[351.5, 350.5]|[498.5, 426]|27.185°|
|junkyard_level_roof_Y|[499, 425]|[633, 356]|-27.245°|
|repair_level_roof_X|[811, 380]|[1065, 512]|27.46°|
|repair_footing_X|[835, 557.5]|[1065, 677.5]|27.553°|
|repair_level_roof_Y|[1065, 512]|[1210, 433]|-28.583°|
|repair_footing_Y|[1065, 677.5]|[1212, 597]|-28.706°|
|paving_X|[492, 686]|[718, 814]|29.526°|

베이스 상하 대응은 전면 모서리 약99px, 좌/우뒤쪽은 가림이 있는 추정84/104px이므로 일정깊이 PASS근거로 쓰지 않는다. 바닥 외곽의 명백한 곡선은 보이지 않으나 실제3D곡률을 검증한 것은 아니다.

왼쪽/오른쪽 폐쇄 게이트 접근은 연속되고 중앙도 비어 있다. 개방 후 연결·문 작동은 계획이며 단일이미지로 애니메이션/콜라이더를 검증하지 않았다. 고물상 절반 기계화·지붕 점유율도 시각 추정이다.

이전2개 시도와 원본을 보존했다. 국소 수정에서 가림 해소가 부족하여 마지막에는 실패 이미지를 입력하지 않고 하나의 구조 가이드로 재구성했다. 접지가 잘 보이게 개선됐지만 작은 공통 투영 불일치가 남았다. 서로 다른 보정 전략 뒤에도 같은 종류의 문제가 남아 무작정 호출을 반복하지 않고 이 상태를 공개한다. 마스터/승인목록은 변경하지 않는다.
