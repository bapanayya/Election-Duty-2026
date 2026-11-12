# -*- coding: utf-8 -*-
"""
Master Builder for Bilingual (English & Telugu) Srikalahasti Election Officers Portal.
"""

import json

with open('srikalahasti_88_polling_stations.json', 'r', encoding='utf-8') as f:
    ps_data = json.load(f)

from prepare_data import reservations, ward_summary

print(f"Data verified: {len(ps_data)} polling stations, {len(ward_summary)} wards.")
