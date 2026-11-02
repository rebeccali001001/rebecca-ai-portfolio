(() => {
  const appOrigin = 'https://english-app-new-523.pages.dev';
  if (parent === window) return;
  let enabled = false;
  const send = (payload) => parent.postMessage({ channel: 'rebecca-learning-v1', ...payload }, appOrigin);
  window.addEventListener('message', (event) => {
    if (event.origin !== appOrigin || event.source !== parent || event.data?.channel !== 'rebecca-learning-v1' || event.data?.type !== 'connect') return;
    enabled = true;
    document.documentElement.classList.add('english-learning-embedded');
    send({ type: 'ready', title: document.title, url: location.href });
  });
  const style = document.createElement('style');
  style.textContent = '.english-learning-embedded body>nav .brand,.english-learning-embedded .site-global-links>a,.english-learning-embedded .site-nav-dropdown{display:none!important}';
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
    send({ type: 'selection', text, rect: { left: box.left, top: box.top, bottom: box.bottom }, title: document.title, url: location.href });
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
        send({ type: 'hover', text: match[0], rect: { left: box.left, top: box.top, bottom: box.bottom }, title: document.title, url: location.href });
        break;
      }
    }, 450);
  });
  window.addEventListener('scroll', () => { clearTimeout(hoverTimer); lastWord = ''; if (enabled) send({ type: 'dismiss' }); }, true);
  send({ type: 'available' });
})();
