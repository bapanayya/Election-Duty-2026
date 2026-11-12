# -*- coding: utf-8 -*-
import json

with open('srikalahasti_88_polling_stations.json', 'r', encoding='utf-8') as f:
    ps_data = json.load(f)

from prepare_data import reservations, ward_summary

ps_json_str = json.dumps(ps_data, ensure_ascii=False)
wards_json_str = json.dumps([ward_summary[w] for w in sorted(ward_summary.keys())], ensure_ascii=False)

# We will generate index.html directly
with open('index.html', 'w', encoding='utf-8') as out:
    out.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Election Officers Guidance Portal | Srikalahasti Municipality Phase 2 Elections 2026</title>
  <style>
    :root {
      --primary: #0b2545;
      --primary-dark: #07192e;
      --secondary: #134074;
      --accent: #d97706;
      --accent-hover: #b45309;
      --success: #15803d;
      --success-light: #dcfce7;
      --danger: #b91c1c;
      --danger-light: #fee2e2;
      --warning: #b45309;
      --warning-light: #fef3c7;
      --info: #0284c7;
      --info-light: #e0f2fe;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-light: #94a3b8;
      --radius: 8px;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Nirmala UI", "Gautami", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    /* Header & Branding */
    header.portal-header {
      background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 70%, var(--secondary) 100%);
      color: #ffffff;
      padding: 1.25rem 2rem;
      border-bottom: 4px solid var(--accent);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-lg);
    }
    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .header-brand {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }
    .emblem-badge {
      width: 58px;
      height: 58px;
      background: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 12px rgba(217, 119, 6, 0.4);
      flex-shrink: 0;
      font-weight: 800;
      color: var(--primary);
      font-size: 1.5rem;
      border: 2px solid var(--accent);
    }
    .brand-text h1 {
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.25;
    }
    .brand-text p {
      font-size: 0.85rem;
      color: #cbd5e1;
      margin-top: 3px;
    }
    .header-controls {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .header-stats {
      display: flex;
      gap: 0.65rem;
      flex-wrap: wrap;
    }
    .stat-pill {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(8px);
      padding: 0.4rem 0.8rem;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      font-size: 0.78rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .stat-pill b { color: #fde047; }
    
    /* Language Switcher Pill */
    .lang-switch-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.35);
      padding: 3px;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
    }
    .lang-btn {
      background: transparent;
      border: none;
      color: #cbd5e1;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.95rem;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .lang-btn.active {
      background: var(--accent);
      color: #ffffff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.25);
    }
    .lang-btn:hover:not(.active) {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.12);
    }

    .live-clock-badge {
      background: var(--accent);
      color: #ffffff;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Sticky Tab Navigation */
    nav.portal-nav {
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 86px;
      z-index: 90;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
      overflow-x: auto;
      white-space: nowrap;
    }
    .nav-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      gap: 0.25rem;
    }
    .nav-btn {
      background: transparent;
      border: none;
      padding: 0.9rem 1.15rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      border-bottom: 3px solid transparent;
      transition: all 0.2s ease;
    }
    .nav-btn:hover {
      color: var(--secondary);
      background: #f1f5f9;
    }
    .nav-btn.active {
      color: var(--secondary);
      border-bottom-color: var(--secondary);
      background: #f8fafc;
    }
    .nav-badge {
      background: var(--border);
      color: var(--text-muted);
      font-size: 0.7rem;
      padding: 0.15rem 0.45rem;
      border-radius: 9999px;
      font-weight: 700;
    }
    .nav-btn.active .nav-badge {
      background: var(--secondary);
      color: #ffffff;
    }

    /* Main Container */
    main.portal-main {
      max-width: 1440px;
      margin: 1.5rem auto 3rem auto;
      padding: 0 1.5rem;
    }

    .tab-content { display: none; }
    .tab-content.active { display: block; animation: fadeIn 0.25s ease-in-out; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Typography & Titles */
    .section-title {
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .section-sub {
      font-size: 0.92rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }

    /* Cards & Containers */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.75rem;
      margin-bottom: 1rem;
    }
    .card-header h3 {
      font-size: 1.1rem;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Notification Banner */
    .banner-notification {
      background: linear-gradient(90deg, #1e3a8a 0%, #1e40af 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      box-shadow: var(--shadow);
    }
    .banner-text h2 {
      font-size: 1.15rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .banner-text p {
      font-size: 0.85rem;
      color: #bfdbfe;
      margin-top: 3px;
    }
    .banner-actions {
      display: flex;
      gap: 0.5rem;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.9rem;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      border: none;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .btn-accent {
      background: var(--accent);
      color: #ffffff;
    }
    .btn-accent:hover { background: var(--accent-hover); }
    .btn-outline {
      background: transparent;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .btn-outline:hover {
      background: rgba(255, 255, 255, 0.1);
    }
    .btn-secondary {
      background: #e2e8f0;
      color: var(--text-main);
    }
    .btn-secondary:hover { background: #cbd5e1; }
    .btn-success { background: var(--success); color: #ffffff; }
    .btn-success:hover { background: #166534; }

    /* Timeline Stepper */
    .timeline-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .timeline-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1rem;
      position: relative;
      border-left: 5px solid var(--secondary);
      box-shadow: var(--shadow);
      transition: transform 0.2s ease;
    }
    .timeline-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
    }
    .timeline-card.active-stage {
      border-left-color: var(--accent);
      background: #fffbeb;
    }
    .timeline-card.poll-stage {
      border-left-color: var(--danger);
      background: #fef2f2;
    }
    .timeline-card.counting-stage {
      border-left-color: var(--success);
      background: #f0fdf4;
    }
    .stage-badge {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      background: #e2e8f0;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }
    .timeline-card.active-stage .stage-badge { background: #fde68a; color: #92400e; }
    .timeline-card.poll-stage .stage-badge { background: #fecaca; color: #991b1b; }
    .timeline-card.counting-stage .stage-badge { background: #bbf7d0; color: #166534; }
    .timeline-date {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
    }
    .timeline-card h4 {
      font-size: 0.95rem;
      color: var(--text-main);
      margin: 0.3rem 0;
    }
    .timeline-card p {
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.4;
    }
    .timeline-time {
      margin-top: 0.5rem;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--accent-hover);
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    /* Stage Steps Accordion */
    .stage-box {
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 1.25rem;
      background: #ffffff;
      overflow: hidden;
      box-shadow: var(--shadow);
    }
    .stage-box-header {
      background: #f8fafc;
      padding: 1rem 1.25rem;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid transparent;
      transition: background 0.2s ease;
    }
    .stage-box-header:hover {
      background: #f1f5f9;
    }
    .stage-box.open .stage-box-header {
      border-bottom-color: var(--border);
      background: #eff6ff;
    }
    .stage-header-title {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .stage-num {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--secondary);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.88rem;
      flex-shrink: 0;
    }
    .stage-box-header h3 {
      font-size: 1rem;
      color: var(--primary);
      font-weight: 700;
    }
    .stage-date-tag {
      font-size: 0.8rem;
      background: #e2e8f0;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-weight: 600;
      color: var(--text-muted);
    }
    .stage-box-body {
      padding: 1.25rem;
      display: none;
    }
    .stage-box.open .stage-box-body {
      display: block;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
    }

    /* Checklist Components */
    .checklist-controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      background: #f8fafc;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      border: 1px solid var(--border);
      margin-bottom: 1rem;
    }
    .progress-bar-container {
      flex: 1;
      min-width: 200px;
    }
    .progress-bar-label {
      display: flex;
      justify-content: space-between;
      font-size: 0.8rem;
      font-weight: 600;
      margin-bottom: 0.25rem;
      color: var(--text-muted);
    }
    .progress-bar {
      height: 8px;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
    }
    .progress-fill {
      height: 100%;
      background: var(--success);
      width: 0%;
      transition: width 0.3s ease;
    }
    .checklist-items {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .chk-item {
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      padding: 0.65rem 0.85rem;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #ffffff;
      transition: all 0.15s ease;
      cursor: pointer;
    }
    .chk-item:hover {
      background: #f8fafc;
      border-color: #cbd5e1;
    }
    .chk-item.checked {
      background: #f0fdf4;
      border-color: #86efac;
    }
    .chk-item.checked .chk-text {
      color: #166534;
      text-decoration: line-through;
    }
    .chk-item input[type="checkbox"] {
      width: 18px;
      height: 18px;
      margin-top: 2px;
      accent-color: var(--success);
      cursor: pointer;
      flex-shrink: 0;
    }
    .chk-content {
      flex: 1;
    }
    .chk-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-main);
    }
    .chk-sub {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    /* Tables */
    .table-container {
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      background: #ffffff;
      margin-bottom: 1.5rem;
    }
    table.data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      text-align: left;
    }
    table.data-table th {
      background: #f1f5f9;
      color: var(--primary);
      font-weight: 700;
      padding: 0.75rem 0.85rem;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }
    table.data-table td {
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }
    table.data-table tr:hover td {
      background: #f8fafc;
    }
    .tag-badge {
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      white-space: nowrap;
    }
    .tag-sc { background: #ede9fe; color: #5b21b6; }
    .tag-st { background: #fae8ff; color: #86198f; }
    .tag-bc { background: #dbeafe; color: #1e40af; }
    .tag-ur { background: #f1f5f9; color: #334155; }
    .tag-women { border: 1px solid #f472b6; color: #9d174d; background: #fdf2f8; }

    /* Do's and Don'ts Cards */
    .dodont-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }
    .dodont-card {
      border-radius: var(--radius);
      padding: 1.25rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }
    .dodont-card.dos {
      background: #f0fdf4;
      border-color: #86efac;
    }
    .dodont-card.donts {
      background: #fef2f2;
      border-color: #fca5a5;
    }
    .dodont-title {
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .dodont-card.dos .dodont-title { color: #166534; }
    .dodont-card.donts .dodont-title { color: #991b1b; }
    .dodont-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    .dodont-list li {
      font-size: 0.83rem;
      line-height: 1.45;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }
    .dodont-list li::before {
      font-weight: 800;
      flex-shrink: 0;
      margin-top: 1px;
    }
    .dodont-card.dos .dodont-list li::before {
      content: "✓";
      color: #16a34a;
    }
    .dodont-card.donts .dodont-list li::before {
      content: "✗";
      color: #dc2626;
    }

    /* Forms Repository */
    .forms-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
    }
    .form-item-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1rem;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .form-item-card h4 {
      font-size: 0.95rem;
      color: var(--primary);
      margin-bottom: 0.25rem;
    }
    .form-meta {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }
    .form-desc {
      font-size: 0.8rem;
      color: var(--text-main);
      margin-bottom: 0.85rem;
      flex: 1;
    }
    .form-actions {
      display: flex;
      gap: 0.5rem;
      border-top: 1px solid var(--border);
      padding-top: 0.75rem;
    }

    /* Guidelines Cards */
    .guideline-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      box-shadow: var(--shadow);
      margin-bottom: 1rem;
    }
    .guideline-card h3 {
      font-size: 1.05rem;
      color: var(--primary);
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.5rem;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .guideline-points {
      list-style-type: disc;
      padding-left: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }
    .guideline-points li {
      font-size: 0.85rem;
      color: var(--text-main);
      line-height: 1.45;
    }
    .guideline-points li strong {
      color: var(--secondary);
    }

    /* Tools */
    .tool-box {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }
    .calc-input-group {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      flex-wrap: wrap;
      margin-top: 0.75rem;
    }
    .calc-input-group input, .calc-input-group select {
      padding: 0.5rem 0.75rem;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.85rem;
      min-width: 180px;
    }
    .calc-res-box {
      margin-top: 1rem;
      padding: 0.85rem 1rem;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.88rem;
    }

    /* Color Coded Covers Visual Guide */
    .cover-guide-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      margin: 1rem 0;
    }
    .cover-item {
      padding: 1rem;
      border-radius: var(--radius);
      color: #ffffff;
      box-shadow: var(--shadow);
    }
    .cover-brown { background: #78350f; }
    .cover-green { background: #166534; }
    .cover-yellow { background: #854d0e; }
    .cover-blue { background: #1e40af; }
    .cover-item h4 {
      font-size: 0.95rem;
      margin-bottom: 0.35rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.3);
      padding-bottom: 0.35rem;
    }
    .cover-item ul {
      list-style-type: none;
      font-size: 0.78rem;
      line-height: 1.4;
    }
    .cover-item ul li {
      margin-bottom: 0.3rem;
      padding-left: 0.8rem;
      position: relative;
    }
    .cover-item ul li::before {
      content: "•";
      position: absolute;
      left: 0;
    }

    /* Modal for Form Details */
    .modal-backdrop {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(4px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
    }
    .modal-backdrop.open { display: flex; }
    .modal-window {
      background: #ffffff;
      border-radius: var(--radius);
      max-width: 800px;
      width: 100%;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border);
      overflow: hidden;
    }
    .modal-header {
      background: var(--primary);
      color: #ffffff;
      padding: 1rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-header h3 { font-size: 1.1rem; }
    .modal-close {
      background: transparent;
      border: none;
      color: #ffffff;
      font-size: 1.5rem;
      cursor: pointer;
      line-height: 1;
    }
    .modal-body {
      padding: 1.25rem;
      overflow-y: auto;
      font-family: monospace;
      font-size: 0.85rem;
      white-space: pre-wrap;
      background: #f8fafc;
      color: #0f172a;
      line-height: 1.5;
    }
    .modal-footer {
      padding: 0.75rem 1.25rem;
      background: #ffffff;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: flex-end;
      gap: 0.5rem;
    }

    /* Footer */
    footer.portal-footer {
      background: var(--primary-dark);
      color: #94a3b8;
      padding: 2rem 1.5rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      font-size: 0.82rem;
      text-align: center;
    }
    footer.portal-footer a { color: #cbd5e1; text-decoration: none; }
    footer.portal-footer a:hover { color: #ffffff; text-decoration: underline; }

    /* Search Box */
    .search-bar-wrap {
      margin-bottom: 1.25rem;
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .search-input {
      flex: 1;
      min-width: 260px;
      padding: 0.6rem 1rem;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.85rem;
      background: #ffffff;
    }
    .search-input:focus {
      outline: none;
      border-color: var(--secondary);
      box-shadow: 0 0 0 3px rgba(19, 64, 116, 0.15);
    }

    /* Print Styles */
    @media print {
      header.portal-header, nav.portal-nav, footer.portal-footer, .btn, .search-bar-wrap, .checklist-controls button, .lang-switch-box {
        display: none !important;
      }
      body { background: #ffffff; color: #000000; }
      .tab-content { display: block !important; margin-bottom: 2rem; }
      .card { box-shadow: none !important; border: 1px solid #94a3b8 !important; page-break-inside: avoid; }
      .stage-box-body { display: block !important; }
      table.data-table { font-size: 8pt; }
    }

    /* Responsive */
    @media (max-width: 768px) {
      header.portal-header { padding: 1rem; }
      .header-brand { gap: 0.75rem; }
      .brand-text h1 { font-size: 1.1rem; }
      .nav-container { padding: 0 0.5rem; }
      .nav-btn { padding: 0.75rem 0.85rem; font-size: 0.8rem; }
      main.portal-main { padding: 0 1rem; margin-top: 1rem; }
    }
  </style>
</head>
<body>

  <!-- Official Header with Language Switcher -->
  <header class="portal-header">
    <div class="header-top">
      <div class="header-brand">
        <div class="emblem-badge">SEC</div>
        <div class="brand-text">
          <h1 id="headerTitle">SRIKALAHASTI MUNICIPALITY — PHASE 2 ORDINARY ELECTIONS, 2026</h1>
          <p id="headerSubtitle">Andhra Pradesh State Election Commission | District Election Authority & Collector, Tirupati District</p>
        </div>
      </div>
      <div class="header-controls">
        <!-- Language Switcher Pill -->
        <div class="lang-switch-box">
          <button class="lang-btn active" id="btnLangEn" onclick="setLanguage('en')">English</button>
          <button class="lang-btn" id="btnLangTe" onclick="setLanguage('te')">తెలుగు</button>
        </div>
        <div class="live-clock-badge">
          <span id="liveClock">12-11-2026</span>
        </div>
      </div>
    </div>
    <div class="header-stats" style="margin-top: 0.85rem;" id="headerStats"></div>
  </header>

  <!-- Navigation Bar -->
  <nav class="portal-nav">
    <div class="nav-container" id="navTabsContainer"></div>
  </nav>

  <!-- Main Content Area -->
  <main class="portal-main">

    <!-- Statutory Alert Banner -->
    <div class="banner-notification" id="bannerNotice"></div>

    <!-- TAB 1: SCHEDULE & DEADLINES -->
    <div id="tab-schedule" class="tab-content active">
      <h2 class="section-title" id="t-sched-title"></h2>
      <p class="section-sub" id="t-sched-sub"></p>
      <div class="timeline-grid" id="timelineGrid"></div>
      <div class="card" id="timeLimitsCard"></div>
    </div>

    <!-- TAB 2: STAGE-BY-STAGE FIELD GUIDE -->
    <div id="tab-stages" class="tab-content">
      <h2 class="section-title" id="t-stages-title"></h2>
      <p class="section-sub" id="t-stages-sub"></p>
      <div id="stagesContainer"></div>
    </div>

    <!-- TAB 3: CHECKLISTS -->
    <div id="tab-checklists" class="tab-content">
      <h2 class="section-title" id="t-chk-title"></h2>
      <p class="section-sub" id="t-chk-sub"></p>
      <div class="checklist-controls" id="chkControls"></div>
      <div id="checklistsContainer"></div>
    </div>

    <!-- TAB 4: IMPORTANT GUIDELINES -->
    <div id="tab-guidelines" class="tab-content">
      <h2 class="section-title" id="t-guide-title"></h2>
      <p class="section-sub" id="t-guide-sub"></p>
      <div class="grid-2" id="guidelinesContainer"></div>
    </div>

    <!-- TAB 5: DO'S AND DON'TS -->
    <div id="tab-dodont" class="tab-content">
      <h2 class="section-title" id="t-dodont-title"></h2>
      <p class="section-sub" id="t-dodont-sub"></p>
      <div id="dodontContainer"></div>
    </div>

    <!-- TAB 6: FORMS & PROFORMAS REPOSITORY -->
    <div id="tab-forms" class="tab-content">
      <h2 class="section-title" id="t-forms-title"></h2>
      <p class="section-sub" id="t-forms-sub"></p>
      <div class="search-bar-wrap">
        <input type="text" id="formSearchInput" class="search-input" placeholder="🔍 Search forms / ఫారాలు వెతకండి..." oninput="filterForms()">
      </div>
      <div class="forms-grid" id="formsContainer"></div>
    </div>

    <!-- TAB 7: SRIKALAHASTI FIELD DIRECTORY -->
    <div id="tab-directory" class="tab-content">
      <h2 class="section-title" id="t-dir-title"></h2>
      <p class="section-sub" id="t-dir-sub"></p>
      <div id="authoritiesBox"></div>
      <div id="wardMasterBox"></div>
      <div id="clusterOfficesBox"></div>
      <div id="zonalRouteBox"></div>
      <div id="surveillanceBox"></div>

      <!-- 88 PS Search Box -->
      <div class="card">
        <div class="card-header">
          <h3 id="t-ps-header">🏫 Polling Stations Directory</h3>
          <span class="tag-badge tag-poll" id="t-ps-badge">Search & Filter</span>
        </div>
        <div class="search-bar-wrap">
          <input type="text" id="psSearchInput" class="search-input" placeholder="🔍 Search polling stations / పోలింగ్ కేంద్రం వెతకండి..." oninput="filterPollingStations()">
          <select id="wardFilterSelect" class="search-input" style="max-width: 200px;" onchange="filterPollingStations()">
            <option value="ALL">All Wards (1 to 44)</option>
          </select>
        </div>
        <div class="table-container">
          <table class="data-table" id="psTable">
            <thead>
              <tr>
                <th id="th-sl">Sl No.</th>
                <th id="th-ward">Ward</th>
                <th id="th-psno">PS No.</th>
                <th id="th-name">Polling Station Building & Name</th>
                <th id="th-electors">Electors</th>
                <th id="th-geo">Geo-Location</th>
              </tr>
            </thead>
            <tbody id="psTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 8: OFFICER TOOLS & PACKING -->
    <div id="tab-tools" class="tab-content">
      <h2 class="section-title" id="t-tools-title"></h2>
      <p class="section-sub" id="t-tools-sub"></p>
      <div id="toolsContainer"></div>
    </div>

  </main>

  <!-- Modal for Forms View -->
  <div id="formModal" class="modal-backdrop">
    <div class="modal-window">
      <div class="modal-header">
        <h3 id="modalTitle">Form Title</h3>
        <button class="modal-close" onclick="closeModal()">&times;</button>
      </div>
      <div class="modal-body" id="modalContent"></div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal()" id="mBtnClose">Close</button>
        <button class="btn btn-accent" id="modalCopyBtn" onclick="copyModalContent()">Copy Form Text</button>
        <button class="btn btn-success" onclick="printModalContent()" id="mBtnPrint">Print Form</button>
      </div>
    </div>
  </div>

  <!-- Official Footer -->
  <footer class="portal-footer" id="portalFooter"></footer>

  <!-- Script data bindings -->
  <script src="portal_translations.js"></script>
  <script src="portal_forms.js"></script>
  <script>
    const POLLING_STATIONS = """ + ps_json_str + """;
    const WARD_SUMMARY = """ + wards_json_str + """;
  </script>
  <script src="portal_app.js"></script>
</body>
</html>
""")

print("Successfully written index.html shell.")
