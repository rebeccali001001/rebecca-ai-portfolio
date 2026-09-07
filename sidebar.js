(function () {
  const mount = document.getElementById('site-directory');
  if (!mount) return;
  const base = new URL('.', document.baseURI);
  fetch(new URL('sidebar.html', base))
    .then((response) => { if (!response.ok) throw new Error('Sidebar unavailable'); return response.text(); })
    .then((html) => {
      mount.innerHTML = html;
      const current = decodeURIComponent(location.pathname.split('/').pop() || 'index.html').toLowerCase();
      let activeDetails;
      mount.querySelectorAll('a[href]').forEach((link) => {
        const url = new URL(link.getAttribute('href'), base);
        if (url.pathname.split('/').pop().toLowerCase() === current) {
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
          activeDetails = link.closest('details');
        }
        const status = link.dataset.status;
        if (status) addStatus(link, status);
      });
      mount.querySelectorAll('details').forEach((detail) => {
        detail.open = detail === activeDetails;
        const summary = detail.querySelector(':scope > summary');
        if (summary) summary.classList.toggle('active-module', detail === activeDetails);
        detail.classList.toggle('expanded', detail === activeDetails);
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
