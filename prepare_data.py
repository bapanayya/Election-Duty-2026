# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive, interactive Election Officers Guidance Portal
for the Phase 2 Ordinary Elections to Srikalahasti Municipality - 2026.
"""

import json
import re

# Load 88 Polling Stations data
with open('srikalahasti_88_polling_stations.json', 'r', encoding='utf-8') as f:
    polling_stations = json.load(f)

# Ward Reservations mapping
# From AP Gazette Extraordinary No. 2578/2026/G-1 dt 01.11.2026
reservations = {
    1: ('SC General', 'SC-G'),
    2: ('Unreserved General', 'UR-G'),
    3: ('SC Women', 'SC-W'),
    4: ('SC General', 'SC-G'),
    5: ('Unreserved General', 'UR-G'),
    6: ('BC Women', 'BC-W'),
    7: ('BC Women', 'BC-W'),
    8: ('BC General', 'BC-G'),
    9: ('Unreserved Women', 'UR-W'),
    10: ('BC Women', 'BC-W'),
    11: ('BC Women', 'BC-W'),
    12: ('Unreserved Women', 'UR-W'),
    13: ('BC Women', 'BC-W'),
    14: ('Unreserved Women', 'UR-W'),
    15: ('Unreserved Women', 'UR-W'),
    16: ('Unreserved Women', 'UR-W'),
    17: ('BC General', 'BC-G'),
    18: ('Unreserved Women', 'UR-W'),
    19: ('Unreserved General', 'UR-G'),
    20: ('Unreserved General', 'UR-G'),
    21: ('ST General', 'ST-G'),
    22: ('Unreserved Women', 'UR-W'),
    23: ('BC Women', 'BC-W'),
    24: ('BC Women', 'BC-W'),
    25: ('BC General', 'BC-G'),
    26: ('Unreserved Women', 'UR-W'),
    27: ('Unreserved General', 'UR-G'),
    28: ('Unreserved General', 'UR-G'),
    29: ('Unreserved Women', 'UR-W'),
    30: ('Unreserved General', 'UR-G'),
    31: ('Unreserved General', 'UR-G'),
    32: ('Unreserved Women', 'UR-W'),
    33: ('BC General', 'BC-G'),
    34: ('Unreserved General', 'UR-G'),
    35: ('SC Women', 'SC-W'),
    36: ('BC General', 'BC-G'),
    37: ('BC General', 'BC-G'),
    38: ('Unreserved General', 'UR-G'),
    39: ('BC General', 'BC-G'),
    40: ('BC General', 'BC-G'),
    41: ('BC General', 'BC-G'),
    42: ('Unreserved Women', 'UR-W'),
    43: ('BC Women', 'BC-W'),
    44: ('Unreserved Women', 'UR-W')
}

# Aggregate ward statistics
ward_summary = {}
for ward in range(1, 45):
    res_name, res_code = reservations[ward]
    ps_in_ward = [ps for ps in polling_stations if ps['ward'] == ward]
    tot_voters = sum(ps['voters'] for ps in ps_in_ward)
    ward_summary[ward] = {
        'ward': ward,
        'res_name': res_name,
        'res_code': res_code,
        'ps_count': len(ps_in_ward),
        'ps_list': [ps['ps_no'] for ps in ps_in_ward],
        'voters': tot_voters
    }

print("Ward summary prepared successfully.")
