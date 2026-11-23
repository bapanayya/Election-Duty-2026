# -*- coding: utf-8 -*-
"""
generate_poll_tracker_html.py
Builds the upgraded, role-based, cumulative auto-calculating Live Hourly Polling Portal (poll-tracker.html).
"""

import json

# 1. Load data
with open('enriched_88_polling_stations.json', encoding='utf-8') as f:
    ps_data = json.load(f)

with open('clusters_data.json', encoding='utf-8') as f:
    clusters_data = json.load(f)

with open('ward_summary.json', encoding='utf-8') as f:
    ward_summary = json.load(f)

with open('po_roster.json', encoding='utf-8') as f:
    po_roster_data = json.load(f)

# Route Officers
route_officers = [
    {"no": 1, "name": "M. Pardha saradhi", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "8686867365", "zone": 1, "wards": "1 to 7", "ps_count": 14},
    {"no": 2, "name": "K. Rajendra", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "7288936923", "zone": 1, "wards": "33 to 37", "ps_count": 10},
    {"no": 3, "name": "N.B. Prabhakar", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "9629297089", "zone": 1, "wards": "40, 41, 43, 44", "ps_count": 7},
    {"no": 4, "name": "Shaik Sulthan Sharief", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "9966011817", "zone": 2, "wards": "38, 39, 40, 42", "ps_count": 7},
    {"no": 5, "name": "B. Sai Prasad", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "9676006961", "zone": 3, "wards": "17, 18, 24, 26, 28, 29, 30", "ps_count": 14},
    {"no": 6, "name": "A. Gireesha", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "8919543675", "zone": 2, "wards": "11, 12, 13, 14", "ps_count": 8},
    {"no": 7, "name": "C. Pramila", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "7036375470", "zone": 2, "wards": "8, 9, 10, 15, 16, 20", "ps_count": 12},
    {"no": 8, "name": "Vinitha", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "7330746514", "zone": 3, "wards": "19, 21, 22, 23, 25", "ps_count": 10},
    {"no": 9, "name": "Chandana", "desig": "Ward Planning & Regulation Secretary", "desig_te": "వార్డు ప్లానింగ్ & రెగ్యులేషన్ కార్యదర్శి", "phone": "8096610523", "zone": 3, "wards": "27, 31, 32", "ps_count": 6}
]

# Zonal Officers
zonal_officers = [
    {"no": 1, "name": "Dr. P. Venugopal", "desig": "Lecturer in Commerce, S.V.A. Govt. College (M)", "desig_te": "వాణిజ్య శాస్త్ర అధ్యాపకులు, ఎస్.వి.ఎ. ప్రభుత్వ పురుషుల కళాశాల", "phone": "9393887222", "routes": [1, 2, 3], "wards": "1-7, 33-37, 40/1, 41, 43, 44", "ps_count": 31},
    {"no": 2, "name": "K. Bhuvaneswari", "desig": "Mandal Education Officer (MEO)", "desig_te": "మండల విద్యాశాఖాధికారి (MEO)", "phone": "9618415439", "alt_phone": "9441592631", "routes": [4, 6, 7], "wards": "8-16, 20, 38, 39, 40/2, 42", "ps_count": 27},
    {"no": 3, "name": "K. Bhagya Lakshmi", "desig": "Supervisor Grade-II, WD&CW Dept", "desig_te": "సూపర్‌వైజర్ గ్రేడ్-II, మహిళా & శిశు సంక్షేమ శాఖ", "phone": "9491000256", "routes": [5, 8, 9], "wards": "17-19, 21-32", "ps_count": 30}
]

ps_json_str = json.dumps(ps_data, ensure_ascii=False)
clusters_json_str = json.dumps(clusters_data, ensure_ascii=False)
routes_json_str = json.dumps(route_officers, ensure_ascii=False)
zones_json_str = json.dumps(zonal_officers, ensure_ascii=False)
wards_json_str = json.dumps(ward_summary, ensure_ascii=False)
po_roster_json_str = json.dumps(po_roster_data, ensure_ascii=False)

html_code = f"""<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>శ్రీకాళహస్తి పురపాలక సంఘం — లైవ్ పోలింగ్ మానిటరింగ్ పోర్టల్ 2026 | Srikalahasti Live Polling Portal</title>
  <link rel="icon" href="Logo-TheCompetitiveEdge.jpg" type="image/jpeg">
  <style>
    :root {{
      --primary: #0b2545;
      --primary-light: #134074;
      --accent: #0284c7;
      --accent-hover: #0369a1;
      --gold: #f59e0b;
      --gold-light: #fef3c7;
      --success: #16a34a;
      --success-bg: #f0fdf4;
      --danger: #dc2626;
      --danger-bg: #fef2f2;
      --warning: #ea580c;
      --warning-bg: #fff7ed;
      --slate-50: #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1e293b;
      --slate-900: #0f172a;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 10px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans Telugu", sans-serif;
    }}

    body {{
      background: #f8fafc;
      color: var(--slate-800);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* HEADER */
    .portal-header {{
      background: linear-gradient(135deg, var(--primary) 0%, #112e51 100%);
      color: #ffffff;
      padding: 0.85rem 1.25rem;
      border-bottom: 3.5px solid var(--gold);
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: var(--shadow-md);
    }}
    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.75rem;
    }}
    .brand-section {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}
    .brand-logo {{
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: #ffffff;
      padding: 2px;
      object-fit: cover;
      box-shadow: 0 0 0 2px var(--gold);
    }}
    .brand-titles h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .live-badge {{
      background: #ef4444;
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 800;
      padding: 0.15rem 0.55rem;
      border-radius: 9999px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      animation: pulse 1.8s infinite;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }}
    .live-badge::before {{
      content: "";
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #ffffff;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.5; }}
    }}
    .brand-titles p {{
      font-size: 0.75rem;
      color: #94a3b8;
      margin-top: 0.1rem;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
      flex-wrap: wrap;
    }}

    /* USER AUTH STATUS PILL */
    .user-auth-pill {{
      background: rgba(255, 255, 255, 0.12);
      border: 1.5px solid rgba(255, 255, 255, 0.25);
      border-radius: 9999px;
      padding: 0.3rem 0.75rem;
      font-size: 0.78rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: #ffffff;
    }}
    .user-auth-role {{
      background: var(--gold);
      color: var(--primary);
      font-weight: 800;
      font-size: 0.7rem;
      padding: 0.1rem 0.45rem;
      border-radius: 9999px;
      text-transform: uppercase;
    }}
    .btn-logout {{
      background: rgba(239, 68, 68, 0.85);
      color: #ffffff;
      border: none;
      border-radius: 4px;
      padding: 0.15rem 0.45rem;
      font-size: 0.7rem;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-logout:hover {{
      background: #dc2626;
    }}

    .header-clock {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 6px;
      padding: 0.35rem 0.65rem;
      font-size: 0.76rem;
      font-weight: 700;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .btn {{
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.18s ease;
      text-decoration: none;
      border: none;
    }}
    .btn-gold {{
      background: var(--gold);
      color: var(--primary);
      font-weight: 800;
    }}
    .btn-gold:hover {{
      background: #d97706;
      color: #ffffff;
    }}
    .btn-outline {{
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}
    .btn-outline:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}
    .btn-primary {{
      background: var(--accent);
      color: #ffffff;
    }}
    .btn-primary:hover {{
      background: var(--accent-hover);
    }}
    .btn-success {{
      background: var(--success);
      color: #ffffff;
    }}
    .btn-success:hover {{
      background: #15803d;
    }}
    .btn-danger {{
      background: var(--danger);
      color: #ffffff;
    }}
    .lang-toggle {{
      display: flex;
      background: rgba(255, 255, 255, 0.12);
      border-radius: 6px;
      padding: 2px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    .lang-btn {{
      padding: 0.25rem 0.55rem;
      font-size: 0.72rem;
      font-weight: 800;
      color: #cbd5e1;
      background: transparent;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }}
    .lang-btn.active {{
      background: var(--gold);
      color: var(--primary);
    }}

    /* MAIN CONTAINER */
    .main-wrapper {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 1.25rem;
      flex: 1;
      width: 100%;
    }}

    /* LOGIN SCREEN MODAL / CARD */
    .login-container {{
      max-width: 650px;
      margin: 2.5rem auto;
      background: #ffffff;
      border: 2px solid var(--primary-light);
      border-radius: 14px;
      padding: 2rem;
      box-shadow: 0 10px 25px rgba(11, 37, 69, 0.12);
    }}
    .login-header {{
      text-align: center;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1.5px solid var(--slate-200);
    }}
    .login-header h2 {{
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--primary);
    }}
    .login-header p {{
      font-size: 0.85rem;
      color: var(--slate-600);
      margin-top: 0.35rem;
    }}
    .quick-chips-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-top: 0.5rem;
    }}
    .quick-chip {{
      background: var(--slate-100);
      border: 1px solid var(--slate-300);
      border-radius: 6px;
      padding: 0.35rem 0.65rem;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      color: var(--slate-700);
      transition: all 0.15s;
    }}
    .quick-chip:hover {{
      background: #e0f2fe;
      border-color: #0284c7;
      color: #0284c7;
    }}

    /* TOP KPI STRIP */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 0.85rem;
      margin-bottom: 1.25rem;
    }}
    .kpi-card {{
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      border-radius: var(--radius);
      padding: 0.9rem 1rem;
      box-shadow: var(--shadow-sm);
      position: relative;
      overflow: hidden;
    }}
    .kpi-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--accent);
    }}
    .kpi-card.kpi-gold::before {{ background: var(--gold); }}
    .kpi-card.kpi-success::before {{ background: var(--success); }}
    .kpi-card.kpi-danger::before {{ background: var(--danger); }}
    .kpi-label {{
      font-size: 0.73rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--slate-500);
      letter-spacing: 0.04em;
    }}
    .kpi-value {{
      font-size: 1.55rem;
      font-weight: 900;
      color: var(--slate-900);
      margin: 0.2rem 0;
      display: flex;
      align-items: baseline;
      gap: 0.35rem;
    }}
    .kpi-sub {{
      font-size: 0.75rem;
      color: var(--slate-600);
    }}

    /* TIME SLOT BAR */
    .slot-bar-card {{
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      border-radius: var(--radius);
      padding: 0.85rem 1.15rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
    }}
    .slot-bar-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .slot-bar-title {{
      font-size: 0.92rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .slot-buttons {{
      display: flex;
      gap: 0.45rem;
      overflow-x: auto;
      padding-bottom: 0.35rem;
    }}
    .slot-btn {{
      background: var(--slate-100);
      border: 1.5px solid var(--slate-200);
      border-radius: 8px;
      padding: 0.55rem 0.85rem;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 110px;
      transition: all 0.18s ease;
    }}
    .slot-btn:hover {{
      background: #e2e8f0;
    }}
    .slot-btn.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 4px 10px rgba(11, 37, 69, 0.25);
    }}
    .slot-btn .slot-time {{
      font-size: 0.92rem;
      font-weight: 900;
    }}
    .slot-btn .slot-label {{
      font-size: 0.68rem;
      opacity: 0.85;
      margin-top: 0.1rem;
    }}
    .slot-btn .slot-pill {{
      margin-top: 0.3rem;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 0.1rem 0.45rem;
      border-radius: 9999px;
      background: rgba(0, 0, 0, 0.08);
    }}
    .slot-btn.active .slot-pill {{
      background: var(--gold);
      color: var(--primary);
    }}

    /* MAIN NAVIGATION TABS */
    .tab-navigation {{
      display: flex;
      gap: 0.5rem;
      border-bottom: 2px solid var(--slate-200);
      margin-bottom: 1.25rem;
      overflow-x: auto;
      padding-bottom: 0.1rem;
    }}
    .tab-btn {{
      background: transparent;
      border: none;
      padding: 0.75rem 1.15rem;
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--slate-600);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      white-space: nowrap;
      transition: all 0.18s;
    }}
    .tab-btn:hover {{
      color: var(--accent);
      background: rgba(2, 132, 199, 0.04);
    }}
    .tab-btn.active {{
      color: var(--primary);
      border-bottom-color: var(--accent);
      background: #ffffff;
      border-top-left-radius: 6px;
      border-top-right-radius: 6px;
    }}
    .tab-badge {{
      font-size: 0.7rem;
      font-weight: 800;
      padding: 0.15rem 0.5rem;
      border-radius: 9999px;
      background: var(--slate-200);
      color: var(--slate-700);
    }}
    .tab-btn.active .tab-badge {{
      background: var(--accent);
      color: #ffffff;
    }}

    /* PANES */
    .tab-pane {{
      display: none;
    }}
    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.25s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* CONTENT CARD */
    .content-card {{
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      border-radius: var(--radius);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
    }}
    .card-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.85rem;
      padding-bottom: 0.65rem;
      border-bottom: 1px solid var(--slate-200);
    }}

    /* FORM STYLES */
    .form-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      margin-bottom: 0.85rem;
    }}
    .form-group label {{
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--slate-700);
    }}
    .form-control {{
      padding: 0.65rem 0.85rem;
      font-size: 0.95rem;
      border: 1.5px solid var(--slate-300);
      border-radius: 8px;
      outline: none;
      width: 100%;
      background: #ffffff;
      transition: border-color 0.18s;
    }}
    .form-control:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }}

    .station-summary-box {{
      background: #f0f9ff;
      border: 1.5px solid #bae6fd;
      border-radius: 10px;
      padding: 1rem 1.25rem;
      margin-bottom: 1.15rem;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.85rem;
    }}
    .summary-item-label {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      color: #0369a1;
    }}
    .summary-item-val {{
      font-size: 0.98rem;
      font-weight: 800;
      color: var(--primary);
      margin-top: 0.15rem;
    }}
    .contact-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      background: #ffffff;
      border: 1px solid #7dd3fc;
      border-radius: 4px;
      padding: 0.2rem 0.5rem;
      font-size: 0.75rem;
      font-weight: 700;
      color: #0284c7;
      text-decoration: none;
      margin-top: 0.25rem;
    }}
    .contact-link:hover {{
      background: #0284c7;
      color: #ffffff;
    }}

    /* CUMULATIVE & SLOT COMPARISON METER */
    .turnout-meter-box {{
      background: #f8fafc;
      border: 1.5px solid var(--slate-200);
      border-radius: 10px;
      padding: 1rem;
      margin-top: 0.75rem;
    }}
    .meter-percentage {{
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--accent);
    }}
    .meter-progress-track {{
      height: 10px;
      background: var(--slate-200);
      border-radius: 9999px;
      overflow: hidden;
      margin: 0.65rem 0;
    }}
    .meter-progress-bar {{
      height: 100%;
      background: linear-gradient(90deg, var(--accent) 0%, var(--success) 100%);
      transition: width 0.3s ease;
      width: 0%;
    }}

    /* TABLES */
    .table-container {{
      overflow-x: auto;
      border-radius: 8px;
      border: 1px solid var(--slate-200);
      background: #ffffff;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: left;
    }}
    .data-table th {{
      background: var(--slate-100);
      color: var(--slate-700);
      font-weight: 800;
      padding: 0.65rem 0.85rem;
      border-bottom: 2px solid var(--slate-200);
      white-space: nowrap;
    }}
    .data-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid var(--slate-200);
      color: var(--slate-800);
    }}
    .data-table tr:hover td {{
      background: #f8fafc;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 800;
    }}
    .badge-success {{ background: var(--success-bg); color: var(--success); border: 1px solid #86efac; }}
    .badge-danger {{ background: var(--danger-bg); color: var(--danger); border: 1px solid #fca5a5; }}
    .badge-neutral {{ background: var(--slate-100); color: var(--slate-600); border: 1px solid var(--slate-200); }}

    /* MODAL */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(15, 23, 42, 0.65);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }}
    .modal-overlay.active {{
      display: flex;
    }}
    .modal-box {{
      background: #ffffff;
      border-radius: 12px;
      max-width: 600px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 1.5rem;
      box-shadow: var(--shadow-lg);
      position: relative;
    }}
    .modal-close {{
      position: absolute;
      top: 1rem;
      right: 1rem;
      font-size: 1.4rem;
      background: none;
      border: none;
      cursor: pointer;
      color: var(--slate-400);
    }}
    .modal-close:hover {{ color: var(--slate-800); }}

    @media print {{
      .portal-header, .slot-bar-card, .tab-navigation, .no-print, .btn, .login-container {{
        display: none !important;
      }}
      body {{ background: #fff; color: #000; }}
      .main-wrapper {{ padding: 0; }}
      .print-header {{ display: block !important; text-align: center; margin-bottom: 1rem; }}
    }}
    .print-header {{ display: none; }}
  </style>
</head>
<body>

  <!-- OFFICIAL HEADER -->
  <header class="portal-header">
    <div class="header-container">
      <div class="brand-section">
        <img src="Logo-TheCompetitiveEdge.jpg" alt="Logo" class="brand-logo" onerror="this.src='https://via.placeholder.com/48/0b2545/ffffff?text=SEC'">
        <div class="brand-titles">
          <h1>
            <span id="txtHeaderTitle">శ్రీకాళహస్తి పురపాలక సంఘం — లైవ్ పోలింగ్ మానిటరింగ్ పోర్టల్</span>
            <span class="live-badge">● LIVE POLLING 2026</span>
          </h1>
          <p id="txtHeaderSub">2వ విడత సాధారణ ఎన్నికలు 2026 | ఎన్నికల & ప్రిసైడింగ్ అధికారుల రియల్-టైమ్ పోలింగ్ డేటా సేకరణ</p>
        </div>
      </div>

      <div class="header-actions">
        <!-- Logged In Identity Pill (Rendered dynamically) -->
        <div id="userAuthDisplay" class="user-auth-pill" style="display: none;">
          <span class="user-auth-role" id="userRoleBadge">EO</span>
          <span id="userNamePhone">Sri K. Shanmugam</span>
          <button class="btn-logout" onclick="logoutUser()" title="లాగౌట్">లాగౌట్</button>
        </div>

        <div class="header-clock" id="liveClock">
          ⏰ <span id="clockText">23.11.2026 11:00:00</span>
        </div>

        <!-- Distinguished Link to Existing Guidance Portal -->
        <a href="index.html" class="btn btn-gold" title="ఎన్నికల అధికారుల మార్గదర్శక పోర్టల్">
          📖 <span id="txtBtnGuidance">మార్గదర్శక పోర్టల్ (Guide)</span>
        </a>

        <div class="lang-toggle">
          <button class="lang-btn active" id="btnLangTe" onclick="setLanguage('te')">తెలుగు</button>
          <button class="lang-btn" id="btnLangEn" onclick="setLanguage('en')">English</button>
        </div>
      </div>
    </div>
  </header>

  <div class="main-wrapper">

    <!-- 1. SIGN IN SCREEN (SHOWN WHEN NOT LOGGED IN) -->
    <div id="loginViewSection" class="login-container" style="display: none;">
      <div class="login-header">
        <div style="font-size: 2.2rem; margin-bottom: 0.35rem;">🔐</div>
        <h2 id="txtLoginTitle">పోలింగ్ పోర్టల్ అధికారిక లాగిన్ (Officer Sign In)</h2>
        <p id="txtLoginSub">మీ అధికారిక మొబైల్ నంబర్‌తో ప్రవేశించి మీ సంబంధిత పోలింగ్ కేంద్రాలను వీక్షించండి</p>
      </div>

      <div class="form-group" style="margin-bottom: 1.25rem;">
        <label for="loginPhoneInput" style="font-size: 0.9rem; font-weight: 800; color: var(--primary);" id="lblLoginMobile">
          📱 10 అంకెల మొబైల్ నంబర్ నమోదు చేయండి:
        </label>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.35rem;">
          <input type="tel" id="loginPhoneInput" class="form-control" placeholder="ఉదా: 8374958749 లేదా 9848000001" maxlength="10" autofocus onkeydown="if(event.key==='Enter') performLogin()">
          <button class="btn btn-primary" style="padding: 0 1.25rem; font-size: 0.95rem; font-weight: 800;" onclick="performLogin()" id="btnLoginSubmit">
            ప్రవేశించండి &rarr;
          </button>
        </div>
        <div id="loginErrorMsg" style="display: none; color: var(--danger); font-size: 0.8rem; font-weight: 700; margin-top: 0.4rem;"></div>
      </div>

      <!-- Quick Demo Login Switcher -->
      <div style="background: var(--slate-50); border: 1px solid var(--slate-200); border-radius: 8px; padding: 1rem; margin-top: 1.25rem;">
        <b style="font-size: 0.82rem; color: var(--slate-700); display: block; margin-bottom: 0.5rem;" id="txtQuickDemoHeader">
          ⚡ త్వరిత డెమో లాగిన్ (Quick Demo Sign-In for Testing):
        </b>
        <div class="quick-chips-grid">
          <button class="quick-chip" onclick="quickLogin('8374958749')">
            🏢 క్లస్టర్ 1 EO: శ్రీ K. షణ్ముగం (8374958749 &bull; వార్డులు 1-4, 8 కేంద్రాలు)
          </button>
          <button class="quick-chip" onclick="quickLogin('9985025035')">
            🏢 క్లస్టర్ 2 EO: డా. B. నాగయ్య (9985025035 &bull; వార్డులు 5-8, 8 కేంద్రాలు)
          </button>
          <button class="quick-chip" onclick="quickLogin('8686867365')">
            🚐 రూట్ 1 అధికారి: M. పార్థసారధి (8686867365 &bull; 14 కేంద్రాలు)
          </button>
          <button class="quick-chip" onclick="quickLogin('9848000001')">
            🏫 ప్రిసైడింగ్ అధికారి PS 1/1 (9848000001 &bull; వార్డు 1)
          </button>
          <button class="quick-chip" onclick="quickLogin('9848000003')">
            🏫 ప్రిసైడింగ్ అధికారి PS 2/1 (9848000003 &bull; వార్డు 2)
          </button>
          <button class="quick-chip" onclick="quickLogin('9999999999')">
            🏛️ కంట్రోల్ రూమ్ / రిటర్నింగ్ అధికారి (9999999999 &bull; అన్ని 88 కేంద్రాలు)
          </button>
        </div>
      </div>

      <div style="margin-top: 1.25rem; font-size: 0.78rem; color: var(--slate-500); line-height: 1.5; border-top: 1px dashed var(--slate-200); padding-top: 0.75rem;">
        <p>• <b>ఎన్నికల అధికారులు (EOs):</b> మీ అధికారిక మొబైల్ నంబర్‌తో ప్రవేశించి మీ పరిధిలోని పోలింగ్ కేంద్రాలను పర్యవేక్షించవచ్చు &amp; ప్రిసైడింగ్ అధికారులకు మొబైల్ నంబర్లను కేటాయించవచ్చు.</p>
        <p>• <b>ప్రిసైడింగ్ అధికారులు (POs):</b> మీ ఎన్నికల అధికారి కేటాయించిన మొబైల్ నంబర్‌తో లాగిన్ అయి మీ పోలింగ్ కేంద్రం వివరాలను మాత్రమే చూడవచ్చు &amp; గంటవారీ ఓట్ల వివరాలను నమోదు చేయవచ్చు.</p>
      </div>
    </div>

    <!-- 2. AUTHENTICATED PORTAL CONTENT -->
    <div id="authenticatedPortalSection" style="display: none;">

      <!-- TOP KPI RIBBON (CUMULATIVE METRICS AUTO-CALCULATED) -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-label" id="kpiLabelElectors">పరిధిలోని మొత్తం ఓటర్లు</div>
          <div class="kpi-value" id="kpiTotalElectors">72,537</div>
          <div class="kpi-sub" id="kpiSubElectors">నమోదైన ఓటర్ల సంఖ్య</div>
        </div>

        <div class="kpi-card kpi-success">
          <div class="kpi-label" id="kpiLabelPolled">సంచిత పోలైన ఓట్లు (Cumulative)</div>
          <div class="kpi-value" id="kpiTotalPolled">0</div>
          <div class="kpi-sub" id="kpiSubPolled">⚡ ఆటో-క్యాలిక్యులేట్ మొత్తం</div>
        </div>

        <div class="kpi-card kpi-gold">
          <div class="kpi-label" id="kpiLabelTurnout">సంచిత పోలింగ్ శాతం (%)</div>
          <div class="kpi-value" id="kpiTurnoutPct">0.00%</div>
          <div class="kpi-sub" id="kpiSubTurnout">⚡ ఆటో-క్యాలిక్యులేట్ శాతం</div>
        </div>

        <div class="kpi-card kpi-purple">
          <div class="kpi-label" id="kpiLabelReported">రిపోర్ట్ చేసిన కేంద్రాలు</div>
          <div class="kpi-value" id="kpiReportedCount">0 / 88</div>
          <div class="kpi-sub" id="kpiSubReported">0 పెండింగ్ ఉన్నాయి</div>
        </div>

        <div class="kpi-card">
          <div class="kpi-label" id="kpiLabelGender">సంచిత పురుషులు / మహిళలు</div>
          <div class="kpi-value" style="font-size: 1.15rem;" id="kpiGenderVal">M: 0 | F: 0</div>
          <div class="kpi-sub" id="kpiSubGender">TG / ఇతరులు: 0</div>
        </div>
      </div>

      <!-- TIME SLOT SELECTOR BAR -->
      <div class="slot-bar-card no-print">
        <div class="slot-bar-header">
          <div class="slot-bar-title">
            <span>⏰</span>
            <span id="txtSlotBarTitle">పోలింగ్ రిపోర్టింగ్ సమయం ఎంచుకోండి (Select Reporting Hour):</span>
          </div>
          <div style="display: flex; gap: 0.5rem; align-items: center;">
            <span style="font-size: 0.78rem; font-weight: 700; color: var(--slate-600);" id="txtSlotActiveStatus">ప్రస్తుత సమయం:</span>
            <span class="badge badge-success" id="badgeActiveSlot">11:00 AM రిపోర్ట్</span>
          </div>
        </div>
        <div class="slot-buttons" id="slotButtonsContainer">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- NAVIGATION TABS -->
      <div class="tab-navigation no-print" id="roleTabNavigation">
        <!-- Rendered based on user role -->
      </div>

      <!-- VIEW A: PRESIDING OFFICER VIEW (STRICTLY FOR ASSIGNED PO) -->
      <div class="tab-pane" id="pane-po-self">
        <div class="content-card" style="border-top: 4px solid var(--accent);">
          <div class="card-title">
            <span>📱</span>
            <span id="txtPOSelfHeader">నా పోలింగ్ కేంద్రం డేటా నమోదు (Presiding Officer Data Entry)</span>
          </div>

          <!-- STATION DETAILS BANNER -->
          <div class="station-summary-box" id="poStationInfoBox">
            <div>
              <div class="summary-item-label">పోలింగ్ కేంద్రం &amp; వార్డు</div>
              <div class="summary-item-val" id="poSelfPS">PS 1/1 &bull; వార్డు 1</div>
              <div style="font-size: 0.8rem; color: #0284c7; margin-top: 0.2rem;" id="poSelfBuilding">Municipal Primary School</div>
            </div>
            <div>
              <div class="summary-item-label">మొత్తం ఓటర్లు</div>
              <div class="summary-item-val" style="color: #0369a1;" id="poSelfVoters">710 ఓటర్లు</div>
              <div style="font-size: 0.75rem; color: #64748b;" id="poSelfRes">రిజర్వేషన్</div>
            </div>
            <div>
              <div class="summary-item-label">బాధ్యత రూట్ అధికారి</div>
              <div class="summary-item-val" style="font-size: 0.9rem;" id="poSelfRouteOfficer">-</div>
              <a href="#" class="contact-link" id="poSelfRouteCall">📞 కాల్ చేయండి</a>
            </div>
            <div>
              <div class="summary-item-label">క్లస్టర్ ఎన్నికల అధికారి (EO)</div>
              <div class="summary-item-val" style="font-size: 0.9rem;" id="poSelfClusterEO">-</div>
              <a href="#" class="contact-link" id="poSelfClusterCall">📞 కాల్ చేయండి</a>
            </div>
          </div>

          <!-- INPUT FORM WITH AUTO-FILL TOTAL & CUMULATIVE AUTO-CALCULATE -->
          <div style="background: #ffffff; border: 1.5px solid var(--slate-200); border-radius: 10px; padding: 1.15rem; margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 0.85rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--slate-200);">
              <h3 style="font-size: 1rem; font-weight: 800; color: var(--primary); display: flex; align-items: center; gap: 0.4rem;">
                <span>🗳️</span>
                <span>గంటవారీ పోలింగ్ సంఖ్య నమోదు (రిపోర్ట్ సమయం: <b id="poFormActiveHourLabel" style="color: var(--accent);">11:00 AM</b>)</span>
              </h3>
              <span class="badge badge-neutral" id="poFormStationBadge">PS 1/1</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
              <div class="form-group">
                <label for="poInputMale">👨 <b>ప్రస్తుత గంటలో పురుషుల ఓట్లు (Male Votes):</b></label>
                <input type="number" id="poInputMale" class="form-control" placeholder="0" min="0" oninput="calculatePOFormCounts()">
              </div>

              <div class="form-group">
                <label for="poInputFemale">👩 <b>ప్రస్తుత గంటలో మహిళల ఓట్లు (Female Votes):</b></label>
                <input type="number" id="poInputFemale" class="form-control" placeholder="0" min="0" oninput="calculatePOFormCounts()">
              </div>

              <div class="form-group">
                <label for="poInputTG">⚧️ <b>ఇతరులు / TG (Third Gender):</b></label>
                <input type="number" id="poInputTG" class="form-control" placeholder="0" min="0" oninput="calculatePOFormCounts()">
              </div>
            </div>

            <!-- DUAL VIEW: THIS HOUR AUTO-FILL VS CUMULATIVE AUTO-CALCULATE -->
            <div class="turnout-meter-box">
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; text-align: center;">
                
                <!-- Box 1: This Hour / Slot Auto-Fill -->
                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 0.85rem;">
                  <div style="font-size: 0.72rem; color: var(--slate-500); font-weight: 800; text-transform: uppercase;">
                    ⚡ ఈ గంటలో పోలైనవి (This Hour Auto-Fill)
                  </div>
                  <div style="font-size: 1.7rem; font-weight: 900; color: var(--slate-800); margin: 0.2rem 0;" id="poSlotCalculatedTotal">0</div>
                  <div style="font-size: 0.78rem; font-weight: 700; color: #0284c7;" id="poSlotCalculatedPct">0.00% టర్నవుట్</div>
                  <div style="font-size: 0.7rem; color: var(--slate-400); margin-top: 0.2rem;">పురుషులు + మహిళలు + ఇతరులు</div>
                </div>

                <!-- Box 2: Cumulative Polled Auto-Calculate -->
                <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 0.85rem;">
                  <div style="font-size: 0.72rem; color: #166534; font-weight: 800; text-transform: uppercase;">
                    ⚡ సంచిత మొత్తం పోలింగ్ (Cumulative Auto-Calculate)
                  </div>
                  <div style="font-size: 1.9rem; font-weight: 900; color: #166534; margin: 0.2rem 0;" id="poCumCalculatedTotal">0</div>
                  <div style="font-size: 0.82rem; font-weight: 800; color: #15803d;" id="poCumCalculatedPct">0.00% సంచిత శాతం</div>
                  <div style="font-size: 0.7rem; color: #166534; margin-top: 0.2rem;" id="poCumGenderBreakdown">M: 0 | F: 0 | TG: 0</div>
                </div>

              </div>

              <!-- PROGRESS BAR FOR CUMULATIVE TURNOUT -->
              <div style="margin-top: 0.85rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-weight: 700; color: var(--slate-600); margin-bottom: 0.2rem;">
                  <span>సంచిత పురోగతి (Cumulative Progress):</span>
                  <span id="poLiveProgressLabel">0 / 710 ఓటర్లు</span>
                </div>
                <div class="meter-progress-track">
                  <div class="meter-progress-bar" id="poLiveProgressBar"></div>
                </div>
              </div>

              <div id="poValidationAlert" style="display: none; color: var(--danger); font-size: 0.82rem; font-weight: 700; margin-top: 0.4rem;">
                ⚠️ హెచ్చరిక: సంచిత మొత్తం ఓట్లు నమోదైన ఓటర్ల కంటే ఎక్కువగా ఉన్నాయి! దయచేసి సంఖ్యలను సరిచూడండి.
              </div>
            </div>

            <!-- QUEUE & STATUS -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
              <div class="form-group">
                <label for="poQueueStatus">⏳ ప్రస్తుత క్యూ పరిస్థితి (Queue Status):</label>
                <select id="poQueueStatus" class="form-control">
                  <option value="nil">క్యూ లేదు (No Queue)</option>
                  <option value="1-15">1 నుండి 15 మంది ఓటర్లు (1-15 Voters)</option>
                  <option value="15-30" selected>15 నుండి 30 మంది ఓటర్లు (15-30 Voters)</option>
                  <option value="30+">30 మంది కంటే ఎక్కువ (30+ Voters)</option>
                </select>
              </div>

              <div class="form-group">
                <label for="poLawStatus">🛡️ పోలింగ్ వాతావరణం (Status):</label>
                <select id="poLawStatus" class="form-control">
                  <option value="peaceful" selected>ప్రశాంతంగా సాగుతోంది (Peaceful)</option>
                  <option value="minor_issue">చిన్న సమస్య - పరిష్కరించబడింది</option>
                  <option value="heavy_rush">విపరీతమైన రద్దీ ఉంది (Heavy Rush)</option>
                  <option value="material">సామగ్రి / బ్యాలెట్ పేపర్లు అవసరం</option>
                </select>
              </div>
            </div>

            <!-- BUTTONS -->
            <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem;">
              <button class="btn btn-success" style="padding: 0.65rem 1.25rem; font-size: 0.95rem;" onclick="savePOFormData()">
                💾 డేటాను భద్రపరచండి (Save Hourly Data)
              </button>
              <button class="btn btn-primary" style="padding: 0.65rem 1.25rem; font-size: 0.95rem; background: #25d366;" onclick="sharePOWhatsApp()">
                📲 ఎన్నికల అధికారికి వాట్సాప్ నివేదిక (Send WhatsApp)
              </button>
              <button class="btn btn-outline" style="color: var(--slate-700); border-color: var(--slate-300);" onclick="copyPOReportText()">
                📋 టెక్స్ట్ కాపీ చేయండి (Copy Text)
              </button>
            </div>

            <div id="poSaveSuccessAlert" style="display: none; background: #f0fdf4; border: 1px solid #86efac; color: #166534; padding: 0.75rem 1rem; border-radius: 8px; margin-top: 1rem; font-weight: 700;">
              ✅ గంటవారీ &amp; సంచిత వివరాలు విజయవంతంగా నమోదయ్యాయి! సెంట్రల్ మానిటరింగ్ సిస్టమ్‌లో అప్‌డేట్ అయ్యాయి.
            </div>
          </div>

          <!-- STATION TIMELINE LEDGER WITH CUMULATIVE AUTO-CALCULATED COLUMNS -->
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>రిపోర్ట్ సమయం</th>
                  <th>ఈ గంటలో పురుషులు</th>
                  <th>ఈ గంటలో మహిళలు</th>
                  <th>ఈ గంట మొత్తం (Auto-Fill)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత పురుషులు (Cum M)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత మహిళలు (Cum F)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత మొత్తం (Cum Total)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత శాతం (Cum %)</th>
                  <th>క్యూ స్థితి</th>
                  <th>నమోదైన సమయం</th>
                </tr>
              </thead>
              <tbody id="poStationHistoryTbody">
                <!-- Rendered by JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- VIEW B: ELECTION OFFICER / JURISDICTION VIEW (CONCERNED STATIONS ONLY) -->
      <div class="tab-pane" id="pane-eo-stations">
        <div class="content-card">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.85rem; padding-bottom: 0.65rem; border-bottom: 1px solid var(--slate-200);">
            <div class="card-title" style="margin: 0; padding: 0; border: none;">
              <span>🏢</span>
              <span id="txtEOConcernedTitle">నా పరిధిలోని పోలింగ్ కేంద్రాలు (My Concerned Polling Stations)</span>
            </div>
            <span class="badge badge-neutral" id="badgeEOJurisdictionMeta">క్లస్టర్ 1 &bull; 8 కేంద్రాలు</span>
          </div>

          <p style="font-size: 0.82rem; color: var(--slate-600); margin-bottom: 1rem;">
            ఎన్నికల అధికారిగా మీ పరిధిలోని పోలింగ్ కేంద్రాల వివరాలు క్రింద ఇవ్వబడ్డాయి. ఈ పట్టికలో ఆయా గంటల వారీగా పోలైన ఓట్లు మరియు <b>సంచిత మొత్తం (Cumulative Polling Data)</b> ఆటో-క్యాలిక్యులేట్ అయి కనిపిస్తాయి.
          </p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>క్రమ నెం</th>
                  <th>వార్డు</th>
                  <th>కేంద్రం నెం</th>
                  <th>పాఠశాల / భవనం పేరు</th>
                  <th>మొత్తం ఓటర్లు</th>
                  <th>ప్రిసైడింగ్ అధికారి (PO ఫోన్)</th>
                  <th>ఈ గంట పోలింగ్ (M+F)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత పురుషులు</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత మహిళలు</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత మొత్తం (Cum Total)</th>
                  <th style="background: #f0fdf4; color: #166534;">సంచిత శాతం (Cum %)</th>
                  <th>స్థితి</th>
                  <th>చర్యలు</th>
                </tr>
              </thead>
              <tbody id="eoConcernedTableBody">
                <!-- Rendered by JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- VIEW C: PO MOBILE REGISTRATION TOOL (FOR EOS TO ASSIGN PO NUMBERS) -->
      <div class="tab-pane" id="pane-eo-po-roster">
        <div class="content-card">
          <div class="card-title">
            <span>👥</span>
            <span>ప్రిసైడింగ్ అధికారుల మొబైల్ నంబర్ల కేటాయింపు &amp; నమోదు (PO Mobile Registration)</span>
          </div>
          <p style="font-size: 0.82rem; color: var(--slate-600); margin-bottom: 1rem;">
            మీ పరిధిలోని పోలింగ్ కేంద్రాల ప్రిసైడింగ్ అధికారుల పేర్లు &amp; మొబైల్ నంబర్లను ఇక్కడ కేటాయించండి/సవరించండి. మీరు నమోదు చేసిన మొబైల్ నంబర్‌తోనే ఆ ప్రిసైడింగ్ అధికారి పోర్టల్‌లోకి లాగిన్ అయి తమ పోలింగ్ కేంద్రం డేటాను నమోదు చేసుకోగలరు.
          </p>

          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>క్రమ నెం</th>
                  <th>వార్డు</th>
                  <th>కేంద్రం నెం</th>
                  <th>భవనం / ప్రదేశం</th>
                  <th>ఓటర్లు</th>
                  <th>ప్రస్తుత PO పేరు</th>
                  <th>కేటాయించిన PO మొబైల్ నంబర్</th>
                  <th>చర్యలు</th>
                </tr>
              </thead>
              <tbody id="eoAssignPOTableBody">
                <!-- Rendered by JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- VIEW D: PENDING STATIONS DESK -->
      <div class="tab-pane" id="pane-pending-desk">
        <div class="content-card" style="border-top: 4px solid var(--danger);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.85rem; padding-bottom: 0.65rem; border-bottom: 1px solid var(--slate-200);">
            <div class="card-title" style="margin: 0; padding: 0; border: none;">
              <span>⚠️</span>
              <span>పెండింగ్ కేంద్రాల ఫాలో-అప్ (Pending Follow-Up)</span>
            </div>
            <span class="badge badge-danger" id="badgePendingCountJurisdiction">0 పెండింగ్ ఉన్నాయి</span>
          </div>

          <div id="pendingJurisdictionContainer">
            <!-- Rendered by JS -->
          </div>
        </div>
      </div>

      <!-- VIEW E: STATUTORY BULLETINS & EXPORTS -->
      <div class="tab-pane" id="pane-bulletin">
        <div class="content-card">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
            <div class="card-title" style="margin: 0; padding: 0; border: none;">
              <span>📑</span>
              <span>అధికారిక గంటవారీ పోలింగ్ బులెటిన్ &amp; నివేదికలు</span>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;" class="no-print">
              <button class="btn btn-primary" onclick="window.print()">🖨️ బులెటిన్ ప్రింట్</button>
              <button class="btn btn-success" onclick="exportDataToCSV()">📥 CSV డౌన్‌లోడ్</button>
              <button class="btn btn-gold" onclick="copyBulletinPressText()">📋 మీడియా సారాంశం కాపీ</button>
            </div>
          </div>

          <div style="background: #ffffff; border: 2px solid var(--slate-300); border-radius: 8px; padding: 1.5rem; font-family: serif; color: #000;" id="bulletinPrintArea">
            <div style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 0.75rem; margin-bottom: 1rem;">
              <h2 style="font-size: 1.3rem; margin: 0; font-weight: bold;">ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం | STATE ELECTION COMMISSION</h2>
              <h3 style="font-size: 1.1rem; margin: 0.2rem 0; font-weight: bold;">జిల్లా ఎన్నికల అధికారి &amp; కలెక్టర్, తిరుపతి జిల్లా</h3>
              <h4 style="font-size: 1rem; margin: 0.2rem 0; text-decoration: underline;" id="bulletinHeadingSlot">శ్రీకాళహస్తి పురపాలక సంఘం — 2వ విడత సాధారణ ఎన్నికలు 2026: 11:00 AM పోలింగ్ సరళి బులెటిన్</h4>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.75rem; background: #f8fafc; border: 1px solid #cbd5e1; padding: 0.75rem; margin-bottom: 1rem; font-size: 0.85rem; text-align: center;">
              <div><b>పరిధిలోని ఓటర్లు:</b><br><span id="bMetaElectors">72,537</span></div>
              <div><b>సంచిత పోలైన ఓట్లు:</b><br><span id="bMetaPolled">0</span></div>
              <div><b>సంచిత పోలింగ్ శాతం:</b><br><b style="font-size: 1.1rem; color: #0284c7;" id="bMetaPct">0.00%</b></div>
              <div><b>రిపోర్ట్ కేంద్రాలు:</b><br><span id="bMetaReported">0 / 88</span></div>
            </div>

            <div class="table-container" style="border: 1px solid #000;">
              <table class="data-table" style="font-size: 0.8rem;">
                <thead>
                  <tr style="background: #e2e8f0; color: #000; border-bottom: 2px solid #000;">
                    <th>కేంద్రం</th>
                    <th>వార్డు</th>
                    <th>పాఠశాల పేరు</th>
                    <th>మొత్తం ఓటర్లు</th>
                    <th>సంచిత పురుషులు</th>
                    <th>సంచిత మహిళలు</th>
                    <th>సంచిత మొత్తం (Auto)</th>
                    <th>సంచిత శాతం (%) (Auto)</th>
                  </tr>
                </thead>
                <tbody id="bulletinTableBody">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

    </div> <!-- /authenticatedPortalSection -->

  </div> <!-- /main-wrapper -->

  <!-- MODAL: EDIT PO MOBILE NUMBER (USED BY EO) -->
  <div class="modal-overlay" id="editPOMobileModal">
    <div class="modal-box">
      <button class="modal-close" onclick="closeEditPOModal()">&times;</button>
      <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--primary); margin-bottom: 0.4rem;">
        ప్రిసైడింగ్ అధికారి మొబైల్ నంబర్ కేటాయింపు
      </h3>
      <p style="font-size: 0.8rem; color: var(--slate-600); margin-bottom: 1rem;" id="modalEditPOSub">
        వార్డు &bull; కేంద్రం నంబర్
      </p>

      <input type="hidden" id="modalEditPOSL">

      <div class="form-group">
        <label for="modalEditPOName">ప్రిసైడింగ్ అధికారి పేరు (PO Name):</label>
        <input type="text" id="modalEditPOName" class="form-control">
      </div>

      <div class="form-group">
        <label for="modalEditPOPhone">10 అంకెల మొబైల్ నంబర్ (10-Digit Mobile Number):</label>
        <input type="tel" id="modalEditPOPhone" class="form-control" maxlength="10">
        <span style="font-size: 0.72rem; color: var(--slate-500); margin-top: 0.2rem;">
          ఈ నంబర్‌తోనే ప్రిసైడింగ్ అధికారి పోర్టల్‌లోకి లాగిన్ అయి డేటా నమోదు చేయగలరు.
        </span>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 0.5rem; margin-top: 1rem;">
        <button class="btn btn-outline" style="color: var(--slate-700); border-color: var(--slate-300);" onclick="closeEditPOModal()">రద్దు (Cancel)</button>
        <button class="btn btn-success" onclick="saveEditedPOMobile()">💾 భద్రపరచండి (Save Mobile)</button>
      </div>
    </div>
  </div>

  <!-- MODAL: QUICK UPDATE FOR EO -->
  <div class="modal-overlay" id="quickUpdateModal">
    <div class="modal-box">
      <button class="modal-close" onclick="closeQuickModal()">&times;</button>
      <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--primary); margin-bottom: 0.4rem;" id="modalStationTitle">
        కేంద్రం వివరాల సత్వర నమోదు (Quick Station Update)
      </h3>
      <p style="font-size: 0.8rem; color: var(--slate-600); margin-bottom: 1rem;" id="modalStationSub"></p>

      <input type="hidden" id="modalTargetSL">

      <div class="form-group">
        <label for="modalSelectSlot">రిపోర్ట్ సమయం (Reporting Hour):</label>
        <select id="modalSelectSlot" class="form-control" onchange="onModalSlotChanged()">
          <option value="09:00">09:00 AM రిపోర్ట్</option>
          <option value="11:00">11:00 AM రిపోర్ట్</option>
          <option value="13:00">01:00 PM రిపోర్ట్</option>
          <option value="15:00">03:00 PM రిపోర్ట్</option>
          <option value="17:00">05:00 PM రిపోర్ట్</option>
          <option value="close">పోలింగ్ ముగింపు (Close of Poll)</option>
        </select>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; margin-bottom: 1rem;">
        <div class="form-group">
          <label for="modalMale">పురుషులు:</label>
          <input type="number" id="modalMale" class="form-control" min="0" oninput="calcModalTurnout()">
        </div>
        <div class="form-group">
          <label for="modalFemale">మహిళలు:</label>
          <input type="number" id="modalFemale" class="form-control" min="0" oninput="calcModalTurnout()">
        </div>
        <div class="form-group">
          <label for="modalTG">ఇతరులు:</label>
          <input type="number" id="modalTG" class="form-control" min="0" oninput="calcModalTurnout()">
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid var(--slate-200); border-radius: 6px; padding: 0.75rem; text-align: center; margin-bottom: 1rem;">
        <span style="font-size: 0.82rem; color: var(--slate-600);">ఈ గంట పోలైనవి: <b id="modalSlotTotalVal">0</b> | సంచిత మొత్తం: <b id="modalCumTotalVal" style="color: #166534;">0</b></span>
        <div style="font-size: 1.4rem; font-weight: 900; color: var(--accent); margin-top: 0.2rem;" id="modalTurnoutVal">0.00%</div>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 0.5rem;">
        <button class="btn btn-outline" style="color: var(--slate-700); border-color: var(--slate-300);" onclick="closeQuickModal()">రద్దు (Cancel)</button>
        <button class="btn btn-success" onclick="saveModalData()">💾 భద్రపరచండి (Save)</button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT MASTER APPLICATION -->
  <script>
    const POLLING_STATIONS = {ps_json_str};
    const ROUTE_OFFICERS = {routes_json_str};
    const ZONAL_OFFICERS = {zones_json_str};
    const CLUSTERS_DATA = {clusters_json_str};
    const WARD_SUMMARY = {wards_json_str};
    const DEFAULT_PO_ROSTER = {po_roster_json_str};

    const TIME_SLOTS = [
      {{ id: "07:00", label_en: "07:00 AM", label_te: "ఉదయం 07:00", desc_en: "Poll Start & Mock Poll", desc_te: "పోలింగ్ ప్రారంభం" }},
      {{ id: "09:00", label_en: "09:00 AM", label_te: "ఉదయం 09:00", desc_en: "1st Hourly Report", desc_te: "1వ గంటవారీ నివేదిక" }},
      {{ id: "11:00", label_en: "11:00 AM", label_te: "ఉదయం 11:00", desc_en: "2nd Hourly Report", desc_te: "2వ గంటవారీ నివేదిక" }},
      {{ id: "13:00", label_en: "01:00 PM", label_te: "మధ్యాహ్నం 01:00", desc_en: "3rd Hourly Report", desc_te: "3వ గంటవారీ నివేదిక" }},
      {{ id: "15:00", label_en: "03:00 PM", label_te: "మధ్యాహ్నం 03:00", desc_en: "4th Hourly Report", desc_te: "4వ గంటవారీ నివేదిక" }},
      {{ id: "17:00", label_en: "05:00 PM", label_te: "సాయంత్రం 05:00", desc_en: "5th Hourly Report & Queue", desc_te: "5వ గంటవారీ నివేదిక" }},
      {{ id: "close", label_en: "Close of Poll", label_te: "పోలింగ్ ముగింపు", desc_en: "Final Turnout & Form-XVIII", desc_te: "తుది పోలింగ్ లెక్క" }}
    ];

    // APPLICATION STATE
    let currentLang = 'te';
    let activeSlot = '11:00';
    let pollDataStore = {{}};
    let poRosterStore = [];
    let currentUser = null; // {{ role: 'PO' | 'CLUSTER_EO' | 'ROUTE_OFFICER' | 'ADMIN', phone, name, ... }}

    window.addEventListener('DOMContentLoaded', () => {{
      loadRosterAndPollData();
      checkAuthSession();
      startLiveClock();
    }});

    function loadRosterAndPollData() {{
      // Load PO Roster
      try {{
        const rawRoster = localStorage.getItem('SRIKALAHASTI_PO_ROSTER_2026');
        if (rawRoster) {{
          poRosterStore = JSON.parse(rawRoster);
        }} else {{
          poRosterStore = JSON.parse(JSON.stringify(DEFAULT_PO_ROSTER));
          savePORoster();
        }}
      }} catch (e) {{
        poRosterStore = JSON.parse(JSON.stringify(DEFAULT_PO_ROSTER));
      }}

      // Load Poll Data
      try {{
        const rawData = localStorage.getItem('SRIKALAHASTI_HOURLY_POLL_2026');
        if (rawData) {{
          pollDataStore = JSON.parse(rawData);
        }} else {{
          pollDataStore = {{}};
          seedInitialSimulation();
        }}
      }} catch (e) {{
        pollDataStore = {{}};
      }}
    }}

    function savePORoster() {{
      localStorage.setItem('SRIKALAHASTI_PO_ROSTER_2026', JSON.stringify(poRosterStore));
    }}

    function savePollData() {{
      localStorage.setItem('SRIKALAHASTI_HOURLY_POLL_2026', JSON.stringify(pollDataStore));
    }}

    function seedInitialSimulation() {{
      // Seed slots 9 AM and 11 AM
      POLLING_STATIONS.forEach(ps => {{
        if (!pollDataStore[ps.sl]) pollDataStore[ps.sl] = {{}};
        
        // 9 AM
        const m9 = Math.round(ps.voters * 0.09);
        const f9 = Math.round(ps.voters * 0.095);
        pollDataStore[ps.sl]['09:00'] = {{
          male: m9,
          female: f9,
          tg: 0,
          total: m9 + f9,
          queue: '10-20',
          incident: 'peaceful',
          updated_at: 'Initial'
        }};

        // 11 AM
        const m11 = Math.round(ps.voters * 0.12);
        const f11 = Math.round(ps.voters * 0.125);
        pollDataStore[ps.sl]['11:00'] = {{
          male: m11,
          female: f11,
          tg: 0,
          total: m11 + f11,
          queue: '15-30',
          incident: 'peaceful',
          updated_at: 'Initial'
        }};
      }});
      savePollData();
    }}

    function startLiveClock() {{
      const el = document.getElementById('clockText');
      function tick() {{
        const now = new Date();
        const d = String(now.getDate()).padStart(2, '0');
        const m = String(now.getMonth() + 1).padStart(2, '0');
        const y = now.getFullYear();
        const hrs = String(now.getHours()).padStart(2, '0');
        const mins = String(now.getMinutes()).padStart(2, '0');
        const secs = String(now.getSeconds()).padStart(2, '0');
        if (el) el.textContent = `${{d}}.${{m}}.${{y}} ${{hrs}}:${{mins}}:${{secs}}`;
      }}
      tick();
      setInterval(tick, 1000);
    }}

    // -------------------------------------------------------------
    // CUMULATIVE AUTO-CALCULATION UTILITY FUNCTIONS
    // -------------------------------------------------------------
    // Given a polling station sl and targetSlotId, calculates the cumulative total votes
    // across all slots up to and including targetSlotId
    function calculateCumulativeForStation(sl, targetSlotId) {{
      const rec = pollDataStore[sl] || {{}};
      let cumMale = 0;
      let cumFemale = 0;
      let cumTG = 0;
      let cumTotal = 0;
      let hasAnyReport = false;

      for (let s of TIME_SLOTS) {{
        const d = rec[s.id];
        if (d && d.total > 0) {{
          hasAnyReport = true;
          cumMale += (d.male || 0);
          cumFemale += (d.female || 0);
          cumTG += (d.tg || 0);
          cumTotal += d.total;
        }}
        if (s.id === targetSlotId) break;
      }}

      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      const electors = ps ? ps.voters : 0;
      const cumPct = electors > 0 ? ((cumTotal / electors) * 100).toFixed(2) : '0.00';

      return {{
        cumMale,
        cumFemale,
        cumTG,
        cumTotal,
        cumPct,
        hasAnyReport
      }};
    }}

    // -------------------------------------------------------------
    // AUTHENTICATION LOGIC (MOBILE NUMBER BASED ACCESS)
    // -------------------------------------------------------------
    function checkAuthSession() {{
      const savedAuth = sessionStorage.getItem('SRIKALAHASTI_AUTH_SESSION');
      if (savedAuth) {{
        try {{
          currentUser = JSON.parse(savedAuth);
          onUserAuthenticated();
          return;
        }} catch(e) {{}}
      }}
      showLoginView();
    }}

    function showLoginView() {{
      document.getElementById('loginViewSection').style.display = 'block';
      document.getElementById('authenticatedPortalSection').style.display = 'none';
      document.getElementById('userAuthDisplay').style.display = 'none';
    }}

    function performLogin() {{
      const input = document.getElementById('loginPhoneInput');
      const err = document.getElementById('loginErrorMsg');
      const phone = (input.value || '').trim().replace(/[^0-9]/g, '');

      if (!phone || phone.length < 10) {{
        err.textContent = 'దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్‌ను నమోదు చేయండి.';
        err.style.display = 'block';
        return;
      }}

      authenticateByPhone(phone);
    }}

    function quickLogin(phone) {{
      document.getElementById('loginPhoneInput').value = phone;
      authenticateByPhone(phone);
    }}

    function authenticateByPhone(phone) {{
      const err = document.getElementById('loginErrorMsg');
      err.style.display = 'none';

      // 1. Admin / RO
      if (phone === '9999999999' || phone === '9848012345') {{
        currentUser = {{
          role: 'ADMIN',
          name: 'కంట్రోల్ రూమ్ & ఎన్నికల రిటర్నింగ్ అధికారి (RO Master)',
          phone: phone,
          jurisdiction_label: 'అన్ని 88 పోలింగ్ కేంద్రాలు (44 వార్డులు)'
        }};
        finalizeLogin();
        return;
      }}

      // 2. Cluster Election Officers (12 Clusters)
      const clusterMatch = CLUSTERS_DATA.find(c => {{
        return (c.eo && c.eo.phone === phone) || 
               (c.addl_eo && c.addl_eo.phone === phone) || 
               (c.aeo && c.aeo.phone === phone);
      }});

      if (clusterMatch) {{
        const clusterPS = POLLING_STATIONS.filter(p => p.cluster === clusterMatch.sl).map(p => p.sl);
        currentUser = {{
          role: 'CLUSTER_EO',
          name: clusterMatch.eo ? clusterMatch.eo.name : 'ఎన్నికల అధికారి',
          phone: phone,
          cluster_sl: clusterMatch.sl,
          wards: clusterMatch.wards,
          ps_list: clusterPS,
          jurisdiction_label: `క్లస్టర్ ${{clusterMatch.sl}} (వార్డులు ${{clusterMatch.wards}} &bull; ${{clusterPS.length}} కేంద్రాలు)`
        }};
        finalizeLogin();
        return;
      }}

      // 3. Route Officers (9 Routes)
      const routeMatch = ROUTE_OFFICERS.find(r => r.phone === phone);
      if (routeMatch) {{
        const routePS = POLLING_STATIONS.filter(p => p.route === routeMatch.no).map(p => p.sl);
        currentUser = {{
          role: 'ROUTE_OFFICER',
          name: routeMatch.name,
          phone: phone,
          route_no: routeMatch.no,
          wards: routeMatch.wards,
          ps_list: routePS,
          jurisdiction_label: `రూట్ ${{routeMatch.no}} అధికారి (వార్డులు ${{routeMatch.wards}} &bull; ${{routePS.length}} కేంద్రాలు)`
        }};
        finalizeLogin();
        return;
      }}

      // 4. Presiding Officers Roster
      const poMatch = poRosterStore.find(p => p.po_phone === phone);
      if (poMatch) {{
        const psObj = POLLING_STATIONS.find(x => x.sl === poMatch.sl);
        currentUser = {{
          role: 'PO',
          name: poMatch.po_name,
          phone: phone,
          station_sl: poMatch.sl,
          ps_no: poMatch.ps_no,
          ward: poMatch.ward,
          ps_details: psObj ? psObj.details : '',
          jurisdiction_label: `PS ${{poMatch.ps_no}} (వార్డు ${{poMatch.ward}})`
        }};
        finalizeLogin();
        return;
      }}

      err.textContent = `మొబైల్ నంబర్ (${{phone}}) ఇంకా ఏ పోలింగ్ కేంద్రానికీ రిజిస్టర్ కాలేదు. దయచేసి మీ సంబంధిత క్లస్టర్ ఎన్నికల అధికారి (EO) ని సంప్రదించి నంబర్‌ను కేటాయించుకోండి.`;
      err.style.display = 'block';
    }}

    function finalizeLogin() {{
      sessionStorage.setItem('SRIKALAHASTI_AUTH_SESSION', JSON.stringify(currentUser));
      onUserAuthenticated();
    }}

    function logoutUser() {{
      sessionStorage.removeItem('SRIKALAHASTI_AUTH_SESSION');
      currentUser = null;
      showLoginView();
    }}

    function onUserAuthenticated() {{
      document.getElementById('loginViewSection').style.display = 'none';
      document.getElementById('authenticatedPortalSection').style.display = 'block';

      // Header status pill
      const authPill = document.getElementById('userAuthDisplay');
      authPill.style.display = 'flex';
      document.getElementById('userRoleBadge').textContent = currentUser.role === 'PO' ? 'PO' : (currentUser.role === 'ADMIN' ? 'RO' : 'EO');
      document.getElementById('userNamePhone').innerHTML = `<b>${{currentUser.name}}</b> (${{currentUser.jurisdiction_label}})`;

      buildRoleTabs();
      renderSlotButtons();
      updateViewsForRole();
    }}

    function buildRoleTabs() {{
      const nav = document.getElementById('roleTabNavigation');
      nav.innerHTML = '';

      if (currentUser.role === 'PO') {{
        nav.innerHTML = `
          <button class="tab-btn active" data-tab="pane-po-self" onclick="switchRoleTab('pane-po-self')">
            <span>📱</span>
            <span>నా పోలింగ్ కేంద్రం డేటా నమోదు (My Station Entry)</span>
            <span class="tab-badge">PS ${{currentUser.ps_no}}</span>
          </button>
        `;
      }} else {{
        nav.innerHTML = `
          <button class="tab-btn active" data-tab="pane-eo-stations" onclick="switchRoleTab('pane-eo-stations')">
            <span>🏢</span>
            <span>నా పరిధిలోని పోలింగ్ కేంద్రాలు (Concerned Polling Stations)</span>
            <span class="tab-badge" id="tabBadgeConcernedCount">${{currentUser.ps_list ? currentUser.ps_list.length : 88}} PS</span>
          </button>
          <button class="tab-btn" data-tab="pane-eo-po-roster" onclick="switchRoleTab('pane-eo-po-roster')">
            <span>👥</span>
            <span>ప్రిసైడింగ్ అధికారుల మొబైల్ నమోదు (PO Mobile Registration)</span>
          </button>
          <button class="tab-btn" data-tab="pane-pending-desk" onclick="switchRoleTab('pane-pending-desk')">
            <span>⚠️</span>
            <span>పెండింగ్ కేంద్రాలు (Pending Follow-Up)</span>
            <span class="tab-badge" id="tabBadgePendingJurisdiction" style="background: var(--danger); color: #fff;">0</span>
          </button>
          <button class="tab-btn" data-tab="pane-bulletin" onclick="switchRoleTab('pane-bulletin')">
            <span>📑</span>
            <span>అధికారిక బులెటిన్ &amp; నివేదికలు (Bulletins &amp; CSV)</span>
          </button>
        `;
      }}
    }}

    function switchRoleTab(tabId) {{
      document.querySelectorAll('#roleTabNavigation .tab-btn').forEach(b => {{
        if (b.getAttribute('data-tab') === tabId) b.classList.add('active');
        else b.classList.remove('active');
      }});

      document.querySelectorAll('.tab-pane').forEach(p => {{
        if (p.id === tabId) p.classList.add('active');
        else p.classList.remove('active');
      }});
    }}

    function selectSlot(slotId) {{
      activeSlot = slotId;
      renderSlotButtons();
      updateViewsForRole();
    }}

    function renderSlotButtons() {{
      const container = document.getElementById('slotButtonsContainer');
      if (!container) return;
      container.innerHTML = '';

      TIME_SLOTS.forEach(slot => {{
        const btn = document.createElement('button');
        btn.className = `slot-btn ${{slot.id === activeSlot ? 'active' : ''}}`;
        btn.onclick = () => selectSlot(slot.id);

        let repCount = 0;
        let totalCount = 0;

        const psSubset = (currentUser && currentUser.ps_list) 
          ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
          : (currentUser && currentUser.station_sl ? POLLING_STATIONS.filter(p => p.sl === currentUser.station_sl) : POLLING_STATIONS);

        totalCount = psSubset.length;
        psSubset.forEach(ps => {{
          const rec = pollDataStore[ps.sl];
          if (rec && rec[slot.id] && rec[slot.id].total > 0) repCount++;
        }});

        btn.innerHTML = `
          <span class="slot-time">${{currentLang === 'te' ? slot.label_te : slot.label_en}}</span>
          <span class="slot-label">${{currentLang === 'te' ? slot.desc_te : slot.desc_en}}</span>
          <span class="slot-pill">${{repCount}}/${{totalCount}} రిపోర్ట్</span>
        `;
        container.appendChild(btn);
      }});

      const activeObj = TIME_SLOTS.find(s => s.id === activeSlot);
      const badge = document.getElementById('badgeActiveSlot');
      if (badge && activeObj) {{
        badge.textContent = `${{activeObj.label_te}} (${{activeObj.desc_te}})`;
      }}
    }}

    function updateViewsForRole() {{
      if (!currentUser) return;

      if (currentUser.role === 'PO') {{
        switchRoleTab('pane-po-self');
        renderPOFormView();
      }} else {{
        switchRoleTab('pane-eo-stations');
        renderEOConcernedView();
        renderEOPORosterView();
        renderEOPendingView();
        renderEOBulletinView();
      }}
      renderJurisdictionKPIs();
    }}

    // JURISDICTION CUMULATIVE KPIS (AUTO-CALCULATED)
    function renderJurisdictionKPIs() {{
      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : (currentUser.station_sl ? POLLING_STATIONS.filter(p => p.sl === currentUser.station_sl) : POLLING_STATIONS);

      let totalElectors = 0;
      let cumTotalPolled = 0;
      let cumTotalMale = 0;
      let cumTotalFemale = 0;
      let cumTotalTG = 0;
      let reportedCount = 0;

      psSubset.forEach(ps => {{
        totalElectors += ps.voters;
        const cumData = calculateCumulativeForStation(ps.sl, activeSlot);
        if (cumData.cumTotal > 0) {{
          reportedCount++;
          cumTotalPolled += cumData.cumTotal;
          cumTotalMale += cumData.cumMale;
          cumTotalFemale += cumData.cumFemale;
          cumTotalTG += cumData.cumTG;
        }}
      }});

      const turnoutPct = totalElectors > 0 ? ((cumTotalPolled / totalElectors) * 100).toFixed(2) : '0.00';

      document.getElementById('kpiTotalElectors').textContent = totalElectors.toLocaleString();
      document.getElementById('kpiTotalPolled').textContent = cumTotalPolled.toLocaleString();
      document.getElementById('kpiTurnoutPct').textContent = `${{turnoutPct}}%`;
      document.getElementById('kpiReportedCount').textContent = `${{reportedCount}} / ${{psSubset.length}}`;
      document.getElementById('kpiSubReported').textContent = `${{psSubset.length - reportedCount}} పెండింగ్ ఉన్నాయి`;

      document.getElementById('kpiGenderVal').textContent = `M: ${{cumTotalMale.toLocaleString()}} | F: ${{cumTotalFemale.toLocaleString()}}`;
      document.getElementById('kpiSubGender').textContent = `TG / ఇతరులు: ${{cumTotalTG.toLocaleString()}}`;

      const badgePending = document.getElementById('badgePendingCountJurisdiction');
      if (badgePending) badgePending.textContent = `${{psSubset.length - reportedCount}} పెండింగ్ ఉన్నాయి`;
      const tabBadgePending = document.getElementById('tabBadgePendingJurisdiction');
      if (tabBadgePending) tabBadgePending.textContent = `${{psSubset.length - reportedCount}}`;
    }}

    // -------------------------------------------------------------
    // PRESIDING OFFICER (PO) FORM VIEW & CUMULATIVE AUTO-CALCULATE
    // -------------------------------------------------------------
    function renderPOFormView() {{
      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      const routeObj = ROUTE_OFFICERS.find(r => r.no === ps.route) || {{}};
      const clusterObj = CLUSTERS_DATA.find(c => c.sl === ps.cluster) || {{}};
      const wardSum = WARD_SUMMARY.find(w => w.ward === ps.ward);

      document.getElementById('poSelfPS').textContent = `PS ${{ps.ps_no}} &bull; వార్డు ${{ps.ward}}`;
      document.getElementById('poSelfBuilding').textContent = ps.details;
      document.getElementById('poSelfVoters').textContent = `${{ps.voters}} ఓటర్లు`;
      document.getElementById('poSelfRes').textContent = wardSum ? wardSum.res_name : 'General';

      document.getElementById('poSelfRouteOfficer').textContent = `${{routeObj.name}} (రూట్ ${{ps.route}})`;
      document.getElementById('poSelfRouteCall').href = `tel:${{routeObj.phone}}`;
      document.getElementById('poSelfRouteCall').textContent = `📞 ${{routeObj.phone}} కి కాల్`;

      document.getElementById('poSelfClusterEO').textContent = clusterObj.eo ? `${{clusterObj.eo.name}} (క్లస్టర్ ${{ps.cluster}})` : '-';
      document.getElementById('poSelfClusterCall').href = `tel:${{clusterObj.eo ? clusterObj.eo.phone : ''}}`;

      document.getElementById('poFormActiveHourLabel').textContent = activeSlot;
      document.getElementById('poFormStationBadge').textContent = `PS ${{ps.ps_no}}`;

      // Load inputs for active hour
      const rec = pollDataStore[sl] || {{}};
      const slotData = rec[activeSlot] || {{}};

      document.getElementById('poInputMale').value = slotData.male || '';
      document.getElementById('poInputFemale').value = slotData.female || '';
      document.getElementById('poInputTG').value = slotData.tg || '';
      document.getElementById('poQueueStatus').value = slotData.queue || '15-30';
      document.getElementById('poLawStatus').value = slotData.incident || 'peaceful';

      calculatePOFormCounts();
      renderPOStationTimeline();
    }}

    function calculatePOFormCounts() {{
      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      // Inputs for THIS slot
      const male = parseInt(document.getElementById('poInputMale').value) || 0;
      const female = parseInt(document.getElementById('poInputFemale').value) || 0;
      const tg = parseInt(document.getElementById('poInputTG').value) || 0;
      const slotTotal = male + female + tg;

      // 1. AUTO-FILL THIS SLOT TOTAL & PERCENTAGE
      document.getElementById('poSlotCalculatedTotal').textContent = slotTotal.toLocaleString();
      const slotPct = ps.voters > 0 ? ((slotTotal / ps.voters) * 100).toFixed(2) : '0.00';
      document.getElementById('poSlotCalculatedPct').textContent = `${{slotPct}}% టర్నవుట్`;

      // 2. AUTO-CALCULATE CUMULATIVE DATA (SUM OF PREVIOUS SLOTS + THIS SLOT)
      let cumMale = 0;
      let cumFemale = 0;
      let cumTG = 0;
      let cumTotal = 0;

      for (let s of TIME_SLOTS) {{
        if (s.id === activeSlot) {{
          // Add currently typed values
          cumMale += male;
          cumFemale += female;
          cumTG += tg;
          cumTotal += slotTotal;
          break;
        }} else {{
          // Add previously saved slot data
          const rec = pollDataStore[sl] || {{}};
          const prevD = rec[s.id];
          if (prevD && prevD.total > 0) {{
            cumMale += (prevD.male || 0);
            cumFemale += (prevD.female || 0);
            cumTG += (prevD.tg || 0);
            cumTotal += prevD.total;
          }}
        }}
      }}

      // Display Auto-Calculated Cumulative Metrics
      document.getElementById('poCumCalculatedTotal').textContent = cumTotal.toLocaleString();
      const cumPct = ps.voters > 0 ? ((cumTotal / ps.voters) * 100).toFixed(2) : '0.00';
      document.getElementById('poCumCalculatedPct').textContent = `${{cumPct}}% సంచిత పోలింగ్`;
      document.getElementById('poCumGenderBreakdown').textContent = `M: ${{cumMale}} | F: ${{cumFemale}} | TG: ${{cumTG}}`;

      // Update Cumulative Progress Bar
      document.getElementById('poLiveProgressLabel').textContent = `${{cumTotal.toLocaleString()}} / ${{ps.voters.toLocaleString()}} ఓటర్లు (${{cumPct}}%)`;
      document.getElementById('poLiveProgressBar').style.width = `${{Math.min(parseFloat(cumPct), 100)}}%`;

      const alertEl = document.getElementById('poValidationAlert');
      if (cumTotal > ps.voters) {{
        alertEl.style.display = 'block';
      }} else {{
        alertEl.style.display = 'none';
      }}
    }}

    function savePOFormData() {{
      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      const male = parseInt(document.getElementById('poInputMale').value) || 0;
      const female = parseInt(document.getElementById('poInputFemale').value) || 0;
      const tg = parseInt(document.getElementById('poInputTG').value) || 0;
      const total = male + female + tg;

      if (!pollDataStore[sl]) pollDataStore[sl] = {{}};
      pollDataStore[sl][activeSlot] = {{
        male, female, tg, total,
        queue: document.getElementById('poQueueStatus').value,
        incident: document.getElementById('poLawStatus').value,
        updated_at: new Date().toLocaleTimeString()
      }};

      savePollData();
      renderSlotButtons();
      renderJurisdictionKPIs();
      renderPOStationTimeline();

      const success = document.getElementById('poSaveSuccessAlert');
      success.style.display = 'block';
      setTimeout(() => {{ success.style.display = 'none'; }}, 3000);
    }}

    function sharePOWhatsApp() {{
      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      const male = parseInt(document.getElementById('poInputMale').value) || 0;
      const female = parseInt(document.getElementById('poInputFemale').value) || 0;
      const tg = parseInt(document.getElementById('poInputTG').value) || 0;
      const total = male + female + tg;
      const cum = calculateCumulativeForStation(sl, activeSlot);
      const queue = document.getElementById('poQueueStatus').value;
      const routeObj = ROUTE_OFFICERS.find(r => r.no === ps.route) || {{}};

      const msg = `🏛️ *శ్రీకాళహస్తి పురపాలక ఎన్నికలు 2026*%0A` +
        `📊 *గంటవారీ &amp; సంచిత పోలింగ్ నివేదిక - ${{activeSlot}}*%0A` +
        `━━━━━━━━━━━━━━━━━━━━━%0A` +
        `📍 వార్డు: ${{ps.ward}} | PS No: ${{ps.ps_no}}%0A` +
        `🏫 భవనం: ${{encodeURIComponent(ps.details)}}%0A` +
        `👥 మొత్తం ఓటర్లు: ${{ps.voters}}%0A` +
        `━━━━━━━━━━━━━━━━━━━━━%0A` +
        `*ఈ గంటలో పోలైనవి (This Slot):*%0A` +
        `🗳️ పురుషులు: ${{male}} | మహిళలు: ${{female}} | TG: ${{tg}}%0A` +
        `⚡ ఈ గంట మొత్తం: *${{total}}*%0A` +
        `━━━━━━━━━━━━━━━━━━━━━%0A` +
        `*సంచిత మొత్తం (Cumulative - Auto-Calculated):*%0A` +
        `👨 సంచిత పురుషులు: *${{cum.cumMale}}*%0A` +
        `👩 సంచిత మహిళలు: *${{cum.cumFemale}}*%0A` +
        `✅ *సంచిత మొత్తం ఓట్లు: ${{cum.cumTotal}} (${{cum.cumPct}}%)*%0A` +
        `⏳ క్యూ: ${{queue}}%0A` +
        `━━━━━━━━━━━━━━━━━━━━━%0A` +
        `ప్రిసైడింగ్ అధికారి PS ${{ps.ps_no}}`;

      const url = `https://wa.me/91${{routeObj.phone}}?text=${{msg}}`;
      window.open(url, '_blank');
    }}

    function copyPOReportText() {{
      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      const male = parseInt(document.getElementById('poInputMale').value) || 0;
      const female = parseInt(document.getElementById('poInputFemale').value) || 0;
      const tg = parseInt(document.getElementById('poInputTG').value) || 0;
      const total = male + female + tg;
      const cum = calculateCumulativeForStation(sl, activeSlot);

      const txt = `SRIKALAHASTI MUNICIPAL ELECTIONS 2026\\n` +
        `HOURLY & CUMULATIVE POLL REPORT: ${{activeSlot}}\\n` +
        `Ward: ${{ps.ward}} | PS: ${{ps.ps_no}}\\n` +
        `Location: ${{ps.details}}\\n` +
        `Electors: ${{ps.voters}}\\n\\n` +
        `THIS SLOT POLLED: Male: ${{male}}, Female: ${{female}}, TG: ${{tg}} (Total: ${{total}})\\n` +
        `CUMULATIVE POLLED (Auto): Male: ${{cum.cumMale}}, Female: ${{cum.cumFemale}}, TG: ${{cum.cumTG}}\\n` +
        `CUMULATIVE TOTAL: ${{cum.cumTotal}} / ${{ps.voters}} (${{cum.cumPct}}%)\\n\\n` +
        `Presiding Officer PS ${{ps.ps_no}}`;

      navigator.clipboard.writeText(txt).then(() => {{
        alert('గంటవారీ & సంచిత పోలింగ్ నివేదిక టెక్స్ట్ కాపీ చేయబడింది!');
      }});
    }}

    function renderPOStationTimeline() {{
      const tbody = document.getElementById('poStationHistoryTbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const sl = currentUser.station_sl;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      const rec = pollDataStore[sl] || {{}};

      let runningMale = 0;
      let runningFemale = 0;
      let runningTG = 0;
      let runningTotal = 0;

      TIME_SLOTS.forEach(slot => {{
        const d = rec[slot.id];
        const has = d && d.total > 0;

        if (has) {{
          runningMale += (d.male || 0);
          runningFemale += (d.female || 0);
          runningTG += (d.tg || 0);
          runningTotal += d.total;
        }}

        const tr = document.createElement('tr');
        const cumPct = (runningTotal > 0 && ps.voters > 0) ? ((runningTotal / ps.voters) * 100).toFixed(2) + '%' : '-';

        tr.innerHTML = `
          <td><b>${{slot.label_te}}</b> (${{slot.desc_te}})</td>
          <td>${{has ? d.male : '-'}}</td>
          <td>${{has ? d.female : '-'}}</td>
          <td><b>${{has ? d.total : '-'}}</b></td>
          <td style="background: #f0fdf4; font-weight: 700; color: #166534;">${{has ? runningMale : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 700; color: #166534;">${{has ? runningFemale : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 900; color: #166534;">${{has ? runningTotal : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 900; color: #15803d;">${{has ? cumPct : '-'}}</td>
          <td>${{has ? (d.queue || '-') : '-'}}</td>
          <td><span style="font-size: 0.72rem; color: var(--slate-500);">${{has ? (d.updated_at || 'నమోదైంది') : 'పెండింగ్'}}</span></td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // -------------------------------------------------------------
    // ELECTION OFFICER (EO) VIEW: CONCERNED STATIONS & CUMULATIVE DATA
    // -------------------------------------------------------------
    function renderEOConcernedView() {{
      const tbody = document.getElementById('eoConcernedTableBody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : POLLING_STATIONS;

      document.getElementById('badgeEOJurisdictionMeta').textContent = currentUser.jurisdiction_label;

      psSubset.forEach(ps => {{
        const rec = pollDataStore[ps.sl] || {{}};
        const slotData = rec[activeSlot];
        const hasSlotData = slotData && slotData.total > 0;

        // Auto-calculated Cumulative Metrics for this Station
        const cum = calculateCumulativeForStation(ps.sl, activeSlot);

        const poInfo = poRosterStore.find(p => p.sl === ps.sl) || {{ po_name: 'PO', po_phone: '-' }};

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${{ps.sl}}</td>
          <td><b>వార్డు ${{ps.ward}}</b></td>
          <td><span class="badge badge-neutral">${{ps.ps_no}}</span></td>
          <td style="max-width: 220px; font-size: 0.78rem;">${{ps.details}}</td>
          <td><b>${{ps.voters}}</b></td>
          <td>
            <div style="font-size: 0.78rem;">
              <b>${{poInfo.po_name}}</b><br>
              <a href="tel:${{poInfo.po_phone}}" style="color: #0284c7; font-weight: 700; text-decoration: none;">📞 ${{poInfo.po_phone}}</a>
              <button class="btn btn-outline" style="padding: 0.1rem 0.4rem; font-size: 0.65rem; margin-left: 0.3rem;" onclick="openEditPOModal(${{ps.sl}})" title="PO మొబైల్ మార్చండి">✏️</button>
            </div>
          </td>
          <td><b>${{hasSlotData ? slotData.total : '-'}}</b> <span style="font-size: 0.7rem; color: var(--slate-500);">${{hasSlotData ? `(M:${{slotData.male}} F:${{slotData.female}})` : ''}}</span></td>
          <td style="background: #f0fdf4; font-weight: 700; color: #166534;">${{cum.hasAnyReport ? cum.cumMale : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 700; color: #166534;">${{cum.hasAnyReport ? cum.cumFemale : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 900; color: #166534; font-size: 0.95rem;">${{cum.hasAnyReport ? cum.cumTotal : '-'}}</td>
          <td style="background: #f0fdf4; font-weight: 900; color: #15803d; font-size: 0.95rem;">${{cum.hasAnyReport ? cum.cumPct + '%' : '0.0%'}}</td>
          <td>
            ${{hasSlotData ? '<span class="badge badge-success">✅ నమోదైంది</span>' : '<span class="badge badge-danger">⏳ పెండింగ్</span>'}}
          </td>
          <td>
            <div style="display: flex; gap: 0.3rem;">
              <button class="btn btn-primary" style="padding: 0.2rem 0.5rem; font-size: 0.72rem;" onclick="openQuickModal(${{ps.sl}})">✏️ నమోదు</button>
              <a href="tel:${{poInfo.po_phone}}" class="btn btn-outline" style="padding: 0.2rem 0.45rem; font-size: 0.72rem; color: #0284c7;">📞</a>
              <button class="btn btn-success" style="padding: 0.2rem 0.45rem; font-size: 0.72rem;" onclick="sendPOWhatsAppDirect('${{poInfo.po_phone}}', '${{ps.ps_no}}', ${{ps.ward}})">📲</button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function sendPOWhatsAppDirect(phone, psNo, ward) {{
      const msg = `*ఎన్నికల అధికారి కార్యాలయం, శ్రీకాళహస్తి పురపాలక సంఘం*%0A%0Aగౌరవ ప్రిసైడింగ్ అధికారి గారికి (వార్డు ${{ward}}, PS ${{psNo}}),%0Aదయచేసి *${{activeSlot}}* గంటవారీ పోలింగ్ ఓట్ల వివరాలను పోర్టల్‌లో వెంటనే అప్‌డేట్ చేయగలరు.%0A%0Aధన్యవాదాలు.`;
      const url = `https://wa.me/91${{phone}}?text=${{msg}}`;
      window.open(url, '_blank');
    }}

    // PO ROSTER MANAGER (FOR EOS TO ASSIGN PO NUMBERS)
    function renderEOPORosterView() {{
      const tbody = document.getElementById('eoAssignPOTableBody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : POLLING_STATIONS;

      psSubset.forEach(ps => {{
        const poInfo = poRosterStore.find(p => p.sl === ps.sl) || {{ po_name: `PO PS ${{ps.ps_no}}`, po_phone: '' }};
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${{ps.sl}}</td>
          <td><b>వార్డు ${{ps.ward}}</b></td>
          <td><span class="badge badge-neutral">${{ps.ps_no}}</span></td>
          <td style="max-width: 250px; font-size: 0.78rem;">${{ps.details}}</td>
          <td>${{ps.voters}}</td>
          <td><b>${{poInfo.po_name}}</b></td>
          <td><b style="color: #0284c7; font-size: 0.95rem;">${{poInfo.po_phone || 'కేటాయించలేదు'}}</b></td>
          <td>
            <button class="btn btn-outline" style="font-size: 0.75rem; padding: 0.25rem 0.65rem; color: #0284c7; border-color: #7dd3fc;" onclick="openEditPOModal(${{ps.sl}})">
              ✏️ మొబైల్ మార్చండి (Edit Mobile)
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function openEditPOModal(sl) {{
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;
      const poInfo = poRosterStore.find(p => p.sl === sl) || {{ po_name: `PO PS ${{ps.ps_no}}`, po_phone: '' }};

      document.getElementById('modalEditPOSL').value = sl;
      document.getElementById('modalEditPOSub').textContent = `వార్డు ${{ps.ward}} &bull; పోలింగ్ కేంద్రం ${{ps.ps_no}} (${{ps.details}})`;
      document.getElementById('modalEditPOName').value = poInfo.po_name;
      document.getElementById('modalEditPOPhone').value = poInfo.po_phone;

      document.getElementById('editPOMobileModal').classList.add('active');
    }}

    function closeEditPOModal() {{
      document.getElementById('editPOMobileModal').classList.remove('active');
    }}

    function saveEditedPOMobile() {{
      const sl = parseInt(document.getElementById('modalEditPOSL').value);
      const name = document.getElementById('modalEditPOName').value.trim();
      const phone = document.getElementById('modalEditPOPhone').value.trim().replace(/[^0-9]/g, '');

      if (!phone || phone.length < 10) {{
        alert('దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్‌ను నమోదు చేయండి.');
        return;
      }}

      let idx = poRosterStore.findIndex(p => p.sl === sl);
      if (idx !== -1) {{
        poRosterStore[idx].po_name = name || poRosterStore[idx].po_name;
        poRosterStore[idx].po_phone = phone;
      }} else {{
        poRosterStore.push({{ sl, po_name: name, po_phone: phone }});
      }}

      savePORoster();
      closeEditPOModal();
      renderEOConcernedView();
      renderEOPORosterView();
      alert(`✅ పోలింగ్ కేంద్రం ${{sl}} ప్రిసైడింగ్ అధికారి మొబైల్ నంబర్ (${{phone}}) విజయవంతంగా భద్రపరచబడింది! ఇకపై ఆ అధికారి ఈ నంబర్‌తో లాగిన్ కావచ్చు.`);
    }}

    // PENDING DESK FOR EO
    function renderEOPendingView() {{
      const container = document.getElementById('pendingJurisdictionContainer');
      if (!container) return;
      container.innerHTML = '';

      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : POLLING_STATIONS;

      const pending = psSubset.filter(ps => {{
        const rec = pollDataStore[ps.sl];
        return !(rec && rec[activeSlot] && rec[activeSlot].total > 0);
      }});

      if (pending.length === 0) {{
        container.innerHTML = `
          <div style="background: #f0fdf4; border: 2px solid #86efac; border-radius: 10px; padding: 2rem; text-align: center; color: #166534;">
            <div style="font-size: 2.2rem; margin-bottom: 0.35rem;">🎉</div>
            <h3 style="font-size: 1.15rem; font-weight: 800;">అభినందనలు! మీ పరిధిలోని అన్ని కేంద్రాల నుండి డేటా అందింది!</h3>
            <p style="font-size: 0.85rem; margin-top: 0.35rem;">ఎంచుకున్న సమయానికి (${{activeSlot}}) ఎలాంటి పెండింగ్ కేంద్రాలు లేవు.</p>
          </div>
        `;
        return;
      }}

      const grid = document.createElement('div');
      grid.style.cssText = `display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 0.85rem;`;

      pending.forEach(ps => {{
        const poInfo = poRosterStore.find(p => p.sl === ps.sl) || {{ po_name: 'PO', po_phone: '-' }};
        const card = document.createElement('div');
        card.style.cssText = `background: #ffffff; border: 1.5px solid #fecdd3; border-radius: 8px; padding: 1rem;`;
        card.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.4rem;">
            <div>
              <span class="badge badge-danger">⏳ పెండింగ్ (${{activeSlot}})</span>
              <h4 style="font-size: 1rem; font-weight: 800; color: var(--primary); margin: 0.2rem 0 0 0;">
                వార్డు ${{ps.ward}} &bull; PS ${{ps.ps_no}}
              </h4>
            </div>
            <span style="font-size: 0.78rem; font-weight: 800; color: #0284c7;">${{ps.voters}} ఓటర్లు</span>
          </div>
          <p style="font-size: 0.78rem; color: var(--slate-600); margin-bottom: 0.65rem;">🏫 ${{ps.details}}</p>
          <div style="background: #f8fafc; border: 1px solid var(--slate-200); border-radius: 6px; padding: 0.5rem; font-size: 0.75rem; margin-bottom: 0.75rem;">
            <b>ప్రిసైడింగ్ అధికారి:</b> ${{poInfo.po_name}}<br>
            <b>ఫోన్ నంబర్:</b> ${{poInfo.po_phone}}
          </div>
          <div style="display: flex; gap: 0.35rem; flex-wrap: wrap;">
            <a href="tel:${{poInfo.po_phone}}" class="btn btn-outline" style="font-size: 0.72rem; padding: 0.25rem 0.5rem; color: #0284c7; border-color: #7dd3fc;">📞 కాల్</a>
            <button class="btn btn-success" style="font-size: 0.72rem; padding: 0.25rem 0.5rem;" onclick="sendPOWhatsAppDirect('${{poInfo.po_phone}}', '${{ps.ps_no}}', ${{ps.ward}})">📲 వాట్సాప్</button>
            <button class="btn btn-primary" style="font-size: 0.72rem; padding: 0.25rem 0.5rem;" onclick="openQuickModal(${{ps.sl}})">✏️ నమోదు</button>
          </div>
        `;
        grid.appendChild(card);
      }});

      container.appendChild(grid);
    }}

    // BULLETIN VIEW FOR EO WITH CUMULATIVE NUMBERS
    function renderEOBulletinView() {{
      const bTitle = document.getElementById('bulletinHeadingSlot');
      const bSlot = TIME_SLOTS.find(s => s.id === activeSlot);
      const slotLabel = bSlot ? bSlot.label_en : activeSlot;
      if (bTitle) bTitle.textContent = `శ్రీకాళహస్తి పురపాలక ఎన్నికలు 2026: ${{slotLabel}} పోలింగ్ బులెటిన్ (${{currentUser.jurisdiction_label}})`;

      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : POLLING_STATIONS;

      let totalElectors = 0;
      let cumTotalPolled = 0;
      let repCount = 0;

      const tbody = document.getElementById('bulletinTableBody');
      if (tbody) tbody.innerHTML = '';

      psSubset.forEach(ps => {{
        totalElectors += ps.voters;
        const cum = calculateCumulativeForStation(ps.sl, activeSlot);
        if (cum.hasAnyReport) {{
          repCount++;
          cumTotalPolled += cum.cumTotal;
        }}

        if (tbody) {{
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><b>PS ${{ps.ps_no}}</b></td>
            <td>వార్డు ${{ps.ward}}</td>
            <td style="font-size: 0.75rem;">${{ps.details}}</td>
            <td>${{ps.voters}}</td>
            <td style="font-weight: 700;">${{cum.hasAnyReport ? cum.cumMale : '-'}}</td>
            <td style="font-weight: 700;">${{cum.hasAnyReport ? cum.cumFemale : '-'}}</td>
            <td><b style="color: #166534;">${{cum.hasAnyReport ? cum.cumTotal : '-'}}</b></td>
            <td><b style="color: #15803d;">${{cum.hasAnyReport ? cum.cumPct + '%' : '-'}}</b></td>
          `;
          tbody.appendChild(tr);
        }}
      }});

      const overallPct = totalElectors > 0 ? ((cumTotalPolled / totalElectors) * 100).toFixed(2) : '0.00';
      document.getElementById('bMetaElectors').textContent = totalElectors.toLocaleString();
      document.getElementById('bMetaPolled').textContent = cumTotalPolled.toLocaleString();
      document.getElementById('bMetaPct').textContent = `${{overallPct}}%`;
      document.getElementById('bMetaReported').textContent = `${{repCount}} / ${{psSubset.length}}`;
    }}

    function exportDataToCSV() {{
      const psSubset = (currentUser.ps_list) 
        ? POLLING_STATIONS.filter(p => currentUser.ps_list.includes(p.sl))
        : POLLING_STATIONS;

      let csv = "Sl,Ward,PS_No,Location,Electors,PO_Name,PO_Phone,Hour,Slot_Male,Slot_Female,Slot_Total,Cum_Male,Cum_Female,Cum_Total,Cum_Turnout_Pct\\n";

      psSubset.forEach(ps => {{
        const rec = pollDataStore[ps.sl] || {{}};
        const poInfo = poRosterStore.find(p => p.sl === ps.sl) || {{ po_name: '', po_phone: '' }};
        TIME_SLOTS.forEach(slot => {{
          const d = rec[slot.id] || {{}};
          const male = d.male || 0;
          const female = d.female || 0;
          const total = d.total || 0;
          const cum = calculateCumulativeForStation(ps.sl, slot.id);
          const loc = `"${{ps.details.replace(/"/g, '""')}}"`;
          csv += `${{ps.sl}},${{ps.ward}},${{ps.ps_no}},${{loc}},${{ps.voters}},"${{poInfo.po_name}}",${{poInfo.po_phone}},${{slot.id}},${{male}},${{female}},${{total}},${{cum.cumMale}},${{cum.cumFemale}},${{cum.cumTotal}},${{cum.cumPct}}\\n`;
        }});
      }});

      const blob = new Blob(["\\uFEFF" + csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `Srikalahasti_Cumulative_Poll_Report_${{activeSlot.replace(':', '')}}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    function copyBulletinPressText() {{
      const totalElectors = 72537;
      let cumTotal = 0;
      let repCount = 0;

      POLLING_STATIONS.forEach(p => {{
        const cum = calculateCumulativeForStation(p.sl, activeSlot);
        if (cum.hasAnyReport) {{
          repCount++;
          cumTotal += cum.cumTotal;
        }}
      }});

      const pct = totalElectors > 0 ? ((cumTotal / totalElectors) * 100).toFixed(2) : '0.00';

      const pressText = `🏛️ *ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం | శ్రీకాళహస్తి పురపాలక సంఘ సాధారణ ఎన్నికలు 2026*\\n` +
        `📊 *${{activeSlot}} అధికారిక సంచిత పోలింగ్ సరళి బులెటిన్ (CUMULATIVE BULLETIN)*\\n` +
        `━━━━━━━━━━━━━━━━━━━━━\\n` +
        `📍 పురపాలక సంఘం: శ్రీకాళహస్తి, తిరుపతి జిల్లా\\n` +
        `👥 మొత్తం నమోదైన ఓటర్లు: 72,537\\n` +
        `🗳️ ఇప్పటివరకు సంచిత పోలైన ఓట్లు: *${{cumTotal.toLocaleString()}}*\\n` +
        `📈 సంచిత పోలింగ్ శాతం: *${{pct}}%*\\n` +
        `🏢 నివేదిక సమర్పించిన కేంద్రాలు: ${{repCount}} / 88\\n` +
        `━━━━━━━━━━━━━━━━━━━━━\\n` +
        `జారీ చేసినవారు: ఎన్నికల అధికారి & మున్సిపల్ కమిషనర్, శ్రీకాళహస్తి`;

      navigator.clipboard.writeText(pressText).then(() => {{
        alert('సంచిత మీడియా ప్రెస్ సారాంశం కాపీ చేయబడింది!');
      }});
    }}

    // QUICK UPDATE MODAL (FOR EO TO ENTER DATA ON PHONE CALL)
    function openQuickModal(sl) {{
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      document.getElementById('modalTargetSL').value = sl;
      document.getElementById('modalStationTitle').textContent = `వార్డు ${{ps.ward}} &bull; PS ${{ps.ps_no}} సత్వర నమోదు`;
      document.getElementById('modalStationSub').textContent = `🏫 ${{ps.details}} (మొత్తం ఓటర్లు: ${{ps.voters}})`;
      document.getElementById('modalElectorsVal').textContent = ps.voters;
      document.getElementById('modalSelectSlot').value = activeSlot === '07:00' ? '09:00' : activeSlot;

      onModalSlotChanged();
      document.getElementById('quickUpdateModal').classList.add('active');
    }}

    function closeQuickModal() {{
      document.getElementById('quickUpdateModal').classList.remove('active');
    }}

    function onModalSlotChanged() {{
      const sl = parseInt(document.getElementById('modalTargetSL').value);
      const slot = document.getElementById('modalSelectSlot').value;
      const rec = pollDataStore[sl] || {{}};
      const d = rec[slot] || {{}};

      document.getElementById('modalMale').value = d.male || '';
      document.getElementById('modalFemale').value = d.female || '';
      document.getElementById('modalTG').value = d.tg || '';
      calcModalTurnout();
    }}

    function calcModalTurnout() {{
      const sl = parseInt(document.getElementById('modalTargetSL').value);
      const slot = document.getElementById('modalSelectSlot').value;
      const ps = POLLING_STATIONS.find(p => p.sl === sl);
      if (!ps) return;

      const male = parseInt(document.getElementById('modalMale').value) || 0;
      const female = parseInt(document.getElementById('modalFemale').value) || 0;
      const tg = parseInt(document.getElementById('modalTG').value) || 0;
      const slotTotal = male + female + tg;

      document.getElementById('modalSlotTotalVal').textContent = slotTotal;

      // Calculate cumulative
      let cumTotal = 0;
      for (let s of TIME_SLOTS) {{
        if (s.id === slot) {{
          cumTotal += slotTotal;
          break;
        }} else {{
          const rec = pollDataStore[sl] || {{}};
          const prevD = rec[s.id];
          if (prevD && prevD.total > 0) cumTotal += prevD.total;
        }}
      }}

      document.getElementById('modalCumTotalVal').textContent = cumTotal;
      const cumPct = ps.voters > 0 ? ((cumTotal / ps.voters) * 100).toFixed(2) : '0.00';
      document.getElementById('modalTurnoutVal').textContent = `${{cumPct}}% (సంచితం)`;
    }}

    function saveModalData() {{
      const sl = parseInt(document.getElementById('modalTargetSL').value);
      const slot = document.getElementById('modalSelectSlot').value;
      const male = parseInt(document.getElementById('modalMale').value) || 0;
      const female = parseInt(document.getElementById('modalFemale').value) || 0;
      const tg = parseInt(document.getElementById('modalTG').value) || 0;
      const total = male + female + tg;

      if (!pollDataStore[sl]) pollDataStore[sl] = {{}};
      pollDataStore[sl][slot] = {{
        male, female, tg, total,
        updated_at: new Date().toLocaleTimeString()
      }};

      savePollData();
      closeQuickModal();
      updateViewsForRole();
    }}

    // BILINGUAL LANGUAGE TOGGLE
    function setLanguage(lang) {{
      currentLang = lang;
      document.getElementById('btnLangTe').classList.toggle('active', lang === 'te');
      document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');

      const isTe = lang === 'te';
      document.getElementById('txtHeaderTitle').textContent = isTe 
        ? 'శ్రీకాళహస్తి పురపాలక సంఘం — లైవ్ పోలింగ్ మానిటరింగ్ పోర్టల్' 
        : 'Srikalahasti Municipality — Live Polling Monitoring Portal';
      document.getElementById('txtHeaderSub').textContent = isTe 
        ? '2వ విడత సాధారణ ఎన్నికలు 2026 | ఎన్నికల & ప్రిసైడింగ్ అధికారుల రియల్-టైమ్ పోలింగ్ డేటా సేకరణ' 
        : '2nd Ordinary Elections 2026 | Real-time Polling Data Collection for EOs & POs';
      document.getElementById('txtBtnGuidance').textContent = isTe ? 'మార్గదర్శక పోర్టల్ (Guide)' : 'Guidance Guide';

      renderSlotButtons();
      if (currentUser) updateViewsForRole();
    }}
  </script>
</body>
</html>
"""

with open('poll-tracker.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("poll-tracker.html with Cumulative Auto-Calculation & Role-based Access generated successfully!")
