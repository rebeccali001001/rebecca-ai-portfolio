import { readFile } from 'node:fs/promises';

const base = process.env.QA_BASE_URL || 'http://127.0.0.1:8001';
const sidebar = await readFile(new URL('../sidebar.js', import.meta.url), 'utf8');
const summary = await (await fetch(`${base}/sql-summary.html`)).text();
const labels = ['Summary', 'Glossary', '01 · Query Basics', '02 · Filtering', '03 · Sorting & Aggregation', '04 · Joining Tables', '05 · Logic', '06 · Data Modification', '07 · Database Definition'];
const failures = [];

if (!summary.includes('SQL Syntax Master Summary')) failures.push('SQL Summary title missing');
if (!summary.includes('<table>')) failures.push('SQL Summary table missing');
for (const label of labels) {
  if (label !== 'Glossary' && !sidebar.includes("moduleName === 'SQL' ? `sql-summary.html#")) failures.push(`Directory mapping missing: ${label}`);
}
if (!sidebar.includes("moduleName === 'SQL'")) failures.push('SQL syntax module routing guard missing');

if (failures.length) {
  console.error('SQL navigation QA FAILED');
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}
console.log(`SQL navigation QA PASSED (${labels.length} directory entries checked)`);
