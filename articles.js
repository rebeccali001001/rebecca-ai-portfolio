(function () {
  const list = document.querySelector('[data-blog-list]');
  if (!list) return;

  const emptyState = document.querySelector('[data-article-empty]');
  const draftPanel = document.querySelector('[data-draft-panel]');
  const draftGrid = document.querySelector('[data-article-grid-drafts]');
  const publishedSection = document.querySelector('.articles-section');
  const visibleSlug = 'local-vs-cloud-api-models';

  const escapeHtml = (value) => String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');

  const safeHref = (value) => {
    const href = String(value ?? '').trim();
    if (/^https?:\/\//i.test(href)) return escapeHtml(href);
    if (/^[a-z0-9_./#?=&%+~-]+$/i.test(href)) return escapeHtml(href);
    return '';
  };

  const dateLabel = (value, status) => {
    if (!value) return status === 'published' ? 'Date to verify' : 'Draft · Date TBD';
    const date = new Date(value);
    return Number.isNaN(date.valueOf())
      ? 'Verify publish date'
      : new Intl.DateTimeFormat('en', { year: 'numeric', month: 'short', day: 'numeric' }).format(date);
  };

  const visualMarkup = (article) => {
    if (article.cover) {
      return '<img src="' + safeHref(article.cover) + '" alt="" loading="lazy">';
    }
    return '<div class="article-card-visual-placeholder">'
      + '<small>' + escapeHtml(article.category || 'Article') + '</small>'
      + '<strong>' + escapeHtml(article.status === 'published' ? 'Field notes' : 'Coming Soon') + '</strong>'
      + '</div>';
  };

  const cardMarkup = (article, allowDraftLink) => {
    const published = article.status === 'published';
    const href = article.path ? safeHref(article.path) : '';
    const reading = article.reading_time
      ? ' · ' + escapeHtml(article.reading_time)
      : '';

    const date = escapeHtml(dateLabel(article.published_at, article.status));
    return '<article class="blog-post" data-status="' + escapeHtml(article.status || 'draft') + '">'
      + '<div class="blog-post-meta"><time>' + date + '</time><span>' + escapeHtml(article.category || 'Blog') + reading + '</span></div>'
      + '<h3>' + (href && (published || allowDraftLink) ? '<a href="' + href + '">' + escapeHtml(article.title) + '</a>' : '<span>' + escapeHtml(article.title) + '</span>') + '</h3>'
      + '</article>';
  };

  const render = (records) => {
    const ordered = records.filter((article) => article.slug === visibleSlug && article.status === 'published').map((article, index) => ({ article, index })).sort((a, b) => {
      const aTime = Date.parse(a.article.published_at || '');
      const bTime = Date.parse(b.article.published_at || '');
      if (Number.isNaN(aTime) && Number.isNaN(bTime)) return a.index - b.index;
      if (Number.isNaN(aTime)) return 1;
      if (Number.isNaN(bTime)) return -1;
      return bTime - aTime;
    }).map(({ article }) => article);
    list.innerHTML = ordered.map((article) => cardMarkup(article, false)).join('');
    if (draftGrid) draftGrid.innerHTML = '';
    if (draftGrid) draftGrid.innerHTML = '';
    if (emptyState) emptyState.hidden = ordered.length > 0;
    if (draftPanel) draftPanel.hidden = true;
    if (publishedSection) publishedSection.hidden = false;
  };

  fetch('articles/data/articles.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error('Article metadata unavailable');
      return response.json();
    })
    .then((records) => {
      if (!Array.isArray(records)) throw new Error('Article metadata must be an array');
      render(records);
    })
    .catch((error) => {
      list.innerHTML = '';
      if (draftGrid) draftGrid.innerHTML = '';
      if (emptyState) {
        emptyState.hidden = false;
        emptyState.querySelector('h3').textContent = 'Blog is temporarily unavailable.';
        emptyState.querySelector('p').textContent = error.message;
      }
    });
})();
