# -*- coding: utf-8 -*-
"""
Script to create portal_translations.js with comprehensive English & Telugu content.
"""

import json

# Compile all translation data into a structured format
data = {
    "en": {
        "headerTitle": "SRIKALAHASTI MUNICIPALITY — PHASE 2 ORDINARY ELECTIONS, 2026",
        "headerSubtitle": "Andhra Pradesh State Election Commission | District Election Authority & Collector, Tirupati District",
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
        "tabs": [
            {"id": "tab-schedule", "icon": "📅", "title": "Schedule & Deadlines", "badge": ""},
            {"id": "tab-stages", "icon": "🚶", "title": "Stage-by-Stage Guide", "badge": "9 Stages"},
            {"id": "tab-checklists", "icon": "✅", "title": "Checklists", "badge": "8 Sets"},
            {"id": "tab-guidelines", "icon": "📌", "title": "Important Guidelines", "badge": ""},
            {"id": "tab-dodont", "icon": "⚖️", "title": "Do's & Don'ts", "badge": ""},
            {"id": "tab-forms", "icon": "📂", "title": "Forms & Proformas", "badge": "22 Forms"},
            {"id": "tab-directory", "icon": "🏛️", "title": "Srikalahasti Roster", "badge": "88 PS / Teams"},
            {"id": "tab-tools", "icon": "🛠️", "title": "Field Tools & Packing", "badge": ""}
        ],
        "sched": {
            "title": "📅 Election Programme & Statutory Timeline",
            "sub": "Comprehensive timeline notified by AP State Election Commission for Phase 2 Ordinary Municipal Elections, 2026.",
            "timelines": [
                {"stage": "Stage 1: Pre-Poll", "date": "14.11.2026 (Saturday)", "title": "Ward Electoral Rolls Display", "desc": "Under Rule 5, Election Officer displays ward-wise voter lists on the notice board.", "time": "⏰ Morning 10:00 AM", "class": ""},
                {"stage": "Stage 2: Public Notice", "date": "14.11.2026 (Saturday)", "title": "Publication of Election Notice", "desc": "Election Notice issued by Election Officer under Rule 6 in prescribed format (Form-1).", "time": "⏰ Morning (Before Nominations)", "class": ""},
                {"stage": "Stage 3: Nominations", "date": "14.11.2026 to 16.11.2026", "title": "Filing & Receipt of Nominations", "desc": "Receipt of nominations at 12 designated offices (Chairperson + 11 Ward Clusters).", "time": "⏰ 11:00 AM to 3:00 PM Daily", "class": "active-stage"},
                {"stage": "Stage 4: Last Date", "date": "16.11.2026 (Monday)", "title": "Close of Nominations & Form-A", "desc": "Last moment for nomination filing (3 PM). Political party Form-A to Collector & DEA before 5 PM.", "time": "⏰ 3:00 PM (Sharp) / 5:00 PM (Form-A)", "class": ""},
                {"stage": "Stage 5: Scrutiny", "date": "17.11.2026 (Tuesday)", "title": "Scrutiny of Nominations", "desc": "Quasi-judicial examination by Election Officer. Publication of Form-IV valid candidate list.", "time": "⏰ From 11:00 AM Onwards", "class": ""},
                {"stage": "Stage 6: Withdrawals", "date": "19.11.2026 (Thursday)", "title": "Withdrawals & Form-VII Publication", "desc": "Notice of withdrawal (Form-V) up to 3 PM. Form-B to EO up to 3 PM. Allotment of symbols & Form-VII.", "time": "⏰ Withdrawal: Up to 3 PM | Form-VII: After 3 PM", "class": ""},
                {"stage": "Stage 7: Poll Day", "date": "26.11.2026 (Thursday)", "title": "Conduct of Poll (Voting)", "desc": "Poll across all 88 Polling Stations using White (Chairperson) and Pink (Ward Member) ballots.", "time": "⏰ 07:00 AM to 05:00 PM", "class": "poll-stage"},
                {"stage": "Stage 8: Re-Poll", "date": "27.11.2026 (Friday)", "title": "Date of Re-poll (If Any)", "desc": "Reserved for any re-poll ordered by APSEC under statutory grounds.", "time": "⏰ 07:00 AM to 05:00 PM", "class": ""},
                {"stage": "Stage 9: Counting", "date": "30.11.2026 (Monday)", "title": "Counting of Votes & Declaration", "desc": "Continuous counting at designated counting centre. Form-XX Part I & II declaration.", "time": "⏰ From 08:00 AM Onwards", "class": "counting-stage"}
            ],
            "timeLimitsTitle": "⏱️ Statutory Time Limits at a Glance (C&DMA VC-23 Ref)"
        },
        "footer": {
            "p1": "Andhra Pradesh State Election Commission — Municipal Ordinary Elections, 2026 (Phase 2)",
            "p2": "Office of the District Election Authority & District Collector, Tirupati | Srikalahasti Municipality",
            "p3": "Statutory References: AP Municipalities Act, 1965 | AP Municipalities (Conduct of Election of Chairpersons & Ward Members) Rules, 2026 | Notification No. 1490/SEC-F1/2026-3"
        }
    },
    "te": {
        "headerTitle": "శ్రీకాళహస్తి పురపాలక సంఘం — 2వ విడత సాధారణ ఎన్నికలు, 2026",
        "headerSubtitle": "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం | జిల్లా ఎన్నికల అధికారి & కలెక్టర్, తిరుపతి జిల్లా",
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
        "tabs": [
            {"id": "tab-schedule", "icon": "📅", "title": "షెడ్యూలు & గడువులు", "badge": ""},
            {"id": "tab-stages", "icon": "🚶", "title": "దశలవారీ మార్గదర్శి", "badge": "9 దశలు"},
            {"id": "tab-checklists", "icon": "✅", "title": "చెక్‌లిస్టులు", "badge": "8 సెట్లు"},
            {"id": "tab-guidelines", "icon": "📌", "title": "ముఖ్య మార్గదర్శకాలు", "badge": ""},
            {"id": "tab-dodont", "icon": "⚖️", "title": "చేయవలసినవి & చేయకూడనివి", "badge": ""},
            {"id": "tab-forms", "icon": "📂", "title": "ఫారాలు & ప్రొఫార్మాలు", "badge": "22 ఫారాలు"},
            {"id": "tab-directory", "icon": "🏛️", "title": "శ్రీకాళహస్తి డైరెక్టరీ", "badge": "88 కేంద్రాలు"},
            {"id": "tab-tools", "icon": "🛠️", "title": "క్షేత్ర సాధనాలు & ప్యాకింగ్", "badge": ""}
        ],
        "sched": {
            "title": "📅 ఎన్నికల కార్యక్రమం & చట్టబద్ధ షెడ్యూలు",
            "sub": "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం (APSEC) చే 2వ విడత పురపాలక సాధారణ ఎన్నికల కొరకు జారీ చేయబడిన సమగ్ర షెడ్యూలు.",
            "timelines": [
                {"stage": "దశ 1: పూర్వ సన్నాహాలు", "date": "14.11.2026 (శనివారం)", "title": "వార్డుల వారీ ఓటర్ల జాబితా ప్రదర్శన", "desc": "రూల్ 5 ప్రకారం ఎన్నికల అధికారి కార్యాలయ నోటీసు బోర్డుపై వార్డుల వారీ ఓటర్ల జాబితాలను ప్రదర్శిస్తారు.", "time": "⏰ ఉదయం 10:00 గంటలకు", "class": ""},
                {"stage": "దశ 2: ఎన్నికల నోటీసు", "date": "14.11.2026 (శనివారం)", "title": "ఎన్నికల నోటీసు ప్రచురణ (ఫారం-1)", "desc": "రూల్ 6 ప్రకారం ఎన్నికల అధికారిచే నిర్దేశిత ఫారంలో ఎన్నికల నోటీసు జారీ చేయబడుతుంది.", "time": "⏰ ఉదయం (నామినేషన్లకు ముందు)", "class": ""},
                {"stage": "దశ 3: నామినేషన్లు", "date": "14.11.2026 నుండి 16.11.2026", "title": "నామినేషన్ల దాఖలు & స్వీకరణ", "desc": "12 నిర్దేశిత ఎన్నికల కార్యాలయాలలో (ఛైర్‌పర్సన్ + 11 వార్డు క్లస్టర్లు) నామినేషన్ల స్వీకరణ.", "time": "⏰ ప్రతిరోజూ ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు", "class": "active-stage"},
                {"stage": "దశ 4: ఆఖరు తేది", "date": "16.11.2026 (సోమవారం)", "title": "నామినేషన్ల ఆఖరు సమయం & ఫారం-A", "desc": "నామినేషన్లకు ఆఖరు గడువు (మధ్యాహ్నం 3 గం). రాజకీయ పార్టీల ఫారం-A జిల్లా కలెక్టర్‌కు సాయంత్రం 5 గం లోపు.", "time": "⏰ మధ్యాహ్నం 3:00 (ఖచ్చితంగా) / సాయంత్రం 5:00 (ఫారం-A)", "class": ""},
                {"stage": "దశ 5: పరిశీలన", "date": "17.11.2026 (మంగళవారం)", "title": "నామినేషన్ల పరిశీలన (స్క్రూటినీ)", "desc": "ఎన్నికల అధికారిచే స్వయంగా న్యాయబద్ధ పరిశీలన. చెల్లుబాటైన అభ్యర్థుల జాబితా (ఫారం-IV) ప్రచురణ.", "time": "⏰ ఉదయం 11:00 గంటల నుండి", "class": ""},
                {"stage": "దశ 6: ఉపసంహరణలు & గుర్తులు", "date": "19.11.2026 (గురువారం)", "title": "ఉపసంహరణ & ఫారం-VII ప్రచురణ", "desc": "అభ్యర్థిత్వాల ఉపసంహరణ (ఫారం-V) మధ్యాహ్నం 3 గం లోపు. గుర్తుల కేటాయింపు & ఫారం-VII ప్రచురణ.", "time": "⏰ ఉపసంహరణ: మధ్యాహ్నం 3:00 లోపు | ఫారం-VII: మధ్యాహ్నం 3:00 తరువాత", "class": ""},
                {"stage": "దశ 7: పోలింగ్ రోజు", "date": "26.11.2026 (గురువారం)", "title": "పోలింగ్ నిర్వహణ (ఓటింగ్)", "desc": "అన్ని 88 పోలింగ్ కేంద్రాలలో తెలుపు (ఛైర్‌పర్సన్) మరియు గులాబీ (వార్డు సభ్యులు) బ్యాలెట్లతో పోలింగ్.", "time": "⏰ ఉదయం 07:00 నుండి సాయంత్రం 05:00 వరకు", "class": "poll-stage"},
                {"stage": "దశ 8: రీ-పోలింగ్", "date": "27.11.2026 (శుక్రవారం)", "title": "రీ-పోలింగ్ తేది (అవసరమైతే)", "desc": "చట్టబద్ధ కారణాలపై రాష్ట్ర ఎన్నికల సంఘం ఆదేశిస్తే నిర్వహించే రీ-పోలింగ్ తేది.", "time": "⏰ ఉదయం 07:00 నుండి సాయంత్రం 05:00 వరకు", "class": ""},
                {"stage": "దశ 9: లెక్కింపు", "date": "30.11.2026 (సోమవారం)", "title": "ఓట్ల లెక్కింపు & ఫలితాల ప్రకటన", "desc": "నిర్దేశిత లెక్కింపు కేంద్రంలో ఓట్ల లెక్కింపు. ఫారం-XX పార్ట్-I & II ద్వారా ఫలితాల ప్రకటన.", "time": "⏰ ఉదయం 08:00 గంటల నుండి", "class": "counting-stage"}
            ],
            "timeLimitsTitle": "⏱️ ముఖ్యమైన చట్టబద్ధ సమయ పరిమితులు (C&DMA నిబంధనలు)"
        },
        "footer": {
            "p1": "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం — పురపాలక సాధారణ ఎన్నికలు, 2026 (2వ విడత)",
            "p2": "జిల్లా ఎన్నికల అధికారి & జిల్లా కలెక్టర్ కార్యాలయం, తిరుపతి | శ్రీకాళహస్తి పురపాలక సంఘం",
            "p3": "చట్టబద్ధ ఆధారాలు: ఎ.పి. మున్సిపాలిటీల చట్టం, 1965 | మున్సిపాలిటీలు/నగర పంచాయతీల ఎన్నికల నిర్వహణ నియమావళి, 2026 | నోటిఫికేషన్ నెం. 1490/SEC-F1/2026-3"
        }
    }
}

print("Base schema populated.")
