import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';

const root = '/Users/rebecca/Desktop/my websit';
const outDir = path.join(root, 'vedio');
const workDir = path.join(root, '.foundations-media');
const envPath = '/Users/rebecca/Documents/Codex/2026-09-06/files-pasted-by-the-user-ai/outputs/rebecca-ai-explainer/.env';
const fps = 30;
const width = 1920;
const height = 1080;

function readEnv(file) {
  const values = {};
  for (const raw of fs.readFileSync(file, 'utf8').split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const index = line.indexOf('=');
    if (index < 0) continue;
    values[line.slice(0, index).trim()] = line.slice(index + 1).trim().replace(/^['"]|['"]$/g, '');
  }
  return values;
}

const env = readEnv(envPath);
if (!env.AZURE_SPEECH_KEY || !env.AZURE_SPEECH_REGION) {
  throw new Error('Azure Speech configuration is missing from the supplied .env file.');
}

const C = {bg:'#071019', panel:'#102032', panel2:'#0b1723', text:'#f7fafc', muted:'#c2cfdd', line:'#38516d', green:'#78e5bd', blue:'#7fb1ff', amber:'#f7c873'};
const common = {
  'artificial-intelligence': {
    title:'Artificial Intelligence',
    voice:'Artificial intelligence is technology that allows computers to perform tasks that normally require human intelligence. AI can recognize patterns, make predictions, generate content, make recommendations, or take actions. Think of it like a student who has studied millions of examples: when something new arrives, it looks for useful patterns and produces a result. The important question is not whether AI thinks like a person, but what task it performs, what evidence supports the result, and where a human reviews it.',
    scenes:[
      ['WHAT AI CAN DO','AI can recognize patterns, predict, recommend, generate, and take actions.','umbrella',['patterns','prediction','generation','action']],
      ['THINK OF IT LIKE A STUDENT','A system learns from many examples, then applies patterns to something new.','flow',['examples','patterns','new input','result']],
      ['FROM INPUT TO OUTPUT','A photo, document, message, or sensor reading becomes a useful result.','pipeline',['input','process','decision','output']],
      ['REAL-WORLD EXAMPLES','Photo recognition labels a scene; invoice processing extracts fields and flags exceptions.','cards',['photo','invoice','review']],
      ['KEEP A PERSON IN THE LOOP','Important or uncertain results need evidence, review, and a safe handoff.','shield',['task','evidence','human review']],
      ['KEY IDEA','AI performs tasks associated with intelligence, but it is not ChatGPT, fixed-rule automation, or the human mind.','takeaway',['task','evidence','human review']],
    ],
  },
  'machine-learning': {
    title:'Machine Learning',
    voice:'Machine learning is a way for computers to learn patterns from examples instead of receiving every rule by hand. Think of teaching with worked examples: show many examples of spam and not spam, and the learner uses those examples to classify a new message. Training turns examples into a model; inference applies that model to new data. The result may be a label, score, rank, or forecast.',
    scenes:[
      ['LEARN FROM EXAMPLES','Machine learning finds useful patterns in data, then applies them to new inputs.','cards',['examples','patterns','prediction']],
      ['WORKED EXAMPLES','Examples pair inputs with expected outcomes so the system can learn patterns.','stack',['input','outcome','pattern']],
      ['TRAINING','The model compares examples and adjusts until its patterns become useful.','training',['data','learn','pattern']],
      ['A NEW ORDER','A new order is an input; the learned pattern produces a prediction.','flow',['new order','model','next step']],
      ['CHECK THE GUESS','Testing measures where predictions work—and where a person should review.','check',['test','confidence','review']],
      ['KEY IDEA','Machine learning learns from examples, then applies learned patterns to new inputs.','takeaway',['examples','learn','new input']],
    ],
  },
  'deep-learning': {
    title:'Deep Learning',
    voice:'Deep learning is machine learning built with many neural-network layers. Like a stack of kitchen sieves, early layers notice edges or simple sounds, middle layers combine parts, and later layers recognize a whole object or intent. The model learns these representations from examples. More layers can capture richer patterns, but they also need enough data, compute, and careful evaluation.',
    scenes:[
      ['LAYERS OF LEARNING','Deep learning uses many neural-network layers to transform input into a useful result.','layers',['input','layers','output']],
      ['FIRST LAYER','Early layers notice simple signals, like edges, colors, or short sounds.','layers',['pixels','edges','signals']],
      ['MIDDLE LAYERS','Middle layers combine simple pieces into shapes, parts, or sound patterns.','layers',['edges','shapes','parts']],
      ['LATER LAYERS','Later layers recognize a whole object, word, or intent.','layers',['parts','object','intent']],
      ['THE TRADE-OFF','Richer patterns need enough examples, compute, and careful evaluation.','balance',['data','compute','testing']],
      ['KEY IDEA','Deep learning learns increasingly useful representations through many connected layers.','takeaway',['simple signals','richer patterns','task output']],
    ],
  },
  'unsupervised-learning': {
    title:'Unsupervised Learning',
    voice:'Unsupervised learning is a machine-learning method that learns from unlabeled data. Instead of receiving a correct answer for each example, the system looks for structure such as similar groups, relationships, recurring patterns, or unusual data points. Think of sorting a mixed box without labels: similarities in the data create the groups, but people interpret whether that structure is useful.',
    scenes:[
      ['NO PREDEFINED LABELS','Unsupervised learning finds structure in data without being given the correct labels in advance.','umbrella',['unlabeled data','patterns','structure']],
      ['THE MIXED BOX','Sorting a mixed box means grouping objects by similarities, without names supplied in advance.','cards',['round','metal','small']],
      ['MEASURE SIMILARITY','The system compares examples using measurable features, then detects recurring relationships.','training',['examples','similarity','relationships']],
      ['FORM GROUPS','A clustering algorithm may form groups, but the groups do not automatically mean “cat” or “dog.”','flow',['data','clusters','human meaning']],
      ['FIND THE UNUSUAL','Normal activity patterns can help flag unusual examples as possible anomalies.','check',['normal','unusual','inspect']],
      ['KEY IDEA','Unsupervised learning finds structure in data without predefined labels; people inspect whether the result is useful.','takeaway',['structure','no labels','inspect']],
    ],
  },
  'reinforcement-learning': {
    title:'Reinforcement Learning',
    voice:'Reinforcement learning is a machine-learning method where an agent learns by interacting with an environment. The agent observes a state, chooses an action, the environment changes, and the agent receives a reward. Over many attempts, behavior is updated toward a policy that produces better long-term reward. Think of learning a game by playing it: good decisions may lead to rewards, while bad decisions may lead to poor outcomes.',
    scenes:[
      ['AGENT AND ENVIRONMENT','An agent is the decision-making system; the environment is the world it interacts with.','flow',['agent','environment','state']],
      ['CHOOSE AN ACTION','The agent observes the current state and chooses what to do next.','pipeline',['state','action','change']],
      ['RECEIVE FEEDBACK','The environment changes and returns a reward: feedback about the result.','training',['action','environment','reward']],
      ['LEARN THROUGH PLAY','Like learning a game, repeated attempts reveal which actions tend to work better.','cards',['try','result','learn']],
      ['LONG-TERM REWARD','The goal is a policy that produces better long-term reward, not a supplied correct answer.','balance',['policy','short term','long term']],
      ['KEY IDEA','Reinforcement learning teaches an agent which actions work better through interaction and reward.','takeaway',['interact','reward','better actions']],
    ],
  },
  'foundation-models': {
    title:'Foundation Models',
    voice:'A foundation model is a broadly trained starting point that can be adapted to many jobs. Imagine a chef who has practiced many cuisines. Prompting gives a recipe, retrieval supplies today’s ingredients, fine-tuning changes habits, and tools let the chef act. The base model is not the finished product. Reliable behavior also needs permissions, validation, and a workflow that fits the real task.',
    scenes:[
      ['A BROAD STARTING POINT','A foundation model learns from large, varied data before it is adapted to a job.','foundation',['broad data','base model','many tasks']],
      ['THE CHEF ANALOGY','Think of a chef with many cuisines in their memory—not a finished restaurant.','chef',['many cuisines','shared skills','new menu']],
      ['ADAPT THE MODEL','A prompt gives direction; retrieval adds fresh facts; fine-tuning changes habits.','adapt',['prompt','retrieve','fine-tune']],
      ['LET IT ACT','Tools connect model output to actions, with permissions around the boundary.','tools',['model','tool','permission']],
      ['FIT THE WORKFLOW','Validation and human handoff turn broad capability into a reliable product.','workflow',['check','handoff','real task']],
      ['KEY IDEA','A foundation model is a reusable base; the product is the model plus its controls and workflow.','takeaway',['base capability','adaptation','workflow']],
    ],
  },
  'generative-ai': {
    title:'Generative AI',
    voice:'Generative AI creates new text, images, code, audio, or structured results from learned patterns. Imagine a kitchen helper drafting a recipe from today’s ingredients. The model proposes, grounding supplies facts, validation checks the format, and a person approves the final dish. Generation can be creative, but fluency is not proof. A safe product makes evidence and handoff visible.',
    scenes:[
      ['CREATE SOMETHING NEW','Generative AI produces new content from learned patterns and a request.','create',['text','image','code','audio']],
      ['DRAFT A RECIPE','A kitchen helper proposes a recipe using the ingredients available today.','chef',['today’s ingredients','draft','recipe']],
      ['ADD THE FACTS','Grounding supplies trusted context so the draft can reflect the real situation.','ground',['source','context','draft']],
      ['CHECK BEFORE USE','Validation checks structure, rules, and required details before anything moves on.','check',['format','policy','evidence']],
      ['HUMAN APPROVAL','A person confirms the final dish when the decision or risk calls for it.','handoff',['model','review','action']],
      ['KEY IDEA','Generative AI can create fluently; a safe workflow makes facts, checks, and handoff visible.','takeaway',['generate','validate','approve']],
    ],
  },
  'llm': {
    title:'Large Language Models',
    voice:'A Large Language Model, or LLM, learns patterns in language and uses them to predict likely next tokens. It can summarize, translate, answer, classify, or generate text, but an output is not automatically true. Think of it like an extremely well-read autocomplete system: it uses the current context and instructions to continue language. Tokens enter, the Transformer processes relationships between them, and the model generates a response one token at a time. Good applications add relevant context, tools, and evaluation.',
    scenes:[
      ['WHAT AN LLM IS','An LLM learns language patterns and predicts likely next tokens.','foundation',['language data','language model','text output']],
      ['THE AUTOCOMPLETE ANALOGY','Think of it like an extremely well-read autocomplete system using the current context.','chef',['context','learned patterns','continuation']],
      ['FROM TEXT TO TOKENS','A prompt becomes tokens, the small units the model processes.','flow',['text','tokens','context','model']],
      ['PROCESS THE CONTEXT','Transformer layers process relationships between tokens and score possible continuations.','adapt',['tokens','relationships','scores']],
      ['GENERATE ONE STEP AT A TIME','Selected tokens are added one by one until the system stops.','tools',['prompt','next token','response']],
      ['KEY IDEA','An LLM generates language from learned patterns and current context; fluency is not proof of truth.','takeaway',['learned patterns','context','check']],
    ],
  },
  'parameters': {
    title:'Parameters',
    voice:'Parameters are the learned numerical values inside a model. Training adjusts many of them so the model becomes better at its task. Think of parameters like the settings inside a large mixing desk: training changes many tiny controls, and inference uses the final settings. During training, the model makes a prediction, compares it with a target, and an optimizer updates the values. During inference, those trained values shape responses to new inputs. Parameter count describes scale, not guaranteed quality, truthfulness, or speed.',
    scenes:[
      ['WHAT PARAMETERS ARE','Parameters are learned numerical values inside a model.','foundation',['model','learned values','behavior']],
      ['THE MIXING DESK ANALOGY','Think of many tiny settings that training adjusts gradually.','chef',['many settings','training','response']],
      ['START WITH A PREDICTION','A model receives an example and produces an output using its current values.','flow',['example','current values','prediction']],
      ['COMPARE AND UPDATE','The system measures error, then an optimizer changes many parameters slightly.','adapt',['prediction','error','update']],
      ['USE THE TRAINED VALUES','During inference, the values stay fixed while they shape results for new inputs.','tools',['new input','trained values','output']],
      ['KEY IDEA','Parameters shape model behavior; more parameters do not automatically mean better quality.','takeaway',['learned values','model behavior','task fit']],
    ],
  },
};

function esc(value) {
  return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}

function textLines(text, x, y, size, fill, weight = 500, anchor = 'start') {
  const words = text.split(' ');
  const lines = [];
  let current = '';
  const max = 48;
  for (const word of words) {
    if ((current + ' ' + word).trim().length > max) { lines.push(current); current = word; } else current = (current + ' ' + word).trim();
  }
  if (current) lines.push(current);
  return lines.map((line, i) => `<text x="${x}" y="${y + i * (size + 10)}" text-anchor="${anchor}" font-family="Arial,Helvetica,sans-serif" font-size="${size}px" font-weight="${weight}" fill="${fill}">${esc(line)}</text>`).join('');
}

function pill(label, x, y, w, active = false) {
  return `<rect x="${x}" y="${y}" width="${w}" height="54" rx="27" fill="${active ? C.green : '#173047'}" stroke="${active ? C.green : C.line}" stroke-width="2"/><text x="${x + w / 2}" y="${y + 34}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="22px" font-weight="700" fill="${active ? '#071019' : C.text}">${esc(label)}</text>`;
}

function boxes(labels, x, y, boxW = 280, gap = 34, active = 1) {
  return labels.map((label, i) => `<g transform="translate(${x + i * (boxW + gap)},${y})"><rect width="${boxW}" height="150" rx="22" fill="${i === active ? '#173b4a' : C.panel}" stroke="${i === active ? C.green : C.line}" stroke-width="3"/><circle cx="42" cy="42" r="20" fill="${i === active ? C.green : C.blue}"/><text x="42" y="50" text-anchor="middle" font-family="Arial" font-size="20px" font-weight="800" fill="#071019">${i + 1}</text>${textLines(label, 28, 94, 27, C.text, 800)}</g>${i < labels.length - 1 ? `<path d="M${x + (i + 1) * boxW + i * gap + 12},${y + 75} L${x + (i + 1) * boxW + i * gap + gap - 12},${y + 75}" stroke="${C.green}" stroke-width="5" marker-end="url(#arrow)"/>` : ''}`).join('');
}

function graphic(kind, labels) {
  if (kind === 'umbrella') return `<path d="M960 250 C650 250 490 440 490 575 H1430 C1430 440 1270 250 960 250Z" fill="#173756" stroke="${C.blue}" stroke-width="5"/><path d="M960 575 V725 C960 790 1065 790 1065 725" fill="none" stroke="${C.green}" stroke-width="12" stroke-linecap="round"/><text x="960" y="475" text-anchor="middle" font-family="Arial" font-size="62px" font-weight="850" fill="${C.text}">AI</text>${labels.map((l, i) => pill(l, 620 + i * 190, 835, 160, i === 0)).join('')}`;
  if (kind === 'layers') return labels.map((l, i) => { const x = 570 + i * 250; const y = 360 - i * 32; return `<g><rect x="${x}" y="${y}" width="210" height="250" rx="28" fill="${i === 1 ? '#173b4a' : C.panel}" stroke="${i === 1 ? C.green : C.line}" stroke-width="4"/><text x="${x + 105}" y="${y + 105}" text-anchor="middle" font-family="Arial" font-size="26px" font-weight="800" fill="${C.text}">${esc(l)}</text><circle cx="${x + 72}" cy="${y + 165}" r="12" fill="${C.blue}"/><circle cx="${x + 105}" cy="${y + 190}" r="12" fill="${C.green}"/><circle cx="${x + 138}" cy="${y + 165}" r="12" fill="${C.blue}"/></g>`; }).join('');
  if (kind === 'shield') return `<path d="M960 250 L1290 380 V600 C1290 805 1115 900 960 950 C805 900 630 805 630 600 V380Z" fill="#173756" stroke="${C.green}" stroke-width="7"/><path d="M800 575 L915 690 L1135 445" fill="none" stroke="${C.green}" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>${labels.map((l, i) => pill(l, 670 + i * 195, 820, 170, i === 2)).join('')}`;
  if (kind === 'stack' || kind === 'cards') return labels.map((l, i) => `<g><rect x="${700 + i * 150}" y="${390 - i * 24}" width="520" height="170" rx="24" fill="${i === 1 ? '#173b4a' : C.panel}" stroke="${i === 1 ? C.green : C.line}" stroke-width="4"/><text x="${960 + i * 150}" y="${485 - i * 24}" text-anchor="middle" font-family="Arial" font-size="34px" font-weight="800" fill="${C.text}">${esc(l)}</text></g>`).join('');
  if (kind === 'training') return `<circle cx="960" cy="515" r="150" fill="#173756" stroke="${C.green}" stroke-width="6"/><text x="960" y="530" text-anchor="middle" font-family="Arial" font-size="42px" font-weight="850" fill="${C.text}">learn</text><path d="M680 515 H790 M1130 515 H1240" stroke="${C.blue}" stroke-width="12" marker-end="url(#arrow)"/><rect x="470" y="425" width="190" height="180" rx="20" fill="${C.panel}" stroke="${C.line}" stroke-width="3"/><text x="565" y="505" text-anchor="middle" font-family="Arial" font-size="25px" font-weight="800" fill="${C.text}">examples</text><rect x="1260" y="425" width="190" height="180" rx="20" fill="${C.panel}" stroke="${C.line}" stroke-width="3"/><text x="1355" y="505" text-anchor="middle" font-family="Arial" font-size="25px" font-weight="800" fill="${C.text}">pattern</text>`;
  if (kind === 'foundation' || kind === 'adapt' || kind === 'tools' || kind === 'workflow' || kind === 'flow' || kind === 'pipeline' || kind === 'ground' || kind === 'handoff' || kind === 'check' || kind === 'balance' || kind === 'create') return boxes(labels, 420, 410, 300, 70, Math.min(1, labels.length - 1));
  if (kind === 'chef') return `<circle cx="960" cy="480" r="170" fill="#173756" stroke="${C.amber}" stroke-width="7"/><text x="960" y="500" text-anchor="middle" font-family="Arial" font-size="56px" font-weight="850" fill="${C.text}">CHEF</text>${labels.map((l, i) => pill(l, 540 + i * 285, 760, 250, i === 1)).join('')}`;
  if (kind === 'takeaway') return `<rect x="500" y="330" width="920" height="300" rx="36" fill="url(#card)" stroke="${C.green}" stroke-width="5"/><text x="960" y="450" text-anchor="middle" font-family="Arial" font-size="58px" font-weight="850" fill="${C.text}">${esc(labels[0])}</text><text x="960" y="545" text-anchor="middle" font-family="Arial" font-size="42px" font-weight="700" fill="${C.green}">${esc(labels[1])} → ${esc(labels[2])}</text>`;
  return boxes(labels, 420, 410, 300, 70, 1);
}

function svgFor(topic, scene, index) {
  const [heading, caption, kind, labels] = scene;
  const data = common[topic];
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071019"/><stop offset="1" stop-color="#10263a"/></linearGradient><linearGradient id="card" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#173756"/><stop offset="1" stop-color="#10261f"/></linearGradient><marker id="arrow" markerWidth="12" markerHeight="12" refX="8" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="${C.green}"/></marker></defs>
  <rect width="${width}" height="${height}" fill="url(#bg)"/><circle cx="1750" cy="80" r="270" fill="#18335a" opacity=".3"/><circle cx="150" cy="1020" r="260" fill="#12352f" opacity=".25"/>
  <text x="100" y="88" font-family="Arial,Helvetica,sans-serif" font-size="25px" font-weight="800" letter-spacing="5" fill="${C.green}">REBECCA AI EXPLAINER · 01</text>
  <text x="100" y="168" font-family="Arial,Helvetica,sans-serif" font-size="60px" font-weight="850" fill="${C.text}">${esc(data.title)}</text>
  <text x="1820" y="88" text-anchor="end" font-family="Arial" font-size="22px" font-weight="700" fill="${C.muted}">${String(index + 1).padStart(2, '0')} / 06</text>
  ${graphic(kind, labels)}
  <rect x="76" y="884" width="1768" height="146" rx="22" fill="#07111a" stroke="${C.line}" stroke-width="3"/>
  <text x="112" y="928" font-family="Arial" font-size="21px" font-weight="800" letter-spacing="2" fill="${C.blue}">${esc(heading)}</text>${textLines(caption, 112, 972, 25, C.text, 600)}
  </svg>`;
}

function ssml(text) {
  return `<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="en-US-JennyNeural"><prosody rate="0%" pitch="0%">${esc(text)}</prosody></voice></speak>`;
}

async function synthesize(text, file) {
  const endpoint = `https://${env.AZURE_SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1`;
  const response = await fetch(endpoint, {method:'POST', headers:{'Ocp-Apim-Subscription-Key':env.AZURE_SPEECH_KEY, 'Content-Type':'application/ssml+xml', 'X-Microsoft-OutputFormat':'audio-24khz-48kbitrate-mono-mp3', 'User-Agent':'rebecca-ai-foundations-media'}, body:ssml(text)});
  if (!response.ok) throw new Error(`Azure Speech returned ${response.status}`);
  fs.writeFileSync(file, Buffer.from(await response.arrayBuffer()));
}

function run(args) {
  execFileSync('/opt/homebrew/bin/ffmpeg', args, {stdio:'ignore'});
}

function duration(file) {
  return Number(execFileSync('/opt/homebrew/bin/ffprobe', ['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',file], {encoding:'utf8'}).trim());
}

function makeVtt(data, totalDuration, out) {
  let cursor = 0;
  const lines = ['WEBVTT', ''];
  for (let i = 0; i < data.scenes.length; i++) {
    const end = (i + 1 === data.scenes.length) ? totalDuration : totalDuration * ((i + 1) / data.scenes.length);
    const stamp = (s) => { const ms = Math.round((s % 1) * 1000); const total = Math.floor(s); const sec = total % 60; const min = Math.floor(total / 60); return `00:${String(min).padStart(2,'0')}:${String(sec).padStart(2,'0')}.${String(ms).padStart(3,'0')}`; };
    lines.push(`${stamp(cursor)} --> ${stamp(end)}`, data.scenes[i][1], '');
    cursor = end;
  }
  fs.writeFileSync(out, lines.join('\n'));
}

async function makeTopic(topic, data) {
  const dir = path.join(workDir, topic);
  fs.mkdirSync(dir, {recursive:true});
  const audioFiles = [];
  const audioDurations = [];
  const sceneVideos = [];
  for (let i = 0; i < data.scenes.length; i++) {
    const svg = path.join(dir, `scene-${i}.svg`);
    const png = path.join(dir, `scene-${i}.png`);
    const mp4 = path.join(dir, `scene-${i}.mp4`);
    const text = data.scenes[i][1];
    fs.writeFileSync(svg, svgFor(topic, data.scenes[i], i));
    execFileSync('/usr/bin/sips', ['-s','format','png',svg,'--out',png], {stdio:'ignore'});
    const audio = path.join(dir, `audio-${i}.mp3`);
    if (!fs.existsSync(audio)) await synthesize(text, audio);
    const d = duration(audio) + 0.35;
    audioFiles.push(audio);
    audioDurations.push(d);
    run(['-y','-loglevel','error','-loop','1','-i',png,'-t',String(d),'-vf',`scale=${width}:${height},format=yuv420p,fade=t=in:st=0:d=0.25,fade=t=out:st=${Math.max(0.3, d - 0.3)}:d=0.3`,'-r',String(fps),'-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p',mp4]);
    sceneVideos.push(mp4);
  }
  const audioList = path.join(dir, 'audio-list.txt');
  const videoList = path.join(dir, 'video-list.txt');
  fs.writeFileSync(audioList, audioFiles.map((f) => `file '${f.replaceAll("'", "'\\''")}'`).join('\n'));
  fs.writeFileSync(videoList, sceneVideos.map((f) => `file '${f.replaceAll("'", "'\\''")}'`).join('\n'));
  const audio = path.join(dir, 'audio.mp3');
  const video = path.join(dir, 'video.mp4');
  run(['-y','-loglevel','error','-f','concat','-safe','0','-i',audioList,'-c:a','libmp3lame','-b:a','48k',audio]);
  run(['-y','-loglevel','error','-f','concat','-safe','0','-i',videoList,'-c','copy',video]);
  const output = path.join(outDir, `${topic}.mp4`);
  run(['-y','-loglevel','error','-i',video,'-i',audio,'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','128k','-shortest',output]);
  fs.copyFileSync(path.join(dir, 'scene-2.png'), path.join(outDir, `${topic}.png`));
  makeVtt(data, duration(output), path.join(outDir, `${topic}.vtt`));
  console.log(`rendered ${topic} (${duration(output).toFixed(1)}s)`);
}

fs.mkdirSync(outDir, {recursive:true});
fs.mkdirSync(workDir, {recursive:true});
const requestedTopics = ['artificial-intelligence', 'machine-learning', 'unsupervised-learning', 'reinforcement-learning', 'deep-learning'];
for (const topic of requestedTopics) await makeTopic(topic, common[topic]);
