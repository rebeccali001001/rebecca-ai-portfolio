(() => {
  const groups = [
    ['01 · AI Foundations','ai-foundations.html',[
      ['Chapter overview','ai-foundations.html'],['Artificial Intelligence','artificial-intelligence.html'],['Machine Learning','machine-learning.html'],['Deep Learning','deep-learning.html'],['Foundation Models','foundation-models.html'],['Generative AI','generative-ai.html']
    ]],
    ['02 · LLMs & Transformers','llms-transformers.html',[
      ['Chapter overview','llms-transformers.html'],['LLM','llm.html'],['Transformer','transformer.html'],['Parameters','parameters.html'],['Pre-training','pre-training.html'],['Fine-tuning','fine-tuning.html']
    ]],
    ['03 · Tokens, Context & Inference','tokens-context-inference.html',[
      ['Chapter overview','tokens-context-inference.html'],['Token','token.html'],['Context Window','context-window.html'],['KV Cache','kv-cache.html'],['Latency','latency.html'],['Tokens per Second','tokens-per-second.html']
    ]],
    ['04 · Prompting & System Design','prompting-system-design.html',[
      ['Chapter overview','prompting-system-design.html']
    ]],
    ['05 · Embeddings, RAG & Vector Search','embeddings-rag-vector-search.html',[
      ['Chapter overview','embeddings-rag-vector-search.html']
    ]],
    ['06 · Agents, Tools & MCP','ai-knowledge.html#agents',[
      ['Chapter section','ai-knowledge.html#agents']
    ]],
    ['07 · Model Serving & Local AI','model-serving-local-ai.html',[
      ['Chapter overview','model-serving-local-ai.html'],['Ollama','ollama.html'],['Quantization','quantization.html'],['Runtime Constraints','runtime-constraints.html']
    ]],
    ['08 · Evaluation & Reliability','evaluation.html',[
      ['Chapter overview','evaluation.html'],['Functional Tests','functional-tests.html']
    ]],
    ['09 · Enterprise AI Deployment','ai-knowledge.html#enterprise',[
      ['Chapter section','ai-knowledge.html#enterprise'],['Workflow Discovery','workflow-discovery.html'],['Technical Scoping','technical-scoping.html'],['Integration','integration.html'],['Adoption','adoption.html']
    ]]
  ];

  if (document.querySelector('.site-directory,.directory')) return;
  const current = location.pathname.split('/').pop() || 'index.html';
  const aside = document.createElement('aside');
  aside.className = 'site-directory';
  aside.setAttribute('aria-label','AI knowledge map');
  const title = document.createElement('h2');
  title.textContent = 'Knowledge map · 01–09';
  aside.append(title);

  groups.forEach(([name, overview, items]) => {
    const details = document.createElement('details');
    const summary = document.createElement('summary');
    const module = document.createElement('a');
    module.className = 'module';
    module.href = overview;
    module.textContent = name + ' ↗';
    summary.append(module);
    details.append(summary);

    const list = document.createElement('ul');
    items.forEach(([label, href]) => {
      const li = document.createElement('li');
      const link = document.createElement('a');
      link.href = href;
      link.textContent = label;
      if (href.split('#')[0] === current) link.className = 'active';
      li.append(link);
      list.append(li);
    });
    details.append(list);
    aside.append(details);
  });
  document.body.prepend(aside);
  document.body.classList.add('has-site-directory');
})();
