// ============================================================================
// BILINGUAL FORMS & PROFORMAS REPOSITORY (22 STATUTORY & NON-STATUTORY FORMS)
// AP Municipalities (Conduct of Election Rules, 2026)
// ============================================================================

const BILINGUAL_FORMS = [
  {
    id: "form-1",
    code: "Form-1",
    name_en: "Notice of Election",
    name_te: "ఎన్నికల నోటీసు",
    rule: "Rule 6 of Election Rules, 2026",
    stage_en: "Pre-Poll / Notice",
    stage_te: "ఎన్నికల నోటీసు",
    desc_en: "Official statutory notice published by Election Officer specifying dates for nominations, scrutiny, withdrawal, and poll.",
    desc_te: "నామినేషన్లు, పరిశీలన, ఉపసంహరణ మరియు పోలింగ్ తేదీలు, వేళలను తెలుపుతూ ఎన్నికల అధికారిచే జారీ చేయబడే చట్టబద్ధ నోటీసు.",
    text_en: `FORM-1
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
Signature of Election Officer / Municipal Commissioner
(Seal)`,
    text_te: `ఫారం-1
[రూల్ 6 చూడండి]
శ్రీకాళహస్తి పురపాలక సంఘ సాధారణ ఎన్నికల నోటీసు - 2026

దీని ద్వారా అందరికీ తెలియజేయడమైనది:
1. ఈ క్రింది స్థానాలకు ఎన్నిక నిర్వహించబడుతుంది:
   (ఎ) ఛైర్‌పర్సన్, శ్రీకాళహస్తి పురపాలక సంఘం (మొత్తం 44 వార్డుల పరిధిలో ప్రత్యక్ష ఎన్నిక).
   (బి) వార్డు సభ్యులు, వార్డు నెం. [_____], రిజర్వేషన్: [_____].

2. నామినేషన్ పత్రాలను అభ్యర్థి లేదా అతని ప్రతిపాదకుడు [కార్యాలయం / గది నెం.] వద్ద ఎన్నికల అధికారి / సహాయక ఎన్నికల అధికారికి 14.11.2026 నుండి 16.11.2026 వరకు ప్రతిరోజూ ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 గంటల మధ్య (సెలవు దినాలతో సహా) అందజేయవచ్చు.

3. ఖాళీ నామినేషన్ ఫారాలను పై ప్రదేశం మరియు వేళలలో ఉచితంగా పొందవచ్చు.

4. నామినేషన్ పత్రాల పరిశీలన [పరిశీలన హాలు] నందు 17.11.2026 తేదీన ఉదయం 11:00 గంటల నుండి ప్రారంభమవుతుంది.

5. అభ్యర్థిత్వాన్ని ఉపసంహరించుకోవాలనుకుంటే అభ్యర్థి స్వయంగా గానీ, ప్రతిపాదకుడు గానీ లేదా లిఖితపూర్వకంగా అధికారం పొందిన ఎన్నికల ఏజెంట్ ద్వారా గానీ 19.11.2026 మధ్యాహ్నం 3:00 గంటల లోపు ఎన్నికల అధికారికి అందజేయాలి.

6. ఎన్నికల పోటీ అనివార్యమైన సందర్భంలో, పోలింగ్ 26.11.2026 తేదీన ఉదయం 07:00 నుండి సాయంత్రం 05:00 గంటల వరకు నిర్వహించబడుతుంది.

తేది: 14.11.2026
స్థలం: శ్రీకాళహస్తి
ఎన్నికల అధికారి / మున్సిపల్ కమిషనర్ సంతకం
(ముద్ర)`
  },
  {
    id: "form-I",
    code: "Form-I",
    name_en: "Receipt for Nomination & Notice of Scrutiny",
    name_te: "నామినేషన్ పత్రం రసీదు & పరిశీలన నోటీసు",
    rule: "Rule 8(7) of Election Rules, 2026",
    stage_en: "Nominations",
    stage_te: "నామినేషన్లు",
    desc_en: "Statutory acknowledgement issued to candidate/proposer acknowledging receipt of nomination and giving notice of scrutiny.",
    desc_te: "నామినేషన్ పత్రం అందినట్లు నిర్ధారిస్తూ మరియు పరిశీలన సమయాన్ని తెలుపుతూ అభ్యర్థికి ఇచ్చే అధికారిక రసీదు.",
    text_en: `FORM-I
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
(Seal)`,
    text_te: `ఫారం-I
[రూల్ 8(7) చూడండి]
నామినేషన్ పత్రం రసీదు మరియు పరిశీలన నోటీసు

నామినేషన్ పత్రం క్రమ సంఖ్య: [_____ / వార్డు నెం. _____]

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి పోటీ చేయు శ్రీ/శ్రీమతి [___________________________] గారి నామినేషన్ పత్రం నా కార్యాలయములో తేది [________] న [_____] గంటలకు *అభ్యర్థి / *ప్రతిపాదకుని చేత నాకు స్వయంగా అందజేయబడింది.

నామినేషన్ పత్రాల పరిశీలన తేది: 17.11.2026 న ఉదయం 11:00 గంటలకు [పరిశీలన గది నెం. _____] నందు చేపట్టబడుతుంది.

పత్రాల చెక్‌లిస్ట్ సరిచూసి ధృవీకరించిన నకలు అందజేయడమైనది.
భద్రతా డిపాజిట్ రసీదు నెం.: [___________] తేది: [__________] మొత్తం: రూ. [_________]

తేది: [__________]
స్థలం: శ్రీకాళహస్తి
ఎన్నికల అధికారి / సహాయక ఎన్నికల అధికారి సంతకం
(ముద్ర)`
  },
  {
    id: "form-IA",
    code: "Form-IA",
    name_en: "Declaration of Choice of Symbols",
    name_te: "ఎన్నికల గుర్తుల ఎంపిక డిక్లరేషన్",
    rule: "Rule 8(9) of Election Rules, 2026",
    stage_en: "Nominations",
    stage_te: "నామినేషన్లు",
    desc_en: "Declaration filed by the candidate indicating three preferences of free symbols in order of priority.",
    desc_te: "అభ్యర్థి తన ప్రాధాన్యతా క్రమంలో మూడు ఉచిత ఎన్నికల గుర్తును ఎంపిక చేసుకుంటూ సమర్పించే డిక్లరేషన్.",
    text_en: `FORM-IA
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
Signature of Candidate`,
    text_te: `ఫారం-IA
[రూల్ 8(9) చూడండి]
ఎన్నికల గుర్తుల ఎంపికపై అభ్యర్థి డిక్లరేషన్

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి అభ్యర్థినైన నేను [________________________________________________], ఈ క్రింది గుర్తులను ప్రాధాన్యతా క్రమంలో ఎంచుకుంటున్నట్లు ప్రకటిస్తున్నాను:

(i) మొదటి ప్రాధాన్యత గుర్తు: [_____________________________]
(ii) రెండవ ప్రాధాన్యత గుర్తు:  [_____________________________]
(iii) మూడవ ప్రాధాన్యత గుర్తు:  [_____________________________]

*నేను [_____________________________] పార్టీ తరపున నిలబడిన గుర్తింపు పొందిన / నమోదైన పార్టీ అభ్యర్థిని.
(లేదా)
*నేను స్వతంత్ర అభ్యర్థిగా పోటీ చేస్తున్నాను.

తేది: [__________]
అభ్యర్థి సంతకం`
  },
  {
    id: "form-II",
    code: "Form-II",
    name_en: "Declaration of Caste / Community (SC/ST/BC)",
    name_te: "కుల ధృవీకరణ డిక్లరేషన్ (SC/ST/BC)",
    rule: "Rule 8(3) of Election Rules, 2026",
    stage_en: "Nominations",
    stage_te: "నామినేషన్లు",
    desc_en: "Declaration by candidate contesting reserved seats or seeking concession in security deposit.",
    desc_te: "రిజర్వ్‌డ్ స్థానాలలో పోటీచేసే లేదా రాయితీ డిపాజిట్ పొందే అభ్యర్థి సమర్పించే కుల డిక్లరేషన్.",
    text_en: `FORM-II
[See Rule 8(3)]
DECLARATION AS TO CASTE / COMMUNITY

I, [________________________________________________], candidate for election to the office of Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, hereby solemnly declare that:

1. I belong to the [_______________________] caste/tribe/community, which is recognized as a *Scheduled Caste / *Scheduled Tribe / *Backward Class in the State of Andhra Pradesh.
2. An attested copy of the Community Certificate issued by the competent authority (not below the rank of Deputy Tahsildar) is enclosed herewith.

Date: [__________]
Signature of Candidate`,
    text_te: `ఫారం-II
[రూల్ 8(3) చూడండి]
కులము / తెగ / కమ్యూనిటీ డిక్లరేషన్

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి అభ్యర్థినైన నేను [________________________________________________], ఈ క్రింది విధంగా ప్రమాణపూర్వకంగా ప్రకటిస్తున్నాను:

1. నేను ఆంధ్రప్రదేశ్ రాష్ట్రంలో గుర్తింపు పొందిన *షెడ్యూల్డ్ కులం / *షెడ్యూల్డ్ తెగ / *వెనుకబడిన తరగతి కి చెందిన [_______________________] కులానికి చెందినవాడను.
2. డిప్యూటీ తహసీల్దార్ హోదా తగ్గని సక్షమ అధికారి జారీచేసిన కుల ధృవీకరణ పత్రం నకలును దీనితో జతపరుస్తున్నాను.

తేది: [__________]
అభ్యర్థి సంతకం`
  },
  {
    id: "decl-antecedents",
    code: "Declaration",
    name_en: "Criminal Antecedents, Assets & Education",
    name_te: "నేర చరిత్ర, ఆస్తులు & విద్యార్హతల డిక్లరేషన్",
    rule: "Rule 8(10) of Election Rules, 2026",
    stage_en: "Nominations",
    stage_te: "నామినేషన్లు",
    desc_en: "Mandatory declaration on criminal antecedents, assets, liabilities, and education attested by two witnesses.",
    desc_te: "ఇద్దరు సాక్షుల ధృవీకరణతో అభ్యర్థి సమర్పించవలసిన నేర రికార్డు, చరాస్తులు, స్థిరాస్తులు, అప్పులు మరియు విద్యార్హతల పత్రం.",
    text_en: `DECLARATION ON CRIMINAL ANTECEDENTS, ASSETS & EDUCATION
[See Rule 8(10)]

I, [___________________________], son/daughter/wife of [___________________________], aged [_____] years, resident of [_______________________________________________________], candidate for election as Chairperson / Ward Member for Ward No. [_____] of Srikalahasti Municipality, do hereby declare:

1. Criminal Cases:
   (a) Whether convicted in any criminal offence: *Yes / No
   (b) Details of pending cases where charges framed: [Nil / Details]

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
2. Name: [_______________________] Voter Roll No: [_____/_____] Signature: [___________]`,
    text_te: `నేర చరిత్ర, ఆస్తులు, అప్పులు మరియు విద్యార్హతల డిక్లరేషన్
[రూల్ 8(10) చూడండి]

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి పోటీచేస్తున్న అభ్యర్థినైన నేను [___________________________], తండ్రి/భర్త పేరు [___________________________], వయస్సు [_____] సంవత్సరాలు, నివాసం [_______________________________________________________], ఈ క్రింది విధంగా ప్రకటిస్తున్నాను:

1. నేర చరిత్ర:
   (ఎ) క్రిమినల్ కేసులో శిక్ష పడిందా: *అవును / కాదు
   (బి) కోర్టులో అభియోగాలు మోపబడిన పెండింగ్ కేసుల వివరాలు: [ఏమీలేవు / కేసు వివరాలు]

2. ఆస్తులు మరియు అప్పులు:
   (ఎ) చరాస్తులు (స్వయంగా / భార్య లేదా భర్త / ఆధారపడినవారు): [వివరాలు / విలువ]
   (బి) స్థిరాస్తులు (స్వయంగా / భార్య లేదా భర్త / ఆధారపడినవారు): [వివరాలు / విలువ]
   (సి) మున్సిపాలిటీ లేదా ఆర్థిక సంస్థలకు బకాయిలు: [ఏమీలేవు / వివరాలు]

3. విద్యార్హతలు:
   పూర్తిచేసిన అత్యున్నత విద్యార్హత: [_____________________________] పాఠశాల/కళాశాల.

ధృవీకరణ:
ఈ పత్రంలోని అంశాలన్నీ నా పూర్తి పరిజ్ఞానం ప్రకారం సత్యమైనవని ధృవీకరిస్తున్నాను. ఏ కాలమ్‌ను ఖాళీగా ఉంచలేదు.

అభ్యర్థి సంతకం: [_____________________________]

సాక్షులు:
1. పేరు: [_______________________] ఓటరు జాబితా సంఖ్య: [_____/_____] సంతకం: [___________]
2. పేరు: [_______________________] ఓటరు జాబితా సంఖ్య: [_____/_____] సంతకం: [___________]`
  },
  {
    id: "form-VII",
    code: "Form-VII",
    name_en: "Final List of Contesting Candidates",
    name_te: "పోటీచేయు అభ్యర్థుల తుది జాబితా",
    rule: "Rule 14(1) of Election Rules, 2026",
    stage_en: "Contesting List & Symbols",
    stage_te: "గుర్తులు & తుది జాబితా",
    desc_en: "Final list of contesting candidates with allotted symbols, arranged in Telugu alphabetical order.",
    desc_te: "కేటాయించిన ఎన్నికల గుర్తులు మరియు అభ్యర్థుల పేర్లతో తెలుగు అక్షర క్రమంలో ప్రచురించే అధికారిక తుది జాబితా.",
    text_en: `FORM-VII
[See Rule 14(1)]
FINAL LIST OF CONTESTING CANDIDATES

Election to Chairperson / Ward Member for Ward No. [_____]
Srikalahasti Municipality

(i) Candidates of Recognised National and State Political Parties:
-----------------------------------------------------------------------------------------
Sl. No. | Name of Candidate       | Address of Candidate    | Party / Symbol Allotted
-----------------------------------------------------------------------------------------
1.      | [Telugu Alph. Order]    |                         |
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
(Seal)`,
    text_te: `ఫారం-VII
[రూల్ 14(1) చూడండి]
పోటీచేయు అభ్యర్థుల తుది జాబితా

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి ఎన్నిక

(i) గుర్తింపు పొందిన జాతీయ మరియు రాష్ట్ర రాజకీయ పార్టీల అభ్యర్థులు:
-----------------------------------------------------------------------------------------
క్రమ సంఖ్య | అభ్యర్థి పేరు (తెలుగు అక్షర క్రమం) | అభ్యర్థి చిరునామా | పార్టీ / కేటాయించిన గుర్తు
-----------------------------------------------------------------------------------------
1.         |                                    |                   |
2.         |                                    |                   |

(ii) నమోదైన (రిజిస్టర్డ్) రాజకీయ పార్టీల అభ్యర్థులు:
3.         |                                    |                   |

(iii) ఇతర (స్వతంత్ర) అభ్యర్థులు:
4.         |                                    |                   |
-----------------------------------------------------------------------------------------
చివరి ప్యానెల్: పైవారెవరూ కాదు (NOTA)

తేది: 19.11.2026 (మధ్యాహ్నం 3:00 గంటల తరువాత)
స్థలం: శ్రీకాళహస్తి
ఎన్నికల అధికారి సంతకం
(ముద్ర)`
  },
  {
    id: "form-X-C",
    code: "Form-X-C",
    name_en: "Ballot Paper Account & Paper Seal Account",
    name_te: "బ్యాలెట్ పేపర్ ఖాతా & పేపర్ సీల్ ఖాతా",
    rule: "Rule 45 of Election Rules, 2026",
    stage_en: "Ballot Accounts",
    stage_te: "బ్యాలెట్ లెక్కలు",
    desc_en: "Crucial statutory account prepared by Presiding Officer at poll close. Attested copy given to all agents.",
    desc_te: "పోలింగ్ ముగిసిన వెంటనే ప్రిసైడింగ్ అధికారి తయారుచేసే చట్టబద్ధ బ్యాలెట్ లెక్కల పత్రం. ఏజెంట్లకు కాపీ ఇవ్వడం తప్పనిసరి.",
    text_en: `FORM-X-C
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

5. Number of Ballot Papers to be found in Ballot Box (3 - 4): [_______]

PART-II: PAPER SEAL ACCOUNT
1. Serial numbers of Green Paper Seals supplied: [_____] to [_____] = Total: [_____]
2. Number of Paper Seals used: [_____] (Sl. Nos.: [_______________])
3. Number of unused Paper Seals returned: [_____]
4. Number of damaged Paper Seals: [_____]

Date: 26.11.2026 (05:00 PM)
Signature of Presiding Officer
Signatures of Polling Agents present:
1. [___________________]  2. [___________________]  3. [___________________]`,
    text_te: `ఫారం-X-C
[రూల్ 45 చూడండి]
పార్ట్-I: బ్యాలెట్ పత్రాల ఖాతా

పురపాలక సంఘం: శ్రీకాళహస్తి పురపాలక సంఘం
వార్డు నెం.: [_____]   పోలింగ్ కేంద్రం నెం.: [_____ / _____]

1. అందిన మొత్తం బ్యాలెట్ పత్రాల సంఖ్య:
   క్రమ సంఖ్య [__________] నుండి [__________] వరకు = మొత్తం: [_______]

2. ఉపయోగించని బ్యాలెట్ పత్రాల సంఖ్య:
   (ఎ) చెడిపోనివి (మిగిలినవి): [_______]
   (బి) రద్దుచేసినవి / సంతకం చేసి వాడనివి: [_______]

3. ఓటర్లకు జారీచేసిన బ్యాలెట్ పత్రాలు (1 - 2): [_______]

4. ఉపయోగించిన టెండర్డ్ బ్యాలెట్ పత్రాల సంఖ్య: [_______]

5. బ్యాలెట్ పెట్టెలో ఉండవలసిన బ్యాలెట్ పత్రాలు (3 - 4): [_______]

పార్ట్-II: పేపర్ సీల్ ఖాతా
1. సరఫరా చేసిన గ్రీన్ పేపర్ సీళ్ల నంబర్లు: [_____] నుండి [_____] వరకు = మొత్తం: [_____]
2. ఉపయోగించిన పేపర్ సీళ్ల సంఖ్య: [_____] (నంబర్లు: [_______________])
3. ఉపయోగించని పేపర్ సీళ్లు: [_____]
4. పాడైన పేపర్ సీళ్లు: [_____]

తేది: 26.11.2026 (సాయంత్రం 05:00 గంటలకు)
ప్రిసైడింగ్ అధికారి సంతకం
హాజరైన పోలింగ్ ఏజెంట్ల సంతకాలు:
1. [___________________]  2. [___________________]  3. [___________________]`
  },
  {
    id: "form-XX-p1",
    code: "Form-XX (Part-I)",
    name_en: "Result Sheet of Election",
    name_te: "ఎన్నిక ఫలితాల లెక్కల పత్రం",
    rule: "Rule 52 of Election Rules, 2026",
    stage_en: "Counting",
    stage_te: "ఓట్ల లెక్కింపు",
    desc_en: "Candidate-wise and table-wise tabulation of votes counted, leading to result announcement.",
    desc_te: "రౌండ్ల వారీగా మరియు టేబుళ్ల వారీగా అభ్యర్థులకు వచ్చిన ఓట్లను నమోదు చేసే తుది లెక్కింపు పత్రం.",
    text_en: `FORM-XX
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
-----------------------------------------------------------------------------------------
Postal Ballots|             |             |             |      |             |
-----------------------------------------------------------------------------------------
GRAND TOTAL   |             |             |             |      |             |
-----------------------------------------------------------------------------------------

Date: 30.11.2026
Place: Counting Hall, Srikalahasti
Signature of Election Officer
(Mandatory 15-Minute Recount Window Observed)`,
    text_te: `ఫారం-XX
[రూల్ 52 చూడండి]
పార్ట్-I: ఎన్నిక ఫలితాల నమోదు పత్రం

శ్రీకాళహస్తి పురపాలక సంఘం ఛైర్‌పర్సన్ / వార్డు నెం. [_____] సభ్యుల స్థానానికి ఎన్నిక - 2026
వార్డులోని మొత్తం ఓటర్లు: [__________]

-----------------------------------------------------------------------------------------
రౌండ్ | టేబుల్ | అభ్యర్థి ఎ | అభ్యర్థి బి | అభ్యర్థి సి | నోటా | చెల్లుబాటు | తిరస్కరించిన
నెం.  | నెం.   | (ఓట్లు)    | (ఓట్లు)    | (ఓట్లు)     |      | ఓట్లు మొత్తం| ఓట్లు
-----------------------------------------------------------------------------------------
1.    | 1      |            |            |             |      |             |
2.    | 2      |            |            |             |      |             |
-----------------------------------------------------------------------------------------
పోస్టల్ బ్యాలెట్లు|         |            |             |      |             |
-----------------------------------------------------------------------------------------
మొత్తం ఓట్లు  |            |            |             |      |             |
-----------------------------------------------------------------------------------------

తేది: 30.11.2026
స్థలం: లెక్కింపు హాలు, శ్రీకాళహస్తి
ఎన్నికల అధికారి సంతకం
(తప్పనిసరి 15 నిమిషాల రీ-కౌంటింగ్ విరామం పాటించడమైనది)`
  },
  {
    id: "form-XX-p2",
    code: "Form-XX (Part-II)",
    name_en: "Formal Declaration of Result",
    name_te: "ఎన్నిక ఫలితాల అధికారిక ప్రకటన",
    rule: "Rule 53 of Election Rules, 2026",
    stage_en: "Declaration",
    stage_te: "ఫలితాల ప్రకటన",
    desc_en: "Official statutory declaration declaring the winning candidate elected.",
    desc_te: "ఎన్నికలలో గెలుపొందిన విజేతను అధికారికంగా ప్రకటిస్తూ ఎన్నికల అధికారి జారీ చేసే సర్టిఫికెట్.",
    text_en: `FORM-XX
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
(Official Seal)`,
    text_te: `ఫారం-XX
[రూల్ 53 చూడండి]
పార్ట్-II: ఎన్నికల ఫలితాల అధికారిక ప్రకటన

ఆంధ్రప్రదేశ్ మున్సిపాలిటీలు / నగర పంచాయతీల (ఛైర్‌పర్సన్లు మరియు వార్డు సభ్యుల ఎన్నికల నిర్వహణ) నియమావళి, 2026 లోని రూల్ 53 ప్రకారం, ఈ క్రింది అభ్యర్థి:

శ్రీ / శ్రీమతి [_______________________________________________________]
పార్టీ: [__________________________________] / స్వతంత్ర అభ్యర్థి
చిరునామా: [_______________________________________________________]

ఈ క్రింది స్థానానికి సక్రమంగా ఎన్నికైనట్లు నేను అధికారికంగా ప్రకటిస్తున్నాను:
* ఛైర్‌పర్సన్, శ్రీకాళహస్తి పురపాలక సంఘం
(లేదా)
* వార్డు సభ్యులు, వార్డు నెం. [_____], శ్రీకాళహస్తి పురపాలక సంఘం.

స్థలం: శ్రీకాళహస్తి
తేది: 30.11.2026
ఎన్నికల అధికారి / మున్సిపల్ కమిషనర్ సంతకం
(అధికారిక ముద్ర)`
  }
];
