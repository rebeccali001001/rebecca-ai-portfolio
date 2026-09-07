(function(){
  if(document.querySelector('.site-directory,.sidebar,.directory')) return;

  // Keep this directory limited to pages that are present in the static site.
  const groups=[
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
      ['Chapter overview','prompting-system-design.html'],['System Prompts','system-prompts.html'],['Structured Outputs','structured-outputs.html'],['Failure Handling','failure-handling.html']
    ]],
    ['05 · Embeddings, RAG & Vector Search','embeddings-rag-vector-search.html',[
      ['Chapter overview','embeddings-rag-vector-search.html'],['Embeddings','embeddings.html'],['RAG','rag.html'],['Vector Search','vector-search.html'],['Grounding','grounding.html']
    ]],
    ['06 · Agents, Tools & MCP','ai-knowledge.html#agents',[
      ['Chapter section','ai-knowledge.html#agents'],['AI Agent','ai-agent.html'],['Tool Calling','tool-calling.html'],['Agent Loop','agent-loop.html']
    ]],
    ['07 · Model Serving & Local AI','model-serving-local-ai.html',[
      ['Chapter overview','model-serving-local-ai.html'],['Ollama','ollama.html'],['Quantization','quantization.html'],['Runtime Constraints','runtime-constraints.html']
    ]],
    ['08 · Evaluation & Reliability','ai-knowledge.html#eval',[
      ['Chapter section','ai-knowledge.html#eval'],['Functional Tests','functional-tests.html'],['Failure Modes','failure-modes.html'],['Deployment Readiness','deployment-readiness.html']
    ]],
    ['09 · Enterprise AI Deployment','enterprise-ai-deployment.html',[
      ['Chapter overview','enterprise-ai-deployment.html'],['Workflow Discovery','workflow-discovery.html'],['Technical Scoping','technical-scoping.html'],['Integration','integration.html'],['Evaluation','evaluation.html'],['Adoption','adoption.html']
    ]]
  ];

  const current=location.pathname.split('/').pop()||'index.html';
  const aside=document.createElement('aside');
  aside.className='site-directory';
  aside.setAttribute('aria-label','AI knowledge map');
  const title=document.createElement('h2');
  title.textContent='Knowledge map · 01–09';
  aside.append(title);
  groups.forEach(([name,overview,items])=>{
    const d=document.createElement('details');
    const s=document.createElement('summary');
    const moduleLink=document.createElement('a');
    moduleLink.className='module';
    moduleLink.href=overview;
    moduleLink.textContent=name+' ↗';
    s.append(moduleLink);
    d.append(s);
    const ul=document.createElement('ul');
    items.forEach(([label,href])=>{
      const li=document.createElement('li');
      const a=document.createElement('a');
      a.href=href;
      a.textContent=label;
      if(href.split('#')[0]===current) a.className='active';
      li.append(a);
      ul.append(li);
    });
    d.append(ul);
    aside.append(d);
  });
  document.body.prepend(aside);
  document.body.classList.add('has-site-directory');
})();
