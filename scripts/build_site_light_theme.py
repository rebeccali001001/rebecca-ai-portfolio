"""Build scoped color overrides and connect the portfolio's light theme.

Only presentation declarations are collected; source layouts and content stay
in their existing files. Python Summary is deliberately excluded.
"""
from pathlib import Path
from datetime import datetime
import colorsys
import hashlib
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
STAMP = datetime.now().strftime('%Y%m%d_%H%M%S')
BACKUPS = []
COLOR = re.compile(r'#[\da-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)|\b(?:white|black|transparent|currentColor|inherit)\b')


def backup(path):
    target = path.parent / 'history' / f'{path.stem}_{STAMP}{path.suffix}'
    target.parent.mkdir(exist_ok=True)
    shutil.copy2(path, target)
    assert target.stat().st_size > 0 and target.stat().st_size == path.stat().st_size
    assert hashlib.sha256(target.read_bytes()).digest() == hashlib.sha256(path.read_bytes()).digest()
    BACKUPS.append(str(target.relative_to(ROOT)))


def split_top(text, separator):
    start = depth = 0
    quote = ''
    escape = False
    for i, char in enumerate(text):
        if escape:
            escape = False
        elif char == '\\':
            escape = True
        elif quote:
            if char == quote:
                quote = ''
        elif char in '\"\'':
            quote = char
        elif char in '([':
            depth += 1
        elif char in ')]':
            depth -= 1
        elif char == separator and depth == 0:
            yield text[start:i].strip()
            start = i + 1
    yield text[start:].strip()


def blocks(text):
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    start = opening = depth = 0
    quote = ''
    escape = False
    for i, char in enumerate(text):
        if escape:
            escape = False
        elif char == '\\':
            escape = True
        elif quote:
            if char == quote:
                quote = ''
        elif char in '\"\'':
            quote = char
        elif char == '{':
            if depth == 0:
                opening = i
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                yield text[start:opening].strip(), text[opening + 1:i]
                start = i + 1


def rgb(value):
    value = value.lower()
    if value == 'white':
        return (255, 255, 255)
    if value == 'black':
        return (0, 0, 0)
    if value.startswith('#'):
        digits = value[1:]
        if len(digits) in (3, 4):
            digits = ''.join(char * 2 for char in digits)
        return tuple(int(digits[i:i + 2], 16) for i in (0, 2, 4))
    if value.startswith('rgb'):
        numbers = re.findall(r'[\d.]+', value)
        return tuple(float(number) for number in numbers[:3])
    if value.startswith('hsl'):
        h, s, light = map(float, re.findall(r'[\d.]+', value)[:3])
        return tuple(x * 255 for x in colorsys.hls_to_rgb(h / 360, light / 100, s / 100))
    return None


def recolor(value, role):
    channels = rgb(value)
    if channels is None:
        return value
    h, light, saturation = colorsys.rgb_to_hls(*(x / 255 for x in channels))
    hue = h * 360
    accent = saturation > .24 and 65 <= hue <= 265 and light > .27
    warning = saturation > .30 and 20 <= hue < 65
    danger = saturation > .30 and (hue < 20 or hue > 330) and light > .3
    if role == 'background':
        if accent:
            return '#eff6ff'
        if warning:
            return '#fffbeb'
        if danger:
            return '#fef2f2'
        return '#ffffff' if light > .96 else '#f8fafc'
    if role == 'border':
        return '#93b4ed' if accent else '#dce3ed'
    if accent:
        return '#1d4ed8'
    if warning:
        return '#92400e'
    if danger:
        return '#b91c1c'
    return '#171717' if light > .93 or light < .18 else '#4b5563'


def theme_value(value, role):
    return COLOR.sub(lambda match: recolor(match[0], role), value)


def declarations(body):
    themed = []
    for item in split_top(body, ';'):
        if ':' not in item:
            continue
        prop, value = item.split(':', 1)
        prop, value = prop.strip().lower(), re.sub(r'\s*!important\s*', '', value.strip())
        result = None
        if prop in ('color', 'text-decoration-color', 'caret-color', 'outline-color', 'stroke'):
            result = theme_value(value, 'text')
        elif prop == 'fill':
            result = theme_value(value, 'background')
        elif prop in ('background', 'background-color', 'background-image'):
            if 'url(' in value or value in ('none', 'inherit', 'transparent'):
                continue
            if 'gradient(' in value:
                themed.extend(['background-image:none!important', 'background-color:#f8fafc!important'])
                continue
            result = theme_value(value, 'background')
        elif prop.startswith('border') and ('color' in prop or prop in ('border', 'border-top', 'border-right', 'border-bottom', 'border-left')):
            if 'color' not in prop:
                colors = re.findall(r'var\([^)]*\)|' + COLOR.pattern, value)
                if not colors:
                    continue
                prop += '-color'
                value = colors[-1]
            result = theme_value(value, 'border')
        elif prop == 'box-shadow':
            result = 'none' if value == 'none' else '0 3px 16px #17223b08'
        elif prop == 'text-shadow':
            result = 'none'
        elif prop.startswith('--') and COLOR.search(value):
            role = 'background' if re.search(r'bg|panel|surface|paper', prop) else 'border' if re.search(r'line|border', prop) else 'text'
            result = theme_value(value, role)
        if result is not None:
            themed.append(f'{prop}:{result}!important')
    if re.search(r'(?:-webkit-)?background-clip\s*:\s*text', body):
        themed.extend(['background:none!important', 'color:#171717!important', '-webkit-text-fill-color:#171717!important'])
    return ';'.join(themed)


def scoped(selector):
    if ':root' in selector:
        return selector.replace(':root', 'html.site-light')
    if re.match(r'^html\b', selector):
        return re.sub(r'^html\b', 'html.site-light', selector)
    return 'html.site-light ' + selector


def rules(text):
    result = []
    for selector, body in blocks(text):
        if selector.startswith(('@media', '@supports', '@layer', '@container')):
            inner = rules(body)
            if inner:
                result.append(selector + '{' + '\n'.join(inner) + '}')
        elif not selector.startswith('@'):
            values = declarations(body)
            if values:
                result.append(','.join(scoped(x) for x in split_top(selector, ',')) + '{' + values + '}')
    return result


def main():
    paths = [ROOT / name for name in subprocess.check_output(['git', 'ls-files', '*.html'], cwd=ROOT, text=True).splitlines()]
    pages = [p for p in paths if p.name not in ('python-summary.html', 'sidebar.html', 'qa-layout.html', 'codex_batch_workbench.html')]
    source_styles = []
    inline_colors = set()
    for p in pages:
        source = p.read_text(encoding='utf-8-sig')
        for href in re.findall(r'<link[^>]*href=[\"\']([^\"\']+\.css[^\"\']*)', source):
            if href.startswith(('http:', 'https:')) or 'site-light' in href:
                continue
            base = ROOT if '<base ' in source else p.parent
            css = (base / href.split('?')[0]).resolve()
            if css.is_file() and css not in source_styles and css.name != 'artificial-intelligence-light.css':
                source_styles.append(css)
        for style in re.findall(r'style=[\"\']([^\"\']+)[\"\']', source):
            inline_colors.update(COLOR.findall(style))
        inline_colors.update(re.findall(r'(?:fill|stroke)=[\"\'](#[\da-fA-F]{3,8})[\"\']', source))
    # A few maps load their CSS from JavaScript after the initial HTML load.
    for css in sorted(ROOT.glob('*.css')):
        if css.name not in ('site-light.css', 'artificial-intelligence-light.css') and not css.name.startswith('python-summary') and css not in source_styles:
            source_styles.append(css)
    output = ['/* Generated color overrides. Rebuild with scripts/build_site_light_theme.py. */']
    seen = set()
    for p in source_styles:
        for rule in rules(p.read_text(encoding='utf-8-sig')):
            if rule not in seen:
                seen.add(rule)
                output.append(rule)
    for p in pages:
        for style in re.findall(r'<style[^>]*>(.*?)</style>', p.read_text(encoding='utf-8-sig'), re.S):
            for rule in rules(style):
                if rule not in seen:
                    seen.add(rule)
                    output.append(rule)
    # Inline colors override CSS unless explicitly themed. Never alter the text
    # of examples or the underlying inline declaration itself.
    for color in sorted(inline_colors):
        for prop, role in [('color', 'text'), ('background', 'background'), ('background-color', 'background'), ('border-color', 'border')]:
            attribute = ','.join(f'html.site-light [style*="{prop}:{space}{color}" i]' for space in ('', ' '))
            output.append(attribute + '{' + prop + ':' + recolor(color, role) + '!important}')
        for prop, role in [('fill', 'background'), ('stroke', 'border')]:
            output.append(f'html.site-light svg [{prop}="{color}" i]' + '{' + prop + ':' + recolor(color, role) + '!important}')
    theme = ROOT / 'site-light.css'
    if theme.exists():
        backup(theme)
    theme.write_text('\n'.join(output) + '\n' + (ROOT / 'scripts/site_light_finishing.css').read_text(encoding='utf-8'), encoding='utf-8')
    changed = []
    for p in pages:
        source = p.read_text(encoding='utf-8-sig')
        if '<html' not in source or '</head>' not in source:
            continue
        updated = re.sub(r'<html\b([^>]*)>', lambda m: '<html' + (re.sub(r'class=([\"\'])(.*?)\1', lambda c: 'class=' + c[1] + c[2] + ' site-light' + c[1], m[1]) if re.search(r'class=', m[1]) else m[1] + ' class="site-light"') + '>', source, count=1) if not re.search(r'<html[^>]*class=[\"\'][^\"\']*\bsite-light\b', source) else source
        updated = re.sub(r'<link[^>]*href=[\"\']artificial-intelligence-light\.css[^\"\']*[\"\'][^>]*>', '', updated)
        if 'href="site-light.css' not in updated and 'href="../site-light.css' not in updated:
            relative = 'site-light.css' if p.parent == ROOT or '<base ' in source else '../' * len(p.relative_to(ROOT).parts[:-1]) + 'site-light.css'
            updated = updated.replace('</head>', f'<link rel="stylesheet" href="{relative}?v=20261016">\n</head>', 1)
        if updated != source:
            backup(p)
            p.write_text(updated, encoding='utf-8')
            changed.append(str(p.relative_to(ROOT)))
    manifest = ROOT / 'history' / f'site-light-backups_{STAMP}.txt'
    manifest.write_text('\n'.join(BACKUPS), encoding='utf-8')
    print(f'Themed {len(pages)} pages from {len(source_styles)} shared stylesheets; updated {len(changed)} HTML files.')
    print(f'Backup manifest: {manifest}')
    print(f'Theme stylesheet: {theme.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
