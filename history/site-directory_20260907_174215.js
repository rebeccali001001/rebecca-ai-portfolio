(function(){
  const groups = [
    { name: '01 · AI Foundations', overview: ['Chapter overview', 'ai-foundations.html'], items: [
      ['Artificial Intelligence', 'artificial-intelligence.html'], ['Machine Learning', 'machine-learning.html'],
      ['Deep Learning', 'deep-learning.html'], ['Foundation Models', 'foundation-models.html'], ['Generative AI', 'generative-ai.html']
    ]},
    { name: '02 · LLMs & Transformers', overview: ['Chapter overview', 'llms-transformers.html'], items: [
      ['LLM', 'llm.html'], ['Transformer', 'transformer.html'], ['Parameters', 'parameters.html'],
      ['Pre-training', 'pre-training.html'], ['Fine-tuning', 'fine-tuning.html']
    ]},
    { name: '03 · Tokens, Context & Inference', overview: ['Chapter overview', 'tokens-context-inference.html'], items: [
      ['Token', 'token.html'], ['Context Window', 'context-window.html'], ['KV Cache', 'kv-cache.html'],
      ['Latency', 'latency.html'], ['Tokens per Second', 'tokens-per-second.html']
    ]},
    { name: '04 · Prompting & System Design', overview: ['Chapter overview', 'prompting-system-design.html'], items: [] },
    { name: '05 · Embeddings, RAG & Vector Search', overview: ['Chapter overview', 'embeddings-rag-vector-search.html'], items: [] },
    { name: '06 · Agents, Tools & MCP', overview: null, items: [], note: 'Topic pages coming soon' },
    { name: '07 · Model Serving & Local AI', overview: ['Chapter overview', 'model-serving-local-ai.html'], items: [
      ['Ollama', 'ollama.html'], ['Quantization', 'quantization.html'], ['Runtime Constraints', 'runtime-constraints.html']
    ]},
    { name: '08 · Evaluation & Reliability', overview: null, items: [['Functional Tests', 'functional-tests.html']], note: 'More evaluation topics coming soon' },
    { name: '09 · Enterprise AI Deployment', overview: null, items: [
      ['Workflow Discovery', 'workflow-discovery.html'], ['Technical Scoping', 'technical-scoping.html'],
      ['Integration', 'integration.html'], ['Adoption', 'adoption.html']
    ], note: 'Deployment practice pages' }
  ];

  const hasDirectory = document.querySelector('.site-directory, .sidebar, .directory');
  if (hasDirectory) return;

  const current = location.pathname.split('/').pop() || 'index.html';
  const aside = document.createElement('aside');
  aside.className = 'site-directory';
  aside.setAttribute('aria-label', 'AI knowledge map');

  const title = document.createElement('h2');
  title.textContent = 'Knowledge map · 01–09';
  aside.append(title);

  groups.forEach(group => {
    const details = document.createElement('details');
    const summary = document.createElement('summary');

    if (group.overview) {
      const link = document.createElement('a');
      link.className = 'module';
      link.href = group.overview[1];
      link.textContent = group.name + ' ↗';
      summary.append(link);
    } else {
      summary.textContent = group.name;
    }
    details.append(summary);

    const list = document.createElement('ul');
    if (group.overview) {
      const li = document.createElement('li');
      const link = document.createElement('a');
      link.href = group.overview[1];
      link.textContent = group.overview[0];
      if (group.overview[1].split('#')[0] === current) link.className = 'active';
      li.append(link);
      list.append(li);
    }
    group.items.forEach(([label, href]) => {
      const li = document.createElement('li');
      const link = document.createElement('a');
      link.href = href;
      link.textContent = label;
      if (href.split('#')[0] === current) link.className = 'active';
      li.append(link);
      list.append(li);
    });
    if (group.note) {
      const li = document.createElement('li');
      li.className = 'directory-note';
      li.textContent = group.note;
      list.append(li);
    }
    details.append(list);
    aside.append(details);
  });

  document.body.prepend(aside);
  document.body.classList.add('has-site-directory');
})();
