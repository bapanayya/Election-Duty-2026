# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('portal_translations.js', 'r', encoding='utf-8') as f:
    trans_js = f.read()

with open('portal_forms.js', 'r', encoding='utf-8') as f:
    forms_js = f.read()

with open('portal_app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

html = html.replace('<script src="portal_translations.js"></script>', '<script>\n' + trans_js + '\n</script>')
html = html.replace('<script src="portal_forms.js"></script>', '<script>\n' + forms_js + '\n</script>')
html = html.replace('<script src="portal_app.js"></script>', '<script>\n' + app_js + '\n</script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully created inlined single-file index.html. Total size:", len(html))
