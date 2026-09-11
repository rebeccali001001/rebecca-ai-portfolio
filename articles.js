(function () {
  const grid = document.querySelector('[data-article-grid]');
  if (!grid) return;

  const emptyState = document.querySelector('[data-article-empty]');
  const draftPanel = document.querySelector('[data-draft-panel]');
  const draftGrid = document.querySelector('[data-article-grid-drafts]');
  const publishedSection = document.querySelector('.articles-section');
  const draftMode = new URLSearchParams(location.search).get('drafts') === '1';

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

  const dateLabel = (value) => {
    if (!value) return 'No publish date';
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
    const action = href && (published || allowDraftLink)
      ? '<a href="' + href + '">' + (published ? 'Read article' : 'Open local draft') + ' →</a>'
      : '<span class="is-disabled">Coming Soon</span>';
    const tags = Array.isArray(article.tags)
      ? article.tags.map((tag) => '<span class="article-chip">' + escapeHtml(tag) + '</span>').join('')
      : '';
    const reading = article.reading_time
      ? ' · ' + escapeHtml(article.reading_time)
      : ' · Reading time TBD';

    return '<article class="article-card" data-status="' + escapeHtml(article.status || 'draft') + '">'
      + '<div class="article-card-visual">' + visualMarkup(article) + '</div>'
      + '<div class="article-card-body">'
      + '<div class="article-card-topline">'
      + '<span>' + escapeHtml(article.category || 'Article') + '</span>'
      + '<span class="article-card-status">' + (published ? 'Published' : 'Coming Soon') + '</span>'
      + '</div>'
      + '<h3>' + escapeHtml(article.title) + '</h3>'
      + '<p class="article-card-summary">' + escapeHtml(article.summary) + '</p>'
      + '<div class="article-card-tags">' + tags + '</div>'
      + '<div class="article-card-action">'
      + '<span>' + escapeHtml(dateLabel(article.published_at)) + reading + '</span>'
      + action
      + '</div>'
      + '</div>'
      + '</article>';
  };

  const render = (records) => {
    const published = records.filter((article) => article.status === 'published');
    const upcoming = records.filter((article) => article.status !== 'published');

    grid.innerHTML = '';
    if (draftGrid) draftGrid.innerHTML = '';
    if (!draftMode) grid.innerHTML = published.map((article) => cardMarkup(article, false)).join('');
    if (draftGrid) draftGrid.innerHTML = upcoming.map((article) => cardMarkup(article, draftMode)).join('');
    if (emptyState) emptyState.hidden = draftMode || published.length > 0;
    if (draftPanel) draftPanel.hidden = upcoming.length === 0;
    if (publishedSection) publishedSection.hidden = draftMode;
    document.body.classList.toggle('draft-preview', draftMode);

    const count = document.querySelector('[data-article-count]');
    if (count) count.textContent = published.length + ' published articles';
    const notice = document.querySelector('[data-draft-notice]');
    if (notice) {
      notice.textContent = draftMode
        ? 'Local draft preview · these cards are intentionally excluded from the default Articles index until their content is verified and published.'
        : 'Coming Soon · planned topics are shown as metadata-only cards; unfinished article pages remain local-only.';
    }
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
      grid.innerHTML = '';
      if (draftGrid) draftGrid.innerHTML = '';
      if (emptyState) {
        emptyState.hidden = false;
        emptyState.querySelector('h3').textContent = 'Articles are temporarily unavailable.';
        emptyState.querySelector('p').textContent = error.message;
      }
    });
})();
