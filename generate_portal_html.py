# -*- coding: utf-8 -*-
"""
Full HTML Builder for Srikalahasti Municipality Phase 2 Ordinary Elections 2026.
"""

import json
from portal_data import (
    reservations, ward_summary, ps_data, supporting_staff,
    zonal_officers, route_officers, surveillance_teams
)

# Convert ps_data to JSON string for client-side search
ps_json_str = json.dumps(ps_data, ensure_ascii=False)
wards_json_str = json.dumps([ward_summary[w] for w in sorted(ward_summary.keys())], ensure_ascii=False)

html_content = """<!DOCTYPE html>
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
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
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
      line-height: 1.2;
    }
    .brand-text p {
      font-size: 0.85rem;
      color: #cbd5e1;
      margin-top: 2px;
    }
    .header-stats {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .stat-pill {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(8px);
      padding: 0.4rem 0.85rem;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      font-size: 0.78rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .stat-pill b { color: #fde047; }
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

    /* Stage Steps Accordion / Details */
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
    .chk-tag {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.1rem 0.45rem;
      border-radius: 4px;
      background: #e2e8f0;
      color: var(--text-muted);
      margin-left: 0.4rem;
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

    /* Interactive Calculator / Tools */
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
      header.portal-header, nav.portal-nav, footer.portal-footer, .btn, .search-bar-wrap, .checklist-controls button {
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

  <!-- Official Header -->
  <header class="portal-header">
    <div class="header-top">
      <div class="header-brand">
        <div class="emblem-badge">SEC</div>
        <div class="brand-text">
          <h1>SRIKALAHASTI MUNICIPALITY — PHASE 2 ORDINARY ELECTIONS, 2026</h1>
          <p>Andhra Pradesh State Election Commission | District Election Authority & Collector, Tirupati District</p>
        </div>
      </div>
      <div class="header-stats">
        <div class="stat-pill">Wards: <b>44</b></div>
        <div class="stat-pill">Polling Stations: <b>88</b></div>
        <div class="stat-pill">Electors: <b>72,537</b></div>
        <div class="stat-pill">Offices: <b>12 Clusters</b></div>
        <div class="live-clock-badge">
          <span id="liveClock">12-11-2026</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Navigation Bar -->
  <nav class="portal-nav">
    <div class="nav-container">
      <button class="nav-btn active" onclick="switchTab('tab-schedule')">
        <span>📅 Schedule & Deadlines</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-stages')">
        <span>🚶 Stage-by-Stage Guide</span>
        <span class="nav-badge">9 Stages</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-checklists')">
        <span>✅ Checklists</span>
        <span class="nav-badge">8 Sets</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-guidelines')">
        <span>📌 Important Guidelines</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-dodont')">
        <span>⚖️ Do's & Don'ts</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-forms')">
        <span>📂 Forms & Proformas</span>
        <span class="nav-badge">22 Forms</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-directory')">
        <span>🏛️ Srikalahasti Roster</span>
        <span class="nav-badge">88 PS / Teams</span>
      </button>
      <button class="nav-btn" onclick="switchTab('tab-tools')">
        <span>🛠️ Field Tools & Packing</span>
      </button>
    </div>
  </nav>

  <!-- Main Content Area -->
  <main class="portal-main">

    <!-- Statutory Alert Banner -->
    <div class="banner-notification">
      <div class="banner-text">
        <h2>⚡ SEC Notification No. 1490/SEC-F1/2026-3 Dated 12.11.2026 Issued</h2>
        <p>Elections called for Chairperson (Direct Election) and Ward Members for 44 Wards under AP Municipalities Act, 1965 & Conduct of Election Rules, 2026.</p>
      </div>
      <div class="banner-actions">
        <button class="btn btn-accent" onclick="switchTab('tab-checklists')">Open Checklists</button>
        <button class="btn btn-outline" onclick="window.print()">Print Quick Kit</button>
      </div>
    </div>

    <!-- TAB 1: SCHEDULE & DEADLINES -->
    <div id="tab-schedule" class="tab-content active">
      <h2 class="section-title">Election Programme & Statutory Timeline</h2>
      <p class="section-sub">Comprehensive timeline notified by AP State Election Commission for Phase 2 Ordinary Municipal Elections, 2026.</p>

      <!-- Stepper Cards -->
      <div class="timeline-grid">
        <div class="timeline-card">
          <span class="stage-badge">Stage 1: Pre-Poll</span>
          <div class="timeline-date">14.11.2026</div>
          <h4>Ward Electoral Rolls Display</h4>
          <p>Under Rule 5, Election Officer displays ward-wise voter lists on the notice board.</p>
          <div class="timeline-time">⏰ Morning 10:00 AM</div>
        </div>

        <div class="timeline-card">
          <span class="stage-badge">Stage 2: Public Notice</span>
          <div class="timeline-date">14.11.2026</div>
          <h4>Publication of Election Notice</h4>
          <p>Election Notice issued by Election Officer under Rule 6 in prescribed format (Form-1).</p>
          <div class="timeline-time">⏰ Morning (Before Nominations)</div>
        </div>

        <div class="timeline-card active-stage">
          <span class="stage-badge">Stage 3: Nominations</span>
          <div class="timeline-date">14.11.2026 to 16.11.2026</div>
          <h4>Filing & Receipt of Nominations</h4>
          <p>Receipt of nominations at 12 designated offices (Chairperson + 11 Ward Clusters).</p>
          <div class="timeline-time">⏰ 11:00 AM to 3:00 PM Daily</div>
        </div>

        <div class="timeline-card">
          <span class="stage-badge">Stage 4: Last Date</span>
          <div class="timeline-date">16.11.2026 (Monday)</div>
          <h4>Close of Nominations & Form-A</h4>
          <p>Last moment for nomination filing (3 PM). Political party Form-A to Collector & DEA before 5 PM.</p>
          <div class="timeline-time">⏰ 3:00 PM (Sharp) / 5:00 PM (Form-A)</div>
        </div>

        <div class="timeline-card">
          <span class="stage-badge">Stage 5: Scrutiny</span>
          <div class="timeline-date">17.11.2026 (Tuesday)</div>
          <h4>Scrutiny of Nominations</h4>
          <p>Quasi-judicial examination by Election Officer. Publication of Form-IV valid candidate list.</p>
          <div class="timeline-time">⏰ From 11:00 AM Onwards</div>
        </div>

        <div class="timeline-card">
          <span class="stage-badge">Stage 6: Withdrawals & Symbols</span>
          <div class="timeline-date">19.11.2026 (Thursday)</div>
          <h4>Withdrawals & Form-VII Publication</h4>
          <p>Notice of withdrawal (Form-V) up to 3 PM. Form-B to EO up to 3 PM. Allotment of symbols & Form-VII.</p>
          <div class="timeline-time">⏰ Withdrawal: Up to 3 PM | Form-VII: After 3 PM</div>
        </div>

        <div class="timeline-card poll-stage">
          <span class="stage-badge">Stage 7: Poll Day</span>
          <div class="timeline-date">26.11.2026 (Thursday)</div>
          <h4>Conduct of Poll (Voting)</h4>
          <p>Poll across all 88 Polling Stations using White (Chairperson) and Pink (Ward Member) ballots.</p>
          <div class="timeline-time">⏰ 07:00 AM to 05:00 PM</div>
        </div>

        <div class="timeline-card">
          <span class="stage-badge">Stage 8: Re-Poll</span>
          <div class="timeline-date">27.11.2026 (Friday)</div>
          <h4>Date of Re-poll (If Any)</h4>
          <p>Reserved for any re-poll ordered by APSEC under statutory grounds.</p>
          <div class="timeline-time">⏰ 07:00 AM to 05:00 PM</div>
        </div>

        <div class="timeline-card counting-stage">
          <span class="stage-badge">Stage 9: Counting</span>
          <div class="timeline-date">30.11.2026 (Monday)</div>
          <h4>Counting of Votes & Declaration</h4>
          <p>Continuous counting at designated counting centre. Form-XX Part I & II declaration.</p>
          <div class="timeline-time">⏰ From 08:00 AM Onwards</div>
        </div>
      </div>

      <!-- Key Statutory Time Limits Table -->
      <div class="card">
        <div class="card-header">
          <h3>⏱️ Statutory Time Limits at a Glance (C&DMA VC-23 Ref)</h3>
          <span class="tag-badge tag-ur">Rule Limits</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Election Activity</th>
                <th>Prescribed Statutory Time Limit</th>
                <th>Responsible Officer / Authority</th>
                <th>Key Legal Citation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Receipt of Nominations</b></td>
                <td>11:00 AM to 3:00 PM (All notified days, incl. public holidays)</td>
                <td>Election Officer (EO) / AEO</td>
                <td>Rule 8(1), Conduct of Election Rules 2026</td>
              </tr>
              <tr>
                <td><b>Submission of Pending Checklist Documents</b></td>
                <td>Before 3:00 PM on the last date for nominations (16.11.2026)</td>
                <td>Candidate / Proposer</td>
                <td>C&DMA Instructions / SEC Guidelines</td>
              </tr>
              <tr>
                <td><b>Submission of Form-A (Party Authorisation)</b></td>
                <td>Before 5:00 PM on the last date for nominations (16.11.2026)</td>
                <td>President / Gen. Secy of Political Party to Collector & DEA</td>
                <td>Para 13, Symbols Order / SEC Orders</td>
              </tr>
              <tr>
                <td><b>Delivery of Form-B (Candidate Sponsorship)</b></td>
                <td>Before 3:00 PM on the last date for withdrawal (19.11.2026)</td>
                <td>Authorized Party Signatory to Election Officer (EO)</td>
                <td>Para 13, Symbols Order</td>
              </tr>
              <tr>
                <td><b>Withdrawal of Candidature (Form-V)</b></td>
                <td>Not later than 3:00 PM on the appointed date (19.11.2026)</td>
                <td>Candidate in person / Proposer / Auth. Election Agent</td>
                <td>Rule 13, Conduct of Election Rules 2026</td>
              </tr>
              <tr>
                <td><b>Despatch of Postal Ballots</b></td>
                <td>Within 48 hours of the last hour of withdrawal (by 21.11.2026, 3 PM)</td>
                <td>Election Officer</td>
                <td>Rule 22 to 27, G.O.Ms.No.213</td>
              </tr>
              <tr>
                <td><b>Polling Agent Appointment Intimation</b></td>
                <td>At least 3 days before poll (by 23.11.2026)</td>
                <td>Candidate / Election Agent to EO / PO</td>
                <td>Rule 18 / SEC Compendium</td>
              </tr>
              <tr>
                <td><b>Campaign Silence Period</b></td>
                <td>48 hours ending with the hour fixed for the conclusion of poll</td>
                <td>All Political Parties / Candidates / Media</td>
                <td>Sec. 343-A AP Municipalities Act</td>
              </tr>
              <tr>
                <td><b>Hours of Poll</b></td>
                <td>07:00 AM to 05:00 PM (Persons in queue at 5 PM receive numbered slips)</td>
                <td>Presiding Officer (PO)</td>
                <td>Notification No. 1490/SEC-F1/2026-3</td>
              </tr>
              <tr>
                <td><b>Candidate Day-to-Day Expense Account</b></td>
                <td>Once every 3 days from date of publication of contesting list</td>
                <td>Candidate to Expenditure Scrutiny Team</td>
                <td>Sec. 343-ZC(1) to (3) / SEC Order 135</td>
              </tr>
              <tr>
                <td><b>Request for Recount of Votes</b></td>
                <td>Within 15 minutes after announcement of total votes scored</td>
                <td>Candidate / Election Agent to EO</td>
                <td>Conduct of Election Rules / Counting Instructions</td>
              </tr>
              <tr>
                <td><b>Choice of Seat (Multiple Wins)</b></td>
                <td>Within 15 days of last result declaration</td>
                <td>Elected Candidate to Municipal Commissioner</td>
                <td>Rule 62, AP Municipal Election Rules 2026</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 2: STAGE-BY-STAGE FIELD GUIDE -->
    <div id="tab-stages" class="tab-content">
      <h2 class="section-title">Stage-by-Stage Field Guide for Election Officers</h2>
      <p class="section-sub">Step-by-step procedures, legal requirements, and essential administrative workflows from Notification to Strong Room custody.</p>

      <!-- Stage 1 -->
      <div class="stage-box open">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">1</span>
            <div>
              <h3>Pre-Poll Preparations, Electoral Rolls Display & Form-1 Notice</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Display of Electoral Rolls (Rule 5) | Issue of Election Notice (Rule 6)</p>
            </div>
          </div>
          <span class="stage-date-tag">12.11.2026 to 14.11.2026</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Key Operational Steps</h4>
              <ul class="guideline-points">
                <li><strong>Roll Freezing:</strong> Ward-wise electoral roll is frozen as on 12.11.2026 (date of SEC notification). Ensure all additions/deletions up to that date ordered by ERO under RP Act 1950 are integrated.</li>
                <li><strong>Roll Display (14.11.2026 morning):</strong> Election Officer must display the updated ward-wise electoral roll on the Municipal Office notice board and at prominent locations in each ward under Rule 5.</li>
                <li><strong>Issue Election Notice (Form-1):</strong> Publish the Election Notice in the prescribed SEC format in both English and Telugu specifying particulars of election, reservations, nomination places, dates & timings.</li>
                <li><strong>Establish 12 Election Offices:</strong> Setup 1 dedicated Election Office for Chairperson and 11 Cluster Offices (each covering 4 wards: Wards 1-4, 5-8, 9-12, 13-16, 17-20, 21-24, 25-28, 29-32, 33-36, 37-40, 41-44).</li>
                <li><strong>Stationery & Forms Stock:</strong> Supply blank nomination forms, declarations on criminal antecedents/assets, and Form-IA free of cost to intending candidates. Keep sufficient copies of all statutory registers.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Legal Checks & Boundaries</h4>
              <ul class="guideline-points">
                <li><strong>Office of Profit & Disqualifications:</strong> Review Sections 13, 13-A, 14, 15, 15-A, and 15-B of the AP Municipalities Act, 1965.</li>
                <li><strong>Expenditure Ceilings:</strong> Brief all officers that statutory expense ceilings are <strong>Rs. 20.00 Lakhs</strong> for Chairperson and <strong>Rs. 7.50 Lakhs</strong> for Ward Members.</li>
                <li><strong>Notice Board Affixture:</strong> Ensure that separate notices are displayed for Chairperson and Ward Member seats showing exact reservation category.</li>
                <li><strong>Help Desk / Assistance:</strong> Ensure supporting staff (Ward Administrative Secretaries & Ward Education & Data Processing Secretaries) report to their cluster rooms immediately.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 2 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">2</span>
            <div>
              <h3>Receipt & Verification of Nominations</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Hours: 11:00 AM – 3:00 PM | Deposit, Proposer & Checklist Verification</p>
            </div>
          </div>
          <span class="stage-date-tag">14.11.2026 to 16.11.2026</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Filing & Documentation Rules</h4>
              <ul class="guideline-points">
                <li><strong>Strict Timing:</strong> Nominations can be received ONLY between 11:00 AM and 3:00 PM on notified days (even on public holidays). Exactly at 3:00 PM on 16.11.2026, close doors; give slips to persons already inside.</li>
                <li><strong>Entry Restrictions:</strong> Maximum 1 vehicle within 100 meters. Maximum 3 persons allowed inside the Election Office (including candidate and proposer).</li>
                <li><strong>Maximum Sets:</strong> A candidate can submit a maximum of <strong>4 sets</strong> of nomination papers for a single ward/office (Rule 8(1)).</li>
                <li><strong>Security Deposit:</strong> 
                  <br>• General Candidate: <strong>Rs. 3,000/-</strong>
                  <br>• SC / ST / BC Candidate: <strong>Rs. 1,500/-</strong> (Must produce Community Certificate issued by Tahsildar / Form-II).
                  <br><em>Deposit valid for unreserved or reserved seat; only one deposit needed per candidate even if 4 sets are filed!</em>
                </li>
                <li><strong>Proposer Eligibility:</strong>
                  <br>• For Ward Member: Proposer MUST be a registered elector in that specific ward.
                  <br>• For Chairperson: Proposer MUST be a registered elector in any ward of Srikalahasti Municipality.
                  <br><em>If a proposer signs nominations for multiple candidates in the same ward, only the first delivered nomination is valid!</em>
                </li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Officer's Actions Upon Receipt</h4>
              <ul class="guideline-points">
                <li><strong>Preliminary Examination:</strong> Check candidate and proposer names against the electoral roll. Minor clerical/printing errors can be overlooked or corrected.</li>
                <li><strong>Running Serial Number & Initials:</strong> Immediately assign a running serial number (e.g., 01/Ward-5), write date and exact minute of receipt, and initial each page.</li>
                <li><strong>Mandatory Enclosures:</strong>
                  <br>1. Declaration on Antecedents, Assets, Liabilities & Education (attested by 2 witnesses - no column left blank; write 'Nil' or 'Not Applicable').
                  <br>2. Form-IA Choice of Symbols (up to 3 preferences).
                  <br>3. Community Certificate / Form-II (if SC/ST/BC).
                  <br>4. Declaration of adherence to Model Code of Conduct.
                </li>
                <li><strong>Checklist & Receipt (Form-I):</strong> Endorse the Checklist of documents. Keep original with nomination; hand over duplicate copy with Form-I receipt and scrutiny notice to the candidate/proposer.</li>
                <li><strong>Daily Notice:</strong> Publish Form-III list of nominations received on the Notice Board after 3:00 PM daily. On 16.11.2026, publish the final consolidated Form-III immediately after 3:00 PM.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 3 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">3</span>
            <div>
              <h3>Scrutiny of Nominations (Quasi-Judicial Enquiry)</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Quasi-Judicial Proceedings | Summary Enquiry | Grounds for Rejection</p>
            </div>
          </div>
          <span class="stage-date-tag">17.11.2026 (From 11:00 AM)</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Scrutiny Room Protocol</h4>
              <ul class="guideline-points">
                <li><strong>Conducted Personally by EO:</strong> The Election Officer MUST conduct scrutiny personally. The Assistant Election Officer can step in only if the EO is unavoidably prevented.</li>
                <li><strong>Persons Entitled to Attend:</strong> Candidate, Election Agent, Proposer, and ONE person authorised in writing by the candidate. (Others strictly barred).</li>
                <li><strong>Summary Examination:</strong> The EO examines each nomination set serially. Inspection of nomination papers by other candidates is allowed, but physical handling is strictly forbidden.</li>
                <li><strong>Crucial Age Rule:</strong> The candidate must have attained the age of <strong>21 years</strong> on the date of scrutiny.</li>
                <li><strong>Every Set Scrutinised:</strong> Even if Set 1 is accepted, examine Sets 2, 3, and 4 so that the record is clear if any appeal or petition arises.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Grounds of Rejection & Protections</h4>
              <ul class="guideline-points">
                <li><strong>Valid Grounds for Rejection:</strong>
                  <br>• Candidate not enrolled in Srikalahasti Municipality electoral roll.
                  <br>• Proposer not enrolled in the specific ward (for Ward Member).
                  <br>• Age below 21 years on date of scrutiny.
                  <br>• Required statutory deposit (Rs. 3,000 / Rs. 1,500) not paid.
                  <br>• Candidate disqualified under Sec. 13, 13-A, 14, 15, 15-A, or 15-B of the Act.
                  <br>• Reserved seat (SC/ST/BC/Women) and candidate does not belong to that category.
                  <br>• Mandatory declaration not attested by two witnesses or columns left blank without writing 'Nil'.
                </li>
                <li><strong>Substantial Character Rule:</strong> Do NOT reject a nomination for any defect that is NOT of a substantial character. Technical, typographical, or clerical errors must be ignored.</li>
                <li><strong>Right of Rebuttal:</strong> If an objection is raised or the EO proposes to reject suo motu, the candidate must be given reasonable opportunity to rebut up to <strong>the next day</strong> (18.11.2026). Scrutiny of other candidates continues.</li>
                <li><strong>Recording Order:</strong> The EO must record a reasoned order on the nomination paper and furnish a copy of rejection order immediately to the candidate.</li>
                <li><strong>Publication of Form-IV:</strong> Affix Form-IV (List of Validly Nominated Candidates) in Telugu alphabetical order on the Notice Board immediately upon conclusion of scrutiny.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 4 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">4</span>
            <div>
              <h3>Withdrawals, Form-A & B Verification, Symbol Allotment & Form-VII</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Deadline: 19.11.2026 3:00 PM | Free vs Reserved Symbols | Uncontested Declaration</p>
            </div>
          </div>
          <span class="stage-date-tag">18.11.2026 to 19.11.2026</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Withdrawal & Political Party Form-B</h4>
              <ul class="guideline-points">
                <li><strong>Notice of Withdrawal (Form-V):</strong> Must be signed by the candidate and delivered in person to the EO before <strong>3:00 PM on 19.11.2026</strong>. If candidate is unable, his proposer or authorised election agent may deliver.</li>
                <li><strong>Irrevocable:</strong> A notice of withdrawal, once submitted, CANNOT be cancelled or withdrawn under any circumstances. Issue Form-V receipt immediately.</li>
                <li><strong>Publication:</strong> Publish Form-VI (Notice of Withdrawals) on the notice board after receipt.</li>
                <li><strong>Political Party Form-B Deadline:</strong> Form-B from the authorized party signatory must reach the EO before <strong>3:00 PM on 19.11.2026</strong>. Form-A must have been submitted to Collector & DEA before 5 PM on 16.11.2026.</li>
                <li><strong>Substitution of Form-B:</strong> If a revised Form-B is submitted, it must specifically state that the earlier Form-B is rescinded. If two Form-Bs are received without rescission, the candidate whose nomination was delivered first gets the symbol.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Allotment of Symbols & Form-VII</h4>
              <ul class="guideline-points">
                <li><strong>Three Distinct Categories:</strong>
                  <br>• Category 1: Candidates of Recognized National & State Parties (Reserved party symbol).
                  <br>• Category 2: Candidates of Registered Political Parties with/without reserved symbols.
                  <br>• Category 3: Independent candidates.
                </li>
                <li><strong>Resolving Symbol Clashes:</strong> If two or more independent candidates seek the same free symbol, the sitting holder gets preference; otherwise decided by drawing lots.</li>
                <li><strong>Form-VII Preparation:</strong> Contesting candidates list prepared in <strong>Telugu alphabetical order of surnames</strong>. Running serial numbers across categories.</li>
                <li><strong>Uncontested Election:</strong> If only ONE valid candidate remains after withdrawal, the EO must immediately declare that candidate duly elected unopposed and send copies to SEC, EA & C&DMA, Collector & DEA, and Municipal Commissioner!</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 5 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">5</span>
            <div>
              <h3>Ballot Paper Printing, Security & Postal Ballots</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">White (Chairperson) & Pink (Ward Member) | NOTA Panel | Postal Ballot Despatch</p>
            </div>
          </div>
          <span class="stage-date-tag">20.11.2026 to 25.11.2026</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Ballot Paper Specifications</h4>
              <ul class="guideline-points">
                <li><strong>Two Types of Ballot Papers:</strong>
                  <br>• <strong>White Wove Paper:</strong> Exclusively used for Chairperson election (Direct Election across all 44 wards).
                  <br>• <strong>Pink Wove Paper:</strong> Exclusively used for Ward Member election in each ward.
                </li>
                <li><strong>NOTA Provision:</strong> None of the Above (NOTA) must be printed as the LAST panel on every ballot paper (both White and Pink).</li>
                <li><strong>Quantity Formula:</strong> Total ward electorate + 10% reserve, rounded to nearest 50. Per polling station requirement rounded to nearest 10.</li>
                <li><strong>Proof-Reading & Strike Order:</strong> The Election Officer must personally proofread the proof at the printing press, check candidate names, Telugu spellings, allotted symbols, and verify serial numbering.</li>
                <li><strong>Security & Custody:</strong> Transport printed ballots under armed police escort to Srikalahasti Municipal Strong Room. Count and sort PS-wise 2 to 3 times before sealing into bundles.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Postal Ballots Protocol</h4>
              <ul class="guideline-points">
                <li><strong>Eligible Categories:</strong> Polling personnel drafted for election duty, service voters & wives, voters under preventive detention.</li>
                <li><strong>Dispatch Deadline:</strong> Postal ballot papers MUST be dispatched within <strong>48 hours</strong> of the last hour of withdrawal (by 21.11.2026, 3:00 PM).</li>
                <li><strong>Postal Ballot Kit:</strong>
                  <br>1. Ballot Paper (Candidate names and party, without symbol + NOTA).
                  <br>2. Form-XI (Declaration by voter).
                  <br>3. Form-XII (Small envelope addressed to EO).
                  <br>4. Form-XIII (Instructions and covering letter).
                </li>
                <li><strong>Marked Electoral Roll Entry:</strong> Write <strong>"P.B."</strong> in red ink against the voter's entry in the marked copy of the electoral roll.</li>
                <li><strong>Receipt Deadline:</strong> Postal ballots must reach the Election Officer before 08:00 AM on Counting Day (30.11.2026). Ballots received late are rejected unopened.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 6 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">6</span>
            <div>
              <h3>P-1 Day Dispatch Operations & Movement to 88 Polling Stations</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Distribution Center | Kit Verification | Route Officers Movement | Setup of PS</p>
            </div>
          </div>
          <span class="stage-date-tag">25.11.2026 (Wednesday - P-1 Day)</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Dispatch Center Operations</h4>
              <ul class="guideline-points">
                <li><strong>Central Distribution:</strong> Presiding Officers (POs) and Assistant Polling Officers (APOs) assemble at Central Distribution Center at Srikalahasti.</li>
                <li><strong>Verification of Polling Kit:</strong> Check all statutory items before leaving the counter:
                  <br>• Ballot Boxes (inspect hinges, locking mechanism, cleanliness).
                  <br>• White Ballot Papers (Chairperson) & Pink Ballot Papers (Ward Member) - verify serial numbers!
                  <br>• 4 copies of Electoral Roll (1 Marked Copy + 3 Working Copies).
                  <br>• Distinguishing Mark Stamp (ULB Code - Ward No / PS No).
                  <br>• Arrow Cross-Mark Rubber Stamps & Purple Stamp Pads.
                  <br>• Indelible Ink phials (check liquid level and cap tightness).
                  <br>• Green Paper Seals, Address Tags, Brass Seal & Sealing Wax.
                  <br>• Presiding Officer's Diary, Ballot Paper Account Form-X-C, and Forms XIV, XV, XVI, XVII.
                </li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Movement & Polling Station Setup</h4>
              <ul class="guideline-points">
                <li><strong>Route Movement:</strong> Polling parties board allotted vehicles along the <strong>9 designated routes</strong> under Route Officers and Zonal Officers.</li>
                <li><strong>Arrival at PS:</strong> Report arrival to Municipal Control Room / Zonal Officer immediately.</li>
                <li><strong>Physical Setup of Polling Station:</strong>
                  <br>• Layout ensures strict one-way flow (Entry → Polling Officer 1 → Polling Officer 2 & 3 → Voting Compartment → Ballot Box → Exit).
                  <br>• Voting Compartment must ensure complete secrecy; adequate lighting for viewing candidate symbols.
                  <br>• Affix Form-VII Candidate Posters and Area Notice outside the building.
                  <br>• Ensure 100-meter and 200-meter security perimeter markings.
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 7 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">7</span>
            <div>
              <h3>Polling Day Operations (P-0) — Mock Poll, Voting & Close of Poll</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">06:00 AM Agent Check | 07:00 AM to 05:00 PM Poll | Sealing of Box Slit | Form-X-C</p>
            </div>
          </div>
          <span class="stage-date-tag">26.11.2026 (Thursday - Poll Day)</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Morning Preparations & Box Sealing</h4>
              <ul class="guideline-points">
                <li><strong>06:00 AM — Polling Agents Seating:</strong> Verify Form-IX appointment letters. Agents must be electors of the same/neighbouring PS. Maximum 1 agent + 2 relief agents per candidate allowed.</li>
                <li><strong>06:30 AM — Box Demonstration & Sealing:</strong>
                  <br>• Demonstrate to agents that the ballot box is completely empty.
                  <br>• Secure the Green Paper Seal across the window; allow agents to note the seal number and sign on the white back.
                  <br>• Insert the Address Tag inside the box.
                  <br>• Close and lock the box; seal outer latch with wire, address tag, and PO's brass seal. Allow agents to add their private seals.
                </li>
                <li><strong>Distinguishing Mark Stamping:</strong> Presiding Officer must stamp the Distinguishing Mark Stamp and sign in full on the REVERSE of each ballot paper before issuance.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Poll Duties & 5:00 PM Close</h4>
              <ul class="guideline-points">
                <li><strong>07:00 AM — Poll Commencement:</strong> Announce the start of poll promptly at 7:00 AM.</li>
                <li><strong>Voting Procedure:</strong>
                  <br>• PO-1: Identifies elector with EPIC / approved ID, calls out name, underlines entry in marked roll (tick for female).
                  <br>• PO-2: Applies Indelible Ink on the left forefinger from tip to cuticle, takes signature/thumb impression in register, issues White & Pink ballot papers folded vertically then horizontally.
                  <br>• Voting Compartment: Voter marks with arrow cross-mark stamp in candidate's column, refolds ballot, and inserts into the Ballot Box.
                </li>
                <li><strong>05:00 PM Queue Slips:</strong> Exactly at 5:00 PM, PO distributes numbered slips signed by PO from the LAST person in queue to the first. Only electors with slips are allowed to vote.</li>
                <li><strong>Box Slit Sealing:</strong> Close and seal the ballot box slit with address tag and brass seal in full view of polling agents.</li>
                <li><strong>Statutory Accounts:</strong> Complete Presiding Officer Diary and Form-X-C (Ballot Paper Account Part-I). Give an attested copy of Form-X-C to every polling agent present!</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 8 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">8</span>
            <div>
              <h3>Reception Center Protocol & Strong Room Double-Locking</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Reception = Counting Center | Floor Squares PS-wise | 4-Color Packet Verification</p>
            </div>
          </div>
          <span class="stage-date-tag">26.11.2026 (Evening & Night)</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Ward-Wise Reception Desks</h4>
              <ul class="guideline-points">
                <li><strong>Direct Reception:</strong> Reception Centre is located at the designated Counting Centre. No transit reception centers allowed!</li>
                <li><strong>Floor Squares Marked PS-wise:</strong> Predetermined square spaces marked on the floor for each of the 88 polling stations.</li>
                <li><strong>Verification of Handover:</strong>
                  <br>1. Check intact seals of Ballot Box (slit seal, green paper seal, address tags).
                  <br>2. Receive Form-X-C (Ballot Paper Account) and PO Diary separately.
                  <br>3. Check 4 Colour-Coded Covers: BROWN, GREEN, YELLOW, and BLUE.
                </li>
                <li><strong>Issue Acknowledgement:</strong> Hand over formal printed receipt/acknowledgement to the Presiding Officer and relieve the polling party.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Strong Room Sealing & Security</h4>
              <ul class="guideline-points">
                <li><strong>Transfer into Strong Room:</strong> Move sealed ballot boxes and Brown/Green covers into the Ward-wise bays inside the Strong Room.</li>
                <li><strong>Double-Lock Protocol:</strong> Strong room secured with double locks. One key with the District Election Authority / Designated Officer, second key with the Municipal Commissioner / EO.</li>
                <li><strong>Multi-Tier Security:</strong> Continuous 24/7 armed police guard + CCTV webcasting coverage (feeds preserved).</li>
                <li><strong>Logbook Maintenance:</strong> Any authorized entry into the corridor must be logged with date, time, reason, and signatures.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Stage 9 -->
      <div class="stage-box">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">9</span>
            <div>
              <h3>Counting of Votes, 15-Minute Recount Rule & Declaration of Results</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">Postal First | Bundles of 25 & Drum Mixing | 100-Ballot Trays | Form-XX Result Sheet</p>
            </div>
          </div>
          <span class="stage-date-tag">30.11.2026 (From 08:00 AM)</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Counting Stages & Adjudication</h4>
              <ul class="guideline-points">
                <li><strong>08:00 AM — Secrecy & Postal Ballots:</strong> Read out Section 343-F (Secrecy of Voting). Begin counting postal ballots at EO's table. Defective Form-XI declarations rejected unopened.</li>
                <li><strong>Stage I — Box Verification & Bundling:</strong> Open boxes PS-wise. Verify seals with counting agents. Unfold ballot papers and make bundles of <strong>25 ballots</strong> each. Tally count with Form-X-C Part-I. Mix all bundles thoroughly in a large mixing drum!</li>
                <li><strong>Stage II — Sorting into Trays:</strong> Draw 40 bundles (1,000 ballots) at random per round. Sort into candidate trays + NOTA + 1 Doubtful tray. Valid votes tied in bundles of <strong>100 ballots</strong>.</li>
                <li><strong>Adjudication of Doubtful Ballots:</strong> The Election Officer MUST personally adjudicate each doubtful ballot. Grounds for rejection: identifying mark, no mark, marked for >1 candidate, spurious/mutilated, lacks distinguishing stamp or PO's signature.</li>
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Recount Window & Declaration</h4>
              <ul class="guideline-points">
                <li><strong>Mandatory 15-Minute Recount Pause:</strong> After totaling all votes in Form-XX Part-I, the EO must announce the candidate-wise votes scored and <strong>PAUSE for exactly 15 minutes</strong>. Allow candidates/agents to submit written recount requests.</li>
                <li><strong>Recount Decision:</strong> EO decides on grounds, records reasons in writing, and amends result sheet if allowed. <em>NO recount request can be entertained once Form-XX Part-I is signed!</em></li>
                <li><strong>Tie-Breaking by Lot:</strong> In case of equality of votes, 5 slips per candidate placed in a box; the first drawn slip is declared elected.</li>
                <li><strong>Result Declaration:</strong> Form-XX Part-II signed and declared. Issue Certificate of Election. Transmit immediate copies to APSEC, EA & C&DMA, Collector & DEA, and Municipal Commissioner.</li>
                <li><strong>Safe Storage:</strong> Sealed candidate-wise valid and rejected ballots packed into steel trunks and deposited in Government Sub-Treasury under double lock.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- TAB 3: CHECKLISTS -->
    <div id="tab-checklists" class="tab-content">
      <h2 class="section-title">Interactive Stage Checklists</h2>
      <p class="section-sub">Tick off completed duties at each stage. Progress is saved automatically to your device for field reference.</p>

      <div class="checklist-controls">
        <div class="progress-bar-container">
          <div class="progress-bar-label">
            <span>Overall Readiness Progress</span>
            <span id="chkProgressPercent">0% Completed (0/40)</span>
          </div>
          <div class="progress-bar">
            <div id="chkProgressBar" class="progress-fill"></div>
          </div>
        </div>
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn btn-secondary" onclick="resetChecklist()">Reset All</button>
          <button class="btn btn-success" onclick="window.print()">Print Checklist</button>
        </div>
      </div>

      <!-- Checklist 1: Pre-Notification & Office Setup -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 1: Pre-Notification & Office Infrastructure Readiness</h3>
          <span class="tag-badge tag-ur">Pre-Poll</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c1">
            <div class="chk-content">
              <div class="chk-title">Ward Electoral Roll Verified & Displayed</div>
              <div class="chk-sub">Updated ward-wise voter rolls displayed on Municipal Notice Board and conspicuous places in each ward under Rule 5.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c2">
            <div class="chk-content">
              <div class="chk-title">Election Notice (Form-1) Published</div>
              <div class="chk-sub">Notice in English & Telugu published before nominations open, specifying offices, reservations, dates, and cluster rooms under Rule 6.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c3">
            <div class="chk-content">
              <div class="chk-title">12 Cluster Election Offices Established & Staffed</div>
              <div class="chk-sub">Chairperson Office + 11 Ward-Cluster Offices furnished with tables, barriers, clocks, running serial registers, and designated supporting staff.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c4">
            <div class="chk-content">
              <div class="chk-title">Blank Nomination Papers & Form-IA Stock Ready</div>
              <div class="chk-sub">Sufficient printed sets of nomination forms, Form-IA (symbols), Form-II (caste), and Antecedents declaration formats available free of cost.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c5">
            <div class="chk-content">
              <div class="chk-title">100m Security Perimeter & CCTV Activated</div>
              <div class="chk-sub">Barricades erected at 100 meters from election offices; 1 vehicle rule enforced; video recording arranged for receipt counters.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 2: Nominations Receipt -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 2: Receipt & Verification of Nominations (14–16 Nov, 11 AM–3 PM)</h3>
          <span class="tag-badge tag-ur">Nominations</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c6">
            <div class="chk-content">
              <div class="chk-title">Strict 11:00 AM to 3:00 PM Timing Enforced</div>
              <div class="chk-sub">Nominations accepted only within official hours. At 3:00 PM on 16.11.2026, doors closed; slips given to persons present inside.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c7">
            <div class="chk-content">
              <div class="chk-title">Personal Delivery by Candidate or Proposer</div>
              <div class="chk-sub">Nomination presented in person by candidate or proposer only (max 3 persons inside). Not by post or unauthorized messenger.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c8">
            <div class="chk-content">
              <div class="chk-title">Proposer & Elector Roll Entry Verification</div>
              <div class="chk-sub">Ward Member proposer verified as registered elector in that specific ward; Chairperson proposer verified as elector in municipality.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c9">
            <div class="chk-content">
              <div class="chk-title">Statutory Security Deposit Collected</div>
              <div class="chk-sub">Rs. 3,000/- for General; Rs. 1,500/- for SC/ST/BC with community certificate. Official receipt issued; cash/challan accounted.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c10">
            <div class="chk-content">
              <div class="chk-title">Mandatory Declaration on Antecedents & Assets Filed</div>
              <div class="chk-sub">Declaration attested by two witnesses; checked that no column is left blank (must write 'Nil' or 'Not applicable').</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c11">
            <div class="chk-content">
              <div class="chk-title">Running Serial Number, Date & Minute Initialed</div>
              <div class="chk-sub">Officer initials each page, notes exact time, issues Form-I receipt and notice of scrutiny, endorses checklist duplicate.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c12">
            <div class="chk-content">
              <div class="chk-title">Daily Notice & Consolidated Form-III Affixed</div>
              <div class="chk-sub">Daily list posted after 3 PM; final consolidated Form-III published immediately after 3:00 PM on 16.11.2026.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 3: Scrutiny Day -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 3: Scrutiny Day Quasi-Judicial Proceedings (17 Nov, 11 AM)</h3>
          <span class="tag-badge tag-ur">Scrutiny</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c13">
            <div class="chk-content">
              <div class="chk-title">Conducted Personally by Election Officer</div>
              <div class="chk-sub">Election Officer presides personally at the notified place. AEO acts only if EO is unavoidably prevented.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c14">
            <div class="chk-content">
              <div class="chk-title">Regulated Admission into Scrutiny Room</div>
              <div class="chk-sub">Only Candidate, Election Agent, Proposer, and ONE authorised representative allowed. General public excluded.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c15">
            <div class="chk-content">
              <div class="chk-title">Verification of Crucial Age (21+ Years) & Qualifications</div>
              <div class="chk-sub">Candidate has completed 21 years on date of scrutiny; enrolled in municipality roll; no statutory disqualification under Sec 13–15.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c16">
            <div class="chk-content">
              <div class="chk-title">Substantial Character Rule Applied</div>
              <div class="chk-sub">No rejection on grounds of clerical or technical defect. Full opportunity (up to next day) given to rebut objections.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c17">
            <div class="chk-content">
              <div class="chk-title">Reasoned Orders Recorded & Form-IV Published</div>
              <div class="chk-sub">Reasons recorded on nomination; copy of rejection order given to candidate; Form-IV list of valid candidates published.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 4: Withdrawals & Symbol Allotment -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 4: Withdrawals, Form-B & Contesting List Form-VII (18–19 Nov)</h3>
          <span class="tag-badge tag-ur">Withdrawal & Symbols</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c18">
            <div class="chk-content">
              <div class="chk-title">Withdrawal Notice (Form-V) Delivered before 3:00 PM</div>
              <div class="chk-sub">Delivered in person by candidate/proposer/auth agent. Form-V receipt issued; Form-VI notice affixed. Irrevocable once given.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c19">
            <div class="chk-content">
              <div class="chk-title">Political Party Form-B Verified before 3:00 PM</div>
              <div class="chk-sub">Form-B delivered by party to EO before 3 PM on 19.11.2026; Form-A confirmed from Collector & DEA.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c20">
            <div class="chk-content">
              <div class="chk-title">Allotment of Symbols (3 Categories)</div>
              <div class="chk-sub">Category 1 (Recognised), Category 2 (Registered), Category 3 (Independents). Clashes resolved by lot / sitting holder.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c21">
            <div class="chk-content">
              <div class="chk-title">Form-VII Prepared in Telugu Alphabetical Order</div>
              <div class="chk-sub">Telugu alphabetical order of surnames. Copies supplied to candidates, posted on notice board, and sent to press.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c22">
            <div class="chk-content">
              <div class="chk-title">Uncontested Candidate Declaration (If Applicable)</div>
              <div class="chk-sub">If single candidate remains, declare elected unopposed forthwith and inform SEC, C&DMA, Collector & DEA, and Municipal Commissioner.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 5: P-1 Day Dispatch Operations -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 5: P-1 Dispatch Operations & Polling Kits Verification (25 Nov)</h3>
          <span class="tag-badge tag-ur">P-1 Day</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c23">
            <div class="chk-content">
              <div class="chk-title">Ballot Boxes Inspected & Verified</div>
              <div class="chk-sub">Locking mechanism, hinges, cleanliness, and outer seals checked for all boxes allotted to 88 polling stations.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c24">
            <div class="chk-content">
              <div class="chk-title">Ballot Papers Handover (White & Pink)</div>
              <div class="chk-sub">Consecutive serial numbers checked: White (Chairperson) & Pink (Ward Member). Quantities match PS voter roll + reserve.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c25">
            <div class="chk-content">
              <div class="chk-title">Statutory Stationery & Indelible Ink Check</div>
              <div class="chk-sub">4 copies of rolls (1 marked), Distinguishing Stamp, Arrow stamps, Purple pads, Indelible ink phials, Green paper seals, Brass seal.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c26">
            <div class="chk-content">
              <div class="chk-title">4 Colour-Coded Covers Received</div>
              <div class="chk-sub">BROWN (Box/Statutory accounts), GREEN (Statutory), YELLOW (Non-statutory), BLUE (Plain stationery/ink/metal seal).</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c27">
            <div class="chk-content">
              <div class="chk-title">Movement along 9 Routes & PS Setup Confirmed</div>
              <div class="chk-sub">Party accompanied by Route Officer to station; voting compartment setup for secrecy; arrival reported to Control Room.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 6: Polling Day Operations -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 6: Polling Day (P-0) Voting & Sealing (26 Nov, 7 AM–5 PM)</h3>
          <span class="tag-badge tag-poll">Poll Day</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c28">
            <div class="chk-content">
              <div class="chk-title">06:00 AM — Polling Agents Verified & Seated</div>
              <div class="chk-sub">Form-IX verified; duplicate signed and returned to agent; max 1 agent + 2 relief per candidate allowed.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c29">
            <div class="chk-content">
              <div class="chk-title">06:30 AM — Empty Box Demonstrated & Sealed</div>
              <div class="chk-sub">Empty box shown; green paper seal inserted; serial number noted by agents; box locked, address tag tied, brass seal affixed.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c30">
            <div class="chk-content">
              <div class="chk-title">Distinguishing Mark & PO Signature on Reverse</div>
              <div class="chk-sub">Every ballot paper stamped with distinguishing mark and signed in full by PO on the back before issue to elector.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c31">
            <div class="chk-content">
              <div class="chk-title">07:00 AM — Prompt Poll Commencement & Turnout Reports</div>
              <div class="chk-sub">Poll started at 7:00 AM; ink applied on left forefinger; periodic 2-hourly turnout reported to Sector/Control Room.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c32">
            <div class="chk-content">
              <div class="chk-title">05:00 PM — Queue Slips Distribution & Slit Sealing</div>
              <div class="chk-sub">Numbered slips issued from back of queue at 5:00 PM; poll closed; box slit sealed in presence of agents; Form-X-C completed.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 7: Reception & Strong Room -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 7: Reception Center & Strong Room Handover (26 Nov Night)</h3>
          <span class="tag-badge tag-ur">Reception</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c33">
            <div class="chk-content">
              <div class="chk-title">Ballot Box Seals Verified at PS Floor Square</div>
              <div class="chk-sub">Intact slit seal, green paper seal, and address tags checked by Receiving Officer at the designated PS floor square.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c34">
            <div class="chk-content">
              <div class="chk-title">Form-X-C & PO Diary Separately Received</div>
              <div class="chk-sub">Ballot Paper Account (Form-X-C Part-I) and Presiding Officer's Diary verified against polled totals.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c35">
            <div class="chk-content">
              <div class="chk-title">4 Colour-Coded Covers Verified</div>
              <div class="chk-sub">Brown cover (accounts/marked roll), Green (statutory), Yellow (non-statutory), Blue (stationery/metal seals).</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c36">
            <div class="chk-content">
              <div class="chk-title">Strong Room Deposited & Double-Locked</div>
              <div class="chk-sub">Boxes and covers deposited ward-wise; double lock locked in presence of candidates/agents; CCTV recording continuous.</div>
            </div>
          </label>
        </div>
      </div>

      <!-- Checklist 8: Counting Day -->
      <div class="card">
        <div class="card-header">
          <h3>📋 Checklist 8: Counting Day Table Management & Adjudication (30 Nov)</h3>
          <span class="tag-badge tag-counting">Counting Day</span>
        </div>
        <div class="checklist-items">
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c37">
            <div class="chk-content">
              <div class="chk-title">Sec. 343-F Read Out & Postal Ballots Counted First</div>
              <div class="chk-sub">Secrecy provision announced; postal ballot box opened first at EO table; Form-XI checked; invalid declarations rejected.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c38">
            <div class="chk-content">
              <div class="chk-title">25-Ballot Bundling & Mixing in Drum (Stage I)</div>
              <div class="chk-sub">Ballot boxes opened PS-wise; tally with Form-X-C; bundled into 25s; mixed thoroughly in large drum.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c39">
            <div class="chk-content">
              <div class="chk-title">1,000-Ballot Rounds & 100-Bundle Trays (Stage II)</div>
              <div class="chk-sub">40 bundles (1,000 ballots) drawn per round; sorted into candidate trays + NOTA; bundled into 100s; doubtful to EO.</div>
            </div>
          </label>
          <label class="chk-item">
            <input type="checkbox" onchange="updateChecklist(this)" data-id="c40">
            <div class="chk-content">
              <div class="chk-title">Mandatory 15-Minute Recount Window & Form-XX Declaration</div>
              <div class="chk-sub">Announce totals; wait 15 minutes for recount petitions; decide before signing; sign Form-XX Part-I & II; seal steel trunks into Treasury.</div>
            </div>
          </label>
        </div>
      </div>

    </div>

    <!-- TAB 4: IMPORTANT GUIDELINES -->
    <div id="tab-guidelines" class="tab-content">
      <h2 class="section-title">Important Guidelines for Election Officers</h2>
      <p class="section-sub">Simple, actionable principles governing legal compliance, polling day management, counting, and expenditure audit.</p>

      <div class="grid-2">
        <div class="guideline-card">
          <h3>⚖️ 1. Legal Authority & Appointment</h3>
          <ul class="guideline-points">
            <li><strong>Superintendence:</strong> Under Article 243-ZA and Sec. 10-A of the AP Municipalities Act, 1965, full authority vests in the State Election Commission.</li>
            <li><strong>Election Officer (EO):</strong> Appointed under Rule 3 of the Conduct of Election Rules, 2026 (G.O.Ms.No.213). EO must be a Gazetted Officer.</li>
            <li><strong>Ward Cluster:</strong> In Srikalahasti, 1 EO covers a cluster of 4 wards (Wards 1-4, 5-8, 9-12, etc.), plus 1 dedicated office for Chairperson.</li>
            <li><strong>Subordination & Control:</strong> Supporting staff (Ward Secretaries) are under the direct administrative control and disciplinary power of the EO till election completion.</li>
          </ul>
        </div>

        <div class="guideline-card">
          <h3>📝 2. Nominations & Proposers</h3>
          <ul class="guideline-points">
            <li><strong>Proposer Rule is Strict:</strong> For a Ward Member candidate, the proposer MUST be an elector in that exact ward. For Chairperson, the proposer can be an elector anywhere in the municipality.</li>
            <li><strong>One Proposer, One Nomination:</strong> If an elector proposes multiple candidates in the same ward, only the first nomination delivered is valid; subsequent ones are invalid.</li>
            <li><strong>Deposit Protection:</strong> SC, ST, and BC candidates pay only Rs. 1,500/- even when contesting an unreserved (general) seat!</li>
            <li><strong>Affidavit / Declaration:</strong> Must be signed by candidate, attested by 2 witnesses. No field left blank — write 'Nil' or 'Not Applicable'.</li>
          </ul>
        </div>

        <div class="guideline-card">
          <h3>🔍 3. Scrutiny Quasi-Judicial Principles</h3>
          <ul class="guideline-points">
            <li><strong>Summary Enquiry:</strong> Scrutiny is a summary enquiry. The EO does not sit as a regular civil court.</li>
            <li><strong>Presumption in Favour of Candidature:</strong> A nomination paper should be accepted unless there is clear, substantial statutory disqualification.</li>
            <li><strong>Technical Defects Ignored:</strong> Minor spelling errors in names, discrepancy in father's name, or serial number mismatch where identity is clear must NOT be grounds for rejection.</li>
            <li><strong>Right to Rebut:</strong> If an objection is raised against a candidate, the EO must allow the candidate time up to 11:00 AM the next day to rebut.</li>
          </ul>
        </div>

        <div class="guideline-card">
          <h3>🗳️ 4. Ballot Paper & Boxes Protocol</h3>
          <ul class="guideline-points">
            <li><strong>Color Differentiation:</strong> White Wove paper for Chairperson; Pink Wove paper for Ward Members.</li>
            <li><strong>Distinguishing Mark:</strong> Presiding Officer must stamp the distinguishing mark (e.g., SKHT-W5/PS1) and sign the back of every ballot paper before issuing.</li>
            <li><strong>Box Slit Sealing:</strong> Close and seal the ballot box slit at 5:00 PM (or when last slip holder votes) in full view of polling agents.</li>
            <li><strong>Paper Seal Account:</strong> Complete Part-I of Form-X-C accounting for all green paper seals used, damaged, and unused.</li>
          </ul>
        </div>

        <div class="guideline-card">
          <h3>👥 5. Polling Day Special Cases</h3>
          <ul class="guideline-points">
            <li><strong>Challenged Votes (Rule 36):</strong> Agent deposits Rs. 5/- fee. PO conducts summary enquiry. If challenge established, debar voter and report to police. If refuted, allow vote and forfeit deposit. Maintain Form-XIV & XV.</li>
            <li><strong>Blind / Infirm Voters:</strong> Companion allowed (must be 18+ years, cannot accompany more than one voter). Record declaration in Form-XVII.</li>
            <li><strong>Tendered Votes (Rule 42):</strong> If a person presents himself and finds his vote already cast, verify identity. Issue a Tendered Ballot Paper (do NOT put into box). Voter marks ballot, hands to PO, kept in Tendered Votes cover (Form-XVI).</li>
            <li><strong>ASD List Check:</strong> Check Absent, Shifted, and Dead (ASD) list thoroughly. If elector appears, verify EPIC, take signature & thumbprint, and record in PO Diary.</li>
          </ul>
        </div>

        <div class="guideline-card">
          <h3>📊 6. Counting & Recount Rules</h3>
          <ul class="guideline-points">
            <li><strong>Drum Mixing:</strong> Unfolded ballots bundled in 25s must be mixed in the drum. This prevents polling station-wise voter trend leakage and protects secrecy.</li>
            <li><strong>Doubtful Ballot Personal Decision:</strong> Only the Election Officer has the legal authority to accept or reject doubtful votes. Counting supervisors cannot reject!</li>
            <li><strong>15-Minute Pause is Mandatory:</strong> After recording totals on Form-XX Part-I, the EO MUST announce results and pause for 15 minutes. Deciding recount petitions is mandatory before signing.</li>
            <li><strong>Secrecy Breach:</strong> Violation of secrecy by any officer, agent, or clerk is punishable with imprisonment up to 3 months or fine under Sec. 343-F.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 5: DO'S AND DON'TS -->
    <div id="tab-dodont" class="tab-content">
      <h2 class="section-title">Do's and Don'ts for Election Functionaries</h2>
      <p class="section-sub">Clear compliance directives for Election Officers, Presiding Officers, Polling Agents, and Field Teams.</p>

      <!-- Category 1: Election Officers & AEOs -->
      <div class="card">
        <div class="card-header">
          <h3>👨‍💼 1. For Election Officers (EOs) & Assistant Election Officers (AEOs)</h3>
          <span class="tag-badge tag-ur">Election Offices</span>
        </div>
        <div class="dodont-grid">
          <div class="dodont-card dos">
            <div class="dodont-title">DO's (Mandatory Actions)</div>
            <ul class="dodont-list">
              <li>Adhere strictly to the 11:00 AM to 3:00 PM window for receipt of nominations on all notified days.</li>
              <li>Affix running serial number, exact date, and minute of receipt on every nomination paper immediately.</li>
              <li>Provide duplicate checklist with Form-I receipt and notice of scrutiny to candidate/proposer.</li>
              <li>Conduct scrutiny personally; examine all 4 sets filed by a candidate even if the first set is valid.</li>
              <li>Give reasonable time up to 11:00 AM the next day if a candidate needs to rebut an objection.</li>
              <li>Verify Form-A (from Collector) and Form-B (from Party) before allotting reserved party symbols.</li>
              <li>Pause for exactly 15 minutes after announcing counting totals to receive recount petitions.</li>
            </ul>
          </div>
          <div class="dodont-card donts">
            <div class="dodont-title">DON'Ts (Prohibited Actions)</div>
            <ul class="dodont-list">
              <li>Do NOT accept nominations sent by post, email, WhatsApp, or through unauthorized messengers.</li>
              <li>Do NOT accept nominations after 3:00 PM on 16.11.2026 under any circumstances.</li>
              <li>Do NOT delegate the scrutiny process to an assistant unless unavoidably prevented.</li>
              <li>Do NOT reject a nomination for clerical, typographical, or technical errors that are not substantial.</li>
              <li>Do NOT allow candidates or agents to physically handle other candidates' nomination papers.</li>
              <li>Do NOT entertain any withdrawal notice received after 3:00 PM on 19.11.2026.</li>
              <li>Do NOT sign Form-XX Part-I without observing the mandatory 15-minute recount pause.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Category 2: Presiding Officers & Polling Parties -->
      <div class="card">
        <div class="card-header">
          <h3>🗳️ 2. For Presiding Officers (POs) & Polling Teams</h3>
          <span class="tag-badge tag-poll">Polling Stations</span>
        </div>
        <div class="dodont-grid">
          <div class="dodont-card dos">
            <div class="dodont-title">DO's (Mandatory Actions)</div>
            <ul class="dodont-list">
              <li>Demonstrate the empty ballot box to all polling agents present at 06:30 AM before sealing.</li>
              <li>Record Green Paper Seal numbers and allow polling agents to note and sign on the white back.</li>
              <li>Stamp Distinguishing Mark and sign in full on the reverse of every White and Pink ballot paper.</li>
              <li>Ensure Indelible Ink is applied on the left forefinger from tip to cuticle before issuing ballot.</li>
              <li>Position voting compartment to ensure absolute secrecy of vote while keeping compartment in view.</li>
              <li>Distribute numbered slips from the back of the queue at 5:00 PM sharp to waiting voters.</li>
              <li>Seal the box slit immediately after the last slip holder votes and furnish Form-X-C copy to agents.</li>
            </ul>
          </div>
          <div class="dodont-card donts">
            <div class="dodont-title">DON'Ts (Prohibited Actions)</div>
            <ul class="dodont-list">
              <li>Do NOT commence poll before 7:00 AM or delay poll commencement for absent agents.</li>
              <li>Do NOT allow any voter to leave the polling station without the indelible ink mark.</li>
              <li>Do NOT put tendered ballot papers into the ballot box; keep them in the designated Form-XVI cover.</li>
              <li>Do NOT allow polling agents to take copies of the marked electoral roll outside the room.</li>
              <li>Do NOT permit mobile phones, cameras, or recording devices inside the voting compartment.</li>
              <li>Do NOT mix statutory and non-statutory covers; pack strictly into Brown, Green, Yellow, Blue covers.</li>
              <li>Do NOT leave the polling station without taking police escort and route officer coordination.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Category 3: Polling Agents & Candidates -->
      <div class="card">
        <div class="card-header">
          <h3>👥 3. For Polling Agents & Candidates</h3>
          <span class="tag-badge tag-ur">Field Conduct</span>
        </div>
        <div class="dodont-grid">
          <div class="dodont-card dos">
            <div class="dodont-title">DO's (Permitted Actions)</div>
            <ul class="dodont-list">
              <li>Arrive at the polling station by 06:00 AM with valid Form-IX appointment letter and EPIC.</li>
              <li>Inspect empty ballot box during demonstration and note down Green Paper Seal numbers.</li>
              <li>Sign the Green Paper Seal and affix your private seal on the ballot box outer latch if desired.</li>
              <li>Observe voter identification and challenge bogus voters upon paying the Rs. 5/- deposit.</li>
              <li>Receive an attested duplicate copy of Form-X-C (Ballot Paper Account) from the Presiding Officer.</li>
            </ul>
          </div>
          <div class="dodont-card donts">
            <div class="dodont-title">DON'Ts (Prohibited Conduct)</div>
            <ul class="dodont-list">
              <li>Do NOT carry mobile phones, smartwatches, or arms inside the polling station.</li>
              <li>Do NOT wear party badges, caps, scarves, or symbols inside the polling station or within 100m.</li>
              <li>Do NOT canvass, shout slogans, or intimidate voters within the 100-meter polling perimeter.</li>
              <li>Do NOT peek into the voting compartment or interfere with voter privacy.</li>
              <li>Do NOT take the marked electoral roll outside the polling station room.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Category 4: MCC & Surveillance Teams -->
      <div class="card">
        <div class="card-header">
          <h3>🚔 4. For MCC, Flying Squads (FST) & Static Surveillance Teams (SST)</h3>
          <span class="tag-badge tag-ur">Surveillance</span>
        </div>
        <div class="dodont-grid">
          <div class="dodont-card dos">
            <div class="dodont-title">DO's (Field Operations)</div>
            <ul class="dodont-list">
              <li>Operate in strict 12-hour shifts: Shift 1 (8 AM – 8 PM) and Shift 2 (8 PM – 8 AM).</li>
              <li>Maintain continuous video recording of vehicle checks and seizures at SST checkpoints.</li>
              <li>Seize cash exceeding Rs. 50,000/- or liquor/freebies carried without valid documented proof.</li>
              <li>Issue formal seizure panchanama and deposit seized items with District Treasury/Nodal Officer.</li>
              <li>Respond within 15 minutes to any MCC complaint reported through control room.</li>
            </ul>
          </div>
          <div class="dodont-card donts">
            <div class="dodont-title">DON'Ts (Restricted Actions)</div>
            <ul class="dodont-list">
              <li>Do NOT harass common citizens, commercial travelers, or patients carrying legitimate money.</li>
              <li>Do NOT conduct checks or seizures without videography by the designated Video Surveillance Team.</li>
              <li>Do NOT release seized cash or goods on your own authority without the District Grievance Committee.</li>
              <li>Do NOT leave your designated static checkpoint (AP Tourism / Nandi Circle) unattended during shift.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: FORMS & PROFORMAS REPOSITORY -->
    <div id="tab-forms" class="tab-content">
      <h2 class="section-title">Statutory & Non-Statutory Forms Repository</h2>
      <p class="section-sub">Prescribed templates under AP Municipalities Act, 1965 and Conduct of Election Rules, 2026. Click 'Preview' to view full standard text or 'Copy' to use.</p>

      <div class="search-bar-wrap">
        <input type="text" id="formSearchInput" class="search-input" placeholder="🔍 Search forms by name, number, or stage (e.g. Form-X-C, Form-VII, Withdrawal, Agent)..." oninput="filterForms()">
      </div>

      <div class="forms-grid" id="formsContainer">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- TAB 7: SRIKALAHASTI FIELD DIRECTORY -->
    <div id="tab-directory" class="tab-content">
      <h2 class="section-title">Srikalahasti Municipality Field Directory</h2>
      <p class="section-sub">Ward reservations, 88 Polling Stations with GIS coordinates & voter counts, 12 Cluster Offices, Zonal & Route Officers, and Surveillance Teams.</p>

      <!-- Key Authorities Card -->
      <div class="card">
        <div class="card-header">
          <h3>🏛️ Key Statutory Authorities & Election Leadership</h3>
          <span class="tag-badge tag-ur">HQ Leadership</span>
        </div>
        <div class="grid-3">
          <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
            <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">State Election Commissioner</div>
            <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Sri Anil Chandra Punetha, IAS (Retd)</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">AP State Election Commission, Vijayawada</div>
          </div>
          <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
            <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">District Election Authority & Collector</div>
            <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Dr. S. Venkateswar, I.A.S.</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">Tirupati District Collectorate, Tirupati</div>
          </div>
          <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
            <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">Asst. Election Authority & Commissioner</div>
            <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Sri K. V. Krishna Reddy</div>
            <div style="font-size: 0.8rem; color: var(--text-muted);">Srikalahasti Municipality</div>
          </div>
        </div>
      </div>

      <!-- Ward Reservations Summary -->
      <div class="card">
        <div class="card-header">
          <h3>📊 Ward Reservations Master Chart (44 Wards)</h3>
          <span class="tag-badge tag-ur">Gazette Roc. No. 2578/2026/G-1</span>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.85rem;">
          Breakdown: <b>ST: 1</b> (1 Gen) | <b>SC: 4</b> (2 Women, 2 Gen) | <b>BC: 17</b> (8 Women, 9 Gen) | <b>UR: 22</b> (12 Women, 10 Gen) | <b>Total Women Seats: 22 (50%)</b>
        </p>
        <div class="table-container">
          <table class="data-table" id="wardTable">
            <thead>
              <tr>
                <th>Ward No.</th>
                <th>Category</th>
                <th>Reservation Name</th>
                <th>No. of Polling Stations</th>
                <th>Polling Stations</th>
                <th>Total Voters</th>
              </tr>
            </thead>
            <tbody>
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- 12 Ward-Cluster Offices & Supporting Staff -->
      <div class="card">
        <div class="card-header">
          <h3>🏢 12 Ward-Cluster Election Offices & Assigned Staff</h3>
          <span class="tag-badge tag-ur">Roc. No. 2578/2025/G1</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Office / Cluster</th>
                <th>Jurisdiction</th>
                <th>Assigned Supporting Staff</th>
                <th>Designation</th>
                <th>Mobile Number</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="2"><b>Chairperson Office</b></td>
                <td rowspan="2">All 44 Wards (Direct Election)</td>
                <td>G. Nithin Singh</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:9492831594">9492831594</a></td>
              </tr>
              <tr>
                <td>A. Leela Krishna</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:7032027606">7032027606</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 1</b></td>
                <td rowspan="2">Wards 1, 2, 3, 4</td>
                <td>B. Sreepathi</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:8374252079">8374252079</a></td>
              </tr>
              <tr>
                <td>E. Jhansi</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:9030881708">9030881708</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 2</b></td>
                <td rowspan="2">Wards 5, 6, 7, 8</td>
                <td>K. Suresh</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9014566244">9014566244</a></td>
              </tr>
              <tr>
                <td>K. Madhavi</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:7204695000">7204695000</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 3</b></td>
                <td rowspan="2">Wards 9, 10, 11, 12</td>
                <td>T. Suresh</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:8919170382">8919170382</a></td>
              </tr>
              <tr>
                <td>K. Kalpana</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:8897890434">8897890434</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 4</b></td>
                <td rowspan="2">Wards 13, 14, 15, 16</td>
                <td>R. Praveen</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9177203062">9177203062</a></td>
              </tr>
              <tr>
                <td>S. Thasleem</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:7842246142">7842246142</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 5</b></td>
                <td rowspan="2">Wards 17, 18, 19, 20</td>
                <td>D. Jayaprakash</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9966449310">9966449310</a></td>
              </tr>
              <tr>
                <td>K. Siva Kumar</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:7207266773">7207266773</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 6</b></td>
                <td rowspan="2">Wards 21, 22, 23, 24</td>
                <td>K. J. Bhaskar</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:7893111073">7893111073</a></td>
              </tr>
              <tr>
                <td>G. Sai Sunil Kumar</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:7013435085">7013435085</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 7</b></td>
                <td rowspan="2">Wards 25, 26, 27, 28</td>
                <td>D. L. Dilli Priya</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:8074332196">8074332196</a></td>
              </tr>
              <tr>
                <td>Muni Chenchu Latha</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:9701786332">9701786332</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 8</b></td>
                <td rowspan="2">Wards 29, 30, 31, 32</td>
                <td>N. Hema Madhuri</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:9912250707">9912250707</a></td>
              </tr>
              <tr>
                <td>C. Yamini</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:8464077105">8464077105</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 9</b></td>
                <td rowspan="2">Wards 33, 34, 35, 36</td>
                <td>K. Sravani</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9985340635">9985340635</a></td>
              </tr>
              <tr>
                <td>G. Kameswara Rao</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:8328075402">8328075402</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 10</b></td>
                <td rowspan="2">Wards 37, 38, 39, 40</td>
                <td>T. Chandra Reddy</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9640473306">9640473306</a></td>
              </tr>
              <tr>
                <td>K. Bhanu Prakash</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:9154562184">9154562184</a></td>
              </tr>
              <tr>
                <td rowspan="2"><b>Cluster 11</b></td>
                <td rowspan="2">Wards 41, 42, 43, 44</td>
                <td>C. Murali</td>
                <td>Ward Education & Data Processing Secy (WEDPS)</td>
                <td><a href="tel:9885743874">9885743874</a></td>
              </tr>
              <tr>
                <td>Y. Yamuna</td>
                <td>Ward Administrative Secretary (WA)</td>
                <td><a href="tel:8897447071">8897447071</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Zonal & Route Officers -->
      <div class="card">
        <div class="card-header">
          <h3>🗺️ Zonal Officers (3 Zones) & Route Officers (9 Routes)</h3>
          <span class="tag-badge tag-ur">Field Supervision</span>
        </div>
        <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Zonal Officers Directory</h4>
        <div class="table-container" style="margin-bottom: 1.25rem;">
          <table class="data-table">
            <thead>
              <tr>
                <th>Zone</th>
                <th>Zonal Officer</th>
                <th>Designation</th>
                <th>Contact</th>
                <th>Allotted Routes</th>
                <th>Wards Covered</th>
                <th>Total PS</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Zone 01</b></td>
                <td>Dr. P. Venugopal</td>
                <td>Lecturer in Commerce</td>
                <td><a href="tel:9393887222">9393887222</a></td>
                <td>Routes 1, 2, 3</td>
                <td>1, 2, 3, 4, 5, 6, 7; 33, 34, 35, 36, 37; 40, 41, 43, 44</td>
                <td><b>31 PS</b></td>
              </tr>
              <tr>
                <td><b>Zone 02</b></td>
                <td>K. Bhuvaneswari</td>
                <td>Mandal Education Officer</td>
                <td><a href="tel:9618415439">9618415439</a> / <a href="tel:9441592631">9441592631</a></td>
                <td>Routes 4, 6, 7</td>
                <td>38, 39, 40, 42; 11, 12, 13, 14; 8, 9, 10, 15, 16, 20</td>
                <td><b>27 PS</b></td>
              </tr>
              <tr>
                <td><b>Zone 03</b></td>
                <td>K. Bhagya Lakshmi</td>
                <td>Supervisor Gr-II, WD&CW Dept.</td>
                <td><a href="tel:9491000256">9491000256</a></td>
                <td>Routes 5, 8, 9</td>
                <td>17, 18, 24, 26, 28, 29, 30; 19, 21, 22, 23, 25; 31, 32, 27</td>
                <td><b>30 PS</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Route Officers Directory (9 Routes)</h4>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Route</th>
                <th>Route Officer</th>
                <th>Designation</th>
                <th>Contact</th>
                <th>Wards Covered</th>
                <th>Allotted Polling Stations</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Route 1</b></td>
                <td>M. Pardhasaradhi</td>
                <td>WPRS</td>
                <td><a href="tel:8686867365">8686867365</a></td>
                <td>1, 2, 3, 4, 5, 6, 7</td>
                <td>1/1, 1/2, 2/1, 2/2, 3/1, 3/2, 4/1, 4/2, 5/1, 5/2, 6/1, 6/2, 7/1, 7/2 (14 PS)</td>
              </tr>
              <tr>
                <td><b>Route 2</b></td>
                <td>K. Rajendra</td>
                <td>WPRS</td>
                <td><a href="tel:7288936923">7288936923</a></td>
                <td>33, 34, 35, 36, 37</td>
                <td>33/1, 33/2, 34/1, 34/2, 35/1, 35/2, 36/1, 36/2, 37/1, 37/2 (10 PS)</td>
              </tr>
              <tr>
                <td><b>Route 3</b></td>
                <td>NB Prabhakar</td>
                <td>WPRS</td>
                <td><a href="tel:9629297089">9629297089</a></td>
                <td>40, 41, 43, 44</td>
                <td>40/1, 41/1, 41/2, 43/1, 43/2, 44/1, 44/2 (7 PS)</td>
              </tr>
              <tr>
                <td><b>Route 4</b></td>
                <td>Shaik Sulthan Sharief</td>
                <td>WPRS</td>
                <td><a href="tel:9966011817">9966011817</a></td>
                <td>38, 39, 40, 42</td>
                <td>38/1, 38/2, 39/1, 39/2, 40/2, 42/1, 42/2 (7 PS)</td>
              </tr>
              <tr>
                <td><b>Route 5</b></td>
                <td>B. Sai Prasad</td>
                <td>WPRS</td>
                <td><a href="tel:9676006961">9676006961</a></td>
                <td>17, 18, 24, 26, 28, 29, 30</td>
                <td>17/1, 17/2, 18/1, 18/2, 24/1, 24/2, 26/1, 26/2, 28/1, 28/2, 29/1, 29/2, 30/1, 30/2 (14 PS)</td>
              </tr>
              <tr>
                <td><b>Route 6</b></td>
                <td>A. Gireesha</td>
                <td>WPRS</td>
                <td><a href="tel:8919543675">8919543675</a></td>
                <td>11, 12, 13, 14</td>
                <td>11/1, 11/2, 12/1, 12/2, 13/1, 13/2, 14/1, 14/2 (8 PS)</td>
              </tr>
              <tr>
                <td><b>Route 7</b></td>
                <td>C. Pramila</td>
                <td>WPRS</td>
                <td><a href="tel:7036375470">7036375470</a></td>
                <td>8, 9, 10, 15, 16, 20</td>
                <td>8/1, 8/2, 9/1, 9/2, 10/1, 10/2, 15/1, 15/2, 16/1, 16/2, 20/1, 20/2 (12 PS)</td>
              </tr>
              <tr>
                <td><b>Route 8</b></td>
                <td>Vinitha</td>
                <td>WPRS</td>
                <td><a href="tel:7330746514">7330746514</a></td>
                <td>19, 21, 22, 23, 25</td>
                <td>19/1, 19/2, 21/1, 21/2, 22/1, 22/2, 23/1, 23/2, 25/1, 25/2 (10 PS)</td>
              </tr>
              <tr>
                <td><b>Route 9</b></td>
                <td>Chandana</td>
                <td>WPRS</td>
                <td><a href="tel:8096610523">8096610523</a></td>
                <td>31, 32, 27</td>
                <td>31/1, 31/2, 32/1, 32/2, 27/1, 27/2 (6 PS)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Surveillance Teams -->
      <div class="card">
        <div class="card-header">
          <h3>🚔 Model Code of Conduct (MCC), Flying Squads & Static Surveillance Teams</h3>
          <span class="tag-badge tag-ur">Roc. No. 2230/2026</span>
        </div>
        <div class="grid-2">
          <div>
            <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">MCC Enforcement Teams (24/7)</h4>
            <ul class="guideline-points">
              <li><strong>Shift 1 (08:00 AM – 08:00 PM):</strong>
                <br>• Dr. C. Narasimha Reddy, Lecturer in Math, SVA Govt College (Cell: <a href="tel:9441209500">9441209500</a>)
                <br>• Deva Rajulu Vedagiri, Sr Assistant (Cell: <a href="tel:7036371140">7036371140</a>)
                <br>• K. Kranthi, Head Constable 981 (Cell: <a href="tel:9505354981">9505354981</a>)
              </li>
              <li><strong>Shift 2 (08:00 PM – 08:00 AM):</strong>
                <br>• D. Bhaskar, Lecturer in Commerce, SVA Govt College (Cell: <a href="tel:9440095961">9440095961</a>)
                <br>• Anil Kumar Reddy Dappili, Sr Assistant (Cell: <a href="tel:9492320039">9492320039</a>)
                <br>• U. Ramanaiah, Head Constable 789 (Cell: <a href="tel:9440846401">9440846401</a>)
              </li>
            </ul>

            <h4 style="color: var(--secondary); margin: 0.75rem 0 0.5rem 0;">Flying Squad Teams (FST - 24/7)</h4>
            <ul class="guideline-points">
              <li><strong>Shift 1 (08:00 AM – 08:00 PM):</strong>
                <br>• Bharathi, Mandal Education Officer (Cell: <a href="tel:9441573295">9441573295</a>)
                <br>• Narasimhulu Chindukuri, Sr Assistant (Cell: <a href="tel:9989671658">9989671658</a>)
                <br>• M. Ramanaiah, Head Constable 844 (Cell: <a href="tel:9449932821">9449932821</a>)
              </li>
              <li><strong>Shift 2 (08:00 PM – 08:00 AM):</strong>
                <br>• A. Balaiah, Mandal Education Officer (Cell: <a href="tel:9440343503">9440343503</a>)
                <br>• Srinivasulu Valluru, Sr Assistant (Cell: <a href="tel:9441132420">9441132420</a>)
                <br>• S. Subramanyam, Head Constable 758 (Cell: <a href="tel:8074660081">8074660081</a>)
              </li>
            </ul>
          </div>

          <div>
            <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">Static Surveillance Teams (SST Checkpoints)</h4>
            <ul class="guideline-points">
              <li><strong>SST-1: AP Tourism, Srikalahasti</strong>
                <br>• Shift 1: K. Vinith Kumar Reddy, AEO (<a href="tel:8919604708">8919604708</a>), Venkata Subba Reddy Paleti, Sr Asst (<a href="tel:8341337654">8341337654</a>), M. Sankar PC 858 (<a href="tel:9985944940">9985944940</a>)
                <br>• Shift 2: P. Venkata Praveen, AEO (<a href="tel:98499997550">98499997550</a>), Malleswaraiah Obulam, Jr Asst (<a href="tel:8297288918">8297288918</a>), V. Mohan Babu PC 2023 (<a href="tel:9676572238">9676572238</a>)
              </li>
              <li><strong>SST-2: Nandi Circle, Naidupeta Road</strong>
                <br>• Shift 1: K. Jyothsna, AEO (<a href="tel:9515577377">9515577377</a>), Siva Kundla, Jr Asst (<a href="tel:6281525335">6281525335</a>), V. Anil Kumar PC 871 (<a href="tel:8897837877">8897837877</a>)
                <br>• Shift 2: A. Ravi Prasad, AEO (<a href="tel:9533910555">9533910555</a>), Subba Reddy Koppula, Jr Asst (<a href="tel:9551223998">9551223998</a>), P. Hari PC 1811 (<a href="tel:9618664654">9618664654</a>)
              </li>
            </ul>

            <h4 style="color: var(--secondary); margin: 0.75rem 0 0.5rem 0;">Expenditure Audit & Video Surveillance</h4>
            <ul class="guideline-points">
              <li><strong>Expenditure Audit Team 1 (Wards 1–22):</strong> Prabhakar, AAO (<a href="tel:9440667769">9440667769</a>), B. Priyanka, Sr Acct (<a href="tel:7997423413">7997423413</a>)</li>
              <li><strong>Expenditure Audit Team 2 (Wards 23–44):</strong> B. Manohara, JAO (<a href="tel:9491781181">9491781181</a>), C. Balaji, Sr Acct (<a href="tel:8008644256">8008644256</a>)</li>
              <li><strong>Video Surveillance Team (VST):</strong> Ramana, Videographer (<a href="tel:9705518400">9705518400</a>), Ch. Chalamaiah, HC 3898 (<a href="tel:8985272119">8985272119</a>)</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Searchable 88 Polling Stations Directory -->
      <div class="card">
        <div class="card-header">
          <h3>🏫 Polling Stations Directory (All 88 Stations, 72,537 Electors)</h3>
          <span class="tag-badge tag-poll">Search & Filter</span>
        </div>
        <div class="search-bar-wrap">
          <input type="text" id="psSearchInput" class="search-input" placeholder="🔍 Search polling stations by Ward, PS No, School Name, Street, or Area..." oninput="filterPollingStations()">
          <select id="wardFilterSelect" class="search-input" style="max-width: 200px;" onchange="filterPollingStations()">
            <option value="ALL">All Wards (1 to 44)</option>
          </select>
        </div>
        <div class="table-container">
          <table class="data-table" id="psTable">
            <thead>
              <tr>
                <th>Sl No.</th>
                <th>Ward</th>
                <th>PS No.</th>
                <th>Polling Station Building & Name</th>
                <th>Electors</th>
                <th>Geo-Location</th>
              </tr>
            </thead>
            <tbody id="psTableBody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- TAB 8: OFFICER TOOLS & PACKING -->
    <div id="tab-tools" class="tab-content">
      <h2 class="section-title">Officer Field Utilities, Calculators & Packing Guide</h2>
      <p class="section-sub">Field calculators for ballot estimation, queue slip tracking, and color-coded envelope packing protocols.</p>

      <div class="grid-2">
        <!-- Ballot Paper Calculator -->
        <div class="tool-box">
          <h3 style="color: var(--primary); margin-bottom: 0.5rem;">🧮 Ballot Paper Procurement Calculator</h3>
          <p style="font-size: 0.82rem; color: var(--text-muted);">Calculates exact ballot requirements: Ward electorate + 10% reserve rounded to nearest 50; PS requirement rounded to nearest 10 (Slide 22 Ref).</p>
          <div class="calc-input-group">
            <label style="font-size: 0.85rem; font-weight: 600;">Ward / PS Electorate: </label>
            <input type="number" id="calcElectorate" value="750" min="1" max="100000" oninput="calculateBallots()">
            <button class="btn btn-accent" onclick="calculateBallots()">Calculate</button>
          </div>
          <div class="calc-res-box" id="calcResults">
            <!-- Rendered by JS -->
          </div>
        </div>

        <!-- Queue Slips Manager -->
        <div class="tool-box">
          <h3 style="color: var(--primary); margin-bottom: 0.5rem;">🎟️ 05:00 PM Queue Slip Numbering Guide</h3>
          <p style="font-size: 0.82rem; color: var(--text-muted);">Generates distribution sequence: Slips must be issued from the LAST person standing in queue to the first person.</p>
          <div class="calc-input-group">
            <label style="font-size: 0.85rem; font-weight: 600;">Electors in Queue at 5 PM: </label>
            <input type="number" id="queueVoters" value="45" min="1" max="500" oninput="generateQueueSlips()">
            <button class="btn btn-accent" onclick="generateQueueSlips()">Generate Sequence</button>
          </div>
          <div class="calc-res-box" id="queueResults">
            <!-- Rendered by JS -->
          </div>
        </div>
      </div>

      <!-- Color Coded Covers Packing Guide -->
      <div class="card">
        <div class="card-header">
          <h3>📦 Color-Coded Polling Material Packaging Protocol (C&DMA VC-23 Ref)</h3>
          <span class="tag-badge tag-poll">Reception Standard</span>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.5rem;">
          At the close of poll, the Presiding Officer must pack all records into exactly four color-coded covers. Misplacing statutory documents into wrong covers will delay reception!
        </p>

        <div class="cover-guide-grid">
          <div class="cover-item cover-brown">
            <h4>1. BROWN COVER (With Box)</h4>
            <ul>
              <li><strong>Ballot Paper Account (Form-X-C Part-I)</strong></li>
              <li><strong>Presiding Officer's Diary</strong></li>
              <li><strong>Marked Copy of Electoral Roll</strong></li>
              <li><strong>Used & Unused Ballot Papers & Counterfoils</strong></li>
              <li><strong>Paper Seal Account</strong></li>
              <li><em>Delivered directly with the Ballot Box at the Reception Table!</em></li>
            </ul>
          </div>

          <div class="cover-item cover-green">
            <h4>2. GREEN COVER (Statutory)</h4>
            <ul>
              <li><strong>Tendered Votes List (Form-XVI) & Ballots</strong></li>
              <li><strong>Challenged Votes List (Form-XIV) & Receipts</strong></li>
              <li><strong>Blind / Infirm Voters Declarations (Form-XVII)</strong></li>
              <li><strong>Polling Agents Letters (Form-IX)</strong></li>
              <li><strong>Signed declarations of Challenged Voters (Form-XV)</strong></li>
            </ul>
          </div>

          <div class="cover-item cover-yellow">
            <h4>3. YELLOW COVER (Non-Statutory)</h4>
            <ul>
              <li><strong>Working Copies of Electoral Roll</strong></li>
              <li><strong>Unused Green Paper Seals</strong></li>
              <li><strong>Unused Address Tags</strong></li>
              <li><strong>Appointment letters of Polling Agents</strong></li>
              <li><strong>Receipt books for challenged votes fee</strong></li>
              <li><strong>Any unused forms and stationery</strong></li>
            </ul>
          </div>

          <div class="cover-item cover-blue">
            <h4>4. BLUE COVER (Plain / Kit)</h4>
            <ul>
              <li><strong>Arrow Cross-Mark Rubber Stamps</strong></li>
              <li><strong>Purple Stamp Pads</strong></li>
              <li><strong>Distinguishing Mark Rubber Stamp</strong></li>
              <li><strong>Presiding Officer's Brass Seal</strong></li>
              <li><strong>Indelible Ink Phials & Cups</strong></li>
              <li><strong>Election Officer / PO Handbook</strong></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Doubtful Ballot Adjudication Cheat-Sheet -->
      <div class="card">
        <div class="card-header">
          <h3>🔍 Doubtful Ballot Adjudication Rules (Counting Table Reference)</h3>
          <span class="tag-badge tag-counting">Adjudication Rules</span>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Ballot Condition / Scenario</th>
                <th>Validity</th>
                <th>Statutory Reasoning & Rule</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Mark placed clearly within one candidate's compartment</td>
                <td><span class="tag-badge" style="background: var(--success-light); color: var(--success);">VALID</span></td>
                <td>Intention of the voter is unambiguous. Vote credited to that candidate.</td>
              </tr>
              <tr>
                <td>Mark placed on the dividing line between two candidates, with major part in one</td>
                <td><span class="tag-badge" style="background: var(--success-light); color: var(--success);">VALID</span></td>
                <td>If the shaded circle / arrow mark predominantly lies in one compartment, count for that candidate.</td>
              </tr>
              <tr>
                <td>Mark placed exactly centered on the dividing line between two candidates</td>
                <td><span class="tag-badge" style="background: var(--danger-light); color: var(--danger);">REJECTED</span></td>
                <td>Impossible to determine voter intention. Vote is void for uncertainty.</td>
              </tr>
              <tr>
                <td>Arrow cross-mark stamped multiple times inside the SAME candidate's box</td>
                <td><span class="tag-badge" style="background: var(--success-light); color: var(--success);">VALID</span></td>
                <td>Intention is clear and reinforced. Count as ONE valid vote for that candidate.</td>
              </tr>
              <tr>
                <td>Arrow cross-mark stamped for two different candidates</td>
                <td><span class="tag-badge" style="background: var(--danger-light); color: var(--danger);">REJECTED</span></td>
                <td>Voter has voted for more than one candidate. Void under Counting Rules.</td>
              </tr>
              <tr>
                <td>Signature, initial, name, or writing of voter on the ballot</td>
                <td><span class="tag-badge" style="background: var(--danger-light); color: var(--danger);">REJECTED</span></td>
                <td>Any identifying mark by which the elector can be identified invalidates the vote (Sec. 343-F).</td>
              </tr>
              <tr>
                <td>Ballot marked with pen, pencil, thumb impression, or foreign instrument</td>
                <td><span class="tag-badge" style="background: var(--danger-light); color: var(--danger);">REJECTED</span></td>
                <td>Mark not made by the official arrow cross-mark rubber stamp provided.</td>
              </tr>
              <tr>
                <td>Faint mark due to folding of ballot paper (smudge / mirror image)</td>
                <td><span class="tag-badge" style="background: var(--success-light); color: var(--success);">VALID</span></td>
                <td>Distinguish original sharp imprint from faint mirror smudge caused by wet ink during folding.</td>
              </tr>
              <tr>
                <td>Ballot paper lacks Distinguishing Mark Stamp or PO's signature on reverse</td>
                <td><span class="tag-badge" style="background: var(--danger-light); color: var(--danger);">REJECTED</span></td>
                <td>Statutory safeguard against spurious ballot papers. However, EO may verify if omission was inadvertent by PO.</td>
              </tr>
              <tr>
                <td>Mark stamped in the NOTA panel</td>
                <td><span class="tag-badge" style="background: var(--info-light); color: var(--info);">COUNTED AS NOTA</span></td>
                <td>Valid elector choice; recorded separately in the NOTA column of Form-XX Part-I.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
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
        <button class="btn btn-secondary" onclick="closeModal()">Close</button>
        <button class="btn btn-accent" id="modalCopyBtn" onclick="copyModalContent()">Copy Form Text</button>
        <button class="btn btn-success" onclick="printModalContent()">Print Form</button>
      </div>
    </div>
  </div>

  <!-- Official Footer -->
  <footer class="portal-footer">
    <p><b>Andhra Pradesh State Election Commission — Municipal Ordinary Elections, 2026 (Phase 2)</b></p>
    <p style="margin-top: 4px;">Office of the District Election Authority & District Collector, Tirupati | Srikalahasti Municipality</p>
    <p style="margin-top: 6px; color: #64748b;">
      Statutory References: AP Municipalities Act, 1965 | AP Municipalities (Conduct of Election of Chairpersons & Ward Members) Rules, 2026 | Notification No. 1490/SEC-F1/2026-3
    </p>
  </footer>

  <!-- Embedded Client-Side Script -->
  <script>
    // Data Injections
    const POLLING_STATIONS = """ + ps_json_str + """;
    const WARD_SUMMARY = """ + wards_json_str + """;

    // Standard Forms Definitions
    const FORMS_DATA = [
      {
        id: "form-1",
        code: "Form-1",
        name: "Notice of Election",
        rule: "Rule 6 of Election Rules, 2026",
        stage: "Pre-Poll / Notice",
        desc: "Official statutory notice published by Election Officer specifying dates for nominations, scrutiny, withdrawal, and poll.",
        text: `FORM-1
[See Rule 6]
NOTICE OF ELECTION TO SRIKALAHASTI MUNICIPALITY - 2026

Notice is hereby given that:
1. An election is to be held for the office of:
   (a) Chairperson, Srikalahasti Municipality (Direct Election across all 44 Wards).
   (b) Ward Member for Ward No. [_____], Reserved for [_____].

2. Nomination papers may be delivered by a candidate or by his proposer to the Election Officer / Assistant Election Officer at [Office Name / Room No.] between 11:00 AM and 3:00 PM on any day (including public holidays) from 14.11.2026 to 16.11.2026.

3. Forms of nomination paper may be obtained at the place and times aforesaid, free of cost.

4. The nomination paper will be taken up for scrutiny at [Scrutiny Room] on 17.11.2026 from 11:00 AM onwards.

5. Notice of withdrawal of candidature may be delivered either by a candidate, his proposer or his election agent who has been authorized in writing by the candidate to deliver it, to the Election Officer at his office before 3:00 PM on 19.11.2026.

6. In the event of the election being contested, the poll will be taken on 26.11.2026 between the hours of 07:00 AM and 05:00 PM.

Date: 14.11.2026
Place: Srikalahasti
Election Officer / Municipal Commissioner
Srikalahasti Municipality`
      },
      {
        id: "form-I",
        code: "Form-I",
        name: "Receipt for Nomination Paper & Notice of Scrutiny",
        rule: "Rule 8(7) of Election Rules, 2026",
        stage: "Nominations",
        desc: "Statutory acknowledgement issued to candidate/proposer acknowledging receipt of nomination and giving notice of scrutiny.",
        text: `FORM-I
[See Rule 8(7)]
RECEIPT FOR NOMINATION PAPER AND NOTICE OF SCRUTINY

Serial No. of Nomination Paper: [_____ / Ward No. _____]

The nomination paper of Sri / Smt. [___________________________], a candidate for election as Chairperson / Ward Member from Ward No. [_____] of Srikalahasti Municipality, was delivered to me at my office at [_____] (hour) on [________] (date) by the *Candidate / *Proposer.

All nomination papers will be taken up for scrutiny at [_____] (hour) on 17.11.2026 at [Scrutiny Hall / Election Office Room No. _____].

Checklist of documents endorsed and handed over.
Statutory Deposit Receipt No.: [___________] Dated: [__________] Amount: Rs. [_________]

Date: [__________]
Place: Srikalahasti
Signature of Election Officer / Assistant Election Officer
(Seal)`
      },
      {
        id: "form-IA",
        code: "Form-IA",
        name: "Declaration of Choice of Symbols",
        rule: "Rule 8(9) of Election Rules, 2026",
        stage: "Nominations",
        desc: "Declaration filed by the candidate indicating three preferences of free symbols in order of priority.",
        text: `FORM-IA
[See Rule 8(9)]
DECLARATION BY CANDIDATE AS TO CHOICE OF SYMBOLS

I, [________________________________________________], a candidate for election as Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, hereby declare that the symbols I have chosen are in the following order of preference:

(i) First Choice:   [_____________________________]
(ii) Second Choice: [_____________________________]
(iii) Third Choice:  [_____________________________]

*I am a candidate set up by the [_____________________________] Party, which is a Recognised / Registered political party.
(or)
*I am contesting as an Independent Candidate.

Date: [__________]
Signature of Candidate`
      },
      {
        id: "form-II",
        code: "Form-II",
        name: "Declaration of Caste / Community (SC/ST/BC)",
        rule: "Rule 8(3) of Election Rules, 2026",
        stage: "Nominations",
        desc: "Declaration by candidate contesting reserved seats or seeking concession in security deposit.",
        text: `FORM-II
[See Rule 8(3)]
DECLARATION AS TO CASTE / COMMUNITY

I, [________________________________________________], candidate for election to the office of Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, hereby solemnly declare that:

1. I belong to the [_______________________] caste/tribe/community, which is recognized as a *Scheduled Caste / *Scheduled Tribe / *Backward Class in the State of Andhra Pradesh.
2. An attested copy of the Community Certificate issued by the competent authority (not below the rank of Deputy Tahsildar) is enclosed herewith.

Date: [__________]
Signature of Candidate`
      },
      {
        id: "decl-antecedents",
        code: "Declaration",
        name: "Declaration on Antecedents, Assets & Education",
        rule: "Rule 8(10) of Election Rules, 2026",
        stage: "Nominations",
        desc: "Mandatory declaration on criminal antecedents, assets, liabilities, and education attested by two witnesses.",
        text: `DECLARATION ON CRIMINAL ANTECEDENTS, ASSETS & EDUCATION
[See Rule 8(10)]

I, [___________________________], son/daughter/wife of [___________________________], aged [_____] years, resident of [_______________________________________________________], candidate for election as Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, do hereby declare:

1. Criminal Cases:
   (a) Whether convicted in any criminal offence: *Yes / No
   (b) Details of pending cases where charges framed: [Nil / Not Applicable / Case Details]

2. Assets and Liabilities:
   (a) Movable Assets (Self / Spouse / Dependents): [Values / Descriptions]
   (b) Immovable Assets (Self / Spouse / Dependents): [Values / Locations]
   (c) Dues to Municipality / Financial Institutions: [Nil / Details]

3. Educational Qualifications:
   Highest qualification completed: [_____________________________] from [School/College].

VERIFICATION:
I verify that the contents of this declaration are true to the best of my knowledge and belief. No column has been left blank.

Signature of Candidate: [_____________________________]

Witnesses:
1. Name: [_______________________] Voter Roll No: [_____/_____] Signature: [___________]
2. Name: [_______________________] Voter Roll No: [_____/_____] Signature: [___________]`
      },
      {
        id: "form-III",
        code: "Form-III",
        name: "List of Nominations Received",
        rule: "Rule 9(1) of Election Rules, 2026",
        stage: "Nominations",
        desc: "Daily and final consolidated list of nominations received affixed on the notice board after 3 PM.",
        text: `FORM-III
[See Rule 9(1)]
LIST OF NOMINATIONS RECEIVED

Office: Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality, Phase 2 Elections - 2026

List of nominations received up to 3:00 PM on [16.11.2026]:
-----------------------------------------------------------------------------------------
Sl. | Name of     | Father / Husband's | Age | Address | Party Affiliation | Proposer Name
No. | Candidate   | Name               |     |         |                   | & Sl. No. in Roll
-----------------------------------------------------------------------------------------
1.  |             |                    |     |         |                   |
2.  |             |                    |     |         |                   |
3.  |             |                    |     |         |                   |
-----------------------------------------------------------------------------------------

Date: 16.11.2026 (3:00 PM)
Place: Srikalahasti
Signature of Election Officer / Assistant Election Officer`
      },
      {
        id: "form-IV",
        code: "Form-IV",
        name: "List of Validly Nominated Candidates",
        rule: "Rule 12 of Election Rules, 2026",
        stage: "Scrutiny",
        desc: "List of candidates whose nominations are accepted after scrutiny, arranged in Telugu alphabetical order.",
        text: `FORM-IV
[See Rule 12]
LIST OF VALIDLY NOMINATED CANDIDATES

Election to the Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality

-----------------------------------------------------------------------------------------
Sl. No. | Name of Candidate       | Address of Candidate    | Party Affiliation
-----------------------------------------------------------------------------------------
1.      | [Telugu Alph. Order]    |                         |
2.      |                         |                         |
3.      |                         |                         |
-----------------------------------------------------------------------------------------

Place: Srikalahasti
Date: 17.11.2026
Signature of Election Officer
(Seal)`
      },
      {
        id: "form-V",
        code: "Form-V",
        name: "Notice of Withdrawal of Candidature & Receipt",
        rule: "Rule 13(1) of Election Rules, 2026",
        stage: "Withdrawals",
        desc: "Notice signed by candidate to withdraw candidature before 3:00 PM on 19.11.2026.",
        text: `FORM-V
[See Rule 13(1)]
NOTICE OF WITHDRAWAL OF CANDIDATURE

To:
The Election Officer,
Srikalahasti Municipality.

I, [________________________________________________], a validly nominated candidate for election as Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, do hereby give notice that I withdraw my candidature.

Date: [__________] (Before 3:00 PM)
Place: Srikalahasti
Signature of Candidate

RECEIPT FOR NOTICE OF WITHDRAWAL
The notice of withdrawal of candidature by Sri/Smt. [___________________________] was delivered to me at my office at [_____] hours on [__________] by the *Candidate / *Proposer / *Authorised Election Agent.

Signature of Election Officer`
      },
      {
        id: "form-VI",
        code: "Form-VI",
        name: "Notice of Withdrawals of Candidature",
        rule: "Rule 13(3) of Election Rules, 2026",
        stage: "Withdrawals",
        desc: "Consolidated public notice of candidatures withdrawn, displayed on the notice board.",
        text: `FORM-VI
[See Rule 13(3)]
NOTICE OF WITHDRAWALS OF CANDIDATURE

Election to Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality

Notice is hereby given that the following candidate/candidates has/have withdrawn candidature today:
-----------------------------------------------------------------------------------------
Sl. No. | Name of Candidate          | Address               | Remarks
-----------------------------------------------------------------------------------------
1.      |                            |                       |
-----------------------------------------------------------------------------------------

Date: 19.11.2026 (After 3:00 PM)
Place: Srikalahasti
Signature of Election Officer`
      },
      {
        id: "form-VII",
        code: "Form-VII",
        name: "Final List of Contesting Candidates",
        rule: "Rule 14(1) of Election Rules, 2026",
        stage: "Contesting List & Symbols",
        desc: "Final list of contesting candidates with allotted symbols, arranged in Telugu alphabetical order.",
        text: `FORM-VII
[See Rule 14(1)]
FINAL LIST OF CONTESTING CANDIDATES

Election to Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality

(i) Candidates of Recognised National and State Political Parties:
-----------------------------------------------------------------------------------------
Sl. No. | Name of Candidate       | Address of Candidate    | Party / Symbol Allotted
-----------------------------------------------------------------------------------------
1.      |                         |                         |
2.      |                         |                         |

(ii) Candidates of Registered Political Parties:
3.      |                         |                         |

(iii) Other (Independent) Candidates:
4.      |                         |                         |
-----------------------------------------------------------------------------------------
Last Panel: NONE OF THE ABOVE (NOTA)

Date: 19.11.2026 (After 3:00 PM)
Place: Srikalahasti
Signature of Election Officer
(Seal)`
      },
      {
        id: "form-VIII",
        code: "Form-VIII",
        name: "Appointment of Election Agent",
        rule: "Rule 17(1) of Election Rules, 2026",
        stage: "Agents",
        desc: "Appointment letter executed by candidate appointing an Election Agent.",
        text: `FORM-VIII
[See Rule 17(1)]
APPOINTMENT OF ELECTION AGENT

To:
The Election Officer,
Srikalahasti Municipality.

I, [___________________________], a candidate for election as Chairperson / Ward Member for Ward No. [_____], do hereby appoint Sri/Smt. [___________________________], resident of [___________________________], as my Election Agent from this day at the said election.

Signature of Candidate: [___________________________]

I accept the above appointment.
Signature of Election Agent: [___________________________]`
      },
      {
        id: "form-IX",
        code: "Form-IX",
        name: "Appointment of Polling Agent (In Duplicate)",
        rule: "Rule 18(1) of Election Rules, 2026",
        stage: "Agents",
        desc: "Appointment letter for Polling Agent presented to Presiding Officer on poll morning.",
        text: `FORM-IX
[See Rule 18(1)]
APPOINTMENT OF POLLING AGENT

Election to Chairperson / Ward Member for Ward No. [_____]
Polling Station No.: [_____ / _____]
Location: [_______________________________________________________]

I, [___________________________], a *Candidate / *Election Agent, hereby appoint Sri/Smt. [___________________________], resident of [___________________________], as a Polling Agent to attend Polling Station No. [_____].

Signature of Candidate / Election Agent: [___________________________]

Declaration of Polling Agent:
I agree to act as Polling Agent and solemnly declare that I will maintain and aid in maintaining the secrecy of voting under Section 343-F of the AP Municipalities Act, 1965.

Signature of Polling Agent: [___________________________]
Signed before me at 06:00 AM on 26.11.2026.
Signature of Presiding Officer`
      },
      {
        id: "form-X",
        code: "Form-X",
        name: "Appointment of Counting Agent",
        rule: "Rule 19(1) of Election Rules, 2026",
        stage: "Agents",
        desc: "Appointment letter for Counting Agent presented to Election Officer before counting.",
        text: `FORM-X
[See Rule 19(1)]
APPOINTMENT OF COUNTING AGENT

To:
The Election Officer,
Srikalahasti Municipality.

I, [___________________________], a *Candidate / *Election Agent, do hereby appoint Sri/Smt. [___________________________], resident of [___________________________], as Counting Agent to attend counting table No. [_____] at the Counting Centre on 30.11.2026.

Signature of Candidate / Election Agent: [___________________________]

Declaration of Counting Agent:
I agree to act as Counting Agent and will maintain the secrecy of voting.
Signature of Counting Agent: [___________________________]`
      },
      {
        id: "form-X-C",
        code: "Form-X-C",
        name: "Ballot Paper Account & Paper Seal Account",
        rule: "Rule 45 of Election Rules, 2026",
        stage: "Ballot Accounts",
        desc: "Crucial statutory account prepared by Presiding Officer at poll close. Attested copy given to all agents.",
        text: `FORM-X-C
[See Rule 45]
PART-I: BALLOT PAPER ACCOUNT

Name of ULB: Srikalahasti Municipality
Ward No.: [_____]   Polling Station No.: [_____ / _____]

1. Number of Ballot Papers received:
   From Sl. No. [__________] to [__________] = Total: [_______]

2. Number of Ballot Papers unused:
   (a) Undamaged: [_______]
   (b) Damaged due to cancel/clerical: [_______]

3. Number of Ballot Papers issued to voters (1 - 2): [_______]

4. Number of Tendered Ballot Papers used: [_______]

5. Number of Ballot Papers to be found in the Ballot Box (3 - 4): [_______]

PART-II: PAPER SEAL ACCOUNT
1. Serial numbers of Green Paper Seals supplied: [_____] to [_____] = Total: [_____]
2. Number of Paper Seals used: [_____] (Sl. Nos.: [_______________])
3. Number of unused Paper Seals returned: [_____]
4. Number of damaged Paper Seals: [_____]

Date: 26.11.2026 (05:00 PM)
Signature of Presiding Officer
Signatures of Polling Agents present:
1. [___________________]  2. [___________________]  3. [___________________]`
      },
      {
        id: "po-diary",
        code: "PO Diary",
        name: "Presiding Officer's Diary",
        rule: "Statutory Field Diary",
        stage: "Poll Day Record",
        desc: "Complete operational diary recorded by Presiding Officer during poll hours.",
        text: `PRESIDING OFFICER'S DIARY
Srikalahasti Municipality Phase 2 Elections - 2026

1. Polling Station No.: [_____ / _____] Name: [__________________________________]
2. Number of electors assigned to PS: Total [_____] (Men: [_____], Women: [_____])
3. Number of electors who voted: Total [_____] (Men: [_____], Women: [_____])
4. Number of challenged votes: Allowed: [_____], Rejected: [_____], Amount forfeited: Rs. [_____]
5. Number of blind/infirm voters assisted: [_____]
6. Number of tendered votes recorded: [_____]
7. Number of polling agents present: [_____]
8. Empty ballot box demonstrated at: 06:30 AM
9. Poll commenced at: 07:00 AM Promptly
10. Poll closed at: 05:00 PM (Slips distributed: [_____])
11. Law and order incidents / disruptions (if any): [NIL]
12. Ballot box sealed with brass seal in presence of agents at: [_____] PM

Signature of Presiding Officer`
      },
      {
        id: "form-XIV",
        code: "Form-XIV",
        name: "List of Challenged Votes",
        rule: "Rule 36 of Election Rules, 2026",
        stage: "Poll Day Operations",
        desc: "Statutory record maintained by PO for challenged votes, fees collected, and decisions.",
        text: `FORM-XIV
[See Rule 36]
LIST OF CHALLENGED VOTES

Polling Station No.: [_____ / _____] Ward No.: [_____]
Srikalahasti Municipality

---------------------------------------------------------------------------------------------------
Sl. | Voter | Name of  | Challenged | Amount   | Name of      | Order of PO | Signature / Thumb
No. | Roll# | Elector  | by (Agent) | Deposited| Identifier   | (Allowed /  | impression of
    |       |          |            | (Rs. 5)  |              |  Rejected)  | voter challenged
---------------------------------------------------------------------------------------------------
1.  |       |          |            | Rs. 5/-  |              |             |
2.  |       |          |            | Rs. 5/-  |              |             |
---------------------------------------------------------------------------------------------------

Signature of Presiding Officer`
      },
      {
        id: "form-XVI",
        code: "Form-XVI",
        name: "List of Tendered Votes",
        rule: "Rule 42 of Election Rules, 2026",
        stage: "Poll Day Operations",
        desc: "Record of voters whose vote was already marked by an imposter and who cast a tendered ballot.",
        text: `FORM-XVI
[See Rule 42]
LIST OF TENDERED VOTES

Polling Station No.: [_____ / _____] Ward No.: [_____]
Srikalahasti Municipality

---------------------------------------------------------------------------------------------------
Sl. | Name of Elector       | Serial Number in | Serial No. of Tendered | Signature / Thumb
No. |                       | Electoral Roll   | Ballot Paper issued    | Impression of Voter
---------------------------------------------------------------------------------------------------
1.  |                       |                  |                        |
2.  |                       |                  |                        |
---------------------------------------------------------------------------------------------------

Signature of Presiding Officer`
      },
      {
        id: "form-XVII",
        code: "Form-XVII",
        name: "Declaration by Companion of Blind or Infirm Voter",
        rule: "Rule 40 of Election Rules, 2026",
        stage: "Poll Day Operations",
        desc: "Declaration executed by adult companion assisting an incapacitated voter.",
        text: `FORM-XVII
[See Rule 40]
DECLARATION BY THE COMPANION OF BLIND OR INFIRM VOTER

Polling Station No.: [_____ / _____] Ward No.: [_____]
Srikalahasti Municipality

I, [___________________________], aged [_____] years, residing at [__________________________________], declare that:
1. I have been permitted to accompany Sri/Smt. [___________________________], who is blind/infirm, to record his/her vote.
2. I have not acted as a companion for any other voter at this or any other polling station today.
3. I will keep secret the vote recorded by me on his/her behalf.

Signature of Companion: [___________________________]
Signature of Presiding Officer`
      },
      {
        id: "form-XX-p1",
        code: "Form-XX (Part-I)",
        name: "Result Sheet of Election",
        rule: "Rule 52 of Election Rules, 2026",
        stage: "Counting",
        desc: "Candidate-wise and table-wise tabulation of votes counted, leading to result announcement.",
        text: `FORM-XX
[See Rule 52]
PART-I: RESULT SHEET OF ELECTION

Election to Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality - 2026

Total Electors in Ward: [__________]

-----------------------------------------------------------------------------------------
Round | Table | Candidate A | Candidate B | Candidate C | NOTA | Valid Total | Rejected
No.   | No.   | (Votes)     | (Votes)     | (Votes)     |      |             | Votes
-----------------------------------------------------------------------------------------
1.    | 1     |             |             |             |      |             |
2.    | 2     |             |             |             |      |             |
...   |       |             |             |             |      |             |
-----------------------------------------------------------------------------------------
Postal Ballots|             |             |             |      |             |
-----------------------------------------------------------------------------------------
GRAND TOTAL   |             |             |             |      |             |
-----------------------------------------------------------------------------------------

Date: 30.11.2026
Place: Counting Hall, Srikalahasti
Signature of Election Officer
(Mandatory 15-Minute Recount Window Observed)`
      },
      {
        id: "form-XX-p2",
        code: "Form-XX (Part-II)",
        name: "Formal Declaration of Result of Election",
        rule: "Rule 53 of Election Rules, 2026",
        stage: "Declaration",
        desc: "Official statutory declaration declaring the winning candidate elected.",
        text: `FORM-XX
[See Rule 53]
PART-II: FORMAL DECLARATION OF RESULT OF ELECTION

In accordance with Rule 53 of the AP Municipalities / Nagar Panchayats (Conduct of Election of Chairpersons and Ward Members) Rules, 2026, I declare that:

Sri / Smt. [_______________________________________________________]
Sponsored by: [__________________________________] Party / Independent
Address: [_______________________________________________________]

has been duly elected as:
* CHAIRPERSON, SRIKALAHASTI MUNICIPALITY
(or)
* WARD MEMBER FOR WARD NO. [_____] OF SRIKALAHASTI MUNICIPALITY.

Place: Srikalahasti
Date: 30.11.2026
Signature of Election Officer / Municipal Commissioner
(Official Seal)`
      }
    ];

    // Initialize Page
    document.addEventListener('DOMContentLoaded', () => {
      initClock();
      renderWardTable();
      renderPollingStations();
      renderFormsList();
      populateWardFilter();
      initChecklistProgress();
      calculateBallots();
      generateQueueSlips();
    });

    // Navigation Tabs
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
      
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');

      const btn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick').includes(tabId));
      if (btn) btn.classList.add('active');

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Live Clock Simulation
    function initClock() {
      const update = () => {
        const now = new Date();
        const str = now.toLocaleDateString('en-GB') + ' ' + now.toLocaleTimeString('en-GB');
        const el = document.getElementById('liveClock');
        if (el) el.textContent = str;
      };
      update();
      setInterval(update, 1000);
    }

    // Toggle Stage Boxes
    function toggleStage(header) {
      const parent = header.parentElement;
      parent.classList.toggle('open');
    }

    // Render Ward Reservation Table
    function renderWardTable() {
      const tbody = document.querySelector('#wardTable tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      WARD_SUMMARY.forEach(w => {
        let tagClass = 'tag-ur';
        if (w.res_code.startsWith('SC')) tagClass = 'tag-sc';
        else if (w.res_code.startsWith('ST')) tagClass = 'tag-st';
        else if (w.res_code.startsWith('BC')) tagClass = 'tag-bc';
        if (w.res_code.endsWith('-W')) tagClass += ' tag-women';

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><b>Ward ${w.ward}</b></td>
          <td><span class="tag-badge ${tagClass}">${w.res_code}</span></td>
          <td>${w.res_name}</td>
          <td><b>${w.ps_count} PS</b></td>
          <td style="font-family: monospace; font-size: 0.8rem;">${w.ps_list.join(', ')}</td>
          <td><b>${w.voters.toLocaleString()}</b></td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Populate Ward Filter Dropdown
    function populateWardFilter() {
      const sel = document.getElementById('wardFilterSelect');
      if (!sel) return;
      for (let w = 1; w <= 44; w++) {
        const opt = document.createElement('option');
        opt.value = w;
        opt.textContent = 'Ward ' + w;
        sel.appendChild(opt);
      }
    }

    // Render 88 Polling Stations
    function renderPollingStations(filtered = POLLING_STATIONS) {
      const tbody = document.getElementById('psTableBody');
      if (!tbody) return;
      tbody.innerHTML = '';

      if (filtered.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">No polling stations matched your search.</td></tr>`;
        return;
      }

      filtered.forEach(ps => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${ps.sl}</td>
          <td><b>Ward ${ps.ward}</b></td>
          <td><span class="tag-badge tag-ur" style="font-size: 0.82rem; font-weight: 800;">${ps.ps_no}</span></td>
          <td>${ps.details}</td>
          <td><b>${ps.voters}</b></td>
          <td style="font-family: monospace; font-size: 0.78rem; color: var(--text-muted);">
            <a href="https://maps.google.com/?q=${ps.lat},${ps.lon}" target="_blank" style="text-decoration: none; color: var(--secondary);">
              📍 ${ps.lat}, ${ps.lon}
            </a>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Filter Polling Stations
    function filterPollingStations() {
      const q = document.getElementById('psSearchInput').value.toLowerCase().trim();
      const ward = document.getElementById('wardFilterSelect').value;

      const filtered = POLLING_STATIONS.filter(ps => {
        const matchesWard = (ward === 'ALL' || ps.ward == ward);
        const matchesQuery = !q || (
          ps.ps_no.toLowerCase().includes(q) ||
          ps.details.toLowerCase().includes(q) ||
          ('ward ' + ps.ward).includes(q) ||
          ps.voters.toString().includes(q)
        );
        return matchesWard && matchesQuery;
      });

      renderPollingStations(filtered);
    }

    // Render Forms List
    function renderFormsList(items = FORMS_DATA) {
      const cont = document.getElementById('formsContainer');
      if (!cont) return;
      cont.innerHTML = '';

      items.forEach(form => {
        const card = document.createElement('div');
        card.className = 'form-item-card';
        card.innerHTML = `
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
              <h4>${form.code}: ${form.name}</h4>
              <span class="tag-badge tag-ur" style="font-size: 0.7rem;">${form.stage}</span>
            </div>
            <div class="form-meta">${form.rule}</div>
            <div class="form-desc">${form.desc}</div>
          </div>
          <div class="form-actions">
            <button class="btn btn-secondary" onclick="viewForm('${form.id}')" style="flex: 1;">Preview</button>
            <button class="btn btn-accent" onclick="quickCopyForm('${form.id}')">Copy</button>
          </div>
        `;
        cont.appendChild(card);
      });
    }

    // Filter Forms
    function filterForms() {
      const q = document.getElementById('formSearchInput').value.toLowerCase().trim();
      if (!q) {
        renderFormsList(FORMS_DATA);
        return;
      }
      const filtered = FORMS_DATA.filter(f => 
        f.code.toLowerCase().includes(q) ||
        f.name.toLowerCase().includes(q) ||
        f.desc.toLowerCase().includes(q) ||
        f.stage.toLowerCase().includes(q) ||
        f.rule.toLowerCase().includes(q)
      );
      renderFormsList(filtered);
    }

    // Modal Handling
    let currentModalForm = null;
    function viewForm(formId) {
      const form = FORMS_DATA.find(f => f.id === formId);
      if (!form) return;
      currentModalForm = form;

      document.getElementById('modalTitle').textContent = `${form.code} — ${form.name}`;
      document.getElementById('modalContent').textContent = form.text;
      document.getElementById('formModal').classList.add('open');
    }

    function closeModal() {
      document.getElementById('formModal').classList.remove('open');
      currentModalForm = null;
    }

    function copyModalContent() {
      if (!currentModalForm) return;
      navigator.clipboard.writeText(currentModalForm.text).then(() => {
        const btn = document.getElementById('modalCopyBtn');
        const orig = btn.textContent;
        btn.textContent = 'Copied! ✓';
        setTimeout(() => btn.textContent = orig, 1500);
      });
    }

    function quickCopyForm(formId) {
      const form = FORMS_DATA.find(f => f.id === formId);
      if (!form) return;
      navigator.clipboard.writeText(form.text).then(() => {
        alert(`${form.code} template copied to clipboard!`);
      });
    }

    function printModalContent() {
      const w = window.open('', '_blank');
      w.document.write(`<html><head><title>${currentModalForm.name}</title><style>body{font-family:monospace;white-space:pre-wrap;padding:2rem;line-height:1.5;}</style></head><body>${currentModalForm.text}</body></html>`);
      w.document.close();
      w.focus();
      w.print();
    }

    // Interactive Checklist Logic with Local Storage
    const STORAGE_KEY = 'SKHT_ELECTION_2026_CHECKLIST';

    function initChecklistProgress() {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      const checkboxes = document.querySelectorAll('.checklist-items input[type="checkbox"]');
      
      checkboxes.forEach(cb => {
        const id = cb.getAttribute('data-id');
        if (saved[id]) {
          cb.checked = true;
          cb.closest('.chk-item').classList.add('checked');
        }
      });
      calculateChecklistProgress();
    }

    function updateChecklist(cb) {
      const id = cb.getAttribute('data-id');
      const item = cb.closest('.chk-item');
      if (cb.checked) {
        item.classList.add('checked');
      } else {
        item.classList.remove('checked');
      }

      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      saved[id] = cb.checked;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
      calculateChecklistProgress();
    }

    function calculateChecklistProgress() {
      const checkboxes = document.querySelectorAll('.checklist-items input[type="checkbox"]');
      const total = checkboxes.length;
      let checked = 0;
      checkboxes.forEach(cb => { if (cb.checked) checked++; });

      const pct = Math.round((checked / total) * 100);
      const bar = document.getElementById('chkProgressBar');
      const lbl = document.getElementById('chkProgressPercent');
      if (bar) bar.style.width = pct + '%';
      if (lbl) lbl.textContent = `${pct}% Completed (${checked}/${total})`;
    }

    function resetChecklist() {
      if (!confirm('Are you sure you want to reset all checklist marks on this device?')) return;
      localStorage.removeItem(STORAGE_KEY);
      document.querySelectorAll('.checklist-items input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
        cb.closest('.chk-item').classList.remove('checked');
      });
      calculateChecklistProgress();
    }

    // Field Calculator: Ballot Paper Requirements
    function calculateBallots() {
      const el = document.getElementById('calcElectorate');
      const res = document.getElementById('calcResults');
      if (!el || !res) return;

      const n = parseInt(el.value, 10) || 0;
      if (n <= 0) {
        res.innerHTML = '<span style="color:var(--danger)">Please enter a valid electorate count.</span>';
        return;
      }

      // Electorate + 10%
      const raw10 = n * 1.10;
      const wardRound50 = Math.ceil(raw10 / 50) * 50;
      const psRound10 = Math.ceil(raw10 / 10) * 10;

      res.innerHTML = `
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.75rem;">
          <div>
            <div style="color:var(--text-muted); font-size: 0.78rem;">Base Electorate:</div>
            <div style="font-size: 1.1rem; font-weight:700;">${n.toLocaleString()} voters</div>
          </div>
          <div>
            <div style="color:var(--text-muted); font-size: 0.78rem;">With 10% Reserve:</div>
            <div style="font-size: 1.1rem; font-weight:700; color:var(--secondary);">${raw10.toFixed(0)} ballots</div>
          </div>
          <div>
            <div style="color:var(--text-muted); font-size: 0.78rem;">Ward Allotment (Round 50):</div>
            <div style="font-size: 1.1rem; font-weight:700; color:var(--accent);">${wardRound50.toLocaleString()} ballots</div>
          </div>
          <div>
            <div style="color:var(--text-muted); font-size: 0.78rem;">PS Allotment (Round 10):</div>
            <div style="font-size: 1.1rem; font-weight:700; color:var(--success);">${psRound10.toLocaleString()} ballots</div>
          </div>
        </div>
        <p style="margin-top:0.5rem; font-size:0.75rem; color:var(--text-muted);">
          Note: Exactly identical quantities required for <b>White Wove</b> (Chairperson) and <b>Pink Wove</b> (Ward Member) ballots.
        </p>
      `;
    }

    // Field Tool: Queue Slips Sequence Generator
    function generateQueueSlips() {
      const el = document.getElementById('queueVoters');
      const res = document.getElementById('queueResults');
      if (!el || !res) return;

      const count = parseInt(el.value, 10) || 0;
      if (count <= 0) {
        res.innerHTML = '<span style="color:var(--danger)">Please enter a valid number of voters in queue.</span>';
        return;
      }

      res.innerHTML = `
        <div style="font-size: 0.85rem; line-height: 1.5;">
          <div style="font-weight: 700; color: var(--primary); margin-bottom: 0.35rem;">
            Distribution Rule: Total <b>${count}</b> numbered slips signed by PO must be distributed.
          </div>
          <p style="color: var(--text-muted); font-size: 0.8rem; margin-bottom: 0.5rem;">
            1. Stand at the very END of the queue at exactly 05:00 PM.<br>
            2. Issue <b>Slip No. 1</b> to the LAST voter standing in the queue.<br>
            3. Move forward towards the door, issuing <b>Slip No. 2, 3, 4...</b><br>
            4. Issue <b>Slip No. ${count}</b> to the FIRST voter at the head of the queue.<br>
            5. Allow voting strictly in reverse order (${count} down to 1), ensuring no newcomer can enter behind Slip No. 1.
          </p>
          <div style="background: #f1f5f9; padding: 0.4rem 0.6rem; border-radius: 4px; font-family: monospace; font-size: 0.8rem;">
            Sequence: Last Person = Slip 1 | First Person = Slip ${count}
          </div>
        </div>
      `;
    }
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully (size: {len(html_content)} bytes).")
