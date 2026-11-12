# -*- coding: utf-8 -*-
"""
Inject mobile Card View toggle and FAB scroll logic into index.html
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Polling Stations Card HTML in Tab 7
old_ps_html = """      <!-- 88 PS Search Box -->
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
      </div>"""

new_ps_html = """      <!-- 88 PS Search Box -->
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

        <!-- Mobile View Toggle Controls -->
        <div class="view-toggle-bar">
          <div class="table-scroll-hint">
            👉 Swipe horizontally to view full table / పట్టిక చూడటానికి పక్కకు జరపండి
          </div>
          <div class="view-toggle-group">
            <button class="view-toggle-btn active" id="btnCardView" onclick="setPSView('card')">📱 Card View</button>
            <button class="view-toggle-btn" id="btnTableView" onclick="setPSView('table')">📊 Table View</button>
          </div>
        </div>

        <!-- Mobile Cards View Container -->
        <div class="ps-cards-grid active-view" id="psCardsGrid"></div>

        <!-- Desktop / Full Table Container -->
        <div class="table-container ps-table-view hidden-view" id="psTableContainer">
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
      </div>"""

html = html.replace(old_ps_html, new_ps_html)

# 2. Update renderPollingStations in script to render both Card view and Table view
old_render_ps = """function renderPollingStations(filtered = POLLING_STATIONS) {
  const tbody = document.getElementById('psTableBody');
  if (!tbody) return;
  tbody.innerHTML = '';

  const isTe = currentLang === 'te';

  if (filtered.length === 0) {
    tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">${isTe ? 'పోలింగ్ కేంద్రాలు ఏవీ లభించలేదు.' : 'No polling stations matched your search.'}</td></tr>`;
    return;
  }

  filtered.forEach(ps => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${ps.sl}</td>
      <td><b>${isTe ? 'వార్డు ' + ps.ward : 'Ward ' + ps.ward}</b></td>
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
}"""

new_render_ps = """let currentPSView = 'card';

function setPSView(viewMode) {
  currentPSView = viewMode;
  const btnCard = document.getElementById('btnCardView');
  const btnTable = document.getElementById('btnTableView');
  const cardsGrid = document.getElementById('psCardsGrid');
  const tableContainer = document.getElementById('psTableContainer');

  if (viewMode === 'card') {
    btnCard?.classList.add('active');
    btnTable?.classList.remove('active');
    cardsGrid?.classList.add('active-view');
    tableContainer?.classList.add('hidden-view');
  } else {
    btnTable?.classList.add('active');
    btnCard?.classList.remove('active');
    cardsGrid?.classList.remove('active-view');
    tableContainer?.classList.remove('hidden-view');
  }
}

function renderPollingStations(filtered = POLLING_STATIONS) {
  const tbody = document.getElementById('psTableBody');
  const cardsGrid = document.getElementById('psCardsGrid');
  const isTe = currentLang === 'te';

  if (!tbody || !cardsGrid) return;
  tbody.innerHTML = '';
  cardsGrid.innerHTML = '';

  if (filtered.length === 0) {
    const noMsg = isTe ? 'పోలింగ్ కేంద్రాలు ఏవీ లభించలేదు.' : 'No polling stations matched your search.';
    tbody.innerHTML = `<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">${noMsg}</td></tr>`;
    cardsGrid.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 1.5rem; background: #ffffff; border-radius: 8px;">${noMsg}</div>`;
    return;
  }

  filtered.forEach(ps => {
    // 1. Table row
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${ps.sl}</td>
      <td><b>${isTe ? 'వార్డు ' + ps.ward : 'Ward ' + ps.ward}</b></td>
      <td><span class="tag-badge tag-ur" style="font-size: 0.82rem; font-weight: 800;">${ps.ps_no}</span></td>
      <td>${ps.details}</td>
      <td><b>${ps.voters}</b></td>
      <td style="white-space: nowrap;">
        <a href="https://maps.google.com/?q=${ps.lat},${ps.lon}" target="_blank" class="map-btn">
          📍 ${isTe ? 'మ్యాప్' : 'Map'}
        </a>
      </td>
    `;
    tbody.appendChild(tr);

    // 2. Mobile Card item
    const card = document.createElement('div');
    card.className = 'ps-card-item';
    card.innerHTML = `
      <div class="ps-card-header">
        <div style="display: flex; gap: 0.5rem; align-items: center;">
          <span class="tag-badge tag-ur" style="font-size: 0.85rem; font-weight: 800;">${isTe ? 'వార్డు ' + ps.ward : 'Ward ' + ps.ward}</span>
          <span class="tag-badge tag-poll" style="font-size: 0.85rem; font-weight: 800; background: #dbeafe; color: #1e40af;">PS ${ps.ps_no}</span>
        </div>
        <div style="font-size: 0.78rem; font-weight: 700; color: var(--text-muted);">
          #${ps.sl} of 88
        </div>
      </div>
      <div class="ps-card-body">
        <div style="font-weight: 600; color: var(--primary); margin-bottom: 0.25rem;">${ps.details}</div>
      </div>
      <div class="ps-card-footer">
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--secondary);">
          👥 ${ps.voters.toLocaleString()} ${isTe ? 'ఓటర్లు' : 'Voters'}
        </div>
        <a href="https://maps.google.com/?q=${ps.lat},${ps.lon}" target="_blank" class="map-btn">
          📍 ${isTe ? 'మ్యాప్ లొకేషన్' : 'Open in Maps'}
        </a>
      </div>
    `;
    cardsGrid.appendChild(card);
  });
}

// Mobile Floating Action Button scroll listener
window.addEventListener('scroll', () => {
  const fab = document.getElementById('fabTop');
  if (fab) {
    if (window.scrollY > 300) {
      fab.classList.add('visible');
    } else {
      fab.classList.remove('visible');
    }
  }
});
"""

html = html.replace(old_render_ps, new_render_ps)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected mobile card view & scroll FAB into index.html successfully.")
