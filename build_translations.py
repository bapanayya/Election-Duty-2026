# -*- coding: utf-8 -*-
"""
Script to generate portal_translations.js containing complete English and Telugu dictionaries.
"""

import json

translations = {
    "en": {
        "title": "SRIKALAHASTI MUNICIPALITY — PHASE 2 ORDINARY ELECTIONS, 2026",
        "subtitle": "Andhra Pradesh State Election Commission | District Election Authority & Collector, Tirupati District",
        "stats": [
            {"label": "Wards", "val": "44"},
            {"label": "Polling Stations", "val": "88"},
            {"label": "Electors", "val": "72,537"},
            {"label": "Offices", "val": "12 Clusters"}
        ],
        "banner": {
            "title": "⚡ SEC Notification No. 1490/SEC-F1/2026-3 Dated 12.11.2026 Issued",
            "desc": "Elections called for Chairperson (Direct Election) and Ward Members for 44 Wards under AP Municipalities Act, 1965 & Conduct of Election Rules, 2026.",
            "btnChecklists": "Open Checklists",
            "btnPrint": "Print Quick Kit"
        },
        "nav": [
            {"id": "tab-schedule", "icon": "📅", "title": "Schedule & Deadlines", "badge": ""},
            {"id": "tab-stages", "icon": "🚶", "title": "Stage-by-Stage Guide", "badge": "9 Stages"},
            {"id": "tab-checklists", "icon": "✅", "title": "Checklists", "badge": "8 Sets"},
            {"id": "tab-guidelines", "icon": "📌", "title": "Important Guidelines", "badge": ""},
            {"id": "tab-dodont", "icon": "⚖️", "title": "Do's & Don'ts", "badge": ""},
            {"id": "tab-forms", "icon": "📂", "title": "Forms & Proformas", "badge": "22 Forms"},
            {"id": "tab-directory", "icon": "🏛️", "title": "Srikalahasti Roster", "badge": "88 PS / Teams"},
            {"id": "tab-tools", "icon": "🛠️", "title": "Field Tools & Packing", "badge": ""}
        ],
        "footer": {
            "p1": "Andhra Pradesh State Election Commission — Municipal Ordinary Elections, 2026 (Phase 2)",
            "p2": "Office of the District Election Authority & District Collector, Tirupati | Srikalahasti Municipality",
            "p3": "Statutory References: AP Municipalities Act, 1965 | AP Municipalities (Conduct of Election of Chairpersons & Ward Members) Rules, 2026 | Notification No. 1490/SEC-F1/2026-3"
        }
    },
    "te": {
        "title": "శ్రీకాళహస్తి పురపాలక సంఘం — 2వ విడత సాధారణ ఎన్నికలు, 2026",
        "subtitle": "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం | జిల్లా ఎన్నికల అధికారి & కలెక్టర్, తిరుపతి జిల్లా",
        "stats": [
            {"label": "వార్డులు", "val": "44"},
            {"label": "పోలింగ్ కేంద్రాలు", "val": "88"},
            {"label": "ఓటర్లు", "val": "72,537"},
            {"label": "కార్యాలయాలు", "val": "12 క్లస్టర్లు"}
        ],
        "banner": {
            "title": "⚡ రాష్ట్ర ఎన్నికల సంఘం నోటిఫికేషన్ నెం. 1490/SEC-F1/2026-3 తేది: 12.11.2026 జారీ చేయబడింది",
            "desc": "ఆంధ్రప్రదేశ్ మున్సిపాలిటీల చట్టం, 1965 మరియు ఎన్నికల నిర్వహణ నియమావళి, 2026 ప్రకారం ఛైర్‌పర్సన్ (ప్రత్యక్ష ఎన్నిక) మరియు 44 వార్డు సభ్యుల స్థానాలకు ఎన్నికలు ప్రకటించబడ్డాయి.",
            "btnChecklists": "చెక్‌లిస్టులు చూడండి",
            "btnPrint": "ప్రింట్ తీసుకోండి"
        },
        "nav": [
            {"id": "tab-schedule", "icon": "📅", "title": "షెడ్యూలు & గడువులు", "badge": ""},
            {"id": "tab-stages", "icon": "🚶", "title": "దశలవారీ మార్గదర్శి", "badge": "9 దశలు"},
            {"id": "tab-checklists", "icon": "✅", "title": "చెక్‌లిస్టులు", "badge": "8 సెట్లు"},
            {"id": "tab-guidelines", "icon": "📌", "title": "ముఖ్య మార్గదర్శకాలు", "badge": ""},
            {"id": "tab-dodont", "icon": "⚖️", "title": "చేయవలసినవి & చేయకూడనివి", "badge": ""},
            {"id": "tab-forms", "icon": "📂", "title": "ఫారాలు & ప్రొఫార్మాలు", "badge": "22 ఫారాలు"},
            {"id": "tab-directory", "icon": "🏛️", "title": "శ్రీకాళహస్తి డైరెక్టరీ", "badge": "88 కేంద్రాలు"},
            {"id": "tab-tools", "icon": "🛠️", "title": "క్షేత్ర సాధనాలు & ప్యాకింగ్", "badge": ""}
        ],
        "footer": {
            "p1": "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం — పురపాలక సాధారణ ఎన్నికలు, 2026 (2వ విడత)",
            "p2": "జిల్లా ఎన్నికల అధికారి & జిల్లా కలెక్టర్ కార్యాలయం, తిరుపతి | శ్రీకాళహస్తి పురపాలక సంఘం",
            "p3": "చట్టబద్ధ ఆధారాలు: ఎ.పి. మున్సిపాలిటీల చట్టం, 1965 | మున్సిపాలిటీలు/నగర పంచాయతీల ఎన్నికల నిర్వహణ నియమావళి, 2026 | నోటిఫికేషన్ నెం. 1490/SEC-F1/2026-3"
        }
    }
}

print("Base i18n structure mapped.")
