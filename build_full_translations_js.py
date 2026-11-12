# -*- coding: utf-8 -*-
"""
Generate portal_translations.js with complete English and Telugu translations.
"""

import json

# We will write the full JS object into portal_translations.js
script_builder = """// ============================================================================
// BILINGUAL TRANSLATION DATA (ENGLISH & TELUGU)
// Srikalahasti Municipality Phase 2 Ordinary Elections - 2026
// ============================================================================

const PORTAL_TRANSLATIONS = {
  en: {
    headerTitle: "SRIKALAHASTI MUNICIPALITY — PHASE 2 ORDINARY ELECTIONS, 2026",
    headerSubtitle: "Andhra Pradesh State Election Commission | District Election Authority & Collector, Tirupati District",
    stats: [
      { label: "Wards", val: "44" },
      { label: "Polling Stations", val: "88" },
      { label: "Electors", val: "72,537" },
      { label: "Offices", val: "12 Clusters" }
    ],
    banner: {
      title: "⚡ SEC Notification No. 1490/SEC-F1/2026-3 Dated 12.11.2026 Issued",
      desc: "Elections called for Chairperson (Direct Election) and Ward Members for 44 Wards under AP Municipalities Act, 1965 & Conduct of Election Rules, 2026.",
      btnChecklists: "Open Checklists",
      btnPrint: "Print Quick Kit"
    },
    tabs: [
      { id: "tab-schedule", icon: "📅", title: "Schedule & Deadlines", badge: "" },
      { id: "tab-stages", icon: "🚶", title: "Stage-by-Stage Guide", badge: "9 Stages" },
      { id: "tab-checklists", icon: "✅", title: "Checklists", badge: "8 Sets" },
      { id: "tab-guidelines", icon: "📌", title: "Important Guidelines", badge: "" },
      { id: "tab-dodont", icon: "⚖️", title: "Do's & Don'ts", badge: "" },
      { id: "tab-forms", icon: "📂", title: "Forms & Proformas", badge: "22 Forms" },
      { id: "tab-directory", icon: "🏛️", title: "Srikalahasti Roster", badge: "88 PS / Teams" },
      { id: "tab-tools", icon: "🛠️", title: "Field Tools & Packing", badge: "" }
    ],
    sched: {
      title: "📅 Election Programme & Statutory Timeline",
      sub: "Comprehensive timeline notified by AP State Election Commission for Phase 2 Ordinary Municipal Elections, 2026.",
      timelines: [
        { stage: "Stage 1: Pre-Poll", date: "14.11.2026 (Saturday)", title: "Ward Electoral Rolls Display", desc: "Under Rule 5, Election Officer displays ward-wise voter lists on the notice board.", time: "⏰ Morning 10:00 AM", class: "" },
        { stage: "Stage 2: Public Notice", date: "14.11.2026 (Saturday)", title: "Publication of Election Notice", desc: "Election Notice issued by Election Officer under Rule 6 in prescribed format (Form-1).", time: "⏰ Morning (Before Nominations)", class: "" },
        { stage: "Stage 3: Nominations", date: "14.11.2026 to 16.11.2026", title: "Filing & Receipt of Nominations", desc: "Receipt of nominations at 12 designated offices (Chairperson + 11 Ward Clusters).", time: "⏰ 11:00 AM to 3:00 PM Daily", class: "active-stage" },
        { stage: "Stage 4: Last Date", date: "16.11.2026 (Monday)", title: "Close of Nominations & Form-A", desc: "Last moment for nomination filing (3 PM). Political party Form-A to Collector & DEA before 5 PM.", time: "⏰ 3:00 PM (Sharp) / 5:00 PM (Form-A)", class: "" },
        { stage: "Stage 5: Scrutiny", date: "17.11.2026 (Tuesday)", title: "Scrutiny of Nominations", desc: "Quasi-judicial examination by Election Officer. Publication of Form-IV valid candidate list.", time: "⏰ From 11:00 AM Onwards", class: "" },
        { stage: "Stage 6: Withdrawals", date: "19.11.2026 (Thursday)", title: "Withdrawals & Form-VII Publication", desc: "Notice of withdrawal (Form-V) up to 3 PM. Form-B to EO up to 3 PM. Allotment of symbols & Form-VII.", time: "⏰ Withdrawal: Up to 3 PM | Form-VII: After 3 PM", class: "" },
        { stage: "Stage 7: Poll Day", date: "26.11.2026 (Thursday)", title: "Conduct of Poll (Voting)", desc: "Poll across all 88 Polling Stations using White (Chairperson) and Pink (Ward Member) ballots.", time: "⏰ 07:00 AM to 05:00 PM", class: "poll-stage" },
        { stage: "Stage 8: Re-Poll", date: "27.11.2026 (Friday)", title: "Date of Re-poll (If Any)", desc: "Reserved for any re-poll ordered by APSEC under statutory grounds.", time: "⏰ 07:00 AM to 05:00 PM", class: "" },
        { stage: "Stage 9: Counting", date: "30.11.2026 (Monday)", title: "Counting of Votes & Declaration", desc: "Continuous counting at designated counting centre. Form-XX Part I & II declaration.", time: "⏰ From 08:00 AM Onwards", class: "counting-stage" }
      ],
      timeLimitsTitle: "⏱️ Statutory Time Limits at a Glance (C&DMA VC-23 Ref)",
      timeLimitsCols: ["Election Activity", "Prescribed Statutory Time Limit", "Responsible Officer / Authority", "Key Legal Citation"],
      timeLimits: [
        { act: "Receipt of Nominations", limit: "11:00 AM to 3:00 PM (All notified days, incl. public holidays)", resp: "Election Officer (EO) / AEO", cite: "Rule 8(1), Conduct of Election Rules 2026" },
        { act: "Submission of Pending Checklist Documents", limit: "Before 3:00 PM on the last date for nominations (16.11.2026)", resp: "Candidate / Proposer", cite: "C&DMA Instructions / SEC Guidelines" },
        { act: "Submission of Form-A (Party Authorisation)", limit: "Before 5:00 PM on the last date for nominations (16.11.2026)", resp: "President / Gen. Secy of Political Party to Collector & DEA", cite: "Para 13, Symbols Order / SEC Orders" },
        { act: "Delivery of Form-B (Candidate Sponsorship)", limit: "Before 3:00 PM on the last date for withdrawal (19.11.2026)", resp: "Authorized Party Signatory to Election Officer (EO)", cite: "Para 13, Symbols Order" },
        { act: "Withdrawal of Candidature (Form-V)", limit: "Not later than 3:00 PM on the appointed date (19.11.2026)", resp: "Candidate in person / Proposer / Auth. Election Agent", cite: "Rule 13, Conduct of Election Rules 2026" },
        { act: "Despatch of Postal Ballots", limit: "Within 48 hours of the last hour of withdrawal (by 21.11.2026, 3 PM)", resp: "Election Officer", cite: "Rule 22 to 27, G.O.Ms.No.213" },
        { act: "Polling Agent Appointment Intimation", limit: "At least 3 days before poll (by 23.11.2026)", resp: "Candidate / Election Agent to EO / PO", cite: "Rule 18 / SEC Compendium" },
        { act: "Campaign Silence Period", limit: "48 hours ending with the hour fixed for conclusion of poll", resp: "All Political Parties / Candidates / Media", cite: "Sec. 343-A AP Municipalities Act" },
        { act: "Hours of Poll", limit: "07:00 AM to 05:00 PM (Queue at 5 PM receives numbered slips)", resp: "Presiding Officer (PO)", cite: "Notification No. 1490/SEC-F1/2026-3" },
        { act: "Candidate Expense Account Submission", limit: "Once every 3 days from date of publication of contesting list", resp: "Candidate to Expenditure Scrutiny Team", cite: "Sec. 343-ZC(1) to (3) / SEC Order 135" },
        { act: "Request for Recount of Votes", limit: "Within 15 minutes after announcement of total votes scored", resp: "Candidate / Election Agent to EO", cite: "Conduct of Election Rules / Counting Instructions" },
        { act: "Choice of Seat (Multiple Wins)", limit: "Within 15 days of last result declaration", resp: "Elected Candidate to Municipal Commissioner", cite: "Rule 62, AP Municipal Election Rules 2026" }
      ]
    },
    stagesTitle: "🚶 Stage-by-Stage Field Guide for Election Officers",
    stagesSub: "Step-by-step procedures, legal requirements, and essential administrative workflows from Notification to Strong Room custody.",
    stages: [
      {
        num: 1,
        title: "Pre-Poll Preparations, Electoral Rolls Display & Form-1 Notice",
        sub: "Display of Electoral Rolls (Rule 5) | Issue of Election Notice (Rule 6)",
        date: "12.11.2026 to 14.11.2026",
        opsTitle: "Key Operational Steps",
        ops: [
          "<strong>Roll Freezing:</strong> Ward-wise electoral roll is frozen as on 12.11.2026 (date of SEC notification). Ensure all additions/deletions ordered by ERO under RP Act 1950 are integrated.",
          "<strong>Roll Display (14.11.2026 morning):</strong> Election Officer must display updated ward voter lists on Municipal Office notice board and conspicuous places in each ward under Rule 5.",
          "<strong>Issue Election Notice (Form-1):</strong> Publish Election Notice in prescribed SEC format in English and Telugu specifying particulars of election, reservations, nomination places, dates & timings.",
          "<strong>Establish 12 Election Offices:</strong> Setup 1 dedicated Election Office for Chairperson and 11 Cluster Offices (covering 4 wards each: Wards 1-4, 5-8, 9-12, etc.).",
          "<strong>Stationery & Forms Stock:</strong> Supply blank nomination forms, declarations on antecedents/assets, and Form-IA free of cost to intending candidates."
        ],
        legalTitle: "Legal Checks & Boundaries",
        legal: [
          "<strong>Office of Profit & Disqualifications:</strong> Review Sections 13, 13-A, 14, 15, 15-A, and 15-B of the AP Municipalities Act, 1965.",
          "<strong>Expenditure Ceilings:</strong> Brief all officers that statutory expense ceilings are <strong>Rs. 20.00 Lakhs</strong> for Chairperson and <strong>Rs. 7.50 Lakhs</strong> for Ward Members.",
          "<strong>Separate Notices:</strong> Ensure separate notices are displayed for Chairperson and Ward Member seats showing exact reservation category.",
          "<strong>Help Desk Staffing:</strong> Ensure supporting staff (Ward Administrative Secretaries & WEDPS) report to their cluster rooms immediately."
        ]
      },
      {
        num: 2,
        title: "Receipt & Verification of Nominations",
        sub: "Hours: 11:00 AM – 3:00 PM | Deposit, Proposer & Checklist Verification",
        date: "14.11.2026 to 16.11.2026",
        opsTitle: "Filing & Documentation Rules",
        ops: [
          "<strong>Strict Timing:</strong> Nominations accepted ONLY between 11:00 AM and 3:00 PM on notified days. At 3:00 PM on 16.11.2026, close doors; give slips to persons inside.",
          "<strong>Entry Restrictions:</strong> Maximum 1 vehicle within 100 meters. Maximum 3 persons allowed inside the Election Office (including candidate and proposer).",
          "<strong>Maximum Sets:</strong> A candidate can submit a maximum of <strong>4 sets</strong> of nomination papers for a single ward/office (Rule 8(1)).",
          "<strong>Security Deposit:</strong> Rs. 3,000/- for General; Rs. 1,500/- for SC/ST/BC with Community Certificate (Tahsildar / Form-II). Valid for unreserved or reserved seat; only one deposit needed per candidate.",
          "<strong>Proposer Eligibility:</strong> Proposer for Ward Member MUST be registered in that specific ward. For Chairperson, proposer MUST be registered anywhere in municipality. First delivered nomination counts if proposer signs for multiple candidates."
        ],
        legalTitle: "Officer's Actions Upon Receipt",
        legal: [
          "<strong>Preliminary Examination:</strong> Check candidate and proposer names against electoral roll. Minor clerical/printing errors can be overlooked or corrected.",
          "<strong>Running Serial Number:</strong> Immediately assign running serial number (e.g., 01/Ward-5), write date and minute of receipt, and initial each page.",
          "<strong>Mandatory Enclosures:</strong> (1) Antecedents declaration attested by 2 witnesses (no blanks - write 'Nil'); (2) Form-IA choice of symbols; (3) Community certificate (if SC/ST/BC); (4) MCC declaration.",
          "<strong>Checklist & Receipt (Form-I):</strong> Hand over duplicate copy of checklist with Form-I receipt and scrutiny notice to the candidate/proposer.",
          "<strong>Daily Notice:</strong> Publish Form-III list of nominations received after 3:00 PM daily. On 16.11.2026, publish final consolidated Form-III immediately after 3:00 PM."
        ]
      },
      {
        num: 3,
        title: "Scrutiny of Nominations (Quasi-Judicial Enquiry)",
        sub: "Quasi-Judicial Proceedings | Summary Enquiry | Grounds for Rejection",
        date: "17.11.2026 (From 11:00 AM)",
        opsTitle: "Scrutiny Room Protocol",
        ops: [
          "<strong>Conducted Personally by EO:</strong> Election Officer MUST conduct scrutiny personally. Assistant can step in only if EO is unavoidably prevented.",
          "<strong>Persons Entitled to Attend:</strong> Candidate, Election Agent, Proposer, and ONE person authorised in writing by candidate.",
          "<strong>Summary Examination:</strong> Examine each nomination set serially. Inspection allowed, but physical handling by competitors is strictly forbidden.",
          "<strong>Crucial Age Rule:</strong> Candidate must have attained the age of <strong>21 years</strong> on the date of scrutiny.",
          "<strong>Every Set Scrutinised:</strong> Even if Set 1 is accepted, examine Sets 2, 3, and 4 so that the record is clear for any legal challenges."
        ],
        legalTitle: "Grounds of Rejection & Protections",
        legal: [
          "<strong>Valid Grounds for Rejection:</strong> Not in municipality roll; proposer not in ward roll; age below 21; statutory deposit not paid; disqualified under Sec 13–15; reserved category mismatch; declaration not attested.",
          "<strong>Substantial Character Rule:</strong> Do NOT reject for any defect that is not of a substantial character. Technical, typographical, or clerical errors must be ignored.",
          "<strong>Right of Rebuttal:</strong> If an objection is raised, give candidate reasonable opportunity to rebut up to <strong>the next day (18.11.2026, 11:00 AM)</strong>. Scrutiny of others continues.",
          "<strong>Recording Order:</strong> Record a reasoned order on nomination paper and furnish copy of rejection order immediately to candidate.",
          "<strong>Publication of Form-IV:</strong> Affix Form-IV (List of Validly Nominated Candidates) in Telugu alphabetical order on Notice Board."
        ]
      },
      {
        num: 4,
        title: "Withdrawals, Form-A & B Verification, Symbol Allotment & Form-VII",
        sub: "Deadline: 19.11.2026 3:00 PM | Free vs Reserved Symbols | Uncontested Declaration",
        date: "18.11.2026 to 19.11.2026",
        opsTitle: "Withdrawal & Political Party Form-B",
        ops: [
          "<strong>Notice of Withdrawal (Form-V):</strong> Must be signed by candidate and delivered in person before <strong>3:00 PM on 19.11.2026</strong>. Proposer or auth election agent may deliver if candidate is unable.",
          "<strong>Irrevocable:</strong> Notice of withdrawal, once submitted, CANNOT be cancelled or withdrawn. Issue Form-V receipt immediately.",
          "<strong>Publication:</strong> Publish Form-VI (Notice of Withdrawals) on the notice board after receipt.",
          "<strong>Political Party Form-B Deadline:</strong> Form-B from authorized party signatory must reach EO before <strong>3:00 PM on 19.11.2026</strong>. Form-A must have reached Collector & DEA before 5 PM on 16.11.2026.",
          "<strong>Substitution of Form-B:</strong> Revised Form-B must state earlier one is rescinded. If two Form-Bs received without rescission, first delivered candidate gets symbol."
        ],
        legalTitle: "Allotment of Symbols & Form-VII",
        legal: [
          "<strong>Three Distinct Categories:</strong> Category 1 (Recognised National & State Parties), Category 2 (Registered Parties), Category 3 (Independents).",
          "<strong>Resolving Symbol Clashes:</strong> Clashes resolved by preference: sitting holder gets preference; otherwise decided by drawing lots.",
          "<strong>Form-VII Preparation:</strong> Contesting candidates list prepared in <strong>Telugu alphabetical order of surnames</strong>. Running serial numbers across categories.",
          "<strong>Uncontested Election:</strong> If only ONE valid candidate remains after withdrawal, EO must immediately declare that candidate elected unopposed and send copies to SEC, C&DMA, Collector & DEA, and Municipal Commissioner."
        ]
      },
      {
        num: 5,
        title: "Ballot Paper Printing, Security & Postal Ballots",
        sub: "White (Chairperson) & Pink (Ward Member) | NOTA Panel | Postal Ballot Despatch",
        date: "20.11.2026 to 25.11.2026",
        opsTitle: "Ballot Paper Specifications",
        ops: [
          "<strong>Two Types of Ballot Papers:</strong> <strong>White Wove Paper</strong> for Chairperson election (Direct); <strong>Pink Wove Paper</strong> for Ward Member election.",
          "<strong>NOTA Provision:</strong> None of the Above (NOTA) must be printed as the LAST panel on every ballot paper (both White and Pink).",
          "<strong>Quantity Formula:</strong> Total ward electorate + 10% reserve, rounded to nearest 50. Per polling station requirement rounded to nearest 10.",
          "<strong>Proof-Reading:</strong> Election Officer must personally proofread at press, check candidate names, Telugu spellings, allotted symbols, and serial numbers.",
          "<strong>Security & Custody:</strong> Transport printed ballots under armed escort to Srikalahasti Strong Room. Sort PS-wise 2 to 3 times before sealing."
        ],
        legalTitle: "Postal Ballots Protocol",
        legal: [
          "<strong>Eligible Categories:</strong> Polling personnel drafted for election duty, service voters & wives, voters under preventive detention.",
          "<strong>Dispatch Deadline:</strong> Postal ballot papers MUST be dispatched within <strong>48 hours</strong> of last hour of withdrawal (by 21.11.2026, 3:00 PM).",
          "<strong>Postal Ballot Kit:</strong> (1) Ballot Paper (without symbol + NOTA); (2) Form-XI declaration; (3) Form-XII small envelope; (4) Form-XIII instructions.",
          "<strong>Marked Roll Entry:</strong> Write <strong>'P.B.'</strong> in red ink against voter's entry in marked copy of electoral roll.",
          "<strong>Receipt Deadline:</strong> Must reach Election Officer before 08:00 AM on Counting Day (30.11.2026). Ballots received late are rejected unopened."
        ]
      },
      {
        num: 6,
        title: "P-1 Day Dispatch Operations & Movement to 88 Polling Stations",
        sub: "Distribution Center | Kit Verification | Route Officers Movement | Setup of PS",
        date: "25.11.2026 (Wednesday - P-1 Day)",
        opsTitle: "Dispatch Center Operations",
        ops: [
          "<strong>Central Distribution:</strong> Presiding Officers (POs) and APOs assemble at Central Distribution Center at Srikalahasti.",
          "<strong>Verification of Polling Kit:</strong> Check Ballot Boxes (hinges, mechanism), White & Pink ballot papers (verify serials!), 4 copies of roll (1 marked), Distinguishing Stamp, Arrow cross-mark stamps, Purple pads, Indelible ink phials, Green paper seals, Brass seal, and Form-X-C.",
          "<strong>4 Colour-Coded Covers:</strong> Ensure receipt of BROWN (Box/Accounts), GREEN (Statutory), YELLOW (Non-statutory), and BLUE (Plain stationery) covers."
        ],
        legalTitle: "Movement & Polling Station Setup",
        legal: [
          "<strong>Route Movement:</strong> Polling parties board allotted vehicles along 9 routes under Route Officers and Zonal Officers.",
          "<strong>Arrival at PS:</strong> Report arrival to Municipal Control Room / Zonal Officer immediately.",
          "<strong>Physical Setup of PS:</strong> Ensure strict one-way flow. Position voting compartment for complete secrecy with good lighting. Affix Form-VII Candidate Posters and Area Notice outside.",
          "<strong>Perimeter Security:</strong> Ensure 100-meter and 200-meter security perimeter markings."
        ]
      },
      {
        num: 7,
        title: "Polling Day Operations (P-0) — Mock Poll, Voting & Close of Poll",
        sub: "06:00 AM Agent Check | 07:00 AM to 05:00 PM Poll | Sealing of Box Slit | Form-X-C",
        date: "26.11.2026 (Thursday - Poll Day)",
        opsTitle: "Morning Preparations & Box Sealing",
        ops: [
          "<strong>06:00 AM — Polling Agents Seating:</strong> Verify Form-IX appointment letters. Agents must be electors of same/neighbouring PS. Max 1 agent + 2 relief per candidate.",
          "<strong>06:30 AM — Box Demo & Sealing:</strong> Demonstrate empty box; insert Green Paper Seal; allow agents to note number and sign; insert Address Tag; lock and seal outer latch with wire, address tag, and brass seal.",
          "<strong>Distinguishing Mark Stamping:</strong> Presiding Officer must stamp Distinguishing Mark and sign in full on REVERSE of each ballot paper before issuance."
        ],
        legalTitle: "Poll Duties & 5:00 PM Close",
        legal: [
          "<strong>07:00 AM — Poll Commencement:</strong> Announce prompt start. PO-1 identifies voter; PO-2 applies Indelible Ink on left forefinger, takes signature/thumb impression, issues White & Pink ballots folded vertically then horizontally.",
          "<strong>05:00 PM Queue Slips:</strong> Distribute numbered slips signed by PO from the LAST person in queue to the first. Only electors with slips are allowed to vote.",
          "<strong>Box Slit Sealing:</strong> Close and seal ballot box slit with address tag and brass seal in full view of polling agents.",
          "<strong>Statutory Accounts:</strong> Complete Presiding Officer Diary and Form-X-C (Ballot Paper Account Part-I). Give attested copy of Form-X-C to every polling agent present!"
        ]
      },
      {
        num: 8,
        title: "Reception Center Protocol & Strong Room Double-Locking",
        sub: "Reception = Counting Center | Floor Squares PS-wise | 4-Color Packet Verification",
        date: "26.11.2026 (Evening & Night)",
        opsTitle: "Ward-Wise Reception Desks",
        ops: [
          "<strong>Direct Reception:</strong> Reception Centre is at the designated Counting Centre. No transit reception centers allowed!",
          "<strong>Floor Squares PS-wise:</strong> Predetermined square spaces marked on floor for each of the 88 polling stations.",
          "<strong>Verification of Handover:</strong> Check intact seals of Ballot Box (slit seal, green paper seal, address tags). Receive Form-X-C and PO Diary separately. Check 4 Colour-Coded Covers (Brown, Green, Yellow, Blue).",
          "<strong>Issue Acknowledgement:</strong> Hand over formal printed acknowledgement to PO and relieve polling party."
        ],
        legalTitle: "Strong Room Sealing & Security",
        legal: [
          "<strong>Transfer to Strong Room:</strong> Move sealed ballot boxes and Brown/Green covers into ward-wise bays.",
          "<strong>Double-Lock Protocol:</strong> Secured with double locks. One key with District Election Authority / Designated Officer, second key with Municipal Commissioner / EO.",
          "<strong>Multi-Tier Security:</strong> Continuous 24/7 armed police guard + CCTV coverage (feeds preserved). Logbook maintained for any entry."
        ]
      },
      {
        num: 9,
        title: "Counting of Votes, 15-Minute Recount Rule & Declaration of Results",
        sub: "Postal First | Bundles of 25 & Drum Mixing | 100-Ballot Trays | Form-XX Result Sheet",
        date: "30.11.2026 (From 08:00 AM)",
        opsTitle: "Counting Stages & Adjudication",
        ops: [
          "<strong>08:00 AM — Secrecy & Postal Ballots:</strong> Read out Section 343-F (Secrecy). Count postal ballots at EO table. Defective Form-XI declarations rejected unopened.",
          "<strong>Stage I — Box Verification & Bundling:</strong> Open boxes PS-wise. Verify seals with agents. Unfold ballots and make bundles of <strong>25 ballots</strong> each. Tally with Form-X-C. Mix bundles thoroughly in mixing drum!",
          "<strong>Stage II — Sorting into Trays:</strong> Draw 40 bundles (1,000 ballots) at random per round. Sort into candidate trays + NOTA + 1 Doubtful tray. Valid votes tied in bundles of <strong>100 ballots</strong>.",
          "<strong>Adjudication of Doubtful Ballots:</strong> Election Officer MUST personally adjudicate each doubtful ballot. Grounds: identifying mark, no mark, marked >1, spurious, lacks distinguishing stamp or PO signature."
        ],
        legalTitle: "Recount Window & Declaration",
        legal: [
          "<strong>Mandatory 15-Minute Recount Pause:</strong> After totaling votes in Form-XX Part-I, announce candidate votes and <strong>PAUSE for exactly 15 minutes</strong>. Allow written recount requests.",
          "<strong>Recount Decision:</strong> Decide on grounds, record reasons in writing, amend result sheet if allowed. <em>NO recount request can be entertained once Form-XX Part-I is signed!</em>",
          "<strong>Tie-Breaking by Lot:</strong> 5 slips per candidate placed in box; first drawn slip declared elected.",
          "<strong>Result Declaration:</strong> Sign Form-XX Part-II and declare result. Issue Certificate of Election. Transmit copies to APSEC, C&DMA, Collector & DEA, and Municipal Commissioner.",
          "<strong>Safe Storage:</strong> Sealed candidate ballots packed into steel trunks and deposited in Sub-Treasury under double lock."
        ]
      }
    ],
    chkTitle: "✅ Interactive Stage Checklists",
    chkSub: "Tick off completed duties at each stage. Progress is saved automatically to your device for field reference.",
    chkProgressLabel: "Overall Readiness Progress",
    chkResetBtn: "Reset All",
    chkPrintBtn: "Print Checklist",
    guideTitle: "📌 Important Guidelines for Election Officers",
    guideSub: "Simple, actionable principles governing legal compliance, polling day management, counting, and expenditure audit.",
    dodontTitle: "⚖️ Do's and Don'ts for Election Functionaries",
    dodontSub: "Clear compliance directives for Election Officers, Presiding Officers, Polling Agents, and Field Teams.",
    formsTitle: "📂 Statutory & Non-Statutory Forms Repository",
    formsSub: "Prescribed templates under AP Municipalities Act, 1965 and Conduct of Election Rules, 2026. Click 'Preview' to view full standard text or 'Copy' to use.",
    dirTitle: "🏛️ Srikalahasti Municipality Field Directory",
    dirSub: "Ward reservations, 88 Polling Stations with GIS coordinates & voter counts, 12 Cluster Offices, Zonal & Route Officers, and Surveillance Teams.",
    toolsTitle: "🛠️ Officer Field Utilities, Calculators & Packing Guide",
    toolsSub: "Field calculators for ballot estimation, queue slip tracking, and color-coded envelope packing protocols."
  },

  te: {
    headerTitle: "శ్రీకాళహస్తి పురపాలక సంఘం — 2వ విడత సాధారణ ఎన్నికలు, 2026",
    headerSubtitle: "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం | జిల్లా ఎన్నికల అధికారి & కలెక్టర్, తిరుపతి జిల్లా",
    stats: [
      { label: "వార్డులు", val: "44" },
      { label: "పోలింగ్ కేంద్రాలు", val: "88" },
      { label: "నమోదైన ఓటర్లు", val: "72,537" },
      { label: "ఎన్నికల కార్యాలయాలు", val: "12 క్లస్టర్లు" }
    ],
    banner: {
      title: "⚡ రాష్ట్ర ఎన్నికల సంఘం నోటిఫికేషన్ నెం. 1490/SEC-F1/2026-3 తేది: 12.11.2026 జారీ చేయబడింది",
      desc: "ఆంధ్రప్రదేశ్ మున్సిపాలిటీల చట్టం, 1965 మరియు ఎన్నికల నిర్వహణ నియమావళి, 2026 ప్రకారం ఛైర్‌పర్సన్ (ప్రత్యక్ష ఎన్నిక) మరియు 44 వార్డు సభ్యుల స్థానాలకు ఎన్నికలు ప్రకటించబడ్డాయి.",
      btnChecklists: "చెక్‌లిస్టులు చూడండి",
      btnPrint: "ప్రింట్ తీసుకోండి"
    },
    tabs: [
      { id: "tab-schedule", icon: "📅", title: "ఎన్నికల షెడ్యూలు & గడువులు", badge: "" },
      { id: "tab-stages", icon: "🚶", title: "దశలవారీ మార్గదర్శి", badge: "9 దశలు" },
      { id: "tab-checklists", icon: "✅", title: "చెక్‌లిస్టులు", badge: "8 సెట్లు" },
      { id: "tab-guidelines", icon: "📌", title: "ముఖ్య మార్గదర్శకాలు", badge: "" },
      { id: "tab-dodont", icon: "⚖️", title: "చేయవలసినవి & చేయకూడనివి", badge: "" },
      { id: "tab-forms", icon: "📂", title: "ఫారాలు & ప్రొఫార్మాలు", badge: "22 ఫారాలు" },
      { id: "tab-directory", icon: "🏛️", title: "శ్రీకాళహస్తి డైరెక్టరీ", badge: "88 కేంద్రాలు" },
      { id: "tab-tools", icon: "🛠️", title: "క్షేత్ర సాధనాలు & ప్యాకింగ్", badge: "" }
    ],
    sched: {
      title: "📅 ఎన్నికల కార్యక్రమం & చట్టబద్ధ షెడ్యూలు",
      sub: "ఆంధ్రప్రదేశ్ రాష్ట్ర ఎన్నికల సంఘం (APSEC) చే 2వ విడత పురపాలక సాధారణ ఎన్నికల కొరకు జారీ చేయబడిన సమగ్ర షెడ్యూలు.",
      timelines: [
        { stage: "దశ 1: పూర్వ సన్నాహాలు", date: "14.11.2026 (శనివారం)", title: "వార్డుల వారీ ఓటర్ల జాబితా ప్రదర్శన", desc: "రూల్ 5 ప్రకారం ఎన్నికల అధికారి కార్యాలయ నోటీసు బోర్డుపై వార్డుల వారీ ఓటర్ల జాబితాలను ప్రదర్శిస్తారు.", time: "⏰ ఉదయం 10:00 గంటలకు", class: "" },
        { stage: "దశ 2: ఎన్నికల నోటీసు", date: "14.11.2026 (శనివారం)", title: "ఎన్నికల నోటీసు ప్రచురణ (ఫారం-1)", desc: "రూల్ 6 ప్రకారం ఎన్నికల అధికారిచే నిర్దేశిత ఫారంలో ఎన్నికల నోటీసు జారీ చేయబడుతుంది.", time: "⏰ ఉదయం (నామినేషన్లకు ముందు)", class: "" },
        { stage: "దశ 3: నామినేషన్లు", date: "14.11.2026 నుండి 16.11.2026", title: "నామినేషన్ల దాఖలు & స్వీకరణ", desc: "12 నిర్దేశిత ఎన్నికల కార్యాలయాలలో (ఛైర్‌పర్సన్ + 11 వార్డు క్లస్టర్లు) నామినేషన్ల స్వీకరణ.", time: "⏰ ప్రతిరోజూ ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు", time: "⏰ 11:00 AM to 3:00 PM Daily", class: "active-stage" },
        { stage: "దశ 4: ఆఖరు తేది", date: "16.11.2026 (సోమవారం)", title: "నామినేషన్ల ఆఖరు సమయం & ఫారం-A", desc: "నామినేషన్లకు ఆఖరు గడువు (మధ్యాహ్నం 3 గం). రాజకీయ పార్టీల ఫారం-A జిల్లా కలెక్టర్‌కు సాయంత్రం 5 గం లోపు.", time: "⏰ మధ్యాహ్నం 3:00 (ఖచ్చితంగా) / సాయంత్రం 5:00 (ఫారం-A)", class: "" },
        { stage: "దశ 5: పరిశీలన", date: "17.11.2026 (మంగళవారం)", title: "నామినేషన్ల పరిశీలన (స్క్రూటినీ)", desc: "ఎన్నికల అధికారిచే స్వయంగా న్యాయబద్ధ పరిశీలన. చెల్లుబాటైన అభ్యర్థుల జాబితా (ఫారం-IV) ప్రచురణ.", time: "⏰ ఉదయం 11:00 గంటల నుండి", class: "" },
        { stage: "దశ 6: ఉపసంహరణలు & గుర్తులు", date: "19.11.2026 (గురువారం)", title: "ఉపసంహరణ & ఫారం-VII ప్రచురణ", desc: "అభ్యర్థిత్వాల ఉపసంహరణ (ఫారం-V) మధ్యాహ్నం 3 గం లోపు. గుర్తుల కేటాయింపు & ఫారం-VII ప్రచురణ.", time: "⏰ ఉపసంహరణ: మధ్యాహ్నం 3:00 లోపు | ఫారం-VII: మధ్యాహ్నం 3:00 తరువాత", class: "" },
        { stage: "దశ 7: పోలింగ్ రోజు", date: "26.11.2026 (గురువారం)", title: "పోలింగ్ నిర్వహణ (ఓటింగ్)", desc: "అన్ని 88 పోలింగ్ కేంద్రాలలో తెలుపు (ఛైర్‌పర్సన్) మరియు గులాబీ (వార్డు సభ్యులు) బ్యాలెట్లతో పోలింగ్.", time: "⏰ ఉదయం 07:00 నుండి సాయంత్రం 05:00 వరకు", class: "poll-stage" },
        { stage: "దశ 8: రీ-పోలింగ్", date: "27.11.2026 (శుక్రవారం)", title: "రీ-పోలింగ్ తేది (అవసరమైతే)", desc: "చట్టబద్ధ కారణాలపై రాష్ట్ర ఎన్నికల సంఘం ఆదేశిస్తే నిర్వహించే రీ-పోలింగ్ తేది.", time: "⏰ ఉదయం 07:00 నుండి సాయంత్రం 05:00 వరకు", class: "" },
        { stage: "దశ 9: లెక్కింపు", date: "30.11.2026 (సోమవారం)", title: "ఓట్ల లెక్కింపు & ఫలితాల ప్రకటన", desc: "నిర్దేశిత లెక్కింపు కేంద్రంలో ఓట్ల లెక్కింపు. ఫారం-XX పార్ట్-I & II ద్వారా ఫలితాల ప్రకటన.", time: "⏰ ఉదయం 08:00 గంటల నుండి", class: "counting-stage" }
      ],
      timeLimitsTitle: "⏱️ ముఖ్యమైన చట్టబద్ధ సమయ పరిమితులు (C&DMA నిబంధనలు)",
      timeLimitsCols: ["ఎన్నికల ప్రక్రియ / విధి", "చట్టబద్ధ సమయ పరిమితి", "బాధ్యతాయుత అధికారి", "చట్టబద్ధ ఆధారం"],
      timeLimits: [
        { act: "నామినేషన్ల స్వీకరణ", limit: "ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు (సెలవు దినాలతో సహా)", resp: "ఎన్నికల అధికారి (EO) / అసిస్టెంట్ EO", cite: "రూల్ 8(1), ఎన్నికల నియమావళి 2026" },
        { act: "చెక్‌లిస్ట్ పెండింగ్ పత్రాల సమర్పణ", limit: "నామినేషన్ల ఆఖరు తేది (16.11.2026) మధ్యాహ్నం 3:00 గంటల లోపు", resp: "అభ్యర్థి / ప్రతిపాదకుడు", cite: "C&DMA / SEC మార్గదర్శకాలు" },
        { act: "ఫారం-A సమర్పణ (పార్టీ అధికార పత్రం)", limit: "నామినేషన్ల ఆఖరు తేది (16.11.2026) సాయంత్రం 5:00 గంటల లోపు", resp: "రాజకీయ పార్టీ అధ్యక్షుడు/కార్యదర్శి కలెక్టర్ & DEA కు", cite: "గుర్తుల ఆర్డర్ పారా 13 / SEC ఉత్తర్వులు" },
        { act: "ఫారం-B సమర్పణ (అభ్యర్థి స్పాన్సర్‌షిప్)", limit: "ఉపసంహరణల ఆఖరు తేది (19.11.2026) మధ్యాహ్నం 3:00 గంటల లోపు", resp: "అధికారిక పార్టీ ప్రతినిధి ఎన్నికల అధికారికి", cite: "గుర్తుల ఆర్డర్ పారా 13" },
        { act: "అభ్యర్థిత్వాల ఉపసంహరణ (ఫారం-V)", limit: "19.11.2026 మధ్యాహ్నం 3:00 గంటల లోపు (ఖచ్చితంగా)", resp: "అభ్యర్థి స్వయంగా / ప్రతిపాదకుడు / ఎన్నికల ఏజెంట్", cite: "రూల్ 13, ఎన్నికల నియమావళి 2026" },
        { act: "పోస్టల్ బ్యాలెట్ల పంపకం", limit: "ఉపసంహరణల సమయం ముగిసిన 48 గంటలలోపు (21.11.2026 మధ్యాహ్నం 3 గం)", resp: "ఎన్నికల అధికారి (EO)", cite: "రూల్ 22 నుండి 27, G.O.Ms.No.213" },
        { act: "పోలింగ్ ఏజెంట్ల నియామక సమాచారం", limit: "పోలింగ్ రోజుకు కనీసం 3 రోజుల ముందుగా (23.11.2026 లోపు)", resp: "అభ్యర్థి / ఎన్నికల ఏజెంట్ EO/PO కు", cite: "రూల్ 18 / SEC మార్గదర్శకాలు" },
        { act: "ప్రచార నిశ్శబ్ద సమయం (సైలెన్స్ పీరియడ్)", limit: "పోలింగ్ ముగిసే సమయానికి ముందు 48 గంటల నుండి", resp: "అన్ని రాజకీయ పార్టీలు / అభ్యర్థులు / మీడియా", cite: "సెక్షన్ 343-A AP మున్సిపాలిటీల చట్టం" },
        { act: "పోలింగ్ వేళలు", limit: "ఉదయం 07:00 నుండి సాయంత్రం 05:00 వరకు (5 గంటలకు క్యూలో ఉన్నవారికి స్లిప్పులు)", resp: "ప్రిసైడింగ్ అధికారి (PO)", cite: "నోటిఫికేషన్ నెం. 1490/SEC-F1/2026-3" },
        { act: "అభ్యర్థి ఎన్నికల ఖర్చుల ఖాతా సమర్పణ", limit: "పోటీచేయు జాబితా ప్రచురణ నుండి ప్రతి 3 రోజులకు ఒకసారి", resp: "అభ్యర్థి వ్యయ పరిశీలన బృందానికి", cite: "సెక్షన్ 343-ZC / SEC ఆర్డర్ 135" },
        { act: "ఓట్ల రీ-కౌంటింగ్ దరఖాస్తు గడువు", limit: "మొత్తం ఓట్ల ప్రకటన జరిగిన 15 నిమిషాల లోపు", resp: "అభ్యర్థి / ఎన్నికల ఏజెంట్ ఎన్నికల అధికారికి", cite: "కౌంటింగ్ నియమావళి నిబంధనలు" },
        { act: "స్థానం ఎంపిక (ఒకటి కంటే ఎక్కువ గెలిస్తే)", limit: "తుది ఫలితాల ప్రకటన నుండి 15 రోజుల లోపు", resp: "గెలిచిన అభ్యర్థి మున్సిపల్ కమిషనర్‌కు", cite: "రూల్ 62, AP మున్సిపల్ ఎన్నికల రూల్స్" }
      ]
    },
    stagesTitle: "🚶 ఎన్నికల అధికారుల కొరకు దశలవారీ క్షేత్ర మార్గదర్శి",
    stagesSub: "నోటిఫికేషన్ నుండి స్ట్రాంగ్ రూమ్ భద్రత వరకు అంచెలంచెలుగా నిర్వహించాల్సిన చట్టబద్ధ విధులు మరియు పద్ధతులు.",
    stages: [
      {
        num: 1,
        title: "పూర్వ సన్నాహాలు, ఓటర్ల జాబితా ప్రదర్శన & ఫారం-1 నోటీసు",
        sub: "ఓటర్ల జాబితా ప్రదర్శన (రూల్ 5) | ఎన్నికల నోటీసు జారీ (రూల్ 6)",
        date: "12.11.2026 నుండి 14.11.2026",
        opsTitle: "ముఖ్య నిర్వహణ చర్యలు",
        ops: [
          "<strong>జాబితా ఫ్రీజింగ్:</strong> 12.11.2026 (నోటిఫికేషన్ తేది) నాటికి ఉన్న వార్డుల వారీ ఓటర్ల జాబితా ఫ్రీజ్ చేయబడింది. RP చట్టం 1950 క్రింద అప్పటివరకు చేర్చిన మార్పులు చేర్పులు పరిగణించబడతాయి.",
          "<strong>ఓటర్ల జాబితా ప్రదర్శన (14.11.2026 ఉదయం):</strong> రూల్ 5 ప్రకారం ఎన్నికల అధికారి మున్సిపల్ కార్యాలయ నోటీసు బోర్డుపై మరియు ప్రతి వార్డులోని ప్రముఖ ప్రదేశాలలో ఓటర్ల జాబితాను ప్రదర్శించాలి.",
          "<strong>ఎన్నికల నోటీసు (ఫారం-1):</strong> రూల్ 6 ప్రకారం నిర్దేశిత ఫారంలో తెలుగు మరియు ఆంగ్లంలో స్థానాలు, రిజర్వేషన్లు, నామినేషన్ గదులు, తేదీలు మరియు వేళలను పేర్కొంటూ నోటీసు ప్రచురించాలి.",
          "<strong>12 ఎన్నికల కార్యాలయాల ఏర్పాటు:</strong> ఛైర్‌పర్సన్ స్థానానికి 1 ప్రత్యేక కార్యాలయం మరియు 11 వార్డు క్లస్టర్ కార్యాలయాలు (ఒక్కొక్కటి 4 వార్డులు: 1-4, 5-8, 9-12 మొదలైనవి) సిద్ధం చేయాలి.",
          "<strong>స్టేషనరీ & ఫారాల పంపిణీ:</strong> ఖాళీ నామినేషన్ పత్రాలు, ఆస్తులు/నేర చరిత్ర డిక్లరేషన్లు, ఫారం-IA మొదలైనవి అభ్యర్థులకు ఉచితంగా అందించాలి."
        ],
        legalTitle: "చట్టబద్ధ నిబంధనలు & పరిమితులు",
        legal: [
          "<strong>లాభదాయక పదవి & అనర్హతలు:</strong> AP మున్సిపాలిటీల చట్టం, 1965 లోని సెక్షన్లు 13, 13-A, 14, 15, 15-A, మరియు 15-B ల క్రింద అనర్హతలను క్షుణ్ణంగా సమీక్షించాలి.",
          "<strong>ఖర్చుల గరిష్ట పరిమితులు:</strong> ఛైర్‌పర్సన్ స్థానానికి గరిష్ట ఖర్చు పరిమితి <strong>రూ. 20.00 లక్షలు</strong>, వార్డు సభ్యుల స్థానానికి <strong>రూ. 7.50 లక్షలు</strong>.",
          "<strong>ప్రత్యేక నోటీసులు:</strong> ఛైర్‌పర్సన్ మరియు వార్డు సభ్యుల స్థానాలకు రిజర్వేషన్ విభాగాలను స్పష్టంగా తెలుపుతూ వేర్వేరు నోటీసులు ప్రదర్శించాలి.",
          "<strong>సహాయక సిబ్బంది హాజరు:</strong> నియమించబడిన వార్డు కార్యదర్శులు (WA & WEDPS) తక్షణమే తమ క్లస్టర్ కార్యాలయాలలో రిపోర్ట్ చేయాలి."
        ]
      },
      {
        num: 2,
        title: "నామినేషన్ల స్వీకరణ & ప్రాథమిక పరిశీలన",
        sub: "వేళలు: ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు | డిపాజిట్, ప్రతిపాదకుడు & చెక్‌లిస్ట్",
        date: "14.11.2026 నుండి 16.11.2026",
        opsTitle: "నామినేషన్ల నిబంధనలు",
        ops: [
          "<strong>ఖచ్చితమైన వేళలు:</strong> ప్రకటించిన తేదీలలో ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 గంటల వరకు మాత్రమే నామినేషన్లు స్వీకరించాలి. 16.11.2026 మధ్యాహ్నం 3:00 కు తలుపులు మూసి, లోపల ఉన్నవారికి స్లిప్పులు ఇవ్వాలి.",
          "<strong>ప్రవేశ పరిమితులు:</strong> 100 మీటర్ల పరిధిలోకి 1 వాహనం మాత్రమే అనుమతి. కార్యాలయం లోపలికి అభ్యర్థి, ప్రతిపాదకుడితో కలిపి గరిష్టంగా 3 గురు మాత్రమే అనుమతింపబడతారు.",
          "<strong>గరిష్ట సెట్లు:</strong> ఒక అభ్యర్థి ఒక వార్డు/స్థానానికి గరిష్టంగా <strong>4 సెట్లు</strong> మాత్రమే నామినేషన్లు దాఖలు చేయవచ్చు (రూల్ 8(1)).",
          "<strong>భద్రతా డిపాజిట్:</strong> జనరల్ అభ్యర్థులకు <strong>రూ. 3,000/-</strong>; ఎస్సీ / ఎస్టీ / బీసీ అభ్యర్థులకు తహసీల్దార్ జారీచేసిన కుల ధృవీకరణ పత్రం / ఫారం-II తో <strong>రూ. 1,500/-</strong>. అభ్యర్థి 4 సెట్లు వేసినా డిపాజిట్ ఒక్కసారే చెల్లించాలి.",
          "<strong>ప్రతిపాదకుడి అర్హత:</strong> వార్డు సభ్యుల స్థానానికి ప్రతిపాదకుడు అదే వార్డులో నమోదైన ఓటర్ అయి ఉండాలి. ఛైర్‌పర్సన్ స్థానానికి మున్సిపాలిటీలోని ఏ వార్డు ఓటరైనా ప్రతిపాదించవచ్చు. ఒకే వార్డులో ఒకరి కంటే ఎక్కువ మందికి ప్రతిపాదిస్తే మొదట అందినదే చెల్లుతుంది."
        ],
        legalTitle: "అధికారి తీసుకోవలసిన చర్యలు",
        legal: [
          "<strong>ప్రాథమిక పరిశీలన:</strong> అభ్యర్థి మరియు ప్రతిపాదకుడి పేర్లను ఓటర్ల జాబితాతో సరిచూడాలి. చిన్న చిన్న సాంకేతిక లేదా ముద్రణ లోపాలను సరిదిద్దవచ్చు.",
          "<strong>వరుస సంఖ్య & సంతకం:</strong> నామినేషన్ అందిన వెంటనే రన్నింగ్ సీరియల్ నంబర్ (ఉదా: 01/వార్డు-5), అందిన తేదీ, ఖచ్చితమైన సమయం నమోదు చేసి అధికారి సంతకం చేయాలి.",
          "<strong>తప్పనిసరి జతపరచవలసినవి:</strong> (1) ఇద్దరు సాక్షుల సంతకాలతో కూడిన నేర చరిత్ర/ఆస్తుల డిక్లరేషన్ (ఏ కాలమ్ ఖాళీగా ఉంచరాదు - 'వర్తించదు/ఏమీలేవు' అని రాయాలి); (2) ఫారం-IA గుర్తుల ఎంపిక; (3) కుల ధృవీకరణ పత్రం; (4) ఎన్నికల ప్రవర్తనా నియమావళి అంగీకార పత్రం.",
          "<strong>చెక్‌లిస్ట్ & రసీదు (ఫారం-I):</strong> పత్రాల చెక్‌లిస్ట్ ఎండార్స్ చేసి, దాని నకలుతో పాటు ఫారం-I రసీదు మరియు పరిశీలన నోటీసును అభ్యర్థి/ప్రతిపాదకుడికి అందజేయాలి.",
          "<strong>రోజువారీ జాబితా:</strong> ప్రతిరోజూ మధ్యాహ్నం 3:00 తరువాత అందిన నామినేషన్ల జాబితా (ఫారం-III) నోటీసు బోర్డుపై ప్రదర్శించాలి. 16.11.2026 న మధ్యాహ్నం 3:00 గంటల తరువాత తుది ఫారం-III ప్రచురించాలి."
        ]
      },
      {
        num: 3,
        title: "నామినేషన్ల పరిశీలన (స్క్రూటినీ - న్యాయబద్ధ విచారణ)",
        sub: "ఎన్నికల అధికారిచే స్వయంగా విచారణ | తిరస్కరణకు చట్టబద్ధ కారణాలు",
        date: "17.11.2026 (ఉదయం 11:00 గంటల నుండి)",
        opsTitle: "పరిశీలన గది నియమావళి",
        ops: [
          "<strong>స్వయంగా అధికారి నిర్వహణ:</strong> ఎన్నికల అధికారి స్వయంగా పరిశీలన జరపాలి. అధికారి అనివార్య కారణాల వల్ల గైర్హాజరైతే తప్ప సహాయక అధికారికి అప్పగించరాదు.",
          "<strong>హాజరు కావడానికి అర్హులు:</strong> అభ్యర్థి, ఎన్నికల ఏజెంట్, ప్రతిపాదకుడు, మరియు అభ్యర్థి లిఖితపూర్వకంగా అనుమతించిన ఒక్క వ్యక్తి మాత్రమే హాజరు కావచ్చు.",
          "<strong>సంక్షిప్త విచారణ:</strong> ఒక్కొక్క నామినేషన్ సెట్‌ను వరుసగా పరిశీలించాలి. ఇతర అభ్యర్థులు పత్రాలను చూసేందుకు అనుమతించవచ్చు, కానీ చేతులతో తాకరాదు.",
          "<strong>వయోపరిమితి నిబంధన:</strong> పరిశీలన తేది నాటికి అభ్యర్థికి ఖచ్చితంగా <strong>21 సంవత్సరాలు</strong> నిండి ఉండాలి.",
          "<strong>అన్ని సెట్ల పరిశీలన:</strong> మొదటి సెట్ ఆమోదించబడినప్పటికీ, మిగిలిన 2, 3, 4 సెట్లను కూడా పూర్తిగా పరిశీలించి రికార్డు నమోదు చేయాలి."
        ],
        legalTitle: "తిరస్కరణ కారణాలు & రక్షణలు",
        legal: [
          "<strong>తిరస్కరణకు చెల్లుబాటు కారణాలు:</strong> మున్సిపల్ ఓటర్ల జాబితాలో పేరు లేకపోవడం; ప్రతిపాదకుడు ఆ వార్డు ఓటర్ కాకపోవడం; 21 ఏళ్ల వయస్సు లేకపోవడం; నిర్దేశిత డిపాజిట్ చెల్లించకపోవడం; సెక్షన్ 13–15 క్రింద అనర్హత కలిగి ఉండడం; రిజర్వేషన్ వర్గం తప్పుగా ఉండడం; డిక్లరేషన్‌లో కాలమ్స్ ఖాళీగా ఉండడం.",
          "<strong>తాత్విక ప్రాధాన్యత సూత్రం:</strong> కీలకమైనది కాని సాధారణ క్లరికల్, స్పెల్లింగ్ లేదా టైపింగ్ తప్పులకు నామినేషన్‌ను ఎట్టిపరిస్థితుల్లో తిరస్కరించరాదు.",
          "<strong>సమాధానమిచ్చే అవకాశం:</strong> ఏదైనా అభ్యంతరం వ్యక్తమైతే, అభ్యర్థి సమాధానం చెప్పుకునేందుకు <strong>మరుసటి రోజు (18.11.2026 ఉదయం 11:00 వరకు)</strong> సమయం ఇవ్వాలి. మిగతా అభ్యర్థుల పరిశీలన కొనసాగించాలి.",
          "<strong>ఉత్తర్వు నమోదు:</strong> తిరస్కరణకు కారణాలను స్పష్టంగా లిఖితపూర్వకంగా నమోదు చేసి, ఆ ఉత్తర్వు ప్రతిని వెంటనే అభ్యర్థికి అందజేయాలి.",
          "<strong>ఫారం-IV ప్రచురణ:</strong> పరిశీలన ముగిసిన వెంటనే చెల్లుబాటైన అభ్యర్థుల జాబితాను తెలుగు అక్షర క్రమంలో ఫారం-IV లో నోటీసు బోర్డుపై ప్రదర్శించాలి."
        ]
      },
      {
        num: 4,
        title: "అభ్యర్థిత్వాల ఉపసంహరణ, ఫారం-B, గుర్తుల కేటాయింపు & ఫారం-VII",
        sub: "గడువు: 19.11.2026 మధ్యాహ్నం 3:00 | పార్టీ గుర్తులు vs ఉచిత గుర్తులు | ఏకగ్రీవ ప్రకటన",
        date: "18.11.2026 నుండి 19.11.2026",
        opsTitle: "ఉపసంహరణ & పార్టీ ఫారం-B",
        ops: [
          "<strong>ఉపసంహరణ నోటీసు (ఫారం-V):</strong> అభ్యర్థి సంతకం చేసిన ఉపసంహరణ పత్రాన్ని <strong>19.11.2026 మధ్యాహ్నం 3:00 లోపు</strong> స్వయంగా అందజేయాలి. అభ్యర్థి రాలేకపోతే ప్రతిపాదకుడు లేదా అధీకృత ఏజెంట్ ఇవ్వవచ్చు.",
          "<strong>రద్దు చేయలేనిది:</strong> ఒక్కసారి ఉపసంహరణ పత్రం సమర్పించిన తరువాత దానిని ఎట్టిపరిస్థితుల్లో వెనక్కి తీసుకోలేరు. వెంటనే ఫారం-V రసీదు జారీ చేయాలి.",
          "<strong>ప్రచురణ:</strong> ఉపసంహరణల వివరాలను ఫారం-VI లో నోటీసు బోర్డుపై ప్రదర్శించాలి.",
          "<strong>పార్టీ ఫారం-B గడువు:</strong> గుర్తింపు పొందిన పార్టీల అధీకృత ప్రతినిధి సంతకం చేసిన ఫారం-B <strong>19.11.2026 మధ్యాహ్నం 3:00 గంటల లోపు</strong> ఎన్నికల అధికారికి అందాలి. ఫారం-A 16.11.2026 సాయంత్రం 5 గం లోపు కలెక్టర్‌కు చేరి ఉండాలి.",
          "<strong>ఫారం-B సవరణ:</strong> సవరించిన ఫారం-B ఇచ్చినప్పుడు మునుపటిది రద్దయినట్లు పేర్కొనాలి. రెండు ఫారం-B లు రద్దు లేకుండా వస్తే మొదట నామినేషన్ వేసిన అభ్యర్థికే గుర్తు లభిస్తుంది."
        ],
        legalTitle: "గుర్తుల కేటాయింపు & ఫారం-VII",
        legal: [
          "<strong>మూడు విభాగాలు:</strong> విభాగం 1 (గుర్తింపు పొందిన జాతీయ & రాష్ట్ర పార్టీలు), విభాగం 2 (రిజిస్టర్డ్ రాజకీయ పార్టీలు), విభాగం 3 (స్వతంత్ర అభ్యర్థులు).",
          "<strong>గుర్తుల వివాద పరిష్కారం:</strong> ఒకే గుర్తును ఇద్దరు స్వతంత్రులు కోరితే, ప్రస్తుత ప్రజాప్రతినిధికి ప్రాధాన్యత ఇస్తారు; లేదా లాటరీ ద్వారా నిర్ణయిస్తారు.",
          "<strong>ఫారం-VII తయారీ:</strong> పోటీచేయు అభ్యర్థుల తుది జాబితాను <strong>తెలుగు అక్షర క్రమంలో (ఇంటిపేరు ఆధారంగా)</strong> తయారు చేసి మధ్యాహ్నం 3:00 గంటల తరువాత ప్రచురించాలి.",
          "<strong>ఏకగ్రీవ ఎన్నిక ప్రకటన:</strong> ఉపసంహరణల తరువాత ఒకే ఒక్క అభ్యర్థి మిగిలితే, ఆ అభ్యర్థి ఏకగ్రీవంగా ఎన్నికైనట్లు వెంటనే ప్రకటించి SEC, C&DMA, కలెక్టర్ మరియు మున్సిపల్ కమిషనర్‌లకు నివేదించాలి."
        ]
      },
      {
        num: 5,
        title: "బ్యాలెట్ పత్రాల ముద్రణ, భద్రత & పోస్టల్ బ్యాలెట్లు",
        sub: "తెలుపు (ఛైర్‌పర్సన్) & గులాబీ (వార్డు సభ్యులు) | నోటా (NOTA) | 48 గంటల్లో పోస్టల్ పంపకం",
        date: "20.11.2026 నుండి 25.11.2026",
        opsTitle: "బ్యాలెట్ పత్రాల ప్రమాణాలు",
        ops: [
          "<strong>రెండు రకాల బ్యాలెట్ పత్రాలు:</strong> ఛైర్‌పర్సన్ ఎన్నికకు <strong>తెలుపు రంగు (White Wove)</strong> పేపర్; వార్డు సభ్యుల ఎన్నికకు <strong>గులాబీ రంగు (Pink Wove)</strong> పేపర్ వాడాలి.",
          "<strong>నోటా (NOTA) నిబంధన:</strong> ప్రతి బ్యాలెట్ పత్రంపై (తెలుపు మరియు గులాబీ రెండింటిలోనూ) చిట్టచివరి ప్యానెల్‌లో 'పైవారెవరూ కాదు (NOTA)' ముద్రించాలి.",
          "<strong>పరిమాణాల లెక్కింపు:</strong> మొత్తం వార్డు ఓటర్ల సంఖ్య + 10% అదనపు నిల్వ, దీనిని సమీప 50 కి రౌండ్ చేయాలి. పోలింగ్ కేంద్రం వారీగా సమీప 10 కి రౌండ్ చేయాలి.",
          "<strong>ప్రూఫ్ రీడింగ్:</strong> ఎన్నికల అధికారి స్వయంగా ప్రింటింగ్ ప్రెస్ వద్ద ప్రూఫ్ తనిఖీ చేసి, అభ్యర్థుల పేర్లు, తెలుగు స్పెల్లింగ్స్, గుర్తులు మరియు వరుస సంఖ్యలను సరిచూడాలి.",
          "<strong>భద్రత & తరలింపు:</strong> ముద్రించిన బ్యాలెట్లను సాయుధ పోలీసు బందోబస్తుతో శ్రీకాళహస్తి స్ట్రాంగ్ రూమ్‌కు తరలించి, పోలింగ్ కేంద్రాల వారీగా 2-3 సార్లు సరిచూసి సీల్ చేయాలి."
        ],
        legalTitle: "పోస్టల్ బ్యాలెట్ల పద్ధతి",
        legal: [
          "<strong>అర్హులైన ఓటర్లు:</strong> ఎన్నికల విధులలో ఉన్న ఉద్యోగులు, సర్వీస్ ఓటర్లు మరియు వారి భార్యలు, ప్రివెంటివ్ డిటెన్షన్‌లో ఉన్న వ్యక్తులు.",
          "<strong>పంపకానికి గడువు:</strong> ఉపసంహరణల సమయం ముగిసిన <strong>48 గంటలలోపు (21.11.2026 మధ్యాహ్నం 3:00 లోపు)</strong> పోస్టల్ బ్యాలెట్లు తప్పనిసరిగా పోస్ట్ చేయాలి.",
          "<strong>పోస్టల్ బ్యాలెట్ కిట్:</strong> (1) గుర్తులేని బ్యాలెట్ పత్రం + NOTA; (2) ఫారం-XI డిక్లరేషన్; (3) ఫారం-XII చిన్న కవర్; (4) ఫారం-XIII సూచనల పత్రం.",
          "<strong>గుర్తుపెట్టిన జాబితాలో నమోదు:</strong> మార్క్డ్ కాపీ ఓటర్ల జాబితాలో సంబంధిత ఓటరు పేరు ఎదురుగా ఎరుపు సిరాతో <strong>'P.B.'</strong> అని నమోదు చేయాలి.",
          "<strong>స్వీకరణ గడువు:</strong> కౌంటింగ్ ప్రారంభ సమయం (30.11.2026 ఉదయం 8:00) లోపు అందిన పోస్టల్ బ్యాలెట్లను మాత్రమే లెక్కింపులోకి తీసుకుంటారు. ఆలస్యంగా వచ్చినవి తెరవకుండానే తిరస్కరిస్తారు."
        ]
      },
      {
        num: 6,
        title: "P-1 రోజు డిస్పాచ్ కార్యకలాపాలు & 88 కేంద్రాలకు తరలింపు",
        sub: "పంపిణీ కేంద్రం | పోలింగ్ కిట్ తనిఖీ | 9 రూట్లలో తరలింపు | పోలింగ్ కేంద్రం ఏర్పాటు",
        date: "25.11.2026 (బుధవారం - P-1 రోజు)",
        opsTitle: "పంపిణీ కేంద్రం విధులు",
        ops: [
          "<strong>కేంద్ర పంపిణీ స్థావరం:</strong> శ్రీకాళహస్తిలోని పంపిణీ కేంద్రం వద్ద ప్రిసైడింగ్ అధికారులు మరియు పోలింగ్ సిబ్బంది హాజరు కావాలి.",
          "<strong>సామగ్రి క్షుణ్ణ తనిఖీ:</strong> బ్యాలెట్ పెట్టెలు (కీలు, లాకింగ్ పనితీరు), తెలుపు & గులాబీ బ్యాలెట్ పత్రాలు (వరుస సంఖ్యలు సరిచూసుకోవాలి!), 4 కాపీల ఓటర్ల జాబితా (1 మార్క్డ్ కాపీ), డిస్టింగ్విషింగ్ మార్క్ స్టాంప్, ఆరో క్రాస్-మార్క్ స్టాంపులు, పర్పుల్ ప్యాడ్లు, చెరగని సిరా సీసాలు, గ్రీన్ పేపర్ సీల్స్, ఇత్తడి సీలు మరియు ఫారం-X-C సరిచూసుకోవాలి.",
          "<strong>4 రంగుల కవర్లు:</strong> బ్రౌన్ (పెట్టె/లెక్కల కవర్), గ్రీన్ (చట్టబద్ధ కవర్), ఎల్లో (చట్టబద్ధేతర కవర్), మరియు బ్లూ (సాధారణ స్టేషనరీ కవర్) అందినట్లు నిర్ధారించుకోవాలి."
        ],
        legalTitle: "తరలింపు & కేంద్రం ఏర్పాటు",
        legal: [
          "<strong>రూట్లలో ప్రయాణం:</strong> కేటాయించిన రూట్ అధికారులు మరియు జోనల్ అధికారుల పర్యవేక్షణలో 9 రూట్లలో ప్రత్యేక వాహనాలలో కేంద్రాలకు చేరుకోవాలి.",
          "<strong>చేరిక నివేదిక:</strong> పోలింగ్ కేంద్రానికి చేరుకున్న వెంటనే మున్సిపల్ కంట్రోల్ రూమ్‌కు సమాచారం అందించాలి.",
          "<strong>కేంద్రం అమరిక:</strong> వన్-వే పద్ధతిలో ఓటర్లు వచ్చి వెళ్లేలా బల్లలు అమర్చాలి. ఓటు గోప్యతను కాపాడుతూ మంచి వెలుతురు ఉండేలా ఓటింగ్ కంపార్ట్‌మెంట్‌ను ఏర్పాటు చేయాలి. బయట ఫారం-VII పోస్టర్ మరియు ఏరియా నోటీసు అతికించాలి.",
          "<strong>భద్రతా పరిధి:</strong> 100 మీటర్లు మరియు 200 మీటర్ల పరిధిని సున్నంతో స్పష్టంగా గుర్తించాలి."
        ]
      },
      {
        num: 7,
        title: "పోలింగ్ రోజు విధులు (P-0) — మాక్ పోల్, ఓటింగ్ & ముగింపు",
        sub: "06:00 AM ఏజెంట్ల తనిఖీ | 07:00 AM నుండి 05:00 PM పోలింగ్ | స్లిట్ సీలింగ్ | ఫారం-X-C",
        date: "26.11.2026 (గురువారం - పోలింగ్ రోజు)",
        opsTitle: "ఉదయపు సన్నాహాలు & పెట్టె సీలింగ్",
        ops: [
          "<strong>06:00 AM — పోలింగ్ ఏజెంట్ల ప్రవేశం:</strong> ఫారం-IX నియామక పత్రాలను తనిఖీ చేసి సంతకం చేయాలి. ఏజెంట్ ఆ కేంద్రం/పొరుగు కేంద్రం ఓటర్ అయి ఉండాలి. అభ్యర్థికి 1 ఏజెంట్ + 2 రిలీవర్ల మాత్రమే అనుమతి.",
          "<strong>06:30 AM — ఖాళీ పెట్టె ప్రదర్శన & సీలింగ్:</strong> బ్యాలెట్ పెట్టె ఖాళీగా ఉన్నట్లు ఏజెంట్లకు చూపించాలి; గ్రీన్ పేపర్ సీల్ వేసి నంబర్ నమోదు చేయించాలి; అడ్రస్ ట్యాగ్ లోపల వేయాలి; పెట్టెను లాక్ చేసి బైండింగ్ వైర్, అడ్రస్ ట్యాగ్ మరియు ఇత్తడి సీలుతో సీల్ చేయాలి.",
          "<strong>డిస్టింగ్విషింగ్ మార్క్ & సంతకం:</strong> ఓటరుకు ఇచ్చే ముందు ప్రిసైడింగ్ అధికారి ప్రతి బ్యాలెట్ పత్రం వెనుక డిస్టింగ్విషింగ్ మార్క్ స్టాంప్ వేసి పూర్తి సంతకం చేయాలి."
        ],
        legalTitle: "ఓటింగ్ నిర్వహణ & సాయంత్రం 5:00 ముగింపు",
        legal: [
          "<strong>07:00 AM — పోలింగ్ ప్రారంభం:</strong> సరిగ్గా 7 గంటలకు పోలింగ్ ప్రారంభించాలి. PO-1 గుర్తింపు కార్డు పరిశీలించి ఓటరు పేరును జాబితాలో మార్క్ చేస్తారు; PO-2 ఎడమ చూపుడు వేలికి గోరు నుండి మొదటి కణుపు వరకు చెరగని సిరా వేసి, సంతకం/వేలిముద్ర తీసుకుని, నిలువుగా అడ్డంగా మడిచిన తెలుపు & గులాబీ బ్యాలెట్లను ఇస్తారు.",
          "<strong>05:00 PM క్యూ స్లిప్పుల పంపిణీ:</strong> సాయంత్రం 5:00 గంటలకు క్యూ చివర నిలబడిన వ్యక్తికి 1వ నంబర్ స్లిప్ ఇచ్చి, ముందున్న వ్యక్తికి ఆఖరి నంబర్ స్లిప్ ఇవ్వాలి. స్లిప్పులు ఉన్నవారిని మాత్రమే ఓటు వేయించాలి.",
          "<strong>పెట్టె స్లిట్ సీలింగ్:</strong> ఆఖరి ఓటు పడిన వెంటనే ఏజెంట్ల సమక్షంలో బ్యాలెట్ పెట్టె రంధ్రాన్ని (Slit) మూసివేసి అడ్రస్ ట్యాగ్ మరియు ఇత్తడి సీలుతో సీల్ చేయాలి.",
          "<strong>చట్టబద్ధ లెక్కలు:</strong> ప్రిసైడింగ్ అధికారి డైరీ మరియు ఫారం-X-C (బ్యాలెట్ పేపర్ ఖాతా పార్ట్-I) పూర్తి చేయాలి. హాజరైన ప్రతి పోలింగ్ ఏజెంట్‌కు ఫారం-X-C ధృవీకరించిన నకలును తప్పనిసరిగా అందజేయాలి!"
        ]
      },
      {
        num: 8,
        title: "రిసెప్షన్ కేంద్రం & స్ట్రాంగ్ రూమ్ డబుల్ లాకింగ్",
        sub: "రిసెప్షన్ = కౌంటింగ్ సెంటర్ | ఫ్లోర్ స్క్వేర్లు | 4 రంగుల కవర్ల తనిఖీ",
        date: "26.11.2026 (రాత్రి)",
        opsTitle: "వార్డుల వారీ రిసెప్షన్ కౌంటర్లు",
        ops: [
          "<strong>ప్రత్యక్ష రిసెప్షన్:</strong> నిర్ణయించిన కౌంటింగ్ కేంద్రం వద్దనే రిసెప్షన్ కేంద్రం పనిచేస్తుంది. ఎక్కడా ట్రాన్సిట్ రిసెప్షన్ కేంద్రాలు ఉండవు.",
          "<strong>పోలింగ్ కేంద్రాల వారీ ఫ్లోర్ స్క్వేర్లు:</strong> 88 పోలింగ్ కేంద్రాలకు నేలపై ముందుగానే గీసిన చతురస్రాకార స్థలాలలో సామగ్రిని స్వీకరిస్తారు.",
          "<strong>సామగ్రి అప్పగింత తనిఖీ:</strong> బ్యాలెట్ పెట్టె సీళ్లు (స్లిట్ సీల్, గ్రీన్ పేపర్ సీల్, అడ్రస్ ట్యాగ్‌లు) చెక్కుచెదరకుండా ఉన్నాయో లేదో తనిఖీ చేయాలి. ఫారం-X-C మరియు PO డైరీని విడిగా తీసుకోవాలి. 4 రంగుల కవర్లు (బ్రౌన్, గ్రీన్, ఎల్లో, బ్లూ) సరిచూసుకోవాలి.",
          "<strong>రసీదు జారీ:</strong> సామగ్రి సమర్పించిన ప్రిసైడింగ్ అధికారికి అధికారిక రసీదును అందజేసి విధుల నుండి రిలీవ్ చేయాలి."
        ],
        legalTitle: "స్ట్రాంగ్ రూమ్ భద్రత & డబుల్ లాక్",
        legal: [
          "<strong>స్ట్రాంగ్ రూమ్‌కు తరలింపు:</strong> సీల్ చేసిన బ్యాలెట్ పెట్టెలు మరియు బ్రౌన్/గ్రీన్ కవర్లను స్ట్రాంగ్ రూమ్‌లోని వార్డుల విభాగాలలో భద్రపరచాలి.",
          "<strong>డబుల్ లాక్ విధానం:</strong> స్ట్రాంగ్ రూమ్‌కు రెండు తాళాలు వేస్తారు. ఒక తాళం చెవి జిల్లా ఎన్నికల అధికారి వద్ద, రెండో తాళం చెవి మున్సిపల్ కమిషనర్ / ఎన్నికల అధికారి వద్ద ఉంటుంది.",
          "<strong>నిరంతర భద్రత:</strong> 24 గంటలూ సాయుధ పోలీసు పహారా + నిరంతర CCTV వెబ్‌కాస్టింగ్ నిఘా ఉంటుంది. లోపలికి ఎవరు ప్రవేశించినా లాగ్‌బుక్‌లో సంతకం చేయాలి."
        ]
      },
      {
        num: 9,
        title: "ఓట్ల లెక్కింపు, 15 నిమిషాల రీ-కౌంటింగ్ నిబంధన & ఫలితాల ప్రకటన",
        sub: "ముందుగా పోస్టల్ బ్యాలెట్లు | 25 బ్యాలెట్ల కట్టలు & డ్రమ్ మిక్సింగ్ | ఫారం-XX ఫలితాల పత్రం",
        date: "30.11.2026 (ఉదయం 08:00 నుండి)",
        opsTitle: "లెక్కింపు దశలు & పరిశీలన",
        ops: [
          "<strong>08:00 AM — గోప్యతా ప్రకటన & పోస్టల్ బ్యాలెట్లు:</strong> సెక్షన్ 343-F (ఓటు గోప్యత) చదివి వినిపించాలి. ఎన్నికల అధికారి టేబుల్ వద్ద ముందుగా పోస్టల్ బ్యాలెట్లను లెక్కించాలి. ఫారం-XI లోపం ఉంటే తెరవకుండానే తిరస్కరించాలి.",
          "<strong>దశ I — పెట్టె పరిశీలన & కట్టలు కట్టడం:</strong> బ్యాలెట్ పెట్టెలను తెరిచి, బ్యాలెట్లను నిడివిగా తీసి <strong>25 పత్రాల చొప్పున కట్టలు</strong> కట్టాలి. ఫారం-X-C తో సంఖ్య సరిచూసి, అన్ని కట్టలను పెద్ద డ్రమ్‌లో వేసి బాగా కలపాలి!",
          "<strong>దశ II — ట్రేలలోకి వర్గీకరణ:</strong> ప్రతి రౌండ్‌కు డ్రమ్ నుండి 40 కట్టలు (1,000 బ్యాలెట్లు) తీసి, అభ్యర్థుల వారీ ట్రేలు + NOTA + 1 సందేహాస్పద ట్రేలలో వేయాలి. చెల్లుబాటైన ఓట్లను <strong>100 చొప్పున కట్టలు</strong> కట్టాలి.",
          "<strong>సందేహాస్పద ఓట్ల నిర్ణయం:</strong> సందేహాస్పద ఓట్లను ఎన్నికల అధికారి స్వయంగా పరిశీలించి నిర్ణయం తీసుకోవాలి. గుర్తింపు చిహ్నం ఉన్నవి, గుర్తులేనివి, ఒకరి కంటే ఎక్కువ మందికి వేసినవి, నకిలీవి, డిస్టింగ్విషింగ్ స్టాంప్/సంతకం లేనివి చెల్లవు."
        ],
        legalTitle: "రీ-కౌంటింగ్ గడువు & ఫలితం",
        legal: [
          "<strong>తప్పనిసరి 15 నిమిషాల వ్యవధి:</strong> ఫారం-XX పార్ట్-I లో మొత్తం ఓట్లను నమోదు చేసిన తరువాత, అభ్యర్థుల ఓట్లను మైక్‌లో ప్రకటించి <strong>ఖచ్చితంగా 15 నిమిషాల పాటు వేచి ఉండాలి</strong>. ఈ సమయంలో రీ-కౌంటింగ్ దరఖాస్తులను స్వీకరించాలి.",
          "<strong>రీ-కౌంటింగ్ నిర్ణయం:</strong> కారణాలను పరిశీలించి లిఖితపూర్వక ఉత్తర్వు ఇవ్వాలి. <em>ఫారం-XX పార్ట్-I పై అధికారి సంతకం చేసిన తరువాత రీ-కౌంటింగ్ దరఖాస్తులను అనుమతించరాదు!</em>",
          "<strong>సమ ఉజ్జీగా ఓట్లు వస్తే:</strong> ఇద్దరికీ సమాన ఓట్లు వస్తే, ఒక్కొక్కరికి 5 స్లిప్పులు రాసి బాక్స్‌లో వేసి లాటరీ తీయాలి; మొదట వచ్చిన అభ్యర్థి విజేతగా ప్రకటింపబడతారు.",
          "<strong>ఫలితాల ప్రకటన:</strong> ఫారం-XX పార్ట్-II పై సంతకం చేసి విజేతను అధికారికంగా ప్రకటించి సర్టిఫికెట్ ఇవ్వాలి. కాపీలను SEC, C&DMA, కలెక్టర్ మరియు కమిషనర్‌లకు పంపాలి.",
          "<strong>ట్రెజరీ భద్రత:</strong> బ్యాలెట్లను స్టీల్ ట్రంకు పెట్టెలలో సీల్ చేసి సబ్-ట్రెజరీ డబుల్ లాక్‌లో భద్రపరచాలి."
        ]
      }
    ],
    chkTitle: "✅ ఎన్నికల అధికారుల సమగ్ర చెక్‌లిస్టులు",
    chkSub: "ప్రతి దశలో పూర్తిచేసిన విధులను టిక్ చేయండి. పురోగతి మీ పరికరంలో భద్రపరచబడుతుంది.",
    chkProgressLabel: "మొత్తం ఎన్నికల సంసిద్ధత పురోగతి",
    chkResetBtn: "అన్నీ క్లియర్ చేయండి",
    chkPrintBtn: "చెక్‌లిస్ట్ ప్రింట్",
    guideTitle: "📌 ఎన్నికల అధికారులకు ముఖ్యమైన మార్గదర్శకాలు",
    guideSub: "చట్టబద్ధ నిబంధనలు, నామినేషన్లు, పరిశీలన, పోలింగ్ రోజు నిర్వహణ, ఓట్ల లెక్కింపుపై సరళమైన మార్గదర్శక సూత్రాలు.",
    dodontTitle: "⚖️ చేయవలసినవి మరియు చేయకూడనివి (Do's & Don'ts)",
    dodontSub: "ఎన్నికల అధికారులు, ప్రిసైడింగ్ అధికారులు, ఏజెంట్లు మరియు నిఘా బృందాలు పాటించవలసిన స్పష్టమైన ఆదేశాలు.",
    formsTitle: "📂 చట్టబద్ధ మరియు చట్టబద్ధేతర ఫారాల నిధి",
    formsSub: "AP మున్సిపాలిటీల ఎన్నికల నియమావళి, 2026 ప్రకారం నిర్దేశిత ఫారాల నమూనాలు. ప్రివ్యూ చూడటానికి లేదా కాపీ చేసుకోవడానికి క్లిక్ చేయండి.",
    dirTitle: "🏛️ శ్రీకాళహస్తి పురపాలక క్షేత్రస్థాయి డైరెక్టరీ",
    dirSub: "44 వార్డుల రిజర్వేషన్లు, 88 పోలింగ్ కేంద్రాలు (ఓటర్లు & లొకేషన్లు), 12 క్లస్టర్ కార్యాలయాలు, జోనల్, రూట్ మరియు నిఘా బృందాల వివరాలు.",
    toolsTitle: "🛠️ క్షేత్రస్థాయి సాధనాలు, కాలిక్యులేటర్లు & ప్యాకింగ్ గైడ్",
    toolsSub: "బ్యాలెట్ పేపర్ల లెక్కింపు, 5 గంటల క్యూ స్లిప్పుల క్రమం, 4 రంగుల కవర్ల ప్యాకింగ్ మరియు సందేహాస్పద ఓట్ల నిర్ణయ సూత్రాలు."
  }
};
"""

with open('portal_translations.js', 'w', encoding='utf-8') as f:
    f.write(script_builder)

print("Generated portal_translations.js successfully.")
