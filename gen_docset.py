#!/usr/bin/env python3
# Adapted from https://github.com/kmatt/pgdash/blob/master/pgdoc2set.py

import os, glob, re, sqlite3
from bs4 import BeautifulSoup as bs

db = sqlite3.connect('gtkmm.docset/Contents/Resources/docSet.dsidx')
cur = db.cursor()

# Clear database
try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = 'gtkmm.docset/Contents/Resources/Documents'
docbase = 'gtkmm/stable'

for file in os.listdir(os.path.join(docpath, docbase)):
    if not file.endswith('.html'):
        continue

    # Regex for title
    title_re = re.compile('gtkmm: *')

    # Regexes for file prefixes
    class_re = re.compile('class.*\.html')
    category_re = re.compile('group.*\.html')
    namespace_re = re.compile('namespace.*\.html')

    # Regexes for headers
    class_remove = re.compile('(gtkmm:|Class *\w* Reference)')
    category_remove = re.compile('gtkmm:')
    namespace_remove = re.compile('(gtkmm:|Namespace Reference)')

    # Create BS object and strip <title> prefix if there is one
    soup = bs(open(os.path.join(docpath, docbase, file)).read(), 'html5lib')
    title = soup.find('title')
    if (title_re.match(title.text.strip())):
        title.string = title_re.sub('', title.text.strip()).strip()
        with open(os.path.join(docpath, docbase, file), 'wb') as out_file:
            out_file.write(soup.prettify('utf-8'))

    header = soup.find('h1').text.strip()

    # Class
    if class_re.match(file):
        name = class_remove.sub('', header).strip()
        if name is not None:
            print("Found class:", name)
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Class', os.path.join(docbase, file)))

    # Category
    elif category_re.match(file):
        name = category_remove.sub('', header).strip()
        if name is not None:
            print("Found category:", name)
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Category', os.path.join(docbase, file)))

    # Namespace
    elif namespace_re.match(file):
        name = namespace_remove.sub('', header).strip()
        if name is not None:
            print("Found namespace:", name)
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Category', os.path.join(docbase, file)))

db.commit()
db.close()
