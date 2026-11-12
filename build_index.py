# -*- coding: utf-8 -*-
"""
Build the full HTML file index.html
"""

import json
from portal_data import (
    reservations, ward_summary, ps_data, supporting_staff,
    zonal_officers, route_officers, surveillance_teams
)

print(f"Loaded {len(ps_data)} polling stations and {len(ward_summary)} wards.")
