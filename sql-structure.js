// Single source of truth for the SQL information architecture.
window.SQL_STRUCTURE = [
  { id: '01', title: 'Query Basics', page: 'sql-query-basics.html', summarySections: ['01 · Basic Query', '02 · SELECT Expressions', '08 · Limiting Results', '41 · Comments'] },
  { id: '02', title: 'Filtering & Conditions', page: 'sql-filtering-conditions.html', summarySections: ['03 · Filtering', '04 · Logical Conditions', '05 · NULL', '06 · IN / BETWEEN / LIKE'] },
  { id: '03', title: 'Sorting & Aggregation', page: 'sql-sorting-aggregation.html', summarySections: ['07 · Sorting', '09 · Aggregate Functions', '10 · GROUP BY', '11 · HAVING'] },
  { id: '04', title: 'Joining & Combining Data', page: 'sql-joining-combining.html', summarySections: ['12 · JOIN Basics', '13 · Self Join', '14 · Table Alias', '15 · UNION', '16 · INTERSECT / EXCEPT'] },
  { id: '05', title: 'Expressions & Functions', page: 'sql-expressions-functions.html', summarySections: ['17 · CASE', '18 · String Functions', '19 · Numeric Functions', '20 · Date / Time', '21 · CAST / CONVERT', '47 · Conditional NULL Functions'] },
  { id: '06', title: 'Subqueries & Advanced Queries', page: 'sql-advanced-queries.html', summarySections: ['22 · Subquery', '23 · EXISTS', '24 · Common Table Expression', '25 · Recursive CTE', '26 · Window Functions', '27 · Partitioned Aggregation', '48 · EXISTS vs IN', '49 · GROUP BY vs Window'] },
  { id: '07', title: 'Data Modification', page: 'sql-data-modification.html', summarySections: ['28 · INSERT', '29 · UPDATE', '30 · DELETE', '31 · TRUNCATE', '40 · Transactions', '44 · SELECT INTO', '45 · MERGE / UPSERT', '46 · Insert Conflict Handling'] },
  { id: '08', title: 'Database Structure', page: 'sql-database-structure.html', summarySections: ['32 · CREATE TABLE', '33 · Common Data Types', '34 · Constraints', '35 · ALTER TABLE', '36 · DROP', '37 · VIEW', '38 · INDEX', '39 · Primary Key / Foreign Key', '42 · CREATE DATABASE / SCHEMA', '43 · Temporary Table'] },
  { id: '09', title: 'SQL Patterns & Reference', page: 'sql-patterns-reference.html', summarySections: ['50 · Common Query Order', '51 · Common SELECT Pattern', '52 · Common Aggregation Pattern', '53 · Common CTE Pattern', '54 · Common Window Pattern', '55 · Common UPDATE Safety Pattern', '56 · Common SQL Keywords', '57 · Common SQL Symbols', '58 · SQL Dialects'] }
];
