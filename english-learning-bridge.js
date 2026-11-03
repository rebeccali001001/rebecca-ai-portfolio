(() => {
  const appOrigin = 'https://english-app-new-523.pages.dev';
  if (parent === window) return;
  let enabled = false;
  const send = (payload) => parent.postMessage({ channel: 'rebecca-learning-v1', ...payload }, appOrigin);
  const pageKey = (value) => {
    const url = new URL(value, location.href);
    return url.origin + url.pathname.replace(/\.html$/, '');
  };
  const anchorFor = (range) => {
    const main = document.querySelector('main');
    if (!main?.contains(range.startContainer) || !main.contains(range.endContainer)) return null;
    const prefix = document.createRange(); prefix.selectNodeContents(main); prefix.setEnd(range.startContainer, range.startOffset);
    const quote = range.toString().slice(0, 2000);
    return { start: prefix.toString().length, end: prefix.toString().length + quote.length, quote };
  };
  const paint = (items) => {
    const main = document.querySelector('main');
    if (!main) return;
    main.querySelectorAll('mark[data-rk-highlight]').forEach((mark) => mark.replaceWith(...mark.childNodes));
    main.normalize();
    const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT);
    const nodes = []; let node; let length = 0;
    while ((node = walker.nextNode())) { nodes.push({ node, start: length, end: length + node.length }); length += node.length; }
    const text = main.textContent;
    const ranges = [];
    for (const item of items.slice(0, 1000)) {
      const anchor = item.anchor;
      if (!anchor || typeof anchor.quote !== 'string' || !anchor.quote) continue;
      let start = anchor.start; let end = anchor.end;
      if (!Number.isInteger(start) || !Number.isInteger(end) || text.slice(start, end) !== anchor.quote) {
        start = text.indexOf(anchor.quote); end = start + anchor.quote.length;
        if (start < 0 || text.indexOf(anchor.quote, start + 1) >= 0) continue;
      }
      const first = nodes.find((n) => n.end > start); const last = nodes.find((n) => n.end >= end);
      if (!first || !last) continue;
      const range = document.createRange(); range.setStart(first.node, start - first.start); range.setEnd(last.node, end - last.start); ranges.push(range);
    }
    if (window.CSS?.highlights && window.Highlight) {
      CSS.highlights.set('rk-yellow', new Highlight(...ranges));
    } else {
      // Work backwards so text splits do not shift the remaining offsets.
      for (const range of ranges.reverse()) {
        for (const entry of nodes.slice().reverse()) {
          if (!range.intersectsNode(entry.node)) continue;
          const start = entry.node === range.startContainer ? range.startOffset : 0;
          const end = entry.node === range.endContainer ? range.endOffset : entry.node.length;
          if (end <= start) continue;
          const part = document.createRange(); part.setStart(entry.node, start); part.setEnd(entry.node, end);
          const mark = document.createElement('mark'); mark.dataset.rkHighlight = 'true'; mark.style.backgroundColor = '#fef08a'; part.surroundContents(mark);
        }
      }
    }
  };
  window.addEventListener('message', (event) => {
    if (event.origin !== appOrigin || event.source !== parent || event.data?.channel !== 'rebecca-learning-v1') return;
    if (enabled && event.data.type === 'clearSelection') { window.getSelection()?.removeAllRanges(); return; }
    if (enabled && event.data.type === 'annotations' && pageKey(event.data.url) === pageKey(location.href) && Array.isArray(event.data.items)) { paint(event.data.items); return; }
    if (event.data.type !== 'connect') return;
    enabled = true;
    document.documentElement.classList.add('english-learning-embedded');
    send({ type: 'ready', title: document.title, url: location.href });
  });
  const style = document.createElement('style');
  style.textContent = '::highlight(rk-yellow){background:#fef08a;color:#111827}.english-learning-embedded body>nav .brand,.english-learning-embedded .site-global-links>a,.english-learning-embedded .site-nav-dropdown{display:none!important}';
  document.head.appendChild(style);
  const publishSelection = () => {
    if (!enabled) return;
    const selection = getSelection();
    const text = selection?.toString().trim().slice(0, 2000);
    if (!text || !selection.rangeCount) return;
    const range = selection.getRangeAt(0);
    const element = range.startContainer.nodeType === Node.ELEMENT_NODE ? range.startContainer : range.startContainer.parentElement;
    if (!element?.closest('main') || element.closest('input,textarea,select')) return;
    const box = range.getBoundingClientRect();
    send({ type: 'selection', text, anchor: anchorFor(range), rect: { left: box.left, top: box.top, bottom: box.bottom }, title: document.title, url: location.href });
  };
  let timer;
  document.addEventListener('selectionchange', () => { clearTimeout(timer); timer = setTimeout(publishSelection, 250); });
  document.addEventListener('mouseup', publishSelection);
  document.addEventListener('keyup', publishSelection);
  let hoverTimer;
  let lastWord = '';
  document.addEventListener('mousemove', (event) => {
    clearTimeout(hoverTimer);
    if (!enabled || !matchMedia('(hover: hover)').matches || getSelection()?.toString().trim()) return;
    if (!event.target.closest('main') || event.target.closest('button,input,textarea,select')) return;
    hoverTimer = setTimeout(() => {
      const caret = document.caretPositionFromPoint?.(event.clientX, event.clientY);
      const fallback = !caret && document.caretRangeFromPoint?.(event.clientX, event.clientY);
      const node = caret?.offsetNode || fallback?.startContainer;
      const offset = caret?.offset ?? fallback?.startOffset;
      if (!node || node.nodeType !== Node.TEXT_NODE) return;
      const matches = node.textContent.matchAll(/[A-Za-z]+(?:['’-][A-Za-z]+)*/g);
      for (const match of matches) {
        if (offset < match.index || offset > match.index + match[0].length) continue;
        const range = document.createRange();
        range.setStart(node, match.index); range.setEnd(node, match.index + match[0].length);
        const box = range.getBoundingClientRect();
        if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) return;
        if (lastWord === match[0]) return;
        lastWord = match[0];
        send({ type: 'hover', text: match[0], anchor: anchorFor(range), rect: { left: box.left, top: box.top, bottom: box.bottom }, title: document.title, url: location.href });
        break;
      }
    }, 450);
  });
  window.addEventListener('scroll', () => { clearTimeout(hoverTimer); lastWord = ''; if (enabled) send({ type: 'dismiss' }); }, true);
  send({ type: 'available' });
})();
