# -*- coding: utf-8 -*-
"""
Generate and update index.html with complete bilingual forms from Election-Officers-Forms.pdf
"""

import json
import re

with open('portal_forms_full.json', 'r', encoding='utf-8') as f:
    forms_data = json.load(f)

# Format into BILINGUAL_FORMS structure
bilingual_forms = []

for f in forms_data:
    bilingual_forms.append({
        "id": f["code"].lower().replace(' ', '-').replace('(', '').replace(')', ''),
        "code": f["code"],
        "name_en": f["title_en"].replace(f["code"] + ": ", ""),
        "name_te": f["title_te"].replace(f["code"] + ": ", ""),
        "rule": f["rule"] + " | " + f["authority"],
        "stage_en": f["category"],
        "stage_te": f["category_te"],
        "desc_en": f["desc_en"],
        "desc_te": f["desc_te"],
        "text_en": f["content_en"],
        "text_te": f["content_te"]
    })

print(f"Prepared {len(bilingual_forms)} forms.")

js_array_str = "const BILINGUAL_FORMS = " + json.dumps(bilingual_forms, ensure_ascii=False, indent=2) + ";\n"

# Now let's update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing BILINGUAL_FORMS
old_forms_match = re.search(r'const BILINGUAL_FORMS = \[.*?\];', html, re.DOTALL)
if old_forms_match:
    html = html[:old_forms_match.start()] + js_array_str.strip() + html[old_forms_match.end():]
    print("Replaced existing BILINGUAL_FORMS array.")
else:
    print("Could not match old BILINGUAL_FORMS directly.")

# Update tab badges for Forms: "18 Forms" / "18 ఫారాలు"
html = html.replace('badge: "22 Forms"', 'badge: "18 Forms"')
html = html.replace('badge: "22 ఫారాలు"', 'badge: "18 ఫారాలు"')
html = html.replace('22 ఫారాలు', '18 ఫారాలు')
html = html.replace('22 Forms', '18 Forms')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully with 18 clean forms!")
