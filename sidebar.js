(function () {
  const mount = document.getElementById('site-directory');
  const installGlobalNav = () => {
    const headerNav = document.querySelector('body > nav');
    const headerWrap = headerNav && headerNav.querySelector(':scope > .wrap');
    if (headerWrap && !headerWrap.querySelector('.site-global-links')) {
      headerNav.classList.add('site-header-nav');
      const globalLinks = document.createElement('div');
      globalLinks.className = 'site-global-links';
      globalLinks.setAttribute('aria-label', 'Portfolio navigation');
      globalLinks.innerHTML = [
        '<a href="portfolio-home.html#profile">Profile</a>',
        '<a href="articles.html">Blog</a>',
        '<div class="site-nav-dropdown"><button class="site-nav-trigger" type="button" aria-expanded="false">Knowledge <span aria-hidden="true">▾</span></button><div class="site-nav-menu"><a href="file:///C:/Users/rebecca.li/Desktop/codex/my%20profile/ai-knowledge-summary.html">AI Knowledge</a><a href="software-knowledge.html">Software Knowledge</a><a href="syntax-overview.html">Language &amp; Syntax</a></div></div>'
      ].join('');
      headerWrap.append(globalLinks);
      const trigger = globalLinks.querySelector('.site-nav-trigger');
      const dropdown = globalLinks.querySelector('.site-nav-dropdown');
      trigger.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        const open = dropdown.classList.toggle('is-open');
        trigger.setAttribute('aria-expanded', String(open));
      });
      dropdown.querySelector('.site-nav-menu').addEventListener('click', (event) => event.stopPropagation());
      document.addEventListener('click', (event) => {
        if (!dropdown.contains(event.target)) {
          dropdown.classList.remove('is-open');
          trigger.setAttribute('aria-expanded', 'false');
        }
      });
      if (mount) {
        const menu = document.createElement('button');
        menu.className = 'knowledge-menu-toggle';
        menu.type = 'button';
        menu.textContent = '☰ Menu';
        menu.setAttribute('aria-expanded', 'false');
        menu.addEventListener('click', () => {
          const open = document.body.classList.toggle('directory-open');
          menu.setAttribute('aria-expanded', String(open));
        });
        headerWrap.append(menu);
      }
    }
  };
  if (!mount) {
    installGlobalNav();
    return;
  }
  mount.classList.add('site-directory');
  const authenticationMapCard = [...document.querySelectorAll('.map-support article')].find((card) => card.textContent.includes('Authentication & Security'));
  if (authenticationMapCard && !authenticationMapCard.querySelector('a[href="session.html"]')) {
    authenticationMapCard.insertAdjacentHTML('beforeend', '<a href="session.html">Explore Session →</a>');
  }
  const developmentMapCard = [...document.querySelectorAll('.map-support article')].find((card) => card.textContent.includes('Development & Git'));
  if (developmentMapCard && !developmentMapCard.querySelector('a[href="code-review.html"]')) {
    developmentMapCard.insertAdjacentHTML('beforeend', '<a href="pull-request.html">Explore Pull Request →</a><a href="code-review.html">Explore Code Review →</a><a href="merge.html">Explore Merge →</a>');
  }
  if (document.body.classList.contains('module04-glossary')) {
    document.querySelectorAll('#glossary td').forEach((cell) => {
      if (cell.textContent.trim() === 'Function' && !cell.querySelector('a')) cell.innerHTML = '<a href="function.html">Function</a>';
    });
  }
  if (document.body.classList.contains('software-glossary')) {
    const databaseGlossary = document.querySelector('#data-database tbody');
    if (databaseGlossary && !databaseGlossary.querySelector('[data-relational-database]')) {
      databaseGlossary.insertAdjacentHTML('beforeend', '<tr data-relational-database><td><a href="relational-database.html">Relational Database</a></td><td>关系型数据库</td><td>A database that stores data in tables and connects related records.</td><td>把数据放在表里，并把相关记录连接起来的数据库。</td></tr>');
    }
    databaseGlossary?.querySelectorAll('td:first-child').forEach((cell) => {
      if (cell.textContent.trim() === 'Relationship' && !cell.querySelector('a')) cell.innerHTML = '<a href="relationship.html">Relationship</a>';
    });
    const deliveryGlossary = document.querySelector('#environment-delivery tbody');
    if (deliveryGlossary && !deliveryGlossary.querySelector('[data-package]')) {
      deliveryGlossary.insertAdjacentHTML('beforeend', '<tr data-package><td><a href="package.html">Package</a></td><td>软件包</td><td>A distributable collection of software files and metadata that can be installed or reused.</td><td>把软件文件和说明信息打包在一起，方便安装或重复使用。</td></tr>');
    }
  }
  const moduleFiveTopics = document.querySelector('.module-five-page .topic-list');
  if (moduleFiveTopics && !moduleFiveTopics.querySelector('a[href="dbms.html"]')) {
    moduleFiveTopics.insertAdjacentHTML('afterbegin', '<a href="dbms.html"><b>DBMS</b><span>Manage, protect, and provide access to databases.</span><em>Open topic →</em></a>');
  }
  if (moduleFiveTopics && !moduleFiveTopics.querySelector('a[href="column.html"]')) {
    moduleFiveTopics.insertAdjacentHTML('beforeend', '<a href="column.html"><b>Column</b><span>One named type of information stored for every row.</span><em>Open topic →</em></a>');
  }
  if (moduleFiveTopics) {
    const sqlTopic = [...moduleFiveTopics.children].find((item) => item.textContent.trim().startsWith('SQL'));
    if (sqlTopic && sqlTopic.tagName === 'A') sqlTopic.href = 'sql.html';
  }
  const moduleFiveGlossary = document.querySelector('.module-five-glossary #glossary');
  if (moduleFiveGlossary && !moduleFiveGlossary.querySelector('tbody tr:first-child td:first-child')?.textContent.includes('DBMS')) {
    moduleFiveGlossary.querySelector('tbody').insertAdjacentHTML('afterbegin', '<tr><td><a href="dbms.html">DBMS</a></td><td>数据库管理系统</td><td>Software that manages databases and access to their data.</td><td>负责管理数据库、处理读写请求并控制访问权限的软件。</td></tr>');
  }
  if (moduleFiveGlossary) {
    moduleFiveGlossary.querySelectorAll('tbody tr').forEach((row) => {
      const term = row.querySelector('td')?.textContent.trim();
      if (term === 'Table') {
        const cell = row.querySelector('td');
        if (cell && !cell.querySelector('a')) cell.innerHTML = '<a href="table.html">Table</a>';
      }
      if (term === 'Column') {
        row.id = 'column';
        const cell = row.querySelector('td');
        if (cell && !cell.querySelector('a')) cell.innerHTML = '<a href="column.html">Column</a>';
      }
      if (term === 'Row') row.id = 'row';
      if (term === 'Field') row.id = 'field';
    });
  }
  document.querySelectorAll('a[href="module03-glossary.html#glossary-http"]').forEach((link) => { link.href = 'http.html'; });
  const topicList = document.querySelector('.software-overview .topic-list');
  if (topicList && !document.body.classList.contains('frontend-browser-overview') && !document.body.classList.contains('http-apis-overview')) {
    const topics = [['Software','Programs and data that help computers perform useful tasks.'],['Application','Software designed for a specific purpose.'],['Client','The side of a system that interacts with a server.'],['Server','A system that receives requests and provides services.'],['Frontend','The part users see and interact with.'],['Backend','The part that processes data and rules.'],['API','A way for software parts to communicate.'],['Request','A message asking for data or an action.'],['Response','The result returned after processing.'],['Business Logic','Rules that decide how the system handles actions.'],['Database','A system used to store application data.'],['JSON','A common format for structured data.'],['Runtime','The environment where software is running.'],['State','Information describing the current condition of a system.']];
    const overviewTopicLinks = {Database: 'database.html', Request: 'request.html', JSON: 'json.html', State: 'state.html'};
    topicList.innerHTML = topics.map(([name, description]) => `<a href="${overviewTopicLinks[name] || `knowledge-placeholder.html?type=software&amp;title=${encodeURIComponent(name)}`}" ><b>${name}</b><span>${description}</span><em>Open →</em></a>`).join('');
  }
  installGlobalNav();
  const base = new URL('.', document.baseURI);
  const pathname = location.pathname.toLowerCase();
  const requestedType = new URL(location.href).searchParams.get('type');
  if (pathname.endsWith('/response.html')) document.body.dataset.forceKnowledgeType = 'software';
    const softwareTopicSlugs = ['frontend-browser','http-apis','http-apis-glossary','module03-glossary','module04-glossary','module05-glossary','module06-glossary','module-05','module-06','module-05-glossary','module-06-glossary','module-07','module-07-glossary','module-08','module-08-glossary','version','release','build','scaling','horizontal-scaling','vertical-scaling','high-availability','fault-tolerance','cdn','object-storage','file-storage','load-balancer','cache','redis','authentication','authorization','backend-overview','backend-glossary','authentication-security','patch','get','rest-api','post','http','https','url','put','browser','server','event','responsive-design','cookie','form','input','button','id','local-storage','event-listener','dom','developer-tools','web-page','client','frontend','request','method','html','attribute','class','javascript','api','runtime','business-logic','validation','database','dbms','relational-database','postgresql','mysql','table','row','column','field','schema','primary-key','foreign-key','relationship','one-to-many','index','constraint','transaction','null','normalization','migration','sql','json','query-parameter','header','backend','python','framework','fastapi','route','function','parameters','parameter','service','repository-dao','dependency','package','environment-variable','configuration','exception','error-handling','logging','external-api','middleware','background-job','api-key','rbac','secret','encryption','hashing','commit'];
    softwareTopicSlugs.push('css');
    softwareTopicSlugs.push('application');
    softwareTopicSlugs.push('environment');
    softwareTopicSlugs.push('element');
    softwareTopicSlugs.push('state');
    softwareTopicSlugs.push('api-http');
    softwareTopicSlugs.push('jwt');
    softwareTopicSlugs.push('oauth');
    softwareTopicSlugs.push('sso');
    softwareTopicSlugs.push('role');
    softwareTopicSlugs.push('permission');
    softwareTopicSlugs.push('authentication-security');
    softwareTopicSlugs.push('authorization');
    softwareTopicSlugs.push('login');
    softwareTopicSlugs.push('module06-glossary');
    softwareTopicSlugs.push('body');
    softwareTopicSlugs.push('delete');
    softwareTopicSlugs.push('endpoint');
    softwareTopicSlugs.push('route');
    softwareTopicSlugs.push('service');
    softwareTopicSlugs.push('backend-overview');
    softwareTopicSlugs.push('backend-glossary');
    softwareTopicSlugs.push('module04-glossary');
    softwareTopicSlugs.push('external-api');
    softwareTopicSlugs.push('cors');
    softwareTopicSlugs.push('csrf');
    softwareTopicSlugs.push('xss');
    softwareTopicSlugs.push('dependency');
    softwareTopicSlugs.push('password');
    softwareTopicSlugs.push('least-privilege');
    softwareTopicSlugs.push('module-07');
    softwareTopicSlugs.push('module-07-glossary');
    softwareTopicSlugs.push('module-08');
    softwareTopicSlugs.push('module-08-glossary');
    softwareTopicSlugs.push('version');
    softwareTopicSlugs.push('release');
    softwareTopicSlugs.push('build');
    softwareTopicSlugs.push('module-08');
    softwareTopicSlugs.push('module-08-glossary');
    softwareTopicSlugs.push('conflict');
    softwareTopicSlugs.push('version');
    softwareTopicSlugs.push('release');
    softwareTopicSlugs.push('source-code');
    softwareTopicSlugs.push('branch');
    softwareTopicSlugs.push('monolith');
    softwareTopicSlugs.push('microservices');
    softwareTopicSlugs.push('event-driven');
    softwareTopicSlugs.push('synchronous');
    softwareTopicSlugs.push('asynchronous');
    softwareTopicSlugs.push('session');
    softwareTopicSlugs.push('mysql');
    softwareTopicSlugs.push('postgresql');
    softwareTopicSlugs.push('development-git');
    softwareTopicSlugs.push('module-08');
    softwareTopicSlugs.push('module-08-glossary');
    softwareTopicSlugs.push('pull-request');
    softwareTopicSlugs.push('source-code');
    softwareTopicSlugs.push('repository');
    softwareTopicSlugs.push('git');
    softwareTopicSlugs.push('github');
    softwareTopicSlugs.push('commit');
    softwareTopicSlugs.push('branch');
    softwareTopicSlugs.push('main');
    softwareTopicSlugs.push('code-review');
    softwareTopicSlugs.push('merge');
    softwareTopicSlugs.push('conflict');
    softwareTopicSlugs.push('version');
    softwareTopicSlugs.push('release');
    softwareTopicSlugs.push('build');
    softwareTopicSlugs.push('package');
    softwareTopicSlugs.push('table');
    softwareTopicSlugs.push('module-05');
    softwareTopicSlugs.push('module-05-glossary');
    softwareTopicSlugs.push('index');
    softwareTopicSlugs.push('null');
    softwareTopicSlugs.push('module-05');
    softwareTopicSlugs.push('module-05-glossary');
    softwareTopicSlugs.push('dbms');
    softwareTopicSlugs.push('relational-database');
    softwareTopicSlugs.push('main');
    softwareTopicSlugs.push('postgresql');
  const isSoftwareTopic = softwareTopicSlugs.some((slug) => pathname.endsWith(`/${slug}`) || pathname.endsWith(`/${slug}.html`));
  const knowledgeType = requestedType || document.body.dataset.forceKnowledgeType || (pathname.includes('software-knowledge') || pathname.includes('software-') || pathname.endsWith('/software.html') || pathname.endsWith('/application.html') || pathname.includes('/software/') || pathname.endsWith('/backend.html') || isSoftwareTopic ? 'software' : pathname.includes('syntax') || pathname.includes('/language/') ? 'syntax' : 'ai');
  document.body.dataset.knowledgeType = knowledgeType;
  const knowledgeTrigger = document.querySelector('.site-nav-trigger');
  if (knowledgeTrigger) knowledgeTrigger.classList.add('active');
  if (knowledgeType !== 'ai') { renderKnowledgeSidebar(mount, knowledgeType); return; }
  fetch(new URL('sidebar.html', base), { cache: 'no-store' })
    .then((response) => { if (!response.ok) throw new Error('Sidebar unavailable'); return response.text(); })
    .then((html) => {
      mount.innerHTML = html;
      // Compare resolved pathnames rather than the raw href. This also works when
      // a page is served from a directory URL instead of a literal .html URL.
      // Cloudflare serves clean URLs such as `/ai-foundations`, while the
      // directory links use `ai-foundations.html`. Normalize both forms so
      // the matching module is found in local and deployed environments.
      const canonicalPath = (pathname) => {
        let path = decodeURIComponent(pathname).replace(/\/$/, '/index.html').toLowerCase();
        const leaf = path.slice(path.lastIndexOf('/') + 1);
        if (leaf && !leaf.includes('.')) path += '.html';
        return path;
      };
      const current = canonicalPath(new URL(location.href).pathname);
      const currentHash = new URL(location.href).hash;
      let activeDetails;
      mount.querySelectorAll('a[href]').forEach((link) => {
        const url = new URL(link.getAttribute('href'), base);
        const status = link.dataset.status;
        if (status) addStatus(link, status);
      });
      const matchingLinks = [...mount.querySelectorAll('a[href]')].filter((link) => {
        const url = new URL(link.getAttribute('href'), base);
        return canonicalPath(url.pathname) === current;
      });
      const activeLink = matchingLinks.find((link) => new URL(link.getAttribute('href'), base).hash === currentHash)
        || matchingLinks.find((link) => !new URL(link.getAttribute('href'), base).hash)
        || matchingLinks[0];
      if (activeLink) {
        activeLink.classList.add('active');
        activeLink.setAttribute('aria-current', 'page');
        activeDetails = activeLink.closest('details');
      }
      mount.querySelectorAll('details').forEach((detail) => {
        // The module containing the current page is always expanded on arrival.
        // Other modules retain their normal, independently collapsible behaviour.
        detail.open = detail === activeDetails;
        const summary = detail.querySelector(':scope > summary');
        if (summary) summary.classList.toggle('active-module', detail === activeDetails);
        detail.classList.toggle('expanded', detail === activeDetails);
      });
      mount.querySelectorAll('a[href]').forEach((link) => {
        link.addEventListener('click', () => {
          const selected = link.closest('details');
          mount.querySelectorAll('details').forEach((detail) => {
            detail.open = detail === selected;
            const summary = detail.querySelector(':scope > summary');
            if (summary) summary.classList.toggle('active-module', detail === selected);
            detail.classList.toggle('expanded', detail === selected);
          });
        });
      });
      if (activeDetails) activeDetails.scrollIntoView({ block: 'nearest' });
    })
    .catch((error) => {
      // Keep local topic pages navigable while the shared AI directory is being rebuilt.
      mount.innerHTML = document.body.classList.contains('guardrails-page') || location.pathname.toLowerCase().endsWith('/evaluation-safety-glossary.html') || location.pathname.toLowerCase().endsWith('/ai-evaluation.html')
        ? '<nav class="sidebar-nav" aria-label="AI Knowledge site directory"><div class="sidebar-heading"><span>AI Knowledge</span><small>Site directory</small></div><details open><summary>12 · Evaluation &amp; Safety</summary><ul><li><a href="evaluation-safety-reliability.html">Overview</a></li><li><a href="evaluation-safety-glossary.html">Glossary</a></li><li><a href="ai-evaluation.html" class="active" aria-current="page">AI Evaluation <i class="status status-new">NEW</i></a></li><li><a href="guardrails.html">Guardrails</a></li><li><a href="evaluation.html">Evaluation</a></li><li><a href="permissions-safety.html">Permissions &amp; Safety</a></li></ul></details></nav>'
        : document.body.classList.contains('context-engineering-page')
        ? '<nav class="sidebar-nav" aria-label="Prompt &amp; Context topic directory"><div class="sidebar-heading"><span>AI Knowledge</span><small>Module 06 · Site directory</small></div><section class="sidebar-part"><details open><summary>06 · Prompt &amp; Context</summary><ul><li><a href="prompting-system-design.html">Overview</a></li><li><a href="context-engineering.html#glossary">Glossary</a></li><li><a href="system-prompts.html">System Prompts</a></li><li><a href="structured-outputs.html">Structured Outputs</a></li><li><a href="prompt-design.html">Prompt Design</a></li><li><a class="active" aria-current="page" href="context-engineering.html">Context Engineering</a></li></ul></details></section></nav>'
        : /(?:agent-harness|agent-loop|multi-agent-systems|agents-agent-systems|agents-agent-systems-glossary)\.html$/.test(location.pathname.toLowerCase())
        ? '<nav class="sidebar-nav" aria-label="Agents &amp; Agent Systems topic directory"><div class="sidebar-heading"><span>Agents &amp; Agent Systems</span><small>Module 08 · Site directory</small></div><section class="sidebar-part"><details open><summary>08 · Agents &amp; Agent Systems</summary><ul><li><a href="agents-agent-systems-glossary.html">Glossary</a></li><li><a href="agents-agent-systems.html">Overview</a></li><li><a href="agent-harness.html">Agent Harness <i class="status status-new">NEW</i></a></li><li><a href="ai-agent.html">AI Agent</a></li><li><a href="tool-calling.html">Tool Calling</a></li><li><a href="agent-loop.html">Agent Loop</a></li><li><a href="planning.html">Planning</a></li><li><a href="memory-state.html">Memory &amp; State</a></li><li><a href="mcp.html">MCP</a></li><li><a href="skills-plugins.html">Skills / Plugins</a></li><li><a href="human-in-the-loop.html">Human in the Loop</a></li><li><a href="multi-agent-systems.html">Multi-Agent Systems</a></li></ul></details></section></nav>'
        : document.body.classList.contains('graph-engineering-page')
        ? '<nav class="sidebar-nav" aria-label="Graph Engineering topic directory"><div class="sidebar-heading"><span>Agents &amp; Agent Systems</span><small>Topic directory</small></div><section class="sidebar-part"><details open><summary>Module 08 · Agents &amp; Agent Systems</summary><ul><li><a href="agent-systems-glossary.html">Glossary</a></li><li><a href="agents-tools-mcp.html">Overview</a></li><li><a class="active" aria-current="page" href="graph-engineering.html">Graph Engineering <i class="status status-new">NEW</i></a></li><li><a href="ai-agent.html">Agent</a></li><li><a href="agent-loop.html">Agent Loop</a></li><li><a href="workflow-automation.html">Workflow</a></li><li><a href="knowledge-placeholder.html?type=ai&amp;title=State%20Machine">State Machine</a></li><li><a href="knowledge-placeholder.html?type=ai&amp;title=Orchestration">Orchestration</a></li></ul></details></section></nav>'
        : '<nav class="sidebar-nav" aria-label="AI Knowledge site directory"><div class="sidebar-heading"><span>AI Knowledge</span><small>Site directory</small></div><details open><summary>11 · Model Adaptation</summary><ul><li><a href="knowledge-placeholder.html?type=ai&amp;title=Glossary">Glossary</a></li><li><a href="training-model-adaptation.html">Overview</a></li><li><a href="fine-tuning.html">Fine-tuning</a></li><li><a href="distillation.html">Distillation <i class="status status-new">NEW</i></a></li><li><a href="quantization.html">Quantization</a></li></ul></details></nav>';
      const currentLink = [...mount.querySelectorAll('a[href]')].find((link) => new URL(link.href).pathname === location.pathname);
      if (currentLink) currentLink.classList.add('active');
      console.error(error);
    });

  function addStatus(item, status) {
    const label = document.createElement('i');
    label.className = `status status-${status.toLowerCase()}`;
    label.textContent = status;
    item.append(' ', label);
  }

  const topicVideos = {
    '/unsupervised-learning.html': ['Unsupervised Learning', 'unlabeled data · structure · inspection'],
    '/reinforcement-learning.html': ['Reinforcement Learning', 'agent · action · reward'],
  };
  const videoConfig = topicVideos[location.pathname.toLowerCase()];
  if (videoConfig) {
    const videoCard = document.querySelector('#video.video-card');
    if (videoCard) {
      videoCard.innerHTML = `<div class="video-label"><div><div class="eyebrow">Independent video · Azure Neural voice</div><h2>Video</h2></div><small>visual explainer · captions included</small></div><video controls preload="metadata" poster="vedio/${location.pathname.split('/').pop().replace('.html', '')}.png" aria-label="${videoConfig[0]} explainer video"><source src="vedio/${location.pathname.split('/').pop().replace('.html', '')}.mp4" type="video/mp4"><track kind="captions" src="vedio/${location.pathname.split('/').pop().replace('.html', '')}.vtt" srclang="en" label="English captions" default></video><div class="video-meta"><span>${videoConfig[1]}</span><span>MP4 · H.264 + AAC</span></div>`;
    }
  }

  function renderKnowledgeSidebar(target, type) {
    const requestedModule = new URL(location.href).searchParams.get('module');
    const software = {
      '01 · How Software Works':['Glossary','Overview','Software','Application','Client','Server','Frontend','Backend','API','Request','Response','Business Logic','Database','JSON','Runtime','State'],
      '02 · Frontend & Browser':['Glossary','Overview','Frontend','Browser','Web Page','HTML','CSS','JavaScript','DOM','Element','Attribute','Class','ID','Form','Input','Button','Event','Event Listener','Responsive Design','Local Storage','Cookie','Developer Tools'],
      '03 · HTTP & APIs':['Glossary','Overview','HTTP','HTTPS','URL','API','REST API','Endpoint','Method','GET','POST','PUT','PATCH','DELETE','Request','Response','Header','Body','Query Parameter','Path Parameter','Status Code','JSON','API Documentation','Swagger / OpenAPI','Webhook','Timeout','Retry','Rate Limit','Idempotency'],
      '04 · Backend':['Glossary','Overview','Backend','Server','Python','Framework','FastAPI','Route','Function','Parameter','Validation','Business Logic','Service','Repository / DAO','Environment Variable','Configuration','Exception','Error Handling','Logging','External API','Middleware','Background Job'],
      '05 · Database & SQL':['Glossary','Overview','Database','DBMS','Relational Database','PostgreSQL','MySQL','Table','Row','Column','Field','Schema','Primary Key','Foreign Key','Relationship','One-to-Many','Index','Constraint','Transaction','NULL','Normalization','Migration','SQL'],
      '06 · Authentication & Security':['Glossary','Overview','Authentication','Authorization','Login','Password','Session','Cookie','Token','JWT','OAuth','SSO','Role','Permission','RBAC','API Key','Secret','Encryption','Hashing','CORS','CSRF','XSS','Least Privilege'],
      '07 · System Architecture':['Glossary','Overview','Architecture','Component','Service','Monolith','Microservices','API Gateway','Load Balancer','Cache','Redis','Message Queue','Event','Synchronous','Event-driven','Asynchronous','CDN','Object Storage','File Storage','Scaling','Horizontal Scaling','Vertical Scaling','Fault Tolerance','High Availability'],
      '08 · Development & Git':['Glossary','Overview','Source Code','Repository','Git','GitHub','Commit','Branch','Main','Pull Request','Code Review','Merge','Conflict','Version','Release','Build','Dependency','Package','Environment'],
      '09 · Cloud & Deployment':['Glossary','Overview','Cloud','Server','Hosting','Deployment','Domain','DNS','IP Address','CDN','Docker','Container','Image','CI','CD','CI/CD','Development','Test','UAT','Staging','Production','Serverless','Environment Variable','Artifact'],
      '10 · Testing & Observability':['Glossary','Overview','Testing','Test Case','Unit Test','Integration Test','E2E Test','Regression Test','QA','Bug','Error','Exception','Log','Log Level','Metric','Monitoring','Alert','Tracing','Observability','Root Cause','Incident']
    };
    const syntax = {Python:['Glossary','Overview','01 · Python Basics','02 · Data Types','03 · Collections','04 · Operators','05 · Conditions','06 · Loops','07 · Functions','08 · Strings','09 · Modules & Packages','10 · Files','11 · Exceptions','12 · Classes & Objects','13 · Comprehensions','14 · Iterators & Generators','15 · JSON & CSV','16 · API Requests','17 · Virtual Environments','18 · Useful Libraries'],SQL:['Glossary','Overview','01 · Query Basics','02 · Filtering','03 · Sorting & Aggregation','04 · Joining Tables','05 · Logic','06 · Data Modification','07 · Database Definition'],Web:['Glossary','Overview','HTML','CSS','JavaScript']};
    const current = new URL(location.href).searchParams.get('title') || (location.pathname.toLowerCase().endsWith('/software-glossary.html') || location.pathname.toLowerCase().endsWith('/module03-glossary.html') || location.pathname.toLowerCase().endsWith('/module04-glossary.html') || location.pathname.toLowerCase().endsWith('/module05-glossary.html') || location.pathname.toLowerCase().endsWith('/module-05-glossary.html') || location.pathname.toLowerCase().endsWith('/module06-glossary.html') || location.pathname.toLowerCase().endsWith('/module-06-glossary.html') || location.pathname.toLowerCase().endsWith('/module-07-glossary.html') || location.pathname.toLowerCase().endsWith('/module-08-glossary.html') ? 'Glossary' : location.pathname.toLowerCase().endsWith('/frontend-browser.html') || location.pathname.toLowerCase().endsWith('/http-apis.html') || location.pathname.toLowerCase().endsWith('/backend-overview.html') || location.pathname.toLowerCase().endsWith('/database-sql.html') || location.pathname.toLowerCase().endsWith('/module-05.html') || location.pathname.toLowerCase().endsWith('/authentication-security.html') || location.pathname.toLowerCase().endsWith('/module-06.html') || location.pathname.toLowerCase().endsWith('/module-07.html') || location.pathname.toLowerCase().endsWith('/module-08.html') ? 'Overview' : document.title.split(' · ')[0]);
    const completedSoftwareTopics = {
      'Event': 'event.html',
      'Responsive Design': 'responsive-design.html',
      'Cookie': 'cookie.html',
      'Form': 'form.html',
      'Input': 'input.html',
      'Button': 'button.html',
      'Element': 'element.html',
      'ID': 'id.html',
      'CSS': 'css.html',
      'Browser': 'browser.html',
      'Web Page': 'web-page.html',
      'Local Storage': 'local-storage.html',
      'Event Listener': 'event-listener.html',
      'DOM': 'dom.html',
      'Class': 'class.html',
      'Attribute': 'attribute.html',
      'Developer Tools': 'developer-tools.html',
      'JavaScript': 'javascript.html',
      'HTML': 'html.html',
      'Client': 'client.html',
      'Frontend': 'frontend.html',
      'Server': 'server.html',
      'Python': 'python.html',
      'Runtime': 'runtime.html',
      'State': 'state.html',
      'HTTP': 'http.html',
      'HTTPS': 'https.html',
      'URL': 'url.html',
      'API': 'api-http.html',
      'REST API': 'rest-api.html',
      'Endpoint': 'endpoint.html',
      'GET': 'get.html',
      'PUT': 'put.html',
      'POST': 'post.html',
      'PATCH': 'patch.html',
      'DELETE': 'delete.html',
      'Header': 'header.html',
      'Body': 'body.html',
      'Status Code': 'http-apis-glossary.html#communication',
      'Request': 'request.html',
      'Method': 'method.html',
      'API Documentation': 'http-apis-glossary.html',
      'Swagger / OpenAPI': 'http-apis-glossary.html',
      'Webhook': 'http-apis-glossary.html',
      'Timeout': 'http-apis-glossary.html',
      'Retry': 'http-apis-glossary.html',
      'Rate Limit': 'http-apis-glossary.html',
      'Idempotency': 'http-apis-glossary.html',
      'Database': 'database.html',
      'Business Logic': 'business-logic.html',
      'Function': 'function.html',
      'Validation': 'validation.html',
      'Parameter': 'parameter.html',
      'JSON': 'json.html',
      'Response': 'response.html',
      'Body': 'body.html',
      'Path Parameter': 'path-parameter.html',
      'Query Parameter': 'query-parameter.html',
      'External API': 'external-api.html'
      ,'Main': 'main.html'
      ,'Route': 'route.html'
      ,'Exception': 'exception.html'
      ,'Pull Request': 'pull-request.html'
      ,'Merge': 'merge.html'
    };
    const httpTopicPages = {
      HTTP: 'http.html', HTTPS: 'https.html', URL: 'url.html', API: 'api-http.html',
      'REST API': 'rest-api.html', Endpoint: 'endpoint.html', Method: 'method.html',
      GET: 'get.html', POST: 'post.html', PUT: 'put.html', PATCH: 'patch.html', DELETE: 'delete.html',
      Request: 'request.html', Response: 'response.html', Header: 'header.html', Body: 'body.html',
      'Query Parameter': 'query-parameter.html', 'Path Parameter': 'path-parameter.html'
    };
    const module04TopicPages = {
      Backend: 'backend.html', Server: 'server.html', Python: 'python.html', Framework: 'framework.html', FastAPI: 'fastapi.html',
      Route: 'route.html', Function: 'function.html', Parameter: 'parameter.html', Validation: 'validation.html',
      'Business Logic': 'business-logic.html', Service: 'service.html', 'Repository / DAO': 'repository-dao.html',
      'Environment Variable': 'environment-variable.html',
      Configuration: 'configuration.html', Exception: 'exception.html', 'Error Handling': 'error-handling.html',
      Logging: 'logging.html', 'External API': 'external-api.html', Middleware: 'middleware.html', 'Background Job': 'background-job.html'
    };
    const module08TopicPages = {
      'Source Code': 'source-code.html', Repository: 'repository.html', Git: 'git.html', GitHub: 'github.html', Commit: 'commit.html', Branch: 'branch.html', Main: 'main.html',
      'Pull Request': 'pull-request.html', 'Code Review': 'code-review.html', Merge: 'merge.html', Conflict: 'conflict.html', Version: 'version.html', Release: 'release.html', Build: 'build.html',
      Dependency: 'dependency.html', Package: 'package.html', Environment: 'environment.html'
    };
    const module06TopicPages = {
      Authentication: 'authentication.html',
      Login: 'login.html',
      Authorization: 'authorization.html',
      Password: 'password.html',
      Session: 'session.html',
      Cookie: 'cookie.html',
      Token: 'token.html',
      JWT: 'jwt.html',
      OAuth: 'oauth.html',
      SSO: 'sso.html',
      Role: 'role.html',
      Permission: 'permission.html',
      'API Key': 'api-key.html',
      RBAC: 'rbac.html',
      Secret: 'secret.html',
      Encryption: 'encryption.html',
      Hashing: 'hashing.html',
      CORS: 'cors.html',
      CSRF: 'csrf.html',
      XSS: 'xss.html',
      'Least Privilege': 'least-privilege.html'
    };
    const module05TopicPages = {
      Database: 'database.html',
      DBMS: 'dbms.html',
      'Relational Database': 'relational-database.html',
      PostgreSQL: 'postgresql.html',
      MySQL: 'mysql.html',
      Table: 'table.html',
      Row: 'row.html',
      Column: 'column.html',
      Field: 'field.html',
      Schema: 'schema.html',
      'Primary Key': 'primary-key.html',
      'Foreign Key': 'foreign-key.html',
      Relationship: 'relationship.html',
      'One-to-Many': 'one-to-many.html',
      Index: 'index.html',
      Constraint: 'constraint.html',
      Transaction: 'transaction.html',
      NULL: 'null.html',
      Normalization: 'normalization.html',
      Migration: 'migration.html',
      SQL: 'sql.html'
    };
    const module07TopicPages = {
      Architecture: 'architecture.html',
      Component: 'component.html',
      Service: 'service.html',
      Monolith: 'monolith.html',
      Microservices: 'microservices.html',
      'API Gateway': 'api-gateway.html',
      'Load Balancer': 'load-balancer.html',
      Cache: 'cache.html',
      Redis: 'redis.html',
      'Message Queue': 'message-queue.html',
      Event: 'event.html',
      'Event-driven': 'event-driven.html',
      Synchronous: 'synchronous.html',
      Asynchronous: 'asynchronous.html',
      CDN: 'cdn.html',
      'Object Storage': 'object-storage.html',
      'File Storage': 'file-storage.html',
      Scaling: 'scaling.html',
      'Horizontal Scaling': 'horizontal-scaling.html',
      'Vertical Scaling': 'vertical-scaling.html',
      'Fault Tolerance': 'fault-tolerance.html',
      'High Availability': 'high-availability.html'
    };
    const item = (label, moduleName) => {
      const moduleId = (moduleName.match(/^\d+/) || [])[0];
      const withModuleContext = (value) => {
        if (type !== 'software' || !moduleId) return value;
        const [pathAndQuery, hash] = value.split('#');
        const separator = pathAndQuery.includes('?') ? '&' : '?';
        return `${pathAndQuery}${separator}module=${moduleId}${hash ? `#${hash}` : ''}`;
      };
      const apiHttpPage = pathname.endsWith('/api-http.html');
      const href = type === 'software' && label === 'Glossary' && moduleName === '03 · HTTP & APIs' ? 'http-apis-glossary.html' : type === 'software' && label === 'Glossary' && moduleName === '04 · Backend' ? 'module04-glossary.html' : type === 'software' && label === 'Glossary' && moduleName === '05 · Database & SQL' ? 'module-05-glossary.html' : type === 'software' && label === 'Glossary' && moduleName === '06 · Authentication & Security' ? 'module-06-glossary.html' : type === 'software' && label === 'Glossary' && moduleName === '07 · System Architecture' ? 'module-07-glossary.html' : type === 'software' && label === 'Glossary' && moduleName === '08 · Development & Git' ? 'module-08-glossary.html' : type === 'software' && label === 'Glossary' ? 'software-glossary.html' : type === 'software' && label === 'Overview' && moduleName === '03 · HTTP & APIs' ? 'http-apis.html' : type === 'software' && label === 'Overview' && moduleName === '04 · Backend' ? 'backend-overview.html' : type === 'software' && label === 'Overview' && moduleName === '05 · Database & SQL' ? 'module-05.html' : type === 'software' && label === 'Overview' && moduleName === '06 · Authentication & Security' ? 'module-06.html' : type === 'software' && label === 'Overview' && moduleName === '07 · System Architecture' ? 'module-07.html' : type === 'software' && label === 'Overview' && moduleName === '08 · Development & Git' ? 'module-08.html' : type === 'software' && moduleName === '04 · Backend' && module04TopicPages[label] ? module04TopicPages[label] : type === 'software' && moduleName === '05 · Database & SQL' && module05TopicPages[label] ? module05TopicPages[label] : type === 'software' && moduleName === '06 · Authentication & Security' && module06TopicPages[label] ? module06TopicPages[label] : type === 'software' && moduleName === '07 · System Architecture' && module07TopicPages[label] ? module07TopicPages[label] : type === 'software' && moduleName === '08 · Development & Git' && module08TopicPages[label] ? module08TopicPages[label] : type === 'software' && label === 'Software' ? 'software.html' : type === 'software' && label === 'Application' ? 'application.html' : type === 'software' && moduleName === '01 · How Software Works' && label === 'Backend' ? 'backend.html' : type === 'software' && completedSoftwareTopics[label] ? completedSoftwareTopics[label] : type === 'software' && moduleName === '03 · HTTP & APIs' && httpTopicPages[label] ? httpTopicPages[label] : `knowledge-placeholder.html?type=${type}&title=${encodeURIComponent(label)}`;
      const module08Href = type === 'software' && moduleName === '08 · Development & Git' && label === 'Glossary' ? 'module-08-glossary.html' : type === 'software' && moduleName === '08 · Development & Git' && label === 'Overview' ? 'module-08.html' : type === 'software' && moduleName === '08 · Development & Git' && module08TopicPages[label] ? module08TopicPages[label] : null;
      const errorHandlingPage = pathname.endsWith('/error-handling.html');
      const backendPage = pathname.endsWith('/backend.html');
      const businessLogicPage = pathname.endsWith('/business-logic.html');
      const pythonPage = pathname.endsWith('/python.html');
      const backendOverviewPage = pathname.endsWith('/backend-overview.html');
      const backendGlossaryPage = pathname.endsWith('/module04-glossary.html');
      const module06OverviewPage = pathname.endsWith('/module-06.html');
      const module06GlossaryPage = pathname.endsWith('/module-06-glossary.html') || pathname.endsWith('/module06-glossary.html');
      const module07OverviewPage = pathname.endsWith('/module-07.html');
      const module07GlossaryPage = pathname.endsWith('/module-07-glossary.html');
      const module05OverviewPage = pathname.endsWith('/database-sql.html') || pathname.endsWith('/module-05.html');
      const module05GlossaryPage = pathname.endsWith('/module05-glossary.html') || pathname.endsWith('/module-05-glossary.html');
      const nullPage = pathname.endsWith('/null.html');
      const primaryKeyPage = pathname.endsWith('/primary-key.html');
      const schemaPage = pathname.endsWith('/schema.html');
      const constraintPage = pathname.endsWith('/constraint.html');
      const postgresqlPage = pathname.endsWith('/postgresql.html');
      const externalApiPage = pathname.endsWith('/external-api.html');
      const frameworkPage = pathname.endsWith('/framework.html');
      const routePage = pathname.endsWith('/route.html');
      const servicePage = pathname.endsWith('/service.html');
      const componentPage = pathname.endsWith('/component.html');
      const databasePage = pathname.endsWith('/database.html');
      const serverPage = pathname.endsWith('/server.html');
      const packagePage = pathname.endsWith('/package.html');
      const frontendPage = pathname.endsWith('/frontend.html');
      const httpPage = pathname.endsWith('/http.html');
      const httpOverviewPage = pathname.endsWith('/http-apis.html');
      const httpGlossaryPage = pathname.endsWith('/module03-glossary.html');
      const responsePage = pathname.endsWith('/response.html');
      const requestPage = pathname.endsWith('/request.html');
      const exceptionPage = pathname.endsWith('/exception.html');
      const environmentVariablePage = pathname.endsWith('/environment-variable.html');
      const resolvedHref = module08Href || (apiHttpPage && moduleName === '03 · HTTP & APIs' && label === 'API' ? 'api-http.html' : href);
      const contextualHref = withModuleContext(resolvedHref);
      const module04Active = moduleName === '04 · Backend' && href.split('#')[0] === pathname.split('/').pop();
      const module08Active = moduleName === '08 · Development & Git' && resolvedHref.split('#')[0] === pathname.split('/').pop();
      const active = module04Active ? true : databasePage ? (label === 'Database' && moduleName === '01 · How Software Works') : pathname.endsWith('/normalization.html') ? (label === 'Normalization' && moduleName === '05 · Database & SQL') : nullPage ? (label === 'NULL' && moduleName === '05 · Database & SQL') : constraintPage ? (label === 'Constraint' && moduleName === '05 · Database & SQL') : businessLogicPage ? (label === 'Business Logic' && moduleName === '04 · Backend') : serverPage ? (label === 'Server' && moduleName === '04 · Backend') : packagePage ? (label === 'Package' && moduleName === '04 · Backend') : pythonPage ? (label === 'Python' && moduleName === '04 · Backend') : externalApiPage ? (label === 'External API' && moduleName === '04 · Backend') : backendPage ? (label === 'Backend' && moduleName === '04 · Backend') : backendOverviewPage ? (label === 'Overview' && moduleName === '04 · Backend') : backendGlossaryPage ? (label === 'Glossary' && moduleName === '04 · Backend') : module06OverviewPage ? (label === 'Overview' && moduleName === '06 · Authentication & Security') : module06GlossaryPage ? (label === 'Glossary' && moduleName === '06 · Authentication & Security') : module07OverviewPage ? (label === 'Overview' && moduleName === '07 · System Architecture') : module07GlossaryPage ? (label === 'Glossary' && moduleName === '07 · System Architecture') : routePage ? (label === 'Route' && moduleName === '04 · Backend') : servicePage ? (label === 'Service' && moduleName === '04 · Backend') : exceptionPage ? (label === 'Exception' && moduleName === '04 · Backend') : frontendPage ? (label === 'Frontend' && moduleName === '02 · Frontend & Browser') : httpPage ? (label === 'HTTP' && moduleName === '03 · HTTP & APIs') : httpOverviewPage ? (label === 'Overview' && moduleName === '03 · HTTP & APIs') : httpGlossaryPage ? (label === 'Glossary' && moduleName === '03 · HTTP & APIs') : pathname.endsWith('/cookie.html') ? (label === 'Cookie' && moduleName === '06 · Authentication & Security') : current === label && (!['Request','Response'].includes(label) || moduleName === ((responsePage || requestPage) ? '03 · HTTP & APIs' : '01 · How Software Works'));
      const resolvedActive = errorHandlingPage ? (label === 'Error Handling' && moduleName === '04 · Backend') : frameworkPage ? (label === 'Framework' && moduleName === '04 · Backend') : environmentVariablePage ? (label === 'Environment Variable' && moduleName === '04 · Backend') : module05OverviewPage ? (label === 'Overview' && moduleName === '05 · Database & SQL') : module05GlossaryPage ? (label === 'Glossary' && moduleName === '05 · Database & SQL') : schemaPage ? (label === 'Schema' && moduleName === '05 · Database & SQL') : primaryKeyPage ? (label === 'Primary Key' && moduleName === '05 · Database & SQL') : postgresqlPage ? (label === 'PostgreSQL' && moduleName === '05 · Database & SQL') : apiHttpPage ? (label === 'API' && moduleName === '03 · HTTP & APIs') : componentPage ? (label === 'Component' && moduleName === '07 · System Architecture') : active;
      const currentPath = pathname.replace(/\/$/, '').replace(/\.html$/, '');
      const linkPath = new URL(resolvedHref, base).pathname.replace(/\/$/, '').replace(/\.html$/, '');
      const contextActive = requestedModule ? moduleId === requestedModule && currentPath === linkPath : resolvedActive || module08Active;
      const unavailableModule08Topic = moduleName === '08 · Development & Git' && resolvedHref.startsWith('knowledge-placeholder.html');
      return `<li>${unavailableModule08Topic ? `<span>${label}</span>` : `<a href="${contextualHref}" class="${contextActive ? 'active' : ''}">${label}</a>`}</li>`;
    };
    const group = (name, items) => `<details><summary>${name}</summary><ul>${items.map((label) => {
      if (type === 'software' && name === '01 · How Software Works' && label === 'Overview') {
        return `<li><a href="software-how-software-works.html" class="${location.pathname.toLowerCase().endsWith('/software-how-software-works.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '02 · Frontend & Browser' && label === 'Overview') {
        return `<li><a href="frontend-browser.html" class="${location.pathname.toLowerCase().endsWith('/frontend-browser.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '03 · HTTP & APIs' && label === 'Overview') {
        return `<li><a href="http-apis.html" class="${location.pathname.toLowerCase().endsWith('/http-apis.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '04 · Backend' && label === 'Overview') {
        return `<li><a href="backend-overview.html" class="${location.pathname.toLowerCase().endsWith('/backend-overview.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '04 · Backend' && label === 'Glossary') {
        return `<li><a href="module04-glossary.html" class="${location.pathname.toLowerCase().endsWith('/module04-glossary.html') ? 'active' : ''}">Glossary</a></li>`;
      }
      if (type === 'software' && name === '05 · Database & SQL' && label === 'Overview') {
        return `<li><a href="module-05.html" class="${location.pathname.toLowerCase().endsWith('/module-05.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '05 · Database & SQL' && label === 'Glossary') {
        return `<li><a href="module-05-glossary.html" class="${location.pathname.toLowerCase().endsWith('/module-05-glossary.html') ? 'active' : ''}">Glossary</a></li>`;
      }
      if (type === 'software' && name === '06 · Authentication & Security' && label === 'Overview') {
        return `<li><a href="module-06.html" class="${location.pathname.toLowerCase().endsWith('/module-06.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '06 · Authentication & Security' && label === 'Glossary') {
        return `<li><a href="module-06-glossary.html" class="${location.pathname.toLowerCase().endsWith('/module-06-glossary.html') ? 'active' : ''}">Glossary</a></li>`;
      }
      if (type === 'software' && name === '08 · Development & Git' && label === 'Overview') {
        return `<li><a href="module-08.html" class="${location.pathname.toLowerCase().endsWith('/module-08.html') ? 'active' : ''}">Overview</a></li>`;
      }
      if (type === 'software' && name === '08 · Development & Git' && label === 'Glossary') {
        return `<li><a href="module-08-glossary.html" class="${location.pathname.toLowerCase().endsWith('/module-08-glossary.html') ? 'active' : ''}">Glossary</a></li>`;
      }
      if (type === 'software' && name === '04 · Backend' && label === 'Dependency') {
        return `<li><a href="dependency.html" class="${location.pathname.toLowerCase().endsWith('/dependency.html') ? 'active' : ''}">Dependency</a></li>`;
      }
      if (type === 'software' && name === '04 · Backend' && label === 'Repository / DAO') {
        return `<li><a href="repository-dao.html" class="${pathname.endsWith('/repository-dao.html') ? 'active' : ''}">Repository / DAO</a></li>`;
      }
      if (type === 'software' && name === '04 · Backend' && label === 'Package') {
        return `<li><a href="package.html" class="${location.pathname.toLowerCase().endsWith('/package.html') ? 'active' : ''}">Package</a></li>`;
      }
      return item(label, name);
    }).join('')}</ul></details>`;
    const mapLink = `<a class="sidebar-map ${current === 'Software Knowledge Map' || current === 'Home' ? 'active' : ''}" href="software-knowledge.html">Home</a>`;
    if (type === 'software') target.innerHTML = `<nav class="sidebar-nav" aria-label="Software Knowledge site directory"><div class="sidebar-heading"><span>Software Knowledge</span><small>Site directory</small></div>${mapLink}${Object.entries(software).map(([name,items])=>group(name,items)).join('')}</nav>`;
    else target.innerHTML = `<nav class="sidebar-nav" aria-label="Language and Syntax site directory"><div class="sidebar-heading"><span>Language &amp; Syntax</span><small>Site directory</small></div><a class="sidebar-map ${current === 'Language & Syntax Overview' ? 'active' : ''}" href="syntax-overview.html">Overview</a>${Object.entries(syntax).map(([name,items])=>group(name,items)).join('')}</nav>`;
    if (type === 'software' && pathname.endsWith('/package.html')) {
      target.querySelectorAll('a[href*="knowledge-placeholder"]').forEach((link) => {
        const label = document.createElement('span');
        label.textContent = link.textContent;
        link.replaceWith(label);
      });
    }
    if (type === 'software' && pathname.endsWith('/database.html')) {
      target.querySelectorAll('a.active').forEach((link) => link.classList.remove('active'));
      const databaseLink = [...target.querySelectorAll('a[href="database.html"]')].find((link) => link.closest('details')?.querySelector('summary')?.textContent.includes('05 · Database'));
      if (databaseLink) { databaseLink.classList.add('active'); databaseLink.setAttribute('aria-current', 'page'); }
    }
    if (type === 'software' && document.body.classList.contains('software-glossary')) {
      const databaseCell = [...document.querySelectorAll('#data-database td')].find((cell) => cell.textContent.trim() === 'Database');
      if (databaseCell && !databaseCell.querySelector('a')) databaseCell.innerHTML = '<a href="database.html">Database</a>';
    }
    if (type === 'software' && document.body.classList.contains('module-eight-glossary')) {
      const environmentCell = [...document.querySelectorAll('#glossary td')].find((cell) => cell.textContent.trim() === 'Environment');
      if (environmentCell && !environmentCell.querySelector('a')) environmentCell.innerHTML = '<a href="environment.html">Environment</a>';
    }
    const module04Chain = [
      ['backend.html', 'http-apis-glossary.html#idempotency', 'server.html'], ['server.html', 'backend.html', 'python.html'], ['python.html', 'server.html', 'framework.html'], ['framework.html', 'python.html', 'fastapi.html'], ['fastapi.html', 'framework.html', 'route.html'], ['route.html', 'fastapi.html', 'function.html'], ['function.html', 'route.html', 'parameter.html'], ['parameter.html', 'function.html', 'validation.html'], ['validation.html', 'parameter.html', 'business-logic.html'], ['business-logic.html', 'validation.html', 'service.html'], ['service.html', 'business-logic.html', 'repository-dao.html'], ['repository-dao.html', 'service.html', 'dependency.html'], ['dependency.html', 'build.html', 'package.html'], ['package.html', 'dependency.html', 'environment-variable.html'], ['environment-variable.html', 'package.html', 'configuration.html'], ['configuration.html', 'environment-variable.html', 'exception.html'], ['exception.html', 'configuration.html', 'error-handling.html'], ['error-handling.html', 'exception.html', 'logging.html'], ['logging.html', 'error-handling.html', 'external-api.html'], ['external-api.html', 'logging.html', 'middleware.html'], ['middleware.html', 'external-api.html', 'background-job.html'], ['background-job.html', 'middleware.html', 'software-glossary.html#data-database']
    ];
    const module04Entry = pathname.endsWith('/package.html') ? null : module04Chain.find((entry) => pathname.endsWith(`/${entry[0]}`));
    const pagination = document.querySelector('.prevnext, .pager, .topic-pagination');
    if (module04Entry && pagination) {
      const paginationLinks = pagination.querySelectorAll('a');
      if (paginationLinks[0]) paginationLinks[0].href = module04Entry[1];
      if (paginationLinks[1]) paginationLinks[1].href = module04Entry[2];
    }
    const module05Chain = [
      ['schema.html', 'field.html', 'primary-key.html'],
      ['foreign-key.html', 'primary-key.html', 'relationship.html'],
      ['sql.html', 'migration.html', 'authentication.html']
    ];
    const module05Entry = module05Chain.find((entry) => pathname.endsWith(`/${entry[0]}`));
    if (module05Entry && pagination) {
      const paginationLinks = pagination.querySelectorAll('a');
      if (paginationLinks[0]) paginationLinks[0].href = module05Entry[1];
      if (paginationLinks[1]) paginationLinks[1].href = module05Entry[2];
    }
    if (document.body.classList.contains('module-five-page')) {
      const topicList = document.querySelector('.module-five-page .topic-list');
      if (topicList && !topicList.querySelector('a[href="mysql.html"]')) {
        topicList.insertAdjacentHTML('beforeend', '<a href="mysql.html"><b>MySQL</b><span>A widely used relational database system.</span><em>Open topic →</em></a><a href="postgresql.html"><b>PostgreSQL</b><span>A powerful relational database system.</span><em>Open topic →</em></a><a href="table.html"><b>Table</b><span>Organize records in rows and columns.</span><em>Open topic →</em></a>');
      }
      if (topicList && !topicList.querySelector('a[href="migration.html"]')) {
        topicList.insertAdjacentHTML('beforeend', '<a href="migration.html"><b>Migration</b><span>Change database structure in a controlled way.</span><em>Open topic →</em></a>');
      }
    }
    if (document.body.classList.contains('module-five-glossary')) {
      const glossaryBody = document.querySelector('.module-five-glossary table tbody');
      if (glossaryBody && !glossaryBody.querySelector('a[href="mysql.html"]')) {
        glossaryBody.insertAdjacentHTML('beforeend', '<tr><td><a href="mysql.html">MySQL</a></td><td>MySQL 数据库</td><td>A widely used relational database management system that uses SQL.</td><td>一种广泛使用、通过 SQL 管理关系型数据的数据库系统。</td></tr>');
      }
    }
    const active = target.querySelector('a.active'); const activeGroup = active?.closest('details'); target.querySelectorAll('details').forEach(d => { d.open = d === activeGroup; });
    target.querySelectorAll('summary').forEach(s => s.addEventListener('click', () => { target.querySelectorAll('details').forEach(d => { if (d !== s.parentElement) d.open = false; }); }));
  }
})();
