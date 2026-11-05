import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PUB = r'e:\hugo\williamlong\public'

def alias(path, target):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    html = f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="https://www.williamlong.info{target}"></head><body><a href="{target}">跳转</a></body></html>'
    open(path, 'w', encoding='utf-8', newline='').write(html)

count = 0
SECTIONS = ['', 'weibo', 'google', 'apps', 'info', 'movie']

# 1. term pages: {prefix}/{kind}/{slug}.html -> {prefix}/{kind}/{slug}/  (term page compat)
#    term pagers: {prefix}/{kind}/{slug}_{N}.html -> {prefix}/{kind}/{slug}/page/{N}/
for sec in SECTIONS:
    for kind in ['cat', 'tag']:
        base = os.path.join(PUB, sec, kind) if sec else os.path.join(PUB, kind)
        if not os.path.isdir(base):
            continue
        prefix = f'/{sec}/{kind}' if sec else f'/{kind}'
        for slug in os.listdir(base):
            sdir = os.path.join(base, slug)
            if not os.path.isdir(sdir):
                continue
            # term page alias
            if os.path.exists(os.path.join(sdir, 'index.html')):
                alias(os.path.join(base, f'{slug}.html'), f'{prefix}/{slug}/')
                count += 1
            # pager aliases
            pdir = os.path.join(sdir, 'page')
            if os.path.isdir(pdir):
                for n in os.listdir(pdir):
                    if n.isdigit() and n != '1' and os.path.exists(os.path.join(pdir, n, 'index.html')):
                        alias(os.path.join(base, f'{slug}_{n}.html'), f'{prefix}/{slug}/page/{n}/')
                        count += 1

# 2. home/section legacy pagers: {sec}/page/index_{N}.html -> {sec}/page/{N}/
for sec in SECTIONS:
    pdir = os.path.join(PUB, sec, 'page') if sec else os.path.join(PUB, 'page')
    if not os.path.isdir(pdir):
        continue
    prefix = f'/{sec}' if sec else ''
    for n in os.listdir(pdir):
        if n.isdigit() and n != '1' and os.path.exists(os.path.join(pdir, n, 'index.html')):
            alias(os.path.join(pdir, f'index_{n}.html'), f'{prefix}/page/{n}/')
            count += 1

print('alias pages generated:', count)
