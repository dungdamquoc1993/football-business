"""Assemble the selected twelve-color review; no image pixels are edited."""
from pathlib import Path
import json,hashlib,shutil
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[3];B=R/'photo-workshop';J=B/'04-WORKSPACE/jobs/2026-11-08-12-color-refresh';OUT=B/'02-REVIEW/2026-11-08-12-colors-v01';assert not OUT.exists()
selected={}
def put(product,color,name,path,operation='generated'):
 assert Path(path).is_file(),path
 selected[(product,color,name)]=(Path(path),operation)
def plans(name):
 for x in json.loads((J/name).read_text()):
  if x.get('file'):put(x.get('product','tiempo-8'),x.get('color','red-black'),x['name'],x['file'])
plans('red-black-results.json')
p=json.loads((J/'tiempo-pilot-v02.json').read_text())
put('tiempo-8','red-black','02-outside.png',p['generated_files'][0],'accepted_pilot')
put('tiempo-8','red-black','05-rear.png',p['generated_files'][1],'accepted_pilot')
plans('tiempo-other-results.json');plans('tiempo-qa-fixes-results.json');plans('last-results.json')
messi={'bac':'silver','xanh-duong':'sky-blue','den-vang':'black-yellow','do':'red-white','xanh-than-cam':'navy-silver-orange'}
for folder,c in messi.items():
 for name,orig in [('01-hero-pair.png','02-doi-goc-cheo.png'),('02-outside.png','01-mat-ngoai.png'),('03-top-pair.png','03-nhin-tu-tren.png'),('04-pair-and-sole.png','04-doi-lo-de.png')]:put('messi',c,name,B/'04-WORKSPACE/sources/legacy-ai/Xstars/xstars-messi'/folder/orig,'reuse_unchanged')
bata={'trang-xanh-ngoc':'white-turquoise','trang-do':'white-red','trang-bac':'white-silver'}
for folder,c in bata.items():
 for name,orig in [('01-hero-pair.png','02-doi-goc-cheo.png'),('02-outside.png','01-ngang.png'),('03-top-pair.png','03-nhin-tu-tren.png'),('04-material-detail.png','04-can-chat-lieu.png')]:put('bata',c,name,B/'04-WORKSPACE/sources/legacy-ai/Xstars/xstars-bata-air-zoom'/folder/orig,'reuse_unchanged')
plans('messi-additions-results.json');plans('bata-and-messi-results.json');plans('final-qa-fixes-results.json');plans('outside-results.json')
assert len(selected)==96,len(selected)
idx=json.loads((B/'04-WORKSPACE/source-index.json').read_text())['assets'];sources={x['sha256']:x['asset_id'] for x in idx};runs=[json.loads(x) for x in (J/'runs.jsonl').read_text().splitlines()];byhash={x['sha256']:x for x in runs if x.get('sha256')};manifest=[]
for (product,color,name),(src,operation) in sorted(selected.items()):
 dst=OUT/product/color/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);sha=hashlib.sha256(dst.read_bytes()).hexdigest();assert sha==hashlib.sha256(src.read_bytes()).hexdigest()
 with Image.open(dst) as im:im.verify()
 origin=byhash.get(sha,{})
 manifest.append({'product':product,'color':color,'filename':name,'path':str(dst.relative_to(R)),'sha256':sha,'image_id':origin.get('image_id',sources.get(sha)),'source_path':origin.get('output_path',str(src.relative_to(R)) if src.is_relative_to(R) else str(src)),'operation':operation,'approval':'accepted_pilot' if operation=='accepted_pilot' else 'pending_full_set_review'})
for product,color in sorted({(p,c) for p,c,_ in selected}):
 folder=OUT/product/color;assert len(list(folder.glob('*.png')))==8
 if product=='tiempo-8':
  extras='05–08: Heel, outsole/alternate detail and inner-side coverage.'
  limit='White-gold: 06 is lacing detail; outsole source missing.' if color=='white-gold' else 'Heel size labels describe the photographed sample only.'
 elif product=='messi':
  extras='05–08: Material, outsole and supported extra views.'
  limit='Supplier-only color; hidden views not verified on held goods.' if color not in ['silver','sky-blue'] else 'Rear sample labels show size 41 (silver) / 42 (blue).'
 else:
  extras='05–08: Outsole, front, lacing and heel/side detail.'
  limit='Supplier-only color; shared outsole mold guided by turquoise sample.' if color!='white-turquoise' else 'Rear size-42 label belongs to photographed sample.'
 (folder/'READ-ME-FIRST.txt').write_text('01–04: Core set; legacy images retained or locally corrected.\n'+extras+'\nQuick selection: 01, 02, 05, 06.\n'+limit+'\n')
 preview=OUT/'Preview';preview.mkdir(exist_ok=True);ps=sorted(folder.glob('*.png'));sheet=Image.new('RGB',(1600,880),'white');draw=ImageDraw.Draw(sheet);draw.text((12,8),product+' / '+color+' — REVIEW',fill='black')
 for i,p in enumerate(ps):
  im=Image.open(p);im.thumbnail((395,395));x=i%4*400;y=30+i//4*425;sheet.paste(im,(x,y));draw.text((x+4,y+397),p.name,fill='black')
 sheet.save(preview/(product+'--'+color+'.jpg'))
(J/'selected-review-v01.json').write_text(json.dumps({'status':'pending_full_set_review','image_count':96,'set_count':12,'entries':manifest},ensure_ascii=False,indent=2)+'\n')
# Clear completed attempts from the user review surface while retaining all history.
relocations={};history=J/'review-history';history.mkdir(exist_ok=True)
for name in ['tiempo-8','messi','bata']:
 src=B/'02-REVIEW'/name
 if src.exists():
  dst=history/name;assert not dst.exists()
  for p in src.rglob('*'):
   if p.is_file():relocations[str(p.relative_to(R))]=str((dst/p.relative_to(src)).relative_to(R))
  shutil.move(src,dst)
(J/'review-relocations.json').write_text(json.dumps(relocations,ensure_ascii=False,indent=2)+'\n')
for x in manifest:x['source_path']=relocations.get(x['source_path'],x['source_path'])
(J/'selected-review-v01.json').write_text(json.dumps({'status':'pending_full_set_review','image_count':96,'set_count':12,'entries':manifest},ensure_ascii=False,indent=2)+'\n')
for rec in runs:
 if rec.get('output_path') in relocations:rec['current_path']=relocations[rec['output_path']]
 for i in rec.get('inputs',[]):
  if isinstance(i,dict) and i.get('path') in relocations:i['current_path']=relocations[i['path']]
(J/'runs.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in runs))
print('Assembled 12 sets / 96 PNGs; verified copies; 12 four-line notes and separate previews. Retained legacy images:',sum(op=='reuse_unchanged' for _,op in selected.values()))
