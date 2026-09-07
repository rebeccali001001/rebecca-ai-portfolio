#!/usr/bin/env python3
from pathlib import Path
import html, os, subprocess, tempfile
ROOT=Path(__file__).resolve().parent; VIDEO=ROOT/'vedio'; ENV=Path('/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env'); VOICE='en-US-JennyNeural'
LINES={
'pre-training':[
'Pre-training is the broad initial training stage that teaches a model general patterns from large amounts of data.',
'Think of it like general education. A student studies many subjects before choosing one job, and a model first learns from broad material.',
'The loop is simple: turn language into tokens, predict a missing or next token, compare the prediction with the target, and update parameters.',
'For example, given “The trader closed the position because it was,” the model may learn that a continuation such as “risky” is likely.',
'Pre-training is not fine-tuning, prompting, or RAG. It changes model parameters during broad initial training; the others are different adaptation or runtime choices.',
'Remember: pre-training teaches broad patterns from large amounts of data before task-specific adaptation.'
],
'fine-tuning':[
'Fine-tuning is additional training that adapts a pre-trained model for a more specific behavior or task.',
'Think of it like specialist training after general education. The learner keeps broad skills and practices a narrower job with focused examples.',
'Start with a base model, prepare target input and output examples, update parameters or adapters, and evaluate quality, safety, and general behavior.',
'Examples include more consistent support categories, a preferred writing tone, or predictable fields from a document.',
'Fine-tuning is not prompting or RAG. It changes learned behavior through additional training; prompting changes runtime instructions, while RAG retrieves external information at query time.',
'Remember: fine-tuning makes a pre-trained model more consistent for a specific task. It is not a live knowledge update.'
]}
def env():
 v={};
 for line in ENV.read_text().splitlines():
  if '=' in line and not line.lstrip().startswith('#'): k,x=line.split('=',1);v[k.strip()]=x.strip().strip('"').strip("'")
 return v.get('AZURE_SPEECH_KEY') or os.environ.get('AZURE_SPEECH_KEY'),v.get('AZURE_SPEECH_REGION') or os.environ.get('AZURE_SPEECH_REGION')
def run(c): subprocess.run(c,check=True)
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(p)]))
def wav(text,key,region,out):
 ssml=f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'><voice name='{VOICE}'><prosody rate='0%'>{html.escape(text)}</prosody></voice></speak>"; s=out.with_suffix('.ssml');s.write_text(ssml);run(['curl','-fsS','--retry','4','--retry-all-errors','--retry-delay','2','--connect-timeout','15','--max-time','120','-X','POST',f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1','-H',f'Ocp-Apim-Subscription-Key: {key}','-H','Content-Type: application/ssml+xml','-H','X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm','--data-binary',f'@{s}','-o',str(out)]);s.unlink()
key,region=env()
if not key or not region: raise SystemExit('Azure Speech configuration is missing')
with tempfile.TemporaryDirectory(prefix='module04-frames-') as td:
 frames=Path(td)/'frames';run(['swift',str(ROOT/'render_module04_frames.swift'),str(frames)])
 for slug,lines in LINES.items():
  with tempfile.TemporaryDirectory(prefix=slug+'-') as t:
   t=Path(t); seg=[]
   for i,line in enumerate(lines):
    a=t/f'{i}.wav';wav(line,key,region,a); s=t/f'{i}.mp4';run(['ffmpeg','-y','-loop','1','-i',str(frames/slug/f'scene-{i:02d}.png'),'-i',str(a),'-vf','scale=1920:1080:flags=lanczos,format=yuv420p','-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','medium','-crf','20','-t',f'{dur(a):.3f}','-c:a','aac','-b:a','160k','-ar','24000','-ac','1','-shortest',str(s)]);seg.append(s)
   c=t/'concat.txt';c.write_text('\n'.join("file '"+str(x)+"'" for x in seg)+'\n');out=VIDEO/f'{slug}.mp4';run(['ffmpeg','-y','-f','concat','-safe','0','-i',str(c),'-c','copy','-movflags','+faststart',str(out)]);run(['ffmpeg','-y','-ss','1','-i',str(out),'-frames:v','1','-update','1',str(VIDEO/f'{slug}.png')]);print(out,dur(out))
