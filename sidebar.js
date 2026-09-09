(function () {
  const mount = document.getElementById('site-directory');
  if (!mount) return;
  const headerNav = document.querySelector('body > nav');
  const headerWrap = headerNav && headerNav.querySelector(':scope > .wrap');
  if (headerWrap && !headerWrap.querySelector('.site-global-links')) {
    headerNav.classList.add('site-header-nav');
    const globalLinks = document.createElement('div');
    globalLinks.className = 'site-global-links';
    globalLinks.setAttribute('aria-label', 'Portfolio navigation');
    globalLinks.innerHTML = [
      '<a href="index.html#about">About</a>',
      '<a href="index.html#deployments">Projects</a>',
      '<a href="index.html#capabilities">FDE Skills</a>',
      '<a href="ai-knowledge.html">AI Knowledge</a>',
      '<a href="index.html#certifications">Certifications</a>',
      '<a href="index.html#experience">Experience</a>',
      '<a href="index.html#contact">Contact</a>'
    ].join('');
    headerWrap.append(globalLinks);
  }
  const base = new URL('.', document.baseURI);
  fetch(new URL('sidebar.html', base))
    .then((response) => { if (!response.ok) throw new Error('Sidebar unavailable'); return response.text(); })
    .then((html) => {
      mount.innerHTML = html;
      const module15Overview = mount.querySelector('a[href="general-agents-computer-use.html"]');
      if (module15Overview) module15Overview.href = 'agent-development.html';
      const modelModule = [...mount.querySelectorAll('details')].find((detail) => detail.querySelector('summary')?.textContent.includes('13 · AI Model Landscape'));
      if (modelModule) {
        modelModule.querySelector('summary').innerHTML = '13 · AI Providers &amp; Models';
        const list = modelModule.querySelector('ul');
        const item = document.createElement('li');
        item.innerHTML = '<a href="model-types-families.html">Model Types &amp; Families</a>';
        list.insertBefore(item, list.children[1]);
      }
      const benchmarkItem = [...mount.querySelectorAll('li > span')].find((item) => item.textContent.trim().startsWith('Benchmarks'));
      if (benchmarkItem) {
        const benchmarkLink = document.createElement('a');
        benchmarkLink.href = 'benchmarks.html';
        benchmarkLink.textContent = 'Benchmarks';
        benchmarkItem.replaceWith(benchmarkLink);
      }
      const codingModule = [...mount.querySelectorAll('details')].find((detail) => detail.querySelector('summary')?.textContent.includes('14 · Coding Agents'));
      if (codingModule && !codingModule.querySelector('a[href="ai-assistants-coding-tools.html"]')) {
        const item = document.createElement('li');
        item.innerHTML = '<a href="ai-assistants-coding-tools.html">AI Assistants &amp; Coding Tools</a>';
        codingModule.querySelector('ul').insertBefore(item, codingModule.querySelector('ul').children[1]);
      }
      const agentModule = [...mount.querySelectorAll('details')].find((detail) => detail.querySelector('summary')?.textContent.includes('15 · Agent Development'));
      if (agentModule && !agentModule.querySelector('a[href="how-agents-are-built.html"]')) {
        const item = document.createElement('li');
        item.innerHTML = '<a href="how-agents-are-built.html">How Agents Are Built</a>';
        agentModule.querySelector('ul')?.insertBefore(item, agentModule.querySelector('ul').children[1] || null);
      }
      // Promote completed concepts from placeholders without duplicating sidebar markup.
      mount.querySelectorAll('span').forEach((item) => {
        if (item.textContent.trim() === 'API NEW') {
          const link = document.createElement('a');
          link.href = 'api.html';
          link.textContent = 'API';
          item.replaceWith(link);
        }
      });
      // Promote completed concepts from placeholder text to real pages.
      mount.querySelectorAll('li > span').forEach((item) => {
        if (item.textContent.trim() === 'Hallucination') {
          const link = document.createElement('a');
          link.href = 'hallucination.html';
          link.textContent = 'Hallucination';
          item.replaceWith(link);
        }
      });
      // Promote newly completed Part I topics whose HTML pages now exist.
      const completedTopics = {
        'Preference Learning / RLHF': 'preference-learning-rlhf.html',
        'Multi-Agent Systems': 'multi-agent-systems.html',
        'API': 'api.html',
        'Hallucination': 'hallucination.html',
        'Guardrails': 'guardrails.html',
        'Benchmarks': 'benchmarks.html',
        'Major AI Providers': 'major-ai-providers.html',
        'Model Types & Families': 'model-types-families.html',
        'Open vs Closed / Local Models': 'open-closed-local-models.html',
        'AI Assistants & Coding Tools': 'ai-assistants-coding-tools.html',
        'General Agents & Computer Use': 'general-agents-computer-use.html',
        'Agent Frameworks': 'agent-frameworks.html',
        'How Agents Are Built': 'how-agents-are-built.html',
        'AI Workflow Platforms': 'ai-workflow-platforms.html',
        'Automation Platforms': 'automation-platforms.html',
        'Frontend & Backend': 'frontend-backend.html',
        'Data, API & Authentication': 'data-api-authentication.html',
        'Deployment & Operations': 'deployment-operations.html',
        'Developer Platforms': 'developer-platforms.html',
        'Web & Cloud Platforms': 'web-cloud-platforms.html',
        'Backend & Data Platforms': 'backend-data-platforms.html',
        'Frontend Technologies': 'frontend-technologies.html',
        'Backend Technologies': 'backend-technologies.html',
        'Data Technologies': 'data-technologies.html',
        'Product Services': 'product-services.html',
        'Monitoring': 'monitoring.html',
        'Permissions & Safety': 'permissions-safety.html',
        'Prompt Injection': 'prompt-injection.html'
      };
      const overviewByModule = {
        '14 · AI Products & Agents': 'ai-products-agents.html',
        '15 · Agent Development': 'agent-development.html',
        '16 · Workflow & Automation': 'workflow-automation.html',
        '17 · Product Architecture': 'product-architecture.html',
        '18 · Development & Cloud Platforms': 'development-cloud-platforms.html',
        '19 · Product Technology Landscape': 'product-technology-landscape.html'
      };
      mount.querySelectorAll('details').forEach((detail) => {
        const moduleName = detail.querySelector(':scope > summary')?.textContent.trim();
        const overview = detail.querySelector('ul > li:first-child a, ul > li:first-child > span');
        if (overviewByModule[moduleName] && overview) {
          const link = overview.tagName === 'A' ? overview : document.createElement('a');
          link.href = overviewByModule[moduleName];
          link.textContent = 'Overview';
          if (overview !== link) overview.replaceWith(link);
        }
      });
      mount.querySelectorAll('li > span').forEach((item) => {
        const label = item.textContent.replace(/\s*NEW\s*$/, '').trim();
        if (completedTopics[label]) {
          const link = document.createElement('a');
          link.href = completedTopics[label];
          link.textContent = label;
          item.replaceWith(link);
        }
      });
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
      let activeDetails;
      mount.querySelectorAll('a[href]').forEach((link) => {
        const url = new URL(link.getAttribute('href'), base);
        if (canonicalPath(url.pathname) === current) {
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
          activeDetails = link.closest('details');
        }
        const status = link.dataset.status;
        if (status) addStatus(link, status);
      });
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
    .catch((error) => { mount.innerHTML = '<p class="directory-note">Site directory is temporarily unavailable.</p>'; console.error(error); });

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
})();
