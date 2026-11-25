"""Copy recorded built-in imagegen outputs to review and append provenance once.
Usage: python3 .../collect_job_outputs.py PATH_TO_RESULT_JSON
No image modification or image generation is performed.
"""
from pathlib import Path
import json,sys,shutil,hashlib
from datetime import datetime
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[3]
def collect(plan):
 job=plan.parent; rows=json.loads(plan.read_text()); log=job/'runs.jsonl'
 existing=[json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
 seen={x.get('image_id') for x in existing}
 for row in rows:
  if not row.get('file'):continue
  product=row.get('product','tiempo-8');color=row.get('color','red-black');revision=row.get('revision','complete-v01')
  dst=ROOT/'photo-workshop/02-REVIEW'/product/color/revision/row['name'];dst.parent.mkdir(parents=True,exist_ok=True)
  source=Path(row['file']);sha=hashlib.sha256(source.read_bytes()).hexdigest()
  if dst.exists():assert hashlib.sha256(dst.read_bytes()).hexdigest()==sha, f'Refusing overwrite: {dst}'
  else:shutil.copy2(source,dst)
  iid=f'IMG-{product}-{color}-{revision}-{dst.stem}'
  if iid not in seen:
   idx=json.loads((ROOT/'photo-workshop/04-WORKSPACE/source-index.json').read_text())['assets'];ids={str(ROOT/x['path']):x['asset_id'] for x in idx}
   rec={'run_id':iid,'image_id':iid,'time':datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(),'product_color':product+'/'+color,'inputs':[{'path':str(Path(p).relative_to(ROOT)) if Path(p).is_relative_to(ROOT) else p,'asset_id':ids.get(p),'role':'edit target or set style' if i==0 else 'construction evidence'} for i,p in enumerate(row['refs'])],'prompt':row['prompt'],'tool':'image_gen.imagegen','model':None,'output_path':str(dst.relative_to(ROOT)),'sha256':sha,'status':'pending_user_review','limitations':row.get('limitations',[])}
   with log.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
   seen.add(iid)
 return len(rows)
if __name__=='__main__':print('Collected',collect(Path(sys.argv[1]).resolve()),'records')
