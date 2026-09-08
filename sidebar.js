(function () {
  const mount = document.getElementById('site-directory');
  if (!mount) return;
  const base = new URL('.', document.baseURI);
  fetch(new URL('sidebar.html', base))
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
})();
