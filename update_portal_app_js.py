# -*- coding: utf-8 -*-
"""
Append directory rendering & forms handling to portal_app.js
"""

app_js_extension = """
// ============================================================================
// DIRECTORY RENDERING (AUTHORITIES, CLUSTERS, ZONAL, SURVEILLANCE)
// ============================================================================

function renderAuthorities(lang) {
  const box = document.getElementById('authoritiesBox');
  if (!box) return;
  const isTe = lang === 'te';

  box.innerHTML = `
    <div class="card">
      <div class="card-header">
        <h3>🏛️ ${isTe ? 'ప్రధాన చట్టబద్ధ అధికారులు & ఎన్నికల నాయకత్వం' : 'Key Statutory Authorities & Election Leadership'}</h3>
        <span class="tag-badge tag-ur">${isTe ? 'జిల్లా & రాష్ట్ర స్థాయి' : 'HQ Leadership'}</span>
      </div>
      <div class="grid-3">
        <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
          <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            ${isTe ? 'రాష్ట్ర ఎన్నికల కమిషనర్' : 'State Election Commissioner'}
          </div>
          <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Sri Anil Chandra Punetha, IAS (Retd)</div>
          <div style="font-size: 0.8rem; color: var(--text-muted);">
            ${isTe ? 'ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం, విజయవాడ' : 'AP State Election Commission, Vijayawada'}
          </div>
        </div>
        <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
          <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            ${isTe ? 'జిల్లా ఎన్నికల అధికారి & కలెక్టర్' : 'District Election Authority & Collector'}
          </div>
          <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Dr. S. Venkateswar, I.A.S.</div>
          <div style="font-size: 0.8rem; color: var(--text-muted);">
            ${isTe ? 'తిరుపతి జిల్లా కలెక్టరేట్, తిరుపతి' : 'Tirupati District Collectorate, Tirupati'}
          </div>
        </div>
        <div style="padding: 0.75rem; background: #f8fafc; border-radius: 6px; border: 1px solid var(--border);">
          <div style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">
            ${isTe ? 'సహాయక ఎన్నికల అధికారి & కమిషనర్' : 'Asst. Election Authority & Commissioner'}
          </div>
          <div style="font-size: 1rem; font-weight: 700; color: var(--primary);">Sri K. V. Krishna Reddy</div>
          <div style="font-size: 0.8rem; color: var(--text-muted);">
            ${isTe ? 'శ్రీకాళహస్తి పురపాలక సంఘం' : 'Srikalahasti Municipality'}
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderClusterOffices(lang) {
  const box = document.getElementById('clusterOfficesBox');
  if (!box) return;
  const isTe = lang === 'te';

  const clusters = [
    { name: isTe ? "ఛైర్‌పర్సన్ కార్యాలయం" : "Chairperson Office", juris: isTe ? "అన్ని 44 వార్డులు (ప్రత్యక్ష ఎన్నిక)" : "All 44 Wards (Direct Election)", staff: [["G. Nithin Singh", "Ward Admin Secretary (WA)", "9492831594"], ["A. Leela Krishna", "Ward Admin Secretary (WA)", "7032027606"]] },
    { name: isTe ? "క్లస్టర్ 1" : "Cluster 1", juris: isTe ? "వార్డులు 1, 2, 3, 4" : "Wards 1, 2, 3, 4", staff: [["B. Sreepathi", "WEDPS", "8374252079"], ["E. Jhansi", "WA", "9030881708"]] },
    { name: isTe ? "క్లస్టర్ 2" : "Cluster 2", juris: isTe ? "వార్డులు 5, 6, 7, 8" : "Wards 5, 6, 7, 8", staff: [["K. Suresh", "WEDPS", "9014566244"], ["K. Madhavi", "WA", "7204695000"]] },
    { name: isTe ? "క్లస్టర్ 3" : "Cluster 3", juris: isTe ? "వార్డులు 9, 10, 11, 12" : "Wards 9, 10, 11, 12", staff: [["T. Suresh", "WEDPS", "8919170382"], ["K. Kalpana", "WA", "8897890434"]] },
    { name: isTe ? "క్లస్టర్ 4" : "Cluster 4", juris: isTe ? "వార్డులు 13, 14, 15, 16" : "Wards 13, 14, 15, 16", staff: [["R. Praveen", "WEDPS", "9177203062"], ["S. Thasleem", "WA", "7842246142"]] },
    { name: isTe ? "క్లస్టర్ 5" : "Cluster 5", juris: isTe ? "వార్డులు 17, 18, 19, 20" : "Wards 17, 18, 19, 20", staff: [["D. Jayaprakash", "WEDPS", "9966449310"], ["K. Siva Kumar", "WA", "7207266773"]] },
    { name: isTe ? "క్లస్టర్ 6" : "Cluster 6", juris: isTe ? "వార్డులు 21, 22, 23, 24" : "Wards 21, 22, 23, 24", staff: [["K. J. Bhaskar", "WEDPS", "7893111073"], ["G. Sai Sunil Kumar", "WA", "7013435085"]] },
    { name: isTe ? "క్లస్టర్ 7" : "Cluster 7", juris: isTe ? "వార్డులు 25, 26, 27, 28" : "Wards 25, 26, 27, 28", staff: [["D. L. Dilli Priya", "WEDPS", "8074332196"], ["Muni Chenchu Latha", "WA", "9701786332"]] },
    { name: isTe ? "క్లస్టర్ 8" : "Cluster 8", juris: isTe ? "వార్డులు 29, 30, 31, 32" : "Wards 29, 30, 31, 32", staff: [["N. Hema Madhuri", "WA", "9912250707"], ["C. Yamini", "WA", "8464077105"]] },
    { name: isTe ? "క్లస్టర్ 9" : "Cluster 9", juris: isTe ? "వార్డులు 33, 34, 35, 36" : "Wards 33, 34, 35, 36", staff: [["K. Sravani", "WEDPS", "9985340635"], ["G. Kameswara Rao", "WA", "8328075402"]] },
    { name: isTe ? "క్లస్టర్ 10" : "Cluster 10", juris: isTe ? "వార్డులు 37, 38, 39, 40" : "Wards 37, 38, 39, 40", staff: [["T. Chandra Reddy", "WEDPS", "9640473306"], ["K. Bhanu Prakash", "WA", "9154562184"]] },
    { name: isTe ? "క్లస్టర్ 11" : "Cluster 11", juris: isTe ? "వార్డులు 41, 42, 43, 44" : "Wards 41, 42, 43, 44", staff: [["C. Murali", "WEDPS", "9885743874"], ["Y. Yamuna", "WA", "8897447071"]] }
  ];

  box.innerHTML = `
    <div class="card">
      <div class="card-header">
        <h3>🏢 ${isTe ? '12 వార్డు-క్లస్టర్ ఎన్నికల కార్యాలయాలు & సహాయక సిబ్బంది' : '12 Ward-Cluster Election Offices & Assigned Staff'}</h3>
        <span class="tag-badge tag-ur">Roc. No. 2578/2025/G1</span>
      </div>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>${isTe ? 'కార్యాలయం / క్లస్టర్' : 'Office / Cluster'}</th>
              <th>${isTe ? 'పరిధి / వార్డులు' : 'Jurisdiction'}</th>
              <th>${isTe ? 'సహాయక సిబ్బంది పేరు' : 'Assigned Supporting Staff'}</th>
              <th>${isTe ? 'హోదా' : 'Designation'}</th>
              <th>${isTe ? 'మొబైల్ నంబర్' : 'Mobile Number'}</th>
            </tr>
          </thead>
          <tbody>
            ${clusters.map(c => `
              <tr>
                <td rowspan="2"><b>${c.name}</b></td>
                <td rowspan="2">${c.juris}</td>
                <td>${c.staff[0][0]}</td>
                <td>${c.staff[0][1]}</td>
                <td><a href="tel:${c.staff[0][2]}">${c.staff[0][2]}</a></td>
              </tr>
              <tr>
                <td>${c.staff[1][0]}</td>
                <td>${c.staff[1][1]}</td>
                <td><a href="tel:${c.staff[1][2]}">${c.staff[1][2]}</a></td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function renderZonalRoute(lang) {
  const box = document.getElementById('zonalRouteBox');
  if (!box) return;
  const isTe = lang === 'te';

  box.innerHTML = `
    <div class="card">
      <div class="card-header">
        <h3>🗺️ ${isTe ? 'జోనల్ అధికారులు (3 జోన్లు) & రూట్ అధికారులు (9 రూట్లు)' : 'Zonal Officers (3 Zones) & Route Officers (9 Routes)'}</h3>
        <span class="tag-badge tag-ur">${isTe ? 'క్షేత్ర పర్యవేక్షణ' : 'Field Supervision'}</span>
      </div>

      <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">
        ${isTe ? 'జోనల్ అధికారుల వివరాలు' : 'Zonal Officers Directory'}
      </h4>
      <div class="table-container" style="margin-bottom: 1.25rem;">
        <table class="data-table">
          <thead>
            <tr>
              <th>${isTe ? 'జోన్' : 'Zone'}</th>
              <th>${isTe ? 'జోనల్ అధికారి' : 'Zonal Officer'}</th>
              <th>${isTe ? 'హోదా' : 'Designation'}</th>
              <th>${isTe ? 'ఫోన్ నంబర్' : 'Contact'}</th>
              <th>${isTe ? 'కేటాయించిన రూట్లు' : 'Allotted Routes'}</th>
              <th>${isTe ? 'వార్డులు' : 'Wards Covered'}</th>
              <th>${isTe ? 'మొత్తం కేంద్రాలు' : 'Total PS'}</th>
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

      <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">
        ${isTe ? 'రూట్ అధికారుల వివరాలు (9 రూట్లు)' : 'Route Officers Directory (9 Routes)'}
      </h4>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>${isTe ? 'రూట్' : 'Route'}</th>
              <th>${isTe ? 'రూట్ అధికారి' : 'Route Officer'}</th>
              <th>${isTe ? 'హోదా' : 'Designation'}</th>
              <th>${isTe ? 'ఫోన్ నంబర్' : 'Contact'}</th>
              <th>${isTe ? 'పరిధి / వార్డులు' : 'Wards Covered'}</th>
              <th>${isTe ? 'కేటాయించిన పోలింగ్ కేంద్రాలు' : 'Allotted Polling Stations'}</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><b>Route 1</b></td><td>M. Pardhasaradhi</td><td>WPRS</td><td><a href="tel:8686867365">8686867365</a></td><td>1, 2, 3, 4, 5, 6, 7</td><td>1/1 to 7/2 (14 PS)</td></tr>
            <tr><td><b>Route 2</b></td><td>K. Rajendra</td><td>WPRS</td><td><a href="tel:7288936923">7288936923</a></td><td>33, 34, 35, 36, 37</td><td>33/1 to 37/2 (10 PS)</td></tr>
            <tr><td><b>Route 3</b></td><td>NB Prabhakar</td><td>WPRS</td><td><a href="tel:9629297089">9629297089</a></td><td>40, 41, 43, 44</td><td>40/1 to 44/2 (7 PS)</td></tr>
            <tr><td><b>Route 4</b></td><td>Shaik Sulthan Sharief</td><td>WPRS</td><td><a href="tel:9966011817">9966011817</a></td><td>38, 39, 40, 42</td><td>38/1 to 42/2 (7 PS)</td></tr>
            <tr><td><b>Route 5</b></td><td>B. Sai Prasad</td><td>WPRS</td><td><a href="tel:9676006961">9676006961</a></td><td>17, 18, 24, 26, 28, 29, 30</td><td>17/1 to 30/2 (14 PS)</td></tr>
            <tr><td><b>Route 6</b></td><td>A. Gireesha</td><td>WPRS</td><td><a href="tel:8919543675">8919543675</a></td><td>11, 12, 13, 14</td><td>11/1 to 14/2 (8 PS)</td></tr>
            <tr><td><b>Route 7</b></td><td>C. Pramila</td><td>WPRS</td><td><a href="tel:7036375470">7036375470</a></td><td>8, 9, 10, 15, 16, 20</td><td>8/1 to 20/2 (12 PS)</td></tr>
            <tr><td><b>Route 8</b></td><td>Vinitha</td><td>WPRS</td><td><a href="tel:7330746514">7330746514</a></td><td>19, 21, 22, 23, 25</td><td>19/1 to 25/2 (10 PS)</td></tr>
            <tr><td><b>Route 9</b></td><td>Chandana</td><td>WPRS</td><td><a href="tel:8096610523">8096610523</a></td><td>31, 32, 27</td><td>31/1 to 27/2 (6 PS)</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function renderSurveillance(lang) {
  const box = document.getElementById('surveillanceBox');
  if (!box) return;
  const isTe = lang === 'te';

  box.innerHTML = `
    <div class="card">
      <div class="card-header">
        <h3>🚔 ${isTe ? 'ఎన్నికల ప్రవర్తనా నియమావళి (MCC), ఫ్లయింగ్ స్క్వాడ్ & స్టాటిక్ నిఘా బృందాలు' : 'MCC, Flying Squads (FST) & Static Surveillance Teams (SST)'}</h3>
        <span class="tag-badge tag-ur">Roc. No. 2230/2026</span>
      </div>
      <div class="grid-2">
        <div>
          <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">
            ${isTe ? 'MCC ప్రవర్తనా నియమావళి బృందాలు (24/7)' : 'MCC Enforcement Teams (24/7)'}
          </h4>
          <ul class="guideline-points">
            <li><strong>Shift 1 (08:00 AM – 08:00 PM):</strong>
              <br>• Dr. C. Narasimha Reddy (Incharge) - <a href="tel:9441209500">9441209500</a>
              <br>• Deva Rajulu Vedagiri, Sr Assistant - <a href="tel:7036371140">7036371140</a>
              <br>• K. Kranthi, Head Constable 981 - <a href="tel:9505354981">9505354981</a>
            </li>
            <li><strong>Shift 2 (08:00 PM – 08:00 AM):</strong>
              <br>• D. Bhaskar (Incharge) - <a href="tel:9440095961">9440095961</a>
              <br>• Anil Kumar Reddy Dappili, Sr Assistant - <a href="tel:9492320039">9492320039</a>
              <br>• U. Ramanaiah, Head Constable 789 - <a href="tel:9440846401">9440846401</a>
            </li>
          </ul>

          <h4 style="color: var(--secondary); margin: 0.75rem 0 0.5rem 0;">
            ${isTe ? 'ఫ్లయింగ్ స్క్వాడ్ బృందాలు (FST - 24/7)' : 'Flying Squad Teams (FST - 24/7)'}
          </h4>
          <ul class="guideline-points">
            <li><strong>Shift 1:</strong> Bharathi, MEO (<a href="tel:9441573295">9441573295</a>), Narasimhulu (<a href="tel:9989671658">9989671658</a>), M. Ramanaiah HC 844 (<a href="tel:9449932821">9449932821</a>)</li>
            <li><strong>Shift 2:</strong> A. Balaiah, MEO (<a href="tel:9440343503">9440343503</a>), Srinivasulu (<a href="tel:9441132420">9441132420</a>), S. Subramanyam HC 758 (<a href="tel:8074660081">8074660081</a>)</li>
          </ul>
        </div>

        <div>
          <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">
            ${isTe ? 'స్టాటిక్ నిఘా బృందాలు (SST చెక్‌పాయింట్లు)' : 'Static Surveillance Teams (SST Checkpoints)'}
          </h4>
          <ul class="guideline-points">
            <li><strong>SST-1: AP Tourism, Srikalahasti</strong>
              <br>• Shift 1: K. Vinith Kumar Reddy, AEO (<a href="tel:8919604708">8919604708</a>), Venkata Subba Reddy (<a href="tel:8341337654">8341337654</a>), M. Sankar PC 858 (<a href="tel:9985944940">9985944940</a>)
              <br>• Shift 2: P. Venkata Praveen, AEO (<a href="tel:98499997550">98499997550</a>), Malleswaraiah (<a href="tel:8297288918">8297288918</a>), V. Mohan Babu PC 2023 (<a href="tel:9676572238">9676572238</a>)
            </li>
            <li><strong>SST-2: Nandi Circle, Naidupeta Road</strong>
              <br>• Shift 1: K. Jyothsna, AEO (<a href="tel:9515577377">9515577377</a>), Siva Kundla (<a href="tel:6281525335">6281525335</a>), V. Anil Kumar PC 871 (<a href="tel:8897837877">8897837877</a>)
              <br>• Shift 2: A. Ravi Prasad, AEO (<a href="tel:9533910555">9533910555</a>), Subba Reddy (<a href="tel:9551223998">9551223998</a>), P. Hari PC 1811 (<a href="tel:9618664654">9618664654</a>)
            </li>
          </ul>

          <h4 style="color: var(--secondary); margin: 0.75rem 0 0.5rem 0;">
            ${isTe ? 'వ్యయ పరిశీలన & వీడియో నిఘా బృందాలు' : 'Expenditure Audit & Video Surveillance'}
          </h4>
          <ul class="guideline-points">
            <li><strong>Team 1 (Wards 1–22):</strong> Prabhakar AAO (<a href="tel:9440667769">9440667769</a>), B. Priyanka (<a href="tel:7997423413">7997423413</a>)</li>
            <li><strong>Team 2 (Wards 23–44):</strong> B. Manohara JAO (<a href="tel:9491781181">9491781181</a>), C. Balaji (<a href="tel:8008644256">8008644256</a>)</li>
            <li><strong>Video Surveillance (VST):</strong> Ramana (<a href="tel:9705518400">9705518400</a>), Ch. Chalamaiah HC 3898 (<a href="tel:8985272119">8985272119</a>)</li>
          </ul>
        </div>
      </div>
    </div>
  `;
}

// Modify applyLanguage to call these directory sub-renderers
const origApplyLang = applyLanguage;
applyLanguage = function(lang) {
  origApplyLang(lang);
  renderAuthorities(lang);
  renderClusterOffices(lang);
  renderZonalRoute(lang);
  renderSurveillance(lang);
};

// Forms Rendering
function renderFormsList(items = (typeof BILINGUAL_FORMS !== 'undefined' ? BILINGUAL_FORMS : [])) {
  const cont = document.getElementById('formsContainer');
  if (!cont) return;
  cont.innerHTML = '';
  const isTe = currentLang === 'te';

  items.forEach(form => {
    const card = document.createElement('div');
    card.className = 'form-item-card';
    const formName = isTe ? form.name_te : form.name_en;
    const formStage = isTe ? form.stage_te : form.stage_en;
    const formDesc = isTe ? form.desc_te : form.desc_en;
    const previewBtn = isTe ? 'ప్రివ్యూ చూడండి' : 'Preview';
    const copyBtn = isTe ? 'కాపీ' : 'Copy';

    card.innerHTML = `
      <div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <h4>${form.code}: ${formName}</h4>
          <span class="tag-badge tag-ur" style="font-size: 0.7rem;">${formStage}</span>
        </div>
        <div class="form-meta">${form.rule}</div>
        <div class="form-desc">${formDesc}</div>
      </div>
      <div class="form-actions">
        <button class="btn btn-secondary" onclick="viewForm('${form.id}')" style="flex: 1;">${previewBtn}</button>
        <button class="btn btn-accent" onclick="quickCopyForm('${form.id}')">${copyBtn}</button>
      </div>
    `;
    cont.appendChild(card);
  });
}

function filterForms() {
  const q = document.getElementById('formSearchInput').value.toLowerCase().trim();
  if (!q) {
    renderFormsList(BILINGUAL_FORMS);
    return;
  }
  const filtered = BILINGUAL_FORMS.filter(f => 
    f.code.toLowerCase().includes(q) ||
    f.name_en.toLowerCase().includes(q) ||
    f.name_te.toLowerCase().includes(q) ||
    f.desc_en.toLowerCase().includes(q) ||
    f.desc_te.toLowerCase().includes(q) ||
    f.stage_en.toLowerCase().includes(q) ||
    f.stage_te.toLowerCase().includes(q)
  );
  renderFormsList(filtered);
}

let currentModalForm = null;
function viewForm(formId) {
  const form = BILINGUAL_FORMS.find(f => f.id === formId);
  if (!form) return;
  currentModalForm = form;
  const isTe = currentLang === 'te';

  document.getElementById('modalTitle').textContent = `${form.code} — ${isTe ? form.name_te : form.name_en}`;
  document.getElementById('modalContent').textContent = isTe ? form.text_te : form.text_en;
  document.getElementById('mBtnClose').textContent = isTe ? 'మూసివేయి' : 'Close';
  document.getElementById('modalCopyBtn').textContent = isTe ? 'ఫారం కాపీ చేయండి' : 'Copy Form Text';
  document.getElementById('mBtnPrint').textContent = isTe ? 'ఫారం ప్రింట్' : 'Print Form';
  document.getElementById('formModal').classList.add('open');
}

function closeModal() {
  document.getElementById('formModal').classList.remove('open');
  currentModalForm = null;
}

function copyModalContent() {
  if (!currentModalForm) return;
  const isTe = currentLang === 'te';
  const text = isTe ? currentModalForm.text_te : currentModalForm.text_en;
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('modalCopyBtn');
    const orig = btn.textContent;
    btn.textContent = isTe ? 'కాపీ చేయబడింది! ✓' : 'Copied! ✓';
    setTimeout(() => btn.textContent = orig, 1500);
  });
}

function quickCopyForm(formId) {
  const form = BILINGUAL_FORMS.find(f => f.id === formId);
  if (!form) return;
  const isTe = currentLang === 'te';
  const text = isTe ? form.text_te : form.text_en;
  navigator.clipboard.writeText(text).then(() => {
    alert(isTe ? `${form.code} పత్రం క్లిప్‌బోర్డ్‌కు కాపీ చేయబడింది!` : `${form.code} template copied to clipboard!`);
  });
}

function printModalContent() {
  if (!currentModalForm) return;
  const isTe = currentLang === 'te';
  const text = isTe ? currentModalForm.text_te : currentModalForm.text_en;
  const title = isTe ? currentModalForm.name_te : currentModalForm.name_en;

  const w = window.open('', '_blank');
  w.document.write(`<html><head><title>${title}</title><style>body{font-family:"Nirmala UI",monospace;white-space:pre-wrap;padding:2rem;line-height:1.6;}</style></head><body>${text}</body></html>`);
  w.document.close();
  w.focus();
  w.print();
}
"""

with open('portal_app.js', 'a', encoding='utf-8') as af:
    af.write(app_js_extension)

print("portal_app.js extended with directory & forms logic.")
