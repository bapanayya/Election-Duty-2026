import json

with open('enriched_88_polling_stations.json', encoding='utf-8') as f:
    ps_list = json.load(f)

po_roster = []
for p in ps_list:
    sl = p['sl']
    phone = f"98480{sl:05d}"
    po_roster.append({
        'sl': sl,
        'ward': p['ward'],
        'ps_no': p['ps_no'],
        'po_name': f"Presiding Officer PS {p['ps_no']}",
        'po_phone': phone,
        'route': p['route'],
        'cluster': p['cluster']
    })

print(f"Generated PO roster for {len(po_roster)} stations.")
print("Sample PO 1:", po_roster[0])
print("Sample PO 88:", po_roster[87])

with open('po_roster.json', 'w', encoding='utf-8') as f:
    json.dump(po_roster, f, indent=2, ensure_ascii=False)
