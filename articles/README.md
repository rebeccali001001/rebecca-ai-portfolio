# Articles system

The Articles module is a small static publishing system:

- ../articles.html is the public index.
- data/articles.json is the single metadata source for article cards.
- drafts/ contains local-only article pages.
- published/ is reserved for articles whose metadata status is published.
- templates/article-template.html is the reusable long-form page skeleton.
- ../articles.js renders only published records by default.

Open ../articles.html?drafts=1 locally to preview records with draft or review status. A record with status "draft" is not shown on the default index. Set published_at, reading_time, and path only after the article has been checked.

Each article can link back to Knowledge concepts and Projects through the related_knowledge and related_projects metadata fields. Keep the article focused on the specific build, experiment, or decision; use Knowledge pages for reusable definitions.
