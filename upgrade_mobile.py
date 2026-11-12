# -*- coding: utf-8 -*-
"""
Upgrade index.html with comprehensive Smartphone & Mobile compatibility features.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update meta tags for mobile
old_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
new_meta = '''<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#0b2545">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="format-detection" content="telephone=no">'''

html = html.replace(old_meta, new_meta)

# 2. Add Smartphone-optimized CSS
mobile_css = """
    /* ==========================================================================
       SMARTPHONE & MOBILE OPTIMIZATIONS
       ========================================================================== */

    /* Touch-friendly Call Buttons */
    a[href^="tel:"] {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: #15803d;
      color: #ffffff !important;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.78rem;
      transition: background 0.15s ease;
      white-space: nowrap;
    }
    a[href^="tel:"]:hover, a[href^="tel:"]:active {
      background: #166534;
      text-decoration: none;
    }
    a[href^="tel:"]::before {
      content: "📞";
      font-size: 0.8rem;
    }

    /* Maps Navigation Button */
    .map-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: #0284c7;
      color: #ffffff !important;
      padding: 0.35rem 0.65rem;
      border-radius: 6px;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.78rem;
      transition: background 0.15s ease;
      white-space: nowrap;
    }
    .map-btn:hover, .map-btn:active {
      background: #0369a1;
      text-decoration: none;
    }

    /* Floating Back-to-Top Button */
    .fab-top {
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--primary);
      color: #ffffff;
      border: 2px solid var(--accent);
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      cursor: pointer;
      z-index: 99;
      transition: all 0.2s ease;
    }
    .fab-top:active {
      transform: scale(0.92);
    }
    .fab-top.visible {
      display: flex;
    }

    /* Mobile Table Scroll Hint */
    .table-scroll-hint {
      display: none;
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-bottom: 0.4rem;
      align-items: center;
      gap: 0.35rem;
      background: #eff6ff;
      padding: 0.35rem 0.65rem;
      border-radius: 4px;
      border-left: 3px solid var(--secondary);
    }

    /* Polling Stations View Toggle */
    .view-toggle-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }
    .view-toggle-group {
      display: inline-flex;
      background: #e2e8f0;
      padding: 2px;
      border-radius: 6px;
    }
    .view-toggle-btn {
      border: none;
      background: transparent;
      padding: 0.35rem 0.75rem;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: 5px;
      cursor: pointer;
      color: var(--text-muted);
    }
    .view-toggle-btn.active {
      background: #ffffff;
      color: var(--primary);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* Polling Stations Mobile Cards Grid */
    .ps-cards-grid {
      display: none;
      grid-template-columns: 1fr;
      gap: 0.85rem;
      margin-bottom: 1.5rem;
    }
    .ps-card-item {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1rem;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .ps-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.5rem;
    }
    .ps-card-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary);
    }
    .ps-card-body {
      font-size: 0.85rem;
      color: var(--text-main);
      line-height: 1.45;
    }
    .ps-card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px dashed var(--border);
      padding-top: 0.5rem;
      margin-top: 0.2rem;
    }

    /* Comprehensive Mobile Responsive Overrides */
    @media (max-width: 768px) {
      header.portal-header {
        padding: 0.75rem 1rem;
        position: relative; /* Allow content to have full view */
      }
      .header-top {
        gap: 0.75rem;
      }
      .header-brand {
        gap: 0.75rem;
      }
      .emblem-badge {
        width: 44px;
        height: 44px;
        font-size: 1.15rem;
      }
      .brand-text h1 {
        font-size: 1.05rem;
        line-height: 1.3;
      }
      .brand-text p {
        font-size: 0.75rem;
      }
      .header-controls {
        width: 100%;
        justify-content: space-between;
        gap: 0.5rem;
      }
      .lang-switch-box {
        padding: 2px;
      }
      .lang-btn {
        padding: 0.35rem 0.8rem;
        font-size: 0.8rem;
        min-height: 38px;
      }
      .live-clock-badge {
        font-size: 0.72rem;
        padding: 0.35rem 0.6rem;
      }
      .header-stats {
        width: 100%;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 4px;
        margin-top: 0.5rem;
        scrollbar-width: none;
      }
      .header-stats::-webkit-scrollbar {
        display: none;
      }
      .stat-pill {
        font-size: 0.74rem;
        padding: 0.3rem 0.65rem;
        flex-shrink: 0;
      }

      /* Sticky Tab Bar on Smartphone */
      nav.portal-nav {
        top: 0;
        z-index: 95;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      }
      .nav-container {
        padding: 0 0.5rem;
        scrollbar-width: none;
      }
      .nav-container::-webkit-scrollbar {
        display: none;
      }
      .nav-btn {
        padding: 0.8rem 0.9rem;
        font-size: 0.82rem;
        min-height: 46px; /* Touch target */
        white-space: nowrap;
      }

      /* Main container padding */
      main.portal-main {
        padding: 0 0.75rem;
        margin-top: 1rem;
        margin-bottom: 4rem;
      }

      /* Titles & Subtitles */
      .section-title {
        font-size: 1.2rem;
        line-height: 1.3;
      }
      .section-sub {
        font-size: 0.82rem;
        margin-bottom: 1rem;
      }

      /* Notification Banner */
      .banner-notification {
        padding: 0.85rem 1rem;
        flex-direction: column;
        align-items: flex-start;
      }
      .banner-actions {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
        margin-top: 0.5rem;
      }
      .banner-actions .btn {
        justify-content: center;
        padding: 0.55rem;
        font-size: 0.82rem;
      }

      /* Cards & Containers */
      .card {
        padding: 1rem;
        margin-bottom: 1rem;
      }
      .card-header h3 {
        font-size: 0.98rem;
      }

      /* Touch-friendly inputs (no iOS auto-zoom) */
      .search-input {
        font-size: 16px !important;
        min-height: 46px;
        padding: 0.65rem 0.85rem;
      }
      .calc-input-group input, .calc-input-group select {
        font-size: 16px !important;
        min-height: 46px;
        width: 100%;
      }

      /* Checklists Touch Targets */
      .chk-item {
        padding: 0.85rem 1rem;
        min-height: 52px;
        gap: 0.85rem;
      }
      .chk-item:active {
        background: #f1f5f9;
        transform: scale(0.99);
      }
      .chk-item input[type="checkbox"] {
        width: 22px;
        height: 22px;
        margin-top: 1px;
      }
      .chk-title {
        font-size: 0.92rem;
      }
      .chk-sub {
        font-size: 0.8rem;
      }

      /* Accordion Stage Headers */
      .stage-box-header {
        padding: 0.85rem 1rem;
        min-height: 52px;
      }
      .stage-header-title {
        gap: 0.6rem;
      }
      .stage-num {
        width: 28px;
        height: 28px;
        font-size: 0.8rem;
      }
      .stage-box-header h3 {
        font-size: 0.92rem;
      }
      .stage-box-body {
        padding: 1rem;
      }
      .stage-date-tag {
        font-size: 0.72rem;
        padding: 0.15rem 0.5rem;
      }

      /* Do's and Don'ts */
      .dodont-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
      }

      /* Forms Cards */
      .forms-grid {
        grid-template-columns: 1fr;
      }
      .form-actions {
        display: flex;
        gap: 0.5rem;
      }
      .form-actions .btn {
        min-height: 42px;
        justify-content: center;
      }

      /* Fullscreen/Mobile Modal */
      .modal-backdrop {
        padding: 0.5rem;
      }
      .modal-window {
        max-height: 94vh;
        width: 100%;
      }
      .modal-header {
        padding: 0.85rem 1rem;
      }
      .modal-header h3 {
        font-size: 0.95rem;
      }
      .modal-body {
        padding: 1rem;
        font-size: 0.8rem;
      }
      .modal-footer {
        padding: 0.65rem 1rem;
        flex-wrap: wrap;
        gap: 0.5rem;
      }
      .modal-footer .btn {
        flex: 1;
        min-height: 42px;
        justify-content: center;
      }

      /* Show horizontal scroll hint */
      .table-scroll-hint {
        display: flex;
      }

      /* Show Polling Stations in Card View on Mobile */
      .ps-cards-grid.active-view {
        display: grid;
      }
      .table-container.ps-table-view.hidden-view {
        display: none;
      }

      /* Grids to 1 column */
      .grid-2, .grid-3 {
        grid-template-columns: 1fr;
      }
    }
"""

# Replace the media query section with mobile_css
html = html.replace('@media (max-width: 768px) {', mobile_css + '\n    @media (max-width: 768px) {')

# 3. Add Floating Action Button in HTML before </body>
fab_html = """
  <!-- Floating Action Button for Mobile -->
  <button class="fab-top" id="fabTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" aria-label="Back to Top">
    ↑
  </button>
"""
html = html.replace('</body>', fab_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected mobile-responsive CSS and FAB.")
