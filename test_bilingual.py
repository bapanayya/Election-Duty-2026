# -*- coding: utf-8 -*-
"""
Builder for Bilingual (English & Telugu) Election Officers Guidance Portal
Srikalahasti Municipality Phase 2 Ordinary Elections 2026
"""

import json

with open('srikalahasti_88_polling_stations.json', 'r', encoding='utf-8') as f:
    ps_data = json.load(f)

from prepare_data import reservations, ward_summary

print(f"Loaded {len(ps_data)} polling stations and {len(ward_summary)} wards.")
