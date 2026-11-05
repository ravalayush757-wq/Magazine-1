import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The problem: the cultural-memory-module has "flex: 1" which makes it grow unbounded,
# pushing the footer off the page. Fix: remove flex: 1, set a specific max height instead.

old = 'display: grid; grid-template-columns: 0.9fr 1.4fr; gap: 5mm; align-items: stretch; flex: 1;'
new = 'display: grid; grid-template-columns: 0.9fr 1.4fr; gap: 5mm; align-items: stretch;'

if old in html:
    html = html.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed: removed flex: 1 from Radha cultural-memory-module")
else:
    print("Target string not found!")
    idx = html.find('cultural-memory-module')
    if idx >= 0:
        print("Context:", repr(html[idx:idx+300]))

