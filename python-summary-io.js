/* Complete independent programs and their captured stdout. */
(() => {
  'use strict';
  const lessons = window.pythonSummaryRunnable;
  if (!lessons) throw new Error('Runnable examples were not loaded.');
  function isKeyLine(line, name, syntax) {
    if (!line.trim() || line.trim().startsWith('#')) return false;
    const method = name.match(/\.?([A-Za-z_]\w*)\(/);
    if (method) return new RegExp(`\\b${method[1]}\\s*\\(`).test(line);
    const keyword = name.match(/^(True|False|None|if|elif|else|for|while|with|try|except|finally|def|class|return|yield|import|from|match|case|assert|del|global|nonlocal|async|await)\b/);
    if (keyword) return new RegExp(`\\b${keyword[1]}\\b`).test(line);
    return line.includes(syntax) || (name.length < 12 && line.includes(name));
  }
  const loops = document.querySelectorAll('#for-loops tbody tr');
  if (loops[5]) loops[5].cells[2].textContent = 'enumerate(items, start=1)';
  if (loops[7]) loops[7].cells[2].textContent = 'data.items()';
  for (const section of document.querySelectorAll('.summary-table section')) {
    const table = section.querySelector('table');
    if (!table) continue;
    const rows = [...table.querySelectorAll('tbody tr')];
    if (lessons[section.id]?.length !== rows.length) throw new Error(`Incomplete examples: ${section.id}`);
    table.querySelector('thead tr').innerHTML = '<th scope="col">名称 Name</th><th scope="col">说明 Explanation</th><th scope="col">语法 Syntax</th><th scope="col">输入代码</th><th scope="col">输出结果</th>';
    rows.forEach((row, index) => {
      const {code: input, output} = lessons[section.id][index];
      const name = row.cells[0].textContent.trim();
      const syntax = row.cells[2].textContent.trim();
      const inputCell = row.cells[3];
      inputCell.replaceChildren();
      const pre = document.createElement('pre');
      pre.className = 'io-code';
      const code = document.createElement('code');
      input.split('\n').forEach((line) => {
        const span = document.createElement('span');
        span.className = `io-line${isKeyLine(line, name, syntax) ? ' is-key' : ''}${line.trim().startsWith('#') ? ' io-comment' : ''}`;
        span.textContent = line || ' ';
        code.append(span);
      });
      pre.append(code);
      inputCell.append(pre);
      const outputCell = row.insertCell();
      outputCell.className = 'io-output';
      outputCell.textContent = output;
    });
    const scroll = document.createElement('div');
    scroll.className = 'summary-table-scroll';
    table.before(scroll);
    scroll.append(table);
  }
  if (location.hash) requestAnimationFrame(() => {
    document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
  });
})();
