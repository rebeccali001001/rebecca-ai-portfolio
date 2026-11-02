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
    send({ type: 'selection', text, title: document.title, url: location.href });
  };
  let timer;
  document.addEventListener('selectionchange', () => { clearTimeout(timer); timer = setTimeout(publishSelection, 250); });
  document.addEventListener('mouseup', publishSelection);
  document.addEventListener('keyup', publishSelection);
  send({ type: 'available' });
})();
