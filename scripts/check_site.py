#!/usr/bin/env python3
"""Check the complete generated site, using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import argparse
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://haojunhan.com'
POSTS = ['competition', 'determinism-copy-2', 'hedonism-copy']
EXPECTED = {'/', '/projects/', '/blog/', '/cv/', '/404.html'} | {
    f'/projects/{slug}/' for slug in (
        'personal-ai-assistant', 'robot-coverage', 'wankai', 'restaurant-website-workflow'
    )
} | {f'/blog/2025/{slug}/' for slug in POSTS}
COMPATIBILITY = {'/blog/2025/A2life/', '/blog/2025/test/'}
EXPECTED |= COMPATIBILITY


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.duplicates, self.references = set(), [], []
        self.images, self.canonicals, self.robots = [], [], []
        self.h1s = self.mains = self.htmls = 0
        self.language = None
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id'):
            if attrs['id'] in self.ids:
                self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.htmls += 1
            self.language = attrs.get('lang')
        if tag == 'h1':
            self.h1s += 1
        if tag == 'main':
            self.mains += 1
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots.append(attrs.get('content', ''))
        for attribute in ('src', 'href'):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])


def route_for(path, site):
    route = '/' + path.relative_to(site).as_posix()
    return route[:-10] if route.endswith('index.html') else route


def check(site):
    errors, docs = [], {}
    paths = sorted(site.rglob('*.html'))
    for path in paths:
        route = route_for(path, site)
        text = path.read_text()
        doc = docs[route] = Document(text)
        if doc.htmls != 1 or doc.h1s != 1 or doc.mains != 1:
            errors.append(f'{route}: expected one document, H1 and main landmark')
        if not doc.language or 'main' not in doc.ids or '#main' not in doc.references:
            errors.append(f'{route}: missing language or skip-link target')
        if doc.canonicals != [ORIGIN + route]:
            errors.append(f'{route}: incorrect or duplicate canonical {doc.canonicals}')
        if doc.duplicates:
            errors.append(f'{route}: duplicate IDs {doc.duplicates}')
        if any('noindex' in value.lower() for value in doc.robots):
            errors.append(f'{route}: production noindex')
        if '{{' in text or '{%' in text:
            errors.append(f'{route}: unrendered Liquid')
        if '&lt;section' in text or '&lt;h2' in text:
            errors.append(f'{route}: HTML incorrectly rendered as a code block')
        for marker in ('Albert Einstein', 'you@example.com', 'al-folio', 'sample-posts'):
            if marker in text:
                errors.append(f'{route}: leftover template marker {marker}')
        for image in doc.images:
            if 'alt' not in image or not all(image.get(key, '').isdigit() and int(image[key]) > 0 for key in ('width', 'height')):
                errors.append(f'{route}: image missing alt text or dimensions')
    if set(docs) != EXPECTED:
        errors.append(f'Unexpected route inventory: missing={EXPECTED - set(docs)}, extra={set(docs) - EXPECTED}')

    references = 0
    for route, doc in docs.items():
        for ref in doc.references:
            parsed = urlsplit(urljoin(ORIGIN + route, ref))
            if parsed.scheme not in ('http', 'https') or parsed.netloc != 'haojunhan.com':
                continue
            target_route = unquote(parsed.path)
            target = (site / target_route.lstrip('/')).resolve()
            if not target.is_relative_to(site):
                errors.append(f'{route}: reference escapes site: {ref}')
                continue
            if target.is_dir():
                target /= 'index.html'
            references += 1
            if not target.is_file():
                errors.append(f'{route}: broken reference {ref}')
            elif parsed.fragment:
                target_doc = docs.get(target_route)
                if target_doc and unquote(parsed.fragment) not in target_doc.ids:
                    errors.append(f'{route}: missing fragment {ref}')
    css = (site/'assets/personal/site.css').read_text()
    for relative in re.findall(r'url\([\"\']?([^\)\"\']+)', css):
        if not (site/'assets/personal'/relative).is_file():
            errors.append(f'Stylesheet references missing asset: {relative}')
    if (site/'CNAME').read_text().strip() != 'haojunhan.com':
        errors.append('Incorrect CNAME')
    for path in site.rglob('*'):
        relative = path.relative_to(site)
        if path.is_file() and relative.parts[0] != 'assets' and path.suffix != '.html' and str(relative) not in {'CNAME', 'robots.txt', 'feed.xml', 'sitemap.xml'}:
            errors.append(f'Unintended public file: {relative}')
        if path.is_file() and relative.parts[0] == 'assets' and relative.parts[1] != 'personal':
            errors.append(f'Unused theme asset: {relative}')
    feed = ET.parse(site/'feed.xml')
    if len(feed.findall('{http://www.w3.org/2005/Atom}entry')) != len(POSTS):
        errors.append('Feed must contain exactly the published original posts')
    sitemap = ET.parse(site/'sitemap.xml')
    listed = {node.text for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    required = {ORIGIN + route for route in EXPECTED - COMPATIBILITY if route != '/404.html'}
    if not required.issubset(listed):
        errors.append(f'Sitemap missing: {required - listed}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(paths)} pages, {references} local references, {len(POSTS)} original feed entries, sitemap, metadata and public-file inventory.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=ROOT/'_site')
    check(parser.parse_args().site.resolve())
