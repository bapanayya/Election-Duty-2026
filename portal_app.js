// ============================================================================
// PORTAL APPLICATION CONTROLLER (BILINGUAL ENGINE)
// Srikalahasti Municipality Phase 2 Ordinary Elections 2026
// ============================================================================

let currentLang = localStorage.getItem('SKHT_ELECTION_LANG') || 'en';
const STORAGE_KEY = 'SKHT_ELECTION_2026_CHECKLIST';

// Checklists Definition (Dual Language with common IDs)
const CHECKLIST_DATA = {
  en: [
    {
      title: "📋 Checklist 1: Pre-Notification & Office Infrastructure Readiness",
      badge: "Pre-Poll",
      items: [
        { id: "c1", title: "Ward Electoral Roll Verified & Displayed", sub: "Updated ward-wise voter rolls displayed on Municipal Notice Board and conspicuous places in each ward under Rule 5." },
        { id: "c2", title: "Election Notice (Form-1) Published", sub: "Notice in English & Telugu published before nominations open, specifying offices, reservations, dates, and cluster rooms under Rule 6." },
        { id: "c3", title: "12 Cluster Election Offices Established & Staffed", sub: "Chairperson Office + 11 Ward-Cluster Offices furnished with tables, barriers, clocks, running serial registers, and designated supporting staff." },
        { id: "c4", title: "Blank Nomination Papers & Form-IA Stock Ready", sub: "Sufficient printed sets of nomination forms, Form-IA (symbols), Form-II (caste), and Antecedents declaration formats available free of cost." },
        { id: "c5", title: "100m Security Perimeter & CCTV Activated", sub: "Barricades erected at 100 meters from election offices; 1 vehicle rule enforced; video recording arranged for receipt counters." }
      ]
    },
    {
      title: "📋 Checklist 2: Receipt & Verification of Nominations (14–16 Nov, 11 AM–3 PM)",
      badge: "Nominations",
      items: [
        { id: "c6", title: "Strict 11:00 AM to 3:00 PM Timing Enforced", sub: "Nominations accepted only within official hours. At 3:00 PM on 16.11.2026, doors closed; slips given to persons present inside." },
        { id: "c7", title: "Personal Delivery by Candidate or Proposer", sub: "Nomination presented in person by candidate or proposer only (max 3 persons inside). Not by post or unauthorized messenger." },
        { id: "c8", title: "Proposer & Elector Roll Entry Verification", sub: "Ward Member proposer verified as registered elector in that specific ward; Chairperson proposer verified as elector in municipality." },
        { id: "c9", title: "Statutory Security Deposit Collected", sub: "Rs. 3,000/- for General; Rs. 1,500/- for SC/ST/BC with community certificate. Official receipt issued; cash/challan accounted." },
        { id: "c10", title: "Mandatory Declaration on Antecedents & Assets Filed", sub: "Declaration attested by two witnesses; checked that no column is left blank (must write 'Nil' or 'Not applicable')." },
        { id: "c11", title: "Running Serial Number, Date & Minute Initialed", sub: "Officer initials each page, notes exact time, issues Form-I receipt and notice of scrutiny, endorses checklist duplicate." },
        { id: "c12", title: "Daily Notice & Consolidated Form-III Affixed", sub: "Daily list posted after 3 PM; final consolidated Form-III published immediately after 3:00 PM on 16.11.2026." }
      ]
    },
    {
      title: "📋 Checklist 3: Scrutiny Day Quasi-Judicial Proceedings (17 Nov, 11 AM)",
      badge: "Scrutiny",
      items: [
        { id: "c13", title: "Conducted Personally by Election Officer", sub: "Election Officer presides personally at the notified place. AEO acts only if EO is unavoidably prevented." },
        { id: "c14", title: "Regulated Admission into Scrutiny Room", sub: "Only Candidate, Election Agent, Proposer, and ONE authorised representative allowed. General public excluded." },
        { id: "c15", title: "Verification of Crucial Age (21+ Years) & Qualifications", sub: "Candidate has completed 21 years on date of scrutiny; enrolled in municipality roll; no statutory disqualification under Sec 13–15." },
        { id: "c16", title: "Substantial Character Rule Applied", sub: "No rejection on grounds of clerical or technical defect. Full opportunity (up to next day) given to rebut objections." },
        { id: "c17", title: "Reasoned Orders Recorded & Form-IV Published", sub: "Reasons recorded on nomination; copy of rejection order given to candidate; Form-IV list of valid candidates published." }
      ]
    },
    {
      title: "📋 Checklist 4: Withdrawals, Form-B & Contesting List Form-VII (18–19 Nov)",
      badge: "Withdrawal & Symbols",
      items: [
        { id: "c18", title: "Withdrawal Notice (Form-V) Delivered before 3:00 PM", sub: "Delivered in person by candidate/proposer/auth agent. Form-V receipt issued; Form-VI notice affixed. Irrevocable once given." },
        { id: "c19", title: "Political Party Form-B Verified before 3:00 PM", sub: "Form-B delivered by party to EO before 3 PM on 19.11.2026; Form-A confirmed from Collector & DEA." },
        { id: "c20", title: "Allotment of Symbols (3 Categories)", sub: "Category 1 (Recognised), Category 2 (Registered), Category 3 (Independents). Clashes resolved by lot / sitting holder." },
        { id: "c21", title: "Form-VII Prepared in Telugu Alphabetical Order", sub: "Telugu alphabetical order of surnames. Copies supplied to candidates, posted on notice board, and sent to press." },
        { id: "c22", title: "Uncontested Candidate Declaration (If Applicable)", sub: "If single candidate remains, declare elected unopposed forthwith and inform SEC, C&DMA, Collector & DEA, and Municipal Commissioner." }
      ]
    },
    {
      title: "📋 Checklist 5: P-1 Dispatch Operations & Polling Kits Verification (25 Nov)",
      badge: "P-1 Day",
      items: [
        { id: "c23", title: "Ballot Boxes Inspected & Verified", sub: "Locking mechanism, hinges, cleanliness, and outer seals checked for all boxes allotted to 88 polling stations." },
        { id: "c24", title: "Ballot Papers Handover (White & Pink)", sub: "Consecutive serial numbers checked: White (Chairperson) & Pink (Ward Member). Quantities match PS voter roll + reserve." },
        { id: "c25", title: "Statutory Stationery & Indelible Ink Check", sub: "4 copies of rolls (1 marked), Distinguishing Stamp, Arrow stamps, Purple pads, Indelible ink phials, Green paper seals, Brass seal." },
        { id: "c26", title: "4 Colour-Coded Covers Received", sub: "BROWN (Box/Statutory accounts), GREEN (Statutory), YELLOW (Non-statutory), BLUE (Plain stationery/ink/metal seal)." },
        { id: "c27", title: "Movement along 9 Routes & PS Setup Confirmed", sub: "Party accompanied by Route Officer to station; voting compartment setup for secrecy; arrival reported to Control Room." }
      ]
    },
    {
      title: "📋 Checklist 6: Polling Day (P-0) Voting & Sealing (26 Nov, 7 AM–5 PM)",
      badge: "Poll Day",
      items: [
        { id: "c28", title: "06:00 AM — Polling Agents Verified & Seated", sub: "Form-IX verified; duplicate signed and returned to agent; max 1 agent + 2 relief per candidate allowed." },
        { id: "c29", title: "06:30 AM — Empty Box Demonstrated & Sealed", sub: "Empty box shown; green paper seal inserted; serial number noted by agents; box locked, address tag tied, brass seal affixed." },
        { id: "c30", title: "Distinguishing Mark & PO Signature on Reverse", sub: "Every ballot paper stamped with distinguishing mark and signed in full by PO on the back before issue to elector." },
        { id: "c31", title: "07:00 AM — Prompt Poll Commencement & Turnout Reports", sub: "Poll started at 7:00 AM; ink applied on left forefinger; periodic 2-hourly turnout reported to Sector/Control Room." },
        { id: "c32", title: "05:00 PM — Queue Slips Distribution & Slit Sealing", sub: "Numbered slips issued from back of queue at 5:00 PM; poll closed; box slit sealed in presence of agents; Form-X-C completed." }
      ]
    },
    {
      title: "📋 Checklist 7: Reception Center & Strong Room Handover (26 Nov Night)",
      badge: "Reception",
      items: [
        { id: "c33", title: "Ballot Box Seals Verified at PS Floor Square", sub: "Intact slit seal, green paper seal, and address tags checked by Receiving Officer at the designated PS floor square." },
        { id: "c34", title: "Form-X-C & PO Diary Separately Received", sub: "Ballot Paper Account (Form-X-C Part-I) and Presiding Officer's Diary verified against polled totals." },
        { id: "c35", title: "4 Colour-Coded Covers Verified", sub: "Brown cover (accounts/marked roll), Green (statutory), Yellow (non-statutory), Blue (stationery/metal seals)." },
        { id: "c36", title: "Strong Room Deposited & Double-Locked", sub: "Boxes and covers deposited ward-wise; double lock locked in presence of candidates/agents; CCTV recording continuous." }
      ]
    },
    {
      title: "📋 Checklist 8: Counting Day Table Management & Adjudication (30 Nov)",
      badge: "Counting Day",
      items: [
        { id: "c37", title: "Sec. 343-F Read Out & Postal Ballots Counted First", sub: "Secrecy provision announced; postal ballot box opened first at EO table; Form-XI checked; invalid declarations rejected." },
        { id: "c38", title: "25-Ballot Bundling & Mixing in Drum (Stage I)", sub: "Ballot boxes opened PS-wise; tally with Form-X-C; bundled into 25s; mixed thoroughly in large drum." },
        { id: "c39", title: "1,000-Ballot Rounds & 100-Bundle Trays (Stage II)", sub: "40 bundles (1,000 ballots) drawn per round; sorted into candidate trays + NOTA; bundled into 100s; doubtful to EO." },
        { id: "c40", title: "Mandatory 15-Minute Recount Window & Form-XX Declaration", sub: "Announce totals; wait 15 minutes for recount petitions; decide before signing; sign Form-XX Part-I & II; seal steel trunks into Treasury." }
      ]
    }
  ],

  te: [
    {
      title: "📋 చెక్‌లిస్ట్ 1: ఎన్నికల నోటీసు పూర్వ సన్నాహాలు & కార్యాలయాల సంసిద్ధత",
      badge: "పూర్వ సన్నాహాలు",
      items: [
        { id: "c1", title: "వార్డుల వారీ ఓటర్ల జాబితా ప్రదర్శన", sub: "రూల్ 5 ప్రకారం మున్సిపల్ నోటీసు బోర్డు మరియు వార్డులలోని ముఖ్య ప్రదేశాలలో ఓటర్ల జాబితా ప్రదర్శించబడింది." },
        { id: "c2", title: "ఎన్నికల నోటీసు (ఫారం-1) ప్రచురణ", sub: "రూల్ 6 ప్రకారం తెలుగు మరియు ఆంగ్లంలో స్థానాలు, రిజర్వేషన్లు, తేదీలు, వేళలతో నోటీసు ప్రచురించబడింది." },
        { id: "c3", title: "12 క్లస్టర్ ఎన్నికల కార్యాలయాల ఏర్పాటు & సిబ్బంది నియామకం", sub: "ఛైర్‌పర్సన్ ఆఫీస్ + 11 వార్డు క్లస్టర్ ఆఫీసులలో బల్లలు, గడియారాలు, రిజిస్టర్లు మరియు కేటాయించిన సిబ్బంది సిద్ధంగా ఉన్నారు." },
        { id: "c4", title: "ఖాళీ నామినేషన్ పత్రాలు & ఫారం-IA నిల్వలు సిద్ధం", sub: "నామినేషన్ ఫారాలు, ఫారం-IA (గుర్తులు), ఫారం-II (కుల ధృవీకరణ), నేర చరిత్ర అఫిడవిట్ నమూనాలు ఉచితంగా అందుబాటులో ఉంచబడ్డాయి." },
        { id: "c5", title: "100 మీటర్ల భద్రతా పరిధి & సీసీటీవీల ఏర్పాటు", sub: "100 మీటర్ల బారికేడ్లు, 1 వాహనం నిబంధన అమలు, నామినేషన్ కౌంటర్ల వద్ద వీడియో రికార్డింగ్ ప్రారంభించబడింది." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 2: నామినేషన్ల స్వీకరణ & తనిఖీ (14–16 నవంబర్, ఉదయం 11 నుండి మధ్యాహ్నం 3 వరకు)",
      badge: "నామినేషన్లు",
      items: [
        { id: "c6", title: "ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు ఖచ్చితమైన వేళల అమలు", sub: "అధికారిక వేళల్లోనే స్వీకరణ. 16.11.2026 మధ్యాహ్నం 3:00 గంటలకు తలుపులు మూసివేసి లోపల ఉన్నవారికి స్లిప్పులు ఇవ్వబడ్డాయి." },
        { id: "c7", title: "అభ్యర్థి లేదా ప్రతిపాదకుడు స్వయంగా అందజేయడం", sub: "గరిష్టంగా 3 గురు మాత్రమే లోపలికి అనుమతి. పోస్టు లేదా ఇతరుల ద్వారా వచ్చినవి స్వీకరించబడవు." },
        { id: "c8", title: "ప్రతిపాదకుడి ఓటరు నమోదు సరిచూడడం", sub: "వార్డు సభ్యుల స్థానానికి ప్రతిపాదకుడు ఆ వార్డు ఓటర్ అయి ఉండాలి; ఛైర్‌పర్సన్ స్థానానికి మున్సిపాలిటీలోని ఓటర్ అయి ఉండాలి." },
        { id: "c9", title: "చట్టబద్ధ భద్రతా డిపాజిట్ స్వీకరణ", sub: "జనరల్ కు రూ. 3,000/-; ఎస్సీ/ఎస్టీ/బీసీ లకు రూ. 1,500/-. అధికారిక రసీదు జారీ చేయబడింది." },
        { id: "c10", title: "నేర చరిత్ర, ఆస్తుల డిక్లరేషన్ దాఖలు", sub: "ఇద్దరు సాక్షుల సంతకాలతో కూడిన డిక్లరేషన్ పరిశీలించబడింది (ఏ కాలమ్ ఖాళీగా ఉంచలేదు, 'ఏమీలేవు' అని రాయబడింది)." },
        { id: "c11", title: "రన్నింగ్ సీరియల్ నంబర్, తేదీ, సమయం నమోదు & సంతకం", sub: "ప్రతి పేజీపై అధికారి సంతకం, సమయం నమోదు, ఫారం-I రసీదు మరియు పరిశీలన నోటీసు అందజేయబడింది." },
        { id: "c12", title: "రోజువారీ నోటీసు & ఏకీకృత ఫారం-III ప్రచురణ", sub: "రోజూ మధ్యాహ్నం 3 గంటల తరువాత జాబితా ప్రదర్శన; 16.11.2026 న మధ్యాహ్నం 3 గం తరువాత తుది ఫారం-III ప్రచురించబడింది." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 3: నామినేషన్ల పరిశీలన రోజు (17 నవంబర్, ఉదయం 11:00 నుండి)",
      badge: "పరిశీలన",
      items: [
        { id: "c13", title: "ఎన్నికల అధికారి స్వయంగా విచారణ నిర్వహించడం", sub: "ఎన్నికల అధికారి స్వయంగా పరిశీలన జరిపారు. సహాయక అధికారికి అప్పగించలేదు." },
        { id: "c14", title: "పరిశీలన గదిలోకి నియంత్రిత ప్రవేశం", sub: "అభ్యర్థి, ఎన్నికల ఏజెంట్, ప్రతిపాదకుడు మరియు ఒక అధీకృత ప్రతినిధి మాత్రమే హాజరయ్యారు." },
        { id: "c15", title: "వయోపరిమితి (21+ ఏళ్లు) & చట్టబద్ధ అర్హతల నిర్ధారణ", sub: "పరిశీలన తేది నాటికి 21 ఏళ్లు నిండి ఉండడం, మున్సిపల్ ఓటరు అయి ఉండడం, సెక్షన్ 13–15 అనర్హతలు లేకపోవడం ధృవీకరించబడింది." },
        { id: "c16", title: "సాంకేతిక లోపాలకు తిరస్కరించకపోవడం", sub: "చిన్న చిన్న స్పెల్లింగ్, ప్రింటింగ్ తప్పులకు తిరస్కరించలేదు. అభ్యంతరాలకు మరుసటి రోజు వరకు అవకాశం ఇవ్వబడింది." },
        { id: "c17", title: "కారణాలతో కూడిన ఉత్తర్వులు & ఫారం-IV ప్రచురణ", sub: "నామినేషన్ పత్రంపై కారణాలు నమోదు, తిరస్కరణ కాపీ అభ్యర్థికి అందజేత, చెల్లుబాటైన జాబితా (ఫారం-IV) ప్రచురణ." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 4: అభ్యర్థిత్వాల ఉపసంహరణ, ఫారం-B & ఫారం-VII ప్రచురణ (18–19 నవంబర్)",
      badge: "ఉపసంహరణ & గుర్తులు",
      items: [
        { id: "c18", title: "మధ్యాహ్నం 3:00 లోపు ఉపసంహరణ నోటీసు (ఫారం-V) స్వీకరణ", sub: "అభ్యర్థి స్వయంగా అందజేశారు. ఫారం-V రసీదు జారీ చేయబడింది; ఫారం-VI నోటీసు బోర్డుపై ప్రదర్శించబడింది." },
        { id: "c19", title: "రాజకీయ పార్టీల ఫారం-B ధృవీకరణ", sub: "19.11.2026 మధ్యాహ్నం 3 గంటల లోపు పార్టీ అధీకృత ప్రతినిధి నుండి ఫారం-B స్వీకరించబడింది; ఫారం-A సరిచూడబడింది." },
        { id: "c20", title: "గుర్తుల కేటాయింపు (3 విభాగాలు)", sub: "గుర్తింపు పొందిన పార్టీలు, రిజిస్టర్డ్ పార్టీలు, స్వతంత్రులకు గుర్తులు కేటాయించబడ్డాయి. వివాదాలు లాటరీ ద్వారా పరిష్కరించబడ్డాయి." },
        { id: "c21", title: "ఫారం-VII తెలుగు అక్షర క్రమంలో తయారీ", sub: "ఇంటిపేర్ల ఆధారంగా తెలుగు అక్షర క్రమంలో పోటీచేయు అభ్యర్థుల జాబితా (ఫారం-VII) ప్రచురించబడింది." },
        { id: "c22", title: "ఏకగ్రీవ ఎన్నికల ప్రకటన (అవసరమైతే)", sub: "ఒకే అభ్యర్థి మిగిలితే తక్షణమే ఏకగ్రీవంగా ఎన్నికైనట్లు ప్రకటించి SEC, కలెక్టర్, కమిషనర్‌లకు నివేదించబడింది." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 5: P-1 రోజు డిస్పాచ్ కార్యకలాపాలు & సామగ్రి తనిఖీ (25 నవంబర్)",
      badge: "P-1 రోజు",
      items: [
        { id: "c23", title: "బ్యాలెట్ పెట్టెల క్షుణ్ణ తనిఖీ", sub: "88 పోలింగ్ కేంద్రాలకు కేటాయించిన పెట్టెల లాకింగ్ పనితీరు, కీలు మరియు శుభ్రత సరిచూడబడింది." },
        { id: "c24", title: "బ్యాలెట్ పత్రాల అప్పగింత (తెలుపు & గులాబీ)", sub: "ఛైర్‌పర్సన్ (తెలుపు) మరియు వార్డు సభ్యుల (గులాబీ) బ్యాలెట్ పత్రాల వరుస సంఖ్యలు క్షుణ్ణంగా సరిచూడబడ్డాయి." },
        { id: "c25", title: "చట్టబద్ధ స్టేషనరీ & చెరగని సిరా తనిఖీ", sub: "4 కాపీల ఓటర్ల జాబితాలు, డిస్టింగ్విషింగ్ స్టాంప్, ఆరో మార్క్ స్టాంపులు, చెరగని సిరా సీసాలు, గ్రీన్ పేపర్ సీల్స్, ఇత్తడి సీలు అందాయి." },
        { id: "c26", title: "4 రంగుల కవర్లు స్వీకరించడం", sub: "బ్రౌన్ (పెట్టె/లెక్కల కవర్), గ్రీన్ (చట్టబద్ధ), ఎల్లో (చట్టబద్ధేతర), బ్లూ (స్టేషనరీ కిట్) కవర్లు సరిచూడబడ్డాయి." },
        { id: "c27", title: "9 రూట్లలో ప్రయాణం & పోలింగ్ కేంద్రం ఏర్పాటు", sub: "రూట్ అధికారితో కలిసి కేంద్రానికి చేరడం, ఓటింగ్ కంపార్ట్‌మెంట్ గోప్యత, కంట్రోల్ రూమ్‌కు రిపోర్టింగ్ పూర్తిచేయబడింది." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 6: పోలింగ్ రోజు (P-0) ఓటింగ్ & సీలింగ్ (26 నవంబర్, ఉదయం 7 నుండి సాయంత్రం 5)",
      badge: "పోలింగ్ రోజు",
      items: [
        { id: "c28", title: "06:00 AM — పోలింగ్ ఏజెంట్ల ప్రవేశం & ధృవీకరణ", sub: "ఫారం-IX సరిచూసి ఏజెంట్లకు సంతకం చేసి ఇవ్వబడింది; అభ్యర్థికి 1 ఏజెంట్ + 2 రిలీవర్ల మాత్రమే అనుమతి." },
        { id: "c29", title: "06:30 AM — ఖాళీ పెట్టె ప్రదర్శన & సీలింగ్", sub: "ఖాళీ పెట్టె చూపించి, గ్రీన్ పేపర్ సీల్ వేసి, నంబర్ నమోదు చేసి, అడ్రస్ ట్యాగ్ వేసి లాక్ చేసి సీల్ చేయబడింది." },
        { id: "c30", title: "బ్యాలెట్ పత్రం వెనుక డిస్టింగ్విషింగ్ స్టాంప్ & PO సంతకం", sub: "ఓటరుకు ఇచ్చే ముందు ప్రిసైడింగ్ అధికారి ప్రతి బ్యాలెట్ వెనుక స్టాంప్ వేసి పూర్తి సంతకం చేశారు." },
        { id: "c31", title: "07:00 AM — సమయానికి పోలింగ్ ప్రారంభం & నివేదికలు", sub: "ఖచ్చితంగా ఉదయం 7 గంటలకు పోలింగ్ ప్రారంభమైంది; ప్రతి 2 గంటలకు ఒకసారి పోలింగ్ శాతం నివేదించబడింది." },
        { id: "c32", title: "05:00 PM — క్యూ స్లిప్పుల పంపిణీ & స్లిట్ సీలింగ్", sub: "సాయంత్రం 5 గంటలకు క్యూ చివర నుండి స్లిప్పులు ఇచ్చి, పోలింగ్ ముగిసిన వెంటనే స్లిట్ సీల్ చేసి, ఫారం-X-C కాపీలు ఏజెంట్లకు ఇవ్వబడ్డాయి." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 7: రిసెప్షన్ కేంద్రం & స్ట్రాంగ్ రూమ్ అప్పగింత (26 నవంబర్ రాత్రి)",
      badge: "రిసెప్షన్",
      items: [
        { id: "c33", title: "ఫ్లోర్ స్క్వేర్ వద్ద బ్యాలెట్ పెట్టె సీళ్ల తనిఖీ", sub: "రిసెప్షన్ టేబుల్ వద్ద స్లిట్ సీల్, గ్రీన్ పేపర్ సీల్ మరియు అడ్రస్ ట్యాగ్‌లు చెక్కుచెదరకుండా ఉన్నట్లు సరిచూడబడింది." },
        { id: "c34", title: "ఫారం-X-C & ప్రిసైడింగ్ అధికారి డైరీ విడిగా స్వీకరణ", sub: "బ్యాలెట్ పేపర్ ఖాతా (ఫారం-X-C పార్ట్-I) మరియు PO డైరీ పరిశీలించి రికార్డు చేయబడింది." },
        { id: "c35", title: "4 రంగుల కవర్ల సరిచూడడం", sub: "బ్రౌన్ కవర్, గ్రీన్ కవర్, ఎల్లో కవర్ మరియు బ్లూ కవర్లలోని పత్రాలు సరిచూడబడ్డాయి." },
        { id: "c36", title: "స్ట్రాంగ్ రూమ్ డిపాజిట్ & డబుల్ లాక్ సీలింగ్", sub: "వార్డుల వారీగా పెట్టెలను భద్రపరచి, ఏజెంట్ల సమక్షంలో డబుల్ లాక్ వేసి సీల్ చేయబడింది; సీసీటీవీ రికార్డింగ్ కొనసాగుతోంది." }
      ]
    },
    {
      title: "📋 చెక్‌లిస్ట్ 8: ఓట్ల లెక్కింపు రోజు నిర్వహణ & ప్రకటన (30 నవంబర్)",
      badge: "లెక్కింపు రోజు",
      items: [
        { id: "c37", title: "సెక్షన్ 343-F చదవడం & పోస్టల్ బ్యాలెట్ల లెక్కింపు", sub: "గోప్యతా నిబంధన వినిపించబడింది; ముందుగా పోస్టల్ బ్యాలెట్లు లెక్కించబడ్డాయి; ఫారం-XI లోపాలున్నవి తిరస్కరించబడ్డాయి." },
        { id: "c38", title: "25 బ్యాలెట్ల కట్టలు & డ్రమ్ మిక్సింగ్ (దశ I)", sub: "పెట్టెలు తెరిచి, ఫారం-X-C తో సరిచూసి, 25 చొప్పున కట్టలు కట్టి పెద్ద డ్రమ్‌లో బాగా కలిపారు." },
        { id: "c39", title: "1,000 బ్యాలెట్ల రౌండ్లు & 100 కట్టల ట్రేలు (దశ II)", sub: "రౌండ్‌కు 1,000 బ్యాలెట్లు తీసి, అభ్యర్థుల ట్రేలలో వేసి, 100 చొప్పున కట్టలు కట్టారు; సందేహాస్పద ఓట్లు అధికారి వద్దకు పంపారు." },
        { id: "c40", title: "తప్పనిసరి 15 నిమిషాల రీ-కౌంటింగ్ విరామం & ఫారం-XX ప్రకటన", sub: "మొత్తం ఓట్లు ప్రకటించి 15 నిమిషాలు వేచి చూశారు; దరఖాస్తులను పరిష్కరించి ఫారం-XX పార్ట్-I & II పై సంతకం చేసి విజేతను ప్రకటించారు." }
      ]
    }
  ]
};

// Guidelines Data (Dual Language)
const GUIDELINES_DATA = {
  en: [
    {
      title: "⚖️ 1. Legal Authority & Appointment",
      points: [
        "<strong>Superintendence:</strong> Under Article 243-ZA and Sec. 10-A of the AP Municipalities Act, 1965, full superintendence, direction, and control vests in the State Election Commission.",
        "<strong>Election Officer (EO):</strong> Appointed under Rule 3 of the Conduct of Election Rules, 2026 (G.O.Ms.No.213). EO must be a Gazetted Officer of the Government or local authority.",
        "<strong>Ward Cluster:</strong> In Srikalahasti, 1 EO covers a cluster of 4 wards (Wards 1-4, 5-8, 9-12, etc.), plus 1 dedicated office for Chairperson.",
        "<strong>Subordination & Control:</strong> Supporting staff (Ward Secretaries) are under the direct administrative control and disciplinary power of the EO till election completion."
      ]
    },
    {
      title: "📝 2. Nominations & Proposers",
      points: [
        "<strong>Proposer Rule is Strict:</strong> For a Ward Member candidate, the proposer MUST be an elector in that exact ward. For Chairperson, the proposer can be an elector anywhere in the municipality.",
        "<strong>One Proposer, One Nomination:</strong> If an elector proposes multiple candidates in the same ward, only the first nomination delivered is valid; subsequent ones are invalid.",
        "<strong>Deposit Protection:</strong> SC, ST, and BC candidates pay only Rs. 1,500/- even when contesting an unreserved (general) seat!",
        "<strong>Affidavit / Declaration:</strong> Must be signed by candidate, attested by 2 witnesses. No field left blank — write 'Nil' or 'Not Applicable'."
      ]
    },
    {
      title: "🔍 3. Scrutiny Quasi-Judicial Principles",
      points: [
        "<strong>Summary Enquiry:</strong> Scrutiny is a summary enquiry. The EO does not sit as a regular civil court.",
        "<strong>Presumption in Favour of Candidature:</strong> A nomination paper should be accepted unless there is clear, substantial statutory disqualification.",
        "<strong>Technical Defects Ignored:</strong> Minor spelling errors in names, discrepancy in father's name, or serial number mismatch where identity is clear must NOT be grounds for rejection.",
        "<strong>Right to Rebut:</strong> If an objection is raised against a candidate, the EO must allow the candidate time up to 11:00 AM the next day to rebut."
      ]
    },
    {
      title: "🗳️ 4. Ballot Paper & Boxes Protocol",
      points: [
        "<strong>Color Differentiation:</strong> White Wove paper for Chairperson; Pink Wove paper for Ward Members.",
        "<strong>Distinguishing Mark:</strong> Presiding Officer must stamp the distinguishing mark (e.g., SKHT-W5/PS1) and sign the back of every ballot paper before issuing.",
        "<strong>Box Slit Sealing:</strong> Close and seal the ballot box slit at 5:00 PM (or when last slip holder votes) in full view of polling agents.",
        "<strong>Paper Seal Account:</strong> Complete Part-I of Form-X-C accounting for all green paper seals used, damaged, and unused."
      ]
    },
    {
      title: "👥 5. Polling Day Special Cases",
      points: [
        "<strong>Challenged Votes (Rule 36):</strong> Agent deposits Rs. 5/- fee. PO conducts summary enquiry. If challenge established, debar voter and report to police. If refuted, allow vote and forfeit deposit. Maintain Form-XIV & XV.",
        "<strong>Blind / Infirm Voters:</strong> Companion allowed (must be 18+ years, cannot accompany more than one voter). Record declaration in Form-XVII.",
        "<strong>Tendered Votes (Rule 42):</strong> If a person presents himself and finds his vote already cast, verify identity. Issue a Tendered Ballot Paper (do NOT put into box). Voter marks ballot, hands to PO, kept in Tendered Votes cover (Form-XVI).",
        "<strong>ASD List Check:</strong> Check Absent, Shifted, and Dead (ASD) list thoroughly. If elector appears, verify EPIC, take signature & thumbprint, and record in PO Diary."
      ]
    },
    {
      title: "📊 6. Counting & Recount Rules",
      points: [
        "<strong>Drum Mixing:</strong> Unfolded ballots bundled in 25s must be mixed in the drum. This prevents polling station-wise voter trend leakage and protects secrecy.",
        "<strong>Doubtful Ballot Personal Decision:</strong> Only the Election Officer has the legal authority to accept or reject doubtful votes. Counting supervisors cannot reject!",
        "<strong>15-Minute Pause is Mandatory:</strong> After recording totals on Form-XX Part-I, the EO MUST announce results and pause for 15 minutes. Deciding recount petitions is mandatory before signing.",
        "<strong>Secrecy Breach:</strong> Violation of secrecy by any officer, agent, or clerk is punishable with imprisonment up to 3 months or fine under Sec. 343-F."
      ]
    }
  ],

  te: [
    {
      title: "⚖️ 1. చట్టబద్ధ అధికారాలు & నియామకాలు",
      points: [
        "<strong>సంపూర్ణ పర్యవేక్షణ:</strong> రాజ్యాంగంలోని ఆర్టికల్ 243-ZA మరియు AP మున్సిపాలిటీల చట్టం, 1965 లోని సెక్షన్ 10-A ప్రకారం ఎన్నికల పర్యవేక్షణ, ఆదేశాలు మరియు నియంత్రణ రాష్ట్ర ఎన్నికల సంఘం వద్ద ఉంటాయి.",
        "<strong>ఎన్నికల అధికారి (EO):</strong> ఎన్నికల నిర్వహణ నియమావళి, 2026 (G.O.Ms.No.213) లోని రూల్ 3 ప్రకారం నియమించబడతారు. EO తప్పనిసరిగా గెజిటెడ్ అధికారి అయి ఉండాలి.",
        "<strong>వార్డుల క్లస్టర్:</strong> శ్రీకాళహస్తిలో ఒక్కొక్క EO 4 వార్డుల క్లస్టర్‌ను (వార్డులు 1-4, 5-8, 9-12 మొదలైనవి) పర్యవేక్షిస్తారు. ఛైర్‌పర్సన్ స్థానానికి ప్రత్యేక అధికారి ఉంటారు.",
        "<strong>అధికారిక నియంత్రణ:</strong> నియమించబడిన వార్డు కార్యదర్శులు ఎన్నికలు ముగిసే వరకు ఎన్నికల అధికారి ప్రత్యక్ష పరిపాలనా మరియు క్రమశిక్షణా నియంత్రణలో పనిచేస్తారు."
      ]
    },
    {
      title: "📝 2. నామినేషన్లు & ప్రతిపాదకుల నిబంధనలు",
      points: [
        "<strong>ప్రతిపాదకుడి నిబంధన స్పష్టం:</strong> వార్డు సభ్యుల స్థానానికి ప్రతిపాదించే వ్యక్తి ఖచ్చితంగా అదే వార్డు ఓటర్ అయి ఉండాలి. ఛైర్‌పర్సన్ స్థానానికి మున్సిపాలిటీలోని ఏ వార్డు ఓటరైనా ప్రతిపాదించవచ్చు.",
        "<strong>ఒక ప్రతిపాదకుడు, ఒకే నామినేషన్:</strong> ఒకే వార్డులో ఒక ఓటరు ఒకరి కంటే ఎక్కువ మంది అభ్యర్థులకు సంతకం చేస్తే, మొదట అందిన నామినేషన్ మాత్రమే చెల్లుతుంది; మిగతావి రద్దవుతాయి.",
        "<strong>డిపాజిట్ మినహాయింపు రక్షణ:</strong> ఎస్సీ, ఎస్టీ, బీసీ అభ్యర్థులు జనరల్ (అన్‌రిజర్వ్‌డ్) స్థానంలో పోటీ చేసినప్పటికీ రూ. 1,500/- మాత్రమే డిపాజిట్ చెల్లించాలి!",
        "<strong>అఫిడవిట్ / డిక్లరేషన్:</strong> అభ్యర్థి సంతకం చేసి, ఇద్దరు సాక్షులు ధృవీకరించాలి. ఏ కాలమ్‌ను ఖాళీగా వదలరాదు - 'వర్తించదు' లేదా 'ఏమీలేవు' అని స్పష్టంగా రాయాలి."
      ]
    },
    {
      title: "🔍 3. నామినేషన్ల పరిశీలన న్యాయబద్ధ సూత్రాలు",
      points: [
        "<strong>సంక్షిప్త విచారణ:</strong> పరిశీలన అనేది సంక్షిప్త న్యాయబద్ధ విచారణ మాత్రమే. ఎన్నికల అధికారి సాధారణ సివిల్ కోర్టుగా వ్యవహరించరాదు.",
        "<strong>అభ్యర్థిత్వానికి అనుకూల ప్రాధాన్యత:</strong> స్పష్టమైన మరియు తీవ్రమైన చట్టబద్ధ అనర్హత ఉంటే తప్ప నామినేషన్‌ను ఆమోదించే దిశగానే పరిశీలించాలి.",
        "<strong>సాంకేతిక లోపాలు విస్మరించాలి:</strong> పేర్లలో చిన్న చిన్న అక్షర దోషాలు, తండ్రి పేరులో తేడాలు, ఓటరు గుర్తింపు స్పష్టంగా ఉన్నప్పుడు జరిగే క్లరికల్ తప్పుల ఆధారంగా తిరస్కరించరాదు.",
        "<strong>సమాధానమిచ్చే హక్కు:</strong> అభ్యర్థిపై ఏదైనా అభ్యంతరం వ్యక్తమైతే, సమాధానం ఇచ్చుకునేందుకు మరుసటి రోజు ఉదయం 11:00 గంటల వరకు తగిన సమయం ఇవ్వాలి."
      ]
    },
    {
      title: "🗳️ 4. బ్యాలెట్ పత్రాలు & పెట్టెల నియమావళి",
      points: [
        "<strong>రంగుల విభజన:</strong> ఛైర్‌పర్సన్ ఎన్నికకు తెలుపు రంగు బ్యాలెట్ పత్రం; వార్డు సభ్యుల ఎన్నికకు గులాబీ రంగు బ్యాలెట్ పత్రం.",
        "<strong>డిస్టింగ్విషింగ్ మార్క్:</strong> ఓటరుకు ఇచ్చే ముందు ప్రిసైడింగ్ అధికారి ప్రతి బ్యాలెట్ వెనుక డిస్టింగ్విషింగ్ మార్క్ స్టాంప్ వేసి పూర్తి సంతకం చేయాలి.",
        "<strong>పెట్టె స్లిట్ సీలింగ్:</strong> సాయంత్రం 5:00 గంటలకు (ఆఖరి స్లిప్ ఓటర్ ఓటు వేసిన తరువాత) పోలింగ్ ఏజెంట్ల సమక్షంలో పెట్టె స్లిట్‌ను సీల్ చేయాలి.",
        "<strong>పేపర్ సీల్ ఖాతా:</strong> ఉపయోగించిన, ఉపయోగించని మరియు పాడైన గ్రీన్ పేపర్ సీళ్ల లెక్కలను ఫారం-X-C పార్ట్-II లో నమోదు చేయాలి."
      ]
    },
    {
      title: "👥 5. పోలింగ్ రోజు ప్రత్యేక పరిస్థితులు",
      points: [
        "<strong>ఛాలెంజ్డ్ ఓట్లు (రూల్ 36):</strong> ఏజెంట్ రూ. 5/- రుసుము చెల్లించాలి. PO సంక్షిప్త విచారణ జరుపుతారు. దొంగ ఓటుగా తేలితే పోలీసులకు అప్పగించాలి. సరైన ఓటరైతే ఓటు వేయించి డిపాజిట్ జప్తు చేయాలి. ఫారం-XIV & XV నిర్వహించాలి.",
        "<strong>అంధ / నిస్సహాయ ఓటర్లు:</strong> 18 ఏళ్లు పైబడిన సహాయకుడిని అనుమతించవచ్చు (ఒక సహాయకుడు ఒక్క ఓటరుకు మాత్రమే సహాయపడాలి). ఫారం-XVII లో డిక్లరేషన్ తీసుకోవాలి.",
        "<strong>టెండర్డ్ ఓట్లు (రూల్ 42):</strong> ఒకరి ఓటు మరొకరు వేసేసినట్లు తేలితే, గుర్తింపు సరిచూసి టెండర్డ్ బ్యాలెట్ పత్రం ఇవ్వాలి (దీనిని పెట్టెలో వేయరాదు). ఫారం-XVI కవరులో భద్రపరచాలి.",
        "<strong>ASD జాబితా తనిఖీ:</strong> గైర్హాజరైన, వలస వెళ్లిన, చనిపోయిన (ASD) జాబితా పరిశీలించాలి. ఎవరైనా వస్తే EPIC కార్డు పరిశీలించి, సంతకం & వేలిముద్ర తీసుకుని డైరీలో నమోదు చేయాలి."
      ]
    },
    {
      title: "📊 6. ఓట్ల లెక్కింపు & రీ-కౌంటింగ్ నిబంధనలు",
      points: [
        "<strong>డ్రమ్ మిక్సింగ్:</strong> 25 బ్యాలెట్ల చొప్పున కట్టిన కట్టలను పెద్ద డ్రమ్‌లో వేసి కలపాలి. ఇది పోలింగ్ కేంద్రాల వారీ సరళి బయటకు రాకుండా ఓటు గోప్యతను కాపాడుతుంది.",
        "<strong>సందేహాస్పద ఓట్ల నిర్ణయం:</strong> సందేహాస్పద ఓట్లను ఆమోదించే లేదా తిరస్కరించే చట్టబద్ధ అధికారం ఒక్క ఎన్నికల అధికారికి మాత్రమే ఉంది. కౌంటింగ్ సూపర్‌వైజర్లు తిరస్కరించరాదు!",
        "<strong>15 నిమిషాల విరామం తప్పనిసరి:</strong> ఫారం-XX పార్ట్-I లో లెక్కలు వేసిన తరువాత ఫలితాన్ని మైక్‌లో ప్రకటించి, సరిగ్గా 15 నిమిషాలు వేచి ఉండాలి. రీ-కౌంటింగ్ దరఖాస్తులను పరిష్కరించిన తర్వాతే సంతకం చేయాలి.",
        "<strong>గోప్యతా భంగం నేరం:</strong> ఎన్నికల గోప్యతను ఉల్లంఘించిన ఏ అధికారి లేదా ఏజెంట్‌కైనా సెక్షన్ 343-F క్రింద 3 నెలల వరకు జైలు శిక్ష లేదా జరిమానా విధించబడుతుంది."
      ]
    }
  ]
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  initClock();
  applyLanguage(currentLang);
  calculateBallots();
  generateQueueSlips();
});

// Set Language Function
function setLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('SKHT_ELECTION_LANG', lang);
  applyLanguage(lang);
}

// Apply Language to the entire page
function applyLanguage(lang) {
  const t = PORTAL_TRANSLATIONS[lang] || PORTAL_TRANSLATIONS.en;

  // Language buttons toggle
  document.getElementById('btnLangEn').classList.toggle('active', lang === 'en');
  document.getElementById('btnLangTe').classList.toggle('active', lang === 'te');

  // Header Titles
  document.getElementById('headerTitle').textContent = t.headerTitle;
  document.getElementById('headerSubtitle').textContent = t.headerSubtitle;

  // Header Stats
  const statsCont = document.getElementById('headerStats');
  if (statsCont) {
    statsCont.innerHTML = t.stats.map(s => `
      <div class="stat-pill">${s.label}: <b>${s.val}</b></div>
    `).join('');
  }

  // Banner
  const banner = document.getElementById('bannerNotice');
  if (banner) {
    banner.innerHTML = `
      <div class="banner-text">
        <h2>${t.banner.title}</h2>
        <p>${t.banner.desc}</p>
      </div>
      <div class="banner-actions">
        <button class="btn btn-accent" onclick="switchTab('tab-checklists')">${t.banner.btnChecklists}</button>
        <button class="btn btn-outline" onclick="window.print()">${t.banner.btnPrint}</button>
      </div>
    `;
  }

  // Navigation Tabs
  const navCont = document.getElementById('navTabsContainer');
  if (navCont) {
    const currentActiveTab = document.querySelector('.tab-content.active')?.id || 'tab-schedule';
    navCont.innerHTML = t.tabs.map(tab => `
      <button class="nav-btn ${tab.id === currentActiveTab ? 'active' : ''}" onclick="switchTab('${tab.id}')">
        <span>${tab.icon} ${tab.title}</span>
        ${tab.badge ? `<span class="nav-badge">${tab.badge}</span>` : ''}
      </button>
    `).join('');
  }

  // Tab 1: Schedule
  document.getElementById('t-sched-title').textContent = t.sched.title;
  document.getElementById('t-sched-sub').textContent = t.sched.sub;

  const tGrid = document.getElementById('timelineGrid');
  if (tGrid) {
    tGrid.innerHTML = t.sched.timelines.map(item => `
      <div class="timeline-card ${item.class}">
        <span class="stage-badge">${item.stage}</span>
        <div class="timeline-date">${item.date}</div>
        <h4>${item.title}</h4>
        <p>${item.desc}</p>
        <div class="timeline-time">${item.time}</div>
      </div>
    `).join('');
  }

  const tlCard = document.getElementById('timeLimitsCard');
  if (tlCard) {
    tlCard.innerHTML = `
      <div class="card-header">
        <h3>${t.sched.timeLimitsTitle}</h3>
        <span class="tag-badge tag-ur">${lang === 'te' ? 'నిబంధనలు' : 'Rule Limits'}</span>
      </div>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              ${t.sched.timeLimitsCols.map(c => `<th>${c}</th>`).join('')}
            </tr>
          </thead>
          <tbody>
            ${t.sched.timeLimits.map(row => `
              <tr>
                <td><b>${row.act}</b></td>
                <td>${row.limit}</td>
                <td>${row.resp}</td>
                <td><code>${row.cite}</code></td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  }

  // Tab 2: Stages
  document.getElementById('t-stages-title').textContent = t.stagesTitle;
  document.getElementById('t-stages-sub').textContent = t.stagesSub;

  const stagesCont = document.getElementById('stagesContainer');
  if (stagesCont) {
    stagesCont.innerHTML = t.stages.map((st, idx) => `
      <div class="stage-box ${idx === 0 ? 'open' : ''}">
        <div class="stage-box-header" onclick="toggleStage(this)">
          <div class="stage-header-title">
            <span class="stage-num">${st.num}</span>
            <div>
              <h3>${st.title}</h3>
              <p style="font-size: 0.8rem; color: var(--text-muted);">${st.sub}</p>
            </div>
          </div>
          <span class="stage-date-tag">${st.date}</span>
        </div>
        <div class="stage-box-body">
          <div class="grid-2">
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">${st.opsTitle}</h4>
              <ul class="guideline-points">
                ${st.ops.map(pt => `<li>${pt}</li>`).join('')}
              </ul>
            </div>
            <div>
              <h4 style="color: var(--secondary); margin-bottom: 0.5rem;">${st.legalTitle}</h4>
              <ul class="guideline-points">
                ${st.legal.map(pt => `<li>${pt}</li>`).join('')}
              </ul>
            </div>
          </div>
        </div>
      </div>
    `).join('');
  }

  // Tab 3: Checklists
  document.getElementById('t-chk-title').textContent = t.chkTitle;
  document.getElementById('t-chk-sub').textContent = t.chkSub;

  const chkControls = document.getElementById('chkControls');
  if (chkControls) {
    chkControls.innerHTML = `
      <div class="progress-bar-container">
        <div class="progress-bar-label">
          <span>${t.chkProgressLabel}</span>
          <span id="chkProgressPercent">0% Completed (0/40)</span>
        </div>
        <div class="progress-bar">
          <div id="chkProgressBar" class="progress-fill"></div>
        </div>
      </div>
      <div style="display: flex; gap: 0.5rem;">
        <button class="btn btn-secondary" onclick="resetChecklist()">${t.chkResetBtn}</button>
        <button class="btn btn-success" onclick="window.print()">${t.chkPrintBtn}</button>
      </div>
    `;
  }

  renderChecklists(lang);

  // Tab 4: Guidelines
  document.getElementById('t-guide-title').textContent = t.guideTitle;
  document.getElementById('t-guide-sub').textContent = t.guideSub;
  const guideCont = document.getElementById('guidelinesContainer');
  if (guideCont) {
    const gList = GUIDELINES_DATA[lang] || GUIDELINES_DATA.en;
    guideCont.innerHTML = gList.map(g => `
      <div class="guideline-card">
        <h3>${g.title}</h3>
        <ul class="guideline-points">
          ${g.points.map(p => `<li>${p}</li>`).join('')}
        </ul>
      </div>
    `).join('');
  }

  // Tab 5: Do's and Don'ts
  document.getElementById('t-dodont-title').textContent = t.dodontTitle;
  document.getElementById('t-dodont-sub').textContent = t.dodontSub;
  renderDoDont(lang);

  // Tab 6: Forms
  document.getElementById('t-forms-title').textContent = t.formsTitle;
  document.getElementById('t-forms-sub').textContent = t.formsSub;
  renderFormsList();

  // Tab 7: Directory
  document.getElementById('t-dir-title').textContent = t.dirTitle;
  document.getElementById('t-dir-sub').textContent = t.dirSub;
  renderDirectory(lang);

  // Tab 8: Tools
  document.getElementById('t-tools-title').textContent = t.toolsTitle;
  document.getElementById('t-tools-sub').textContent = t.toolsSub;
  renderTools(lang);

  // Footer
  const ft = document.getElementById('portalFooter');
  if (ft) {
    ft.innerHTML = `
      <p><b>${t.footer.p1}</b></p>
      <p style="margin-top: 4px;">${t.footer.p2}</p>
      <p style="margin-top: 6px; color: #64748b;">${t.footer.p3}</p>
    `;
  }
}

// Render Checklists
function renderChecklists(lang) {
  const cont = document.getElementById('checklistsContainer');
  if (!cont) return;

  const groups = CHECKLIST_DATA[lang] || CHECKLIST_DATA.en;
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');

  cont.innerHTML = groups.map(group => `
    <div class="card">
      <div class="card-header">
        <h3>${group.title}</h3>
        <span class="tag-badge tag-ur">${group.badge}</span>
      </div>
      <div class="checklist-items">
        ${group.items.map(item => `
          <label class="chk-item ${saved[item.id] ? 'checked' : ''}">
            <input type="checkbox" data-id="${item.id}" ${saved[item.id] ? 'checked' : ''} onchange="updateChecklist(this)">
            <div class="chk-content">
              <div class="chk-title">${item.title}</div>
              <div class="chk-sub">${item.sub}</div>
            </div>
          </label>
        `).join('')}
      </div>
    </div>
  `).join('');

  calculateChecklistProgress();
}

// Update Checklist item
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
  const total = checkboxes.length || 40;
  let checked = 0;
  checkboxes.forEach(cb => { if (cb.checked) checked++; });

  const pct = Math.round((checked / total) * 100);
  const bar = document.getElementById('chkProgressBar');
  const lbl = document.getElementById('chkProgressPercent');
  if (bar) bar.style.width = pct + '%';
  if (lbl) {
    const isTe = currentLang === 'te';
    lbl.textContent = isTe ? `${pct}% పూర్తయింది (${checked}/${total})` : `${pct}% Completed (${checked}/${total})`;
  }
}

function resetChecklist() {
  const isTe = currentLang === 'te';
  const msg = isTe ? 'మీ పరికరంలో భద్రపరిచిన అన్ని చెక్‌లిస్ట్ టిక్కులను రీసెట్ చేయాలనుకుంటున్నారా?' : 'Are you sure you want to reset all checklist marks on this device?';
  if (!confirm(msg)) return;

  localStorage.removeItem(STORAGE_KEY);
  document.querySelectorAll('.checklist-items input[type="checkbox"]').forEach(cb => {
    cb.checked = false;
    cb.closest('.chk-item').classList.remove('checked');
  });
  calculateChecklistProgress();
}

// Render Do's and Don'ts
function renderDoDont(lang) {
  const cont = document.getElementById('dodontContainer');
  if (!cont) return;

  const isTe = lang === 'te';

  const data = [
    {
      cat: isTe ? "👨‍💼 1. ఎన్నికల అధికారులు (EOs) & సహాయక ఎన్నికల అధికారులు (AEOs)" : "👨‍💼 1. For Election Officers (EOs) & Assistant Election Officers (AEOs)",
      dos: isTe ? [
        "నామినేషన్ల స్వీకరణకు ప్రకటించిన ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 వరకు ఖచ్చితంగా పాటించండి.",
        "ప్రతి నామినేషన్ పత్రంపై రన్నింగ్ సీరియల్ నంబర్, అందిన తేదీ, సమయాన్ని తప్పనిసరిగా నమోదు చేసి సంతకం చేయండి.",
        "ఫారం-I రసీదు మరియు పరిశీలన నోటీసుతో పాటు చెక్‌లిస్ట్ కాపీని అభ్యర్థి/ప్రతిపాదకుడికి అందజేయండి.",
        "నామినేషన్ల పరిశీలనను స్వయంగా నిర్వహించండి; మొదటి సెట్ చెల్లినప్పటికీ మిగతా సెట్లను కూడా పరిశీలించండి.",
        "అభ్యంతరాలు వ్యక్తమైనప్పుడు సమాధానం చెప్పుకునేందుకు మరుసటి రోజు ఉదయం 11:00 వరకు సమయం ఇవ్వండి.",
        "పార్టీ గుర్తులను కేటాయించే ముందు ఫారం-A (కలెక్టర్ నుండి) మరియు ఫారం-B (పార్టీ నుండి) సరిచూడండి.",
        "ఫలితాలు ప్రకటించిన తరువాత రీ-కౌంటింగ్ దరఖాస్తుల కొరకు ఖచ్చితంగా 15 నిమిషాలు వేచి ఉండండి."
      ] : [
        "Adhere strictly to the 11:00 AM to 3:00 PM window for receipt of nominations on all notified days.",
        "Affix running serial number, exact date, and minute of receipt on every nomination paper immediately.",
        "Provide duplicate checklist with Form-I receipt and notice of scrutiny to candidate/proposer.",
        "Conduct scrutiny personally; examine all 4 sets filed by a candidate even if the first set is valid.",
        "Give reasonable time up to 11:00 AM the next day if a candidate needs to rebut an objection.",
        "Verify Form-A (from Collector) and Form-B (from Party) before allotting reserved party symbols.",
        "Pause for exactly 15 minutes after announcing counting totals to receive recount petitions."
      ],
      donts: isTe ? [
        "పోస్టు, ఈమెయిల్, కొరియర్ లేదా అనధికార వ్యక్తుల ద్వారా వచ్చిన నామినేషన్లను స్వీకరించవద్దు.",
        "16.11.2026 మధ్యాహ్నం 3:00 గంటల తరువాత వచ్చిన ఏ నామినేషన్‌ను ఎట్టిపరిస్థితుల్లో స్వీకరించరాదు.",
        "అనివార్య కారణాలుంటే తప్ప పరిశీలన ప్రక్రియను సహాయక అధికారులకు అప్పగించరాదు.",
        "సాధారణ క్లరికల్, ప్రింటింగ్ లేదా స్పెల్లింగ్ తప్పులకు నామినేషన్‌ను తిరస్కరించవద్దు.",
        "ఇతర అభ్యర్థుల నామినేషన్ పత్రాలను చేతులతో తాకడానికి ఎవరినీ అనుమతించవద్దు.",
        "19.11.2026 మధ్యాహ్నం 3:00 గంటల తరువాత వచ్చిన ఉపసంహరణలను పరిగణించరాదు.",
        "15 నిమిషాల రీ-కౌంటింగ్ విరామం పాటించకుండా ఫారం-XX పార్ట్-I పై సంతకం చేయవద్దు."
      ] : [
        "Do NOT accept nominations sent by post, email, WhatsApp, or through unauthorized messengers.",
        "Do NOT accept nominations after 3:00 PM on 16.11.2026 under any circumstances.",
        "Do NOT delegate the scrutiny process to an assistant unless unavoidably prevented.",
        "Do NOT reject a nomination for clerical, typographical, or technical errors that are not substantial.",
        "Do NOT allow candidates or agents to physically handle other candidates' nomination papers.",
        "Do NOT entertain any withdrawal notice received after 3:00 PM on 19.11.2026.",
        "Do NOT sign Form-XX Part-I without observing the mandatory 15-minute recount pause."
      ]
    },
    {
      cat: isTe ? "🗳️ 2. ప్రిసైడింగ్ అధికారులు (POs) & పోలింగ్ సిబ్బంది" : "🗳️ 2. For Presiding Officers (POs) & Polling Teams",
      dos: isTe ? [
        "ఉదయం 06:30 గంటలకు పోలింగ్ ఏజెంట్ల సమక్షంలో ఖాళీ బ్యాలెట్ పెట్టెను ప్రదర్శించి సీల్ చేయండి.",
        "గ్రీన్ పేపర్ సీల్ సీరియల్ నంబర్లను రికార్డు చేసి, ఏజెంట్లను వెనుకవైపు సంతకాలు చేయనివ్వండి.",
        "ఓటరుకు ఇచ్చే ముందు తెలుపు మరియు గులాబీ బ్యాలెట్ల వెనుక డిస్టింగ్విషింగ్ స్టాంప్ వేసి పూర్తి సంతకం చేయండి.",
        "ఓటరు ఎడమ చూపుడు వేలికి గోరు నుండి కణుపు వరకు చెరగని సిరా తప్పనిసరిగా వేయండి.",
        "ఓటు గోప్యత కాపాడేలా, మంచి వెలుతురు ఉండేలా ఓటింగ్ కంపార్ట్‌మెంట్‌ను ఏర్పాటు చేయండి.",
        "సాయంత్రం 5:00 గంటలకు క్యూ చివర నిలబడిన వ్యక్తి నుండి 1వ నంబర్ స్లిప్ పంపిణీ చేయండి.",
        "పోలింగ్ ముగిసిన వెంటనే స్లిట్ సీల్ చేసి, ఫారం-X-C ధృవీకరించిన నకలును ఏజెంట్లకు అందజేయండి."
      ] : [
        "Demonstrate the empty ballot box to all polling agents present at 06:30 AM before sealing.",
        "Record Green Paper Seal numbers and allow polling agents to note and sign on the white back.",
        "Stamp Distinguishing Mark and sign in full on the reverse of every White and Pink ballot paper.",
        "Ensure Indelible Ink is applied on the left forefinger from tip to cuticle before issuing ballot.",
        "Position voting compartment to ensure absolute secrecy of vote while keeping compartment in view.",
        "Distribute numbered slips from the back of the queue at 5:00 PM sharp to waiting voters.",
        "Seal the box slit immediately after the last slip holder votes and furnish Form-X-C copy to agents."
      ],
      donts: isTe ? [
        "ఉదయం 07:00 గంటల కంటే ముందు పోలింగ్ ప్రారంభించవద్దు; ఏజెంట్లు రాలేదని ఆలస్యం చేయవద్దు.",
        "ఎడమ చూపుడు వేలికి చెరగని సిరా గుర్తు వేయకుండా ఏ ఓటరునూ వెళ్లనివ్వరాదు.",
        "టెండర్డ్ బ్యాలెట్ పత్రాలను బ్యాలెట్ పెట్టెలో వేయరాదు (ఫారం-XVI కవరులో మాత్రమే ఉంచాలి).",
        "గుర్తుపెట్టిన ఓటర్ల జాబితాను ఏజెంట్లు గది బయటకు తీసుకెళ్లడానికి అనుమతించవద్దు.",
        "ఓటింగ్ కంపార్ట్‌మెంట్ లోపలికి మొబైల్ ఫోన్లు, కెమెరాలను ఎట్టిపరిస్థితుల్లో అనుమతించరాదు.",
        "చట్టబద్ధ మరియు చట్టబద్ధేతర పత్రాలను కలపవద్దు; కేటాయించిన 4 రంగుల కవర్లలోనే భద్రపరచండి.",
        "పోలీసు ఎస్కార్ట్ మరియు రూట్ అధికారి తోడు లేకుండా కేంద్రాన్ని విడిచి వెళ్లరాదు."
      ] : [
        "Do NOT commence poll before 7:00 AM or delay poll commencement for absent agents.",
        "Do NOT allow any voter to leave the polling station without the indelible ink mark.",
        "Do NOT put tendered ballot papers into the ballot box; keep them in the designated Form-XVI cover.",
        "Do NOT allow polling agents to take copies of the marked electoral roll outside the room.",
        "Do NOT permit mobile phones, cameras, or recording devices inside the voting compartment.",
        "Do NOT mix statutory and non-statutory covers; pack strictly into Brown, Green, Yellow, Blue covers.",
        "Do NOT leave the polling station without taking police escort and route officer coordination."
      ]
    }
  ];

  cont.innerHTML = data.map(sec => `
    <div class="card">
      <div class="card-header">
        <h3>${sec.cat}</h3>
      </div>
      <div class="dodont-grid">
        <div class="dodont-card dos">
          <div class="dodont-title">${isTe ? 'చేయవలసినవి (తప్పనిసరి చర్యలు)' : "DO's (Mandatory Actions)"}</div>
          <ul class="dodont-list">
            ${sec.dos.map(d => `<li>${d}</li>`).join('')}
          </ul>
        </div>
        <div class="dodont-card donts">
          <div class="dodont-title">${isTe ? 'చేయకూడనివి (నిషిద్ధ చర్యలు)' : "DON'Ts (Prohibited Actions)"}</div>
          <ul class="dodont-list">
            ${sec.donts.map(d => `<li>${d}</li>`).join('')}
          </ul>
        </div>
      </div>
    </div>
  `).join('');
}

// Render Directory Tables
function renderDirectory(lang) {
  const isTe = lang === 'te';

  // Master Chart
  const wmBox = document.getElementById('wardMasterBox');
  if (wmBox) {
    const resMap = {
      'SC General': isTe ? 'ఎస్సీ జనరల్' : 'SC General',
      'SC Women': isTe ? 'ఎస్సీ మహిళ' : 'SC Women',
      'ST General': isTe ? 'ఎస్టీ జనరల్' : 'ST General',
      'BC General': isTe ? 'బీసీ జనరల్' : 'BC General',
      'BC Women': isTe ? 'బీసీ మహిళ' : 'BC Women',
      'Unreserved General': isTe ? 'అన్‌రిజర్వ్‌డ్ జనరల్' : 'Unreserved General',
      'Unreserved Women': isTe ? 'అన్‌రిజర్వ్‌డ్ మహిళ' : 'Unreserved Women'
    };

    wmBox.innerHTML = `
      <div class="card">
        <div class="card-header">
          <h3>📊 ${isTe ? 'వార్డు రిజర్వేషన్ల సమగ్ర చార్ట్ (44 వార్డులు)' : 'Ward Reservations Master Chart (44 Wards)'}</h3>
          <span class="tag-badge tag-ur">Roc. No. 2578/2026/G-1</span>
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.85rem;">
          ${isTe 
            ? 'విభజన: <b>ఎస్టీ: 1</b> (1 జనరల్) | <b>ఎస్సీ: 4</b> (2 మహిళ, 2 జనరల్) | <b>బీసీ: 17</b> (8 మహిళ, 9 జనరల్) | <b>జనరల్: 22</b> (12 మహిళ, 10 జనరల్) | <b>మహిళా స్థానాలు: 22 (50%)</b>'
            : 'Breakdown: <b>ST: 1</b> (1 Gen) | <b>SC: 4</b> (2 Women, 2 Gen) | <b>BC: 17</b> (8 Women, 9 Gen) | <b>UR: 22</b> (12 Women, 10 Gen) | <b>Total Women Seats: 22 (50%)</b>'}
        </p>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>${isTe ? 'వార్డు నెం.' : 'Ward No.'}</th>
                <th>${isTe ? 'విభాగం' : 'Category'}</th>
                <th>${isTe ? 'రిజర్వేషన్ పేరు' : 'Reservation Name'}</th>
                <th>${isTe ? 'పోలింగ్ కేంద్రాలు' : 'Polling Stations'}</th>
                <th>${isTe ? 'కేంద్రాల సంఖ్యలు' : 'PS Numbers'}</th>
                <th>${isTe ? 'మొత్తం ఓటర్లు' : 'Total Voters'}</th>
              </tr>
            </thead>
            <tbody>
              ${WARD_SUMMARY.map(w => {
                let tagClass = 'tag-ur';
                if (w.res_code.startsWith('SC')) tagClass = 'tag-sc';
                else if (w.res_code.startsWith('ST')) tagClass = 'tag-st';
                else if (w.res_code.startsWith('BC')) tagClass = 'tag-bc';
                if (w.res_code.endsWith('-W')) tagClass += ' tag-women';

                return `
                  <tr>
                    <td><b>${isTe ? 'వార్డు ' + w.ward : 'Ward ' + w.ward}</b></td>
                    <td><span class="tag-badge ${tagClass}">${w.res_code}</span></td>
                    <td>${resMap[w.res_name] || w.res_name}</td>
                    <td><b>${w.ps_count} PS</b></td>
                    <td style="font-family: monospace; font-size: 0.8rem;">${w.ps_list.join(', ')}</td>
                    <td><b>${w.voters.toLocaleString()}</b></td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;
  }

  // Polling Station Table headers
  document.getElementById('th-sl').textContent = isTe ? 'క్రమ సంఖ్య' : 'Sl No.';
  document.getElementById('th-ward').textContent = isTe ? 'వార్డు' : 'Ward';
  document.getElementById('th-psno').textContent = isTe ? 'కేంద్రం నెం.' : 'PS No.';
  document.getElementById('th-name').textContent = isTe ? 'పోలింగ్ కేంద్రం భవనం & చిరునామా' : 'Polling Station Building & Name';
  document.getElementById('th-electors').textContent = isTe ? 'ఓటర్ల సంఖ్య' : 'Electors';
  document.getElementById('th-geo').textContent = isTe ? 'లొకేషన్ మ్యాప్' : 'Geo-Location';
  document.getElementById('t-ps-header').textContent = isTe ? '🏫 పోలింగ్ కేంద్రాల వివరాలు (మొత్తం 88 కేంద్రాలు, 72,537 ఓటర్లు)' : '🏫 Polling Stations Directory (All 88 Stations, 72,537 Electors)';

  renderPollingStations();
}

// Render Tools
function renderTools(lang) {
  const cont = document.getElementById('toolsContainer');
  if (!cont) return;
  const isTe = lang === 'te';

  cont.innerHTML = `
    <div class="grid-2">
      <!-- Calculator -->
      <div class="tool-box">
        <h3 style="color: var(--primary); margin-bottom: 0.5rem;">
          🧮 ${isTe ? 'బ్యాలెట్ పత్రాల అవసరాల గణన యంత్రం' : 'Ballot Paper Procurement Calculator'}
        </h3>
        <p style="font-size: 0.82rem; color: var(--text-muted);">
          ${isTe 
            ? 'అధికారిక సూత్రం: వార్డు ఓటర్లు + 10% అదనపు నిల్వ (సమీప 50 కి రౌండ్); పోలింగ్ కేంద్రం పరిమాణం సమీప 10 కి రౌండ్.'
            : 'Official formula: Ward electorate + 10% reserve rounded to nearest 50; PS requirement rounded to nearest 10.'}
        </p>
        <div class="calc-input-group">
          <label style="font-size: 0.85rem; font-weight: 600;">
            ${isTe ? 'ఓటర్ల సంఖ్య:' : 'Ward / PS Electorate:'}
          </label>
          <input type="number" id="calcElectorate" value="750" min="1" max="100000" oninput="calculateBallots()">
          <button class="btn btn-accent" onclick="calculateBallots()">${isTe ? 'లెక్కించండి' : 'Calculate'}</button>
        </div>
        <div class="calc-res-box" id="calcResults"></div>
      </div>

      <!-- Queue Slips -->
      <div class="tool-box">
        <h3 style="color: var(--primary); margin-bottom: 0.5rem;">
          🎟️ ${isTe ? 'సాయంత్రం 05:00 గంటల క్యూ స్లిప్పుల క్రమం' : '05:00 PM Queue Slip Numbering Guide'}
        </h3>
        <p style="font-size: 0.82rem; color: var(--text-muted);">
          ${isTe 
            ? 'పంపిణీ నియమం: క్యూలో ఆఖరి వ్యక్తికి 1వ నంబర్ స్లిప్ ఇచ్చి, మొదటి వ్యక్తికి చివరి నంబర్ స్లిప్ ఇవ్వాలి.'
            : 'Distribution Rule: Issued from the LAST person standing in queue (Slip 1) to the first person.'}
        </p>
        <div class="calc-input-group">
          <label style="font-size: 0.85rem; font-weight: 600;">
            ${isTe ? 'క్యూలో ఉన్న ఓటర్లు:' : 'Electors in Queue at 5 PM:'}
          </label>
          <input type="number" id="queueVoters" value="45" min="1" max="500" oninput="generateQueueSlips()">
          <button class="btn btn-accent" onclick="generateQueueSlips()">${isTe ? 'క్రమం చూడండి' : 'Generate Sequence'}</button>
        </div>
        <div class="calc-res-box" id="queueResults"></div>
      </div>
    </div>
  `;

  calculateBallots();
  generateQueueSlips();
}

// Navigation Tab switcher
function switchTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));

  const target = document.getElementById(tabId);
  if (target) target.classList.add('active');

  const btn = Array.from(document.querySelectorAll('.nav-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
  if (btn) btn.classList.add('active');

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Accordion Stage Toggle
function toggleStage(header) {
  const parent = header.parentElement;
  parent.classList.toggle('open');
}

// Live Clock
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

// Render 88 Polling Stations
function renderPollingStations(filtered = POLLING_STATIONS) {
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
}

function filterPollingStations() {
  const q = document.getElementById('psSearchInput').value.toLowerCase().trim();
  const ward = document.getElementById('wardFilterSelect').value;

  const filtered = POLLING_STATIONS.filter(ps => {
    const matchesWard = (ward === 'ALL' || ps.ward == ward);
    const matchesQuery = !q || (
      ps.ps_no.toLowerCase().includes(q) ||
      ps.details.toLowerCase().includes(q) ||
      ('ward ' + ps.ward).includes(q) ||
      ('వార్డు ' + ps.ward).includes(q) ||
      ps.voters.toString().includes(q)
    );
    return matchesWard && matchesQuery;
  });

  renderPollingStations(filtered);
}

// Ballot Calculator
function calculateBallots() {
  const el = document.getElementById('calcElectorate');
  const res = document.getElementById('calcResults');
  if (!el || !res) return;

  const n = parseInt(el.value, 10) || 0;
  const isTe = currentLang === 'te';

  if (n <= 0) {
    res.innerHTML = `<span style="color:var(--danger)">${isTe ? 'దయచేసి సరైన ఓటర్ల సంఖ్యను నమోదు చేయండి.' : 'Please enter a valid electorate count.'}</span>`;
    return;
  }

  const raw10 = n * 1.10;
  const wardRound50 = Math.ceil(raw10 / 50) * 50;
  const psRound10 = Math.ceil(raw10 / 10) * 10;

  res.innerHTML = `
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.75rem;">
      <div>
        <div style="color:var(--text-muted); font-size: 0.78rem;">${isTe ? 'ఓటర్ల సంఖ్య:' : 'Base Electorate:'}</div>
        <div style="font-size: 1.1rem; font-weight:700;">${n.toLocaleString()}</div>
      </div>
      <div>
        <div style="color:var(--text-muted); font-size: 0.78rem;">${isTe ? '10% నిల్వతో:' : 'With 10% Reserve:'}</div>
        <div style="font-size: 1.1rem; font-weight:700; color:var(--secondary);">${raw10.toFixed(0)}</div>
      </div>
      <div>
        <div style="color:var(--text-muted); font-size: 0.78rem;">${isTe ? 'వార్డు కోటా (రౌండ్ 50):' : 'Ward Allotment (Round 50):'}</div>
        <div style="font-size: 1.1rem; font-weight:700; color:var(--accent);">${wardRound50.toLocaleString()}</div>
      </div>
      <div>
        <div style="color:var(--text-muted); font-size: 0.78rem;">${isTe ? 'కేంద్రం కోటా (రౌండ్ 10):' : 'PS Allotment (Round 10):'}</div>
        <div style="font-size: 1.1rem; font-weight:700; color:var(--success);">${psRound10.toLocaleString()}</div>
      </div>
    </div>
    <p style="margin-top:0.5rem; font-size:0.75rem; color:var(--text-muted);">
      ${isTe 
        ? 'గమనిక: తెలుపు రంగు (ఛైర్‌పర్సన్) మరియు గులాబీ రంగు (వార్డు సభ్యులు) రెండింటికీ సమాన సంఖ్యలో బ్యాలెట్ పత్రాలు అవసరమవుతాయి.'
        : 'Note: Identical quantities required for White (Chairperson) and Pink (Ward Member) ballots.'}
    </p>
  `;
}

// Queue Slips Sequence Generator
function generateQueueSlips() {
  const el = document.getElementById('queueVoters');
  const res = document.getElementById('queueResults');
  if (!el || !res) return;

  const count = parseInt(el.value, 10) || 0;
  const isTe = currentLang === 'te';

  if (count <= 0) {
    res.innerHTML = `<span style="color:var(--danger)">${isTe ? 'దయచేసి సరైన సంఖ్యను నమోదు చేయండి.' : 'Please enter a valid number of voters in queue.'}</span>`;
    return;
  }

  res.innerHTML = `
    <div style="font-size: 0.85rem; line-height: 1.5;">
      <div style="font-weight: 700; color: var(--primary); margin-bottom: 0.35rem;">
        ${isTe ? `పంపిణీ క్రమం: ప్రిసైడింగ్ అధికారి సంతకం చేసిన మొత్తం <b>${count}</b> స్లిప్పులు ఇవ్వాలి.` : `Distribution Rule: Total <b>${count}</b> numbered slips signed by PO must be distributed.`}
      </div>
      <p style="color: var(--text-muted); font-size: 0.8rem; margin-bottom: 0.5rem;">
        ${isTe 
          ? `1. సరిగ్గా సాయంత్రం 5:00 గంటలకు క్యూ చివర నిలబడండి.<br>
             2. క్యూ చివర నిలబడిన ఓటరుకు <b>స్లిప్ నెం. 1</b> ఇవ్వండి.<br>
             3. ముందుకు నడుస్తూ <b>స్లిప్ నెం. 2, 3, 4...</b> ఇస్తూ రండి.<br>
             4. క్యూలో మొదట ఉన్న వ్యక్తికి <b>స్లిప్ నెం. ${count}</b> ఇవ్వండి.<br>
             5. ఓటింగ్ రివర్స్ క్రమంలో (${count} నుండి 1 వరకు) నిర్వహించాలి. దీనివల్ల వెనుక ఎవరూ కొత్తగా చేరలేరు.`
          : `1. Stand at the very END of the queue at exactly 05:00 PM.<br>
             2. Issue <b>Slip No. 1</b> to the LAST voter standing in the queue.<br>
             3. Move forward towards the door, issuing <b>Slip No. 2, 3, 4...</b><br>
             4. Issue <b>Slip No. ${count}</b> to the FIRST voter at the head of the queue.<br>
             5. Allow voting strictly in reverse order (${count} down to 1), ensuring no newcomer can enter behind Slip No. 1.`}
      </p>
      <div style="background: #f1f5f9; padding: 0.4rem 0.6rem; border-radius: 4px; font-family: monospace; font-size: 0.8rem;">
        ${isTe ? `క్రమం: ఆఖరి వ్యక్తి = స్లిప్ 1 | మొదటి వ్యక్తి = స్లిప్ ${count}` : `Sequence: Last Person = Slip 1 | First Person = Slip ${count}`}
      </div>
    </div>
  `;
}

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
