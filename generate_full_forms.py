# -*- coding: utf-8 -*-
"""
Generate complete bilingual forms dataset including all forms from Election-Officers-Forms.pdf
Cleaned of any handwritten text.
"""

import json

forms = [
  {
    "code": "Form-I",
    "rule": "Rule 8(1)",
    "title_en": "Form - I: Nomination Paper for Chairperson / Ward Member",
    "title_te": "ఫారం - I: అభ్యర్థి పూరించవలసిన నామినేషన్ పత్రము",
    "desc_en": "Statutory nomination paper [Rule 8(1)] for Chairperson (White Ballot) or Ward Member (Pink Ballot). Contains 10 candidate/proposer fields, MCC declaration, RO scrutiny receipt, and acceptance/rejection order.",
    "desc_te": "మునిసిపాలిటీ చైర్‌పర్సన్ లేదా వార్డు సభ్యుని పదవికి నామినేషన్ పత్రము [నియమం 8(1)]. 10 అంశాల అభ్యర్థి వివరాలు, ప్రవర్తనా నియమావళి డిక్లరేషన్, పరిశీలన రశీదు మరియు ఆమోద/తిరస్కార ఉత్తర్వులను కలిగి ఉంటుంది.",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Pages 1 & 2)",
    "content_en": """FORM - I
NOMINATION PAPER
[See Rule 8(1)]

Election to the office of Chairperson of SRIKALAHASTI Municipality
(OR)
Election as Ward Member to Ward No. ________ of SRIKALAHASTI Municipality

1. Full Name of Candidate (in BLOCK LETTERS): _____________________________________________
2. Candidate's Serial Number in Electoral Roll: Ward No. _______, Sl. No. ____________________
3. Father's / Husband's Name: ___________________________________________________________
4. Age: ________ years
5. Gender: [  ] Male    [  ] Female    [  ] Third Gender
6. Occupation & Full Postal Address: _____________________________________________________
   ____________________________________________________________________________________
7. Social Category: [  ] OC    [  ] SC    [  ] ST    [  ] BC
8. Full Name of Proposer: ______________________________________________________________
9. Proposer's Serial Number in Electoral Roll: Ward No. _______, Sl. No. ____________________
10. Signature of the Proposer: _________________________________ Date: ___________________

--------------------------------------------------------------------------------
CANDIDATE'S DECLARATION
I hereby declare that I agree to this nomination and that I am set up at this election by:
[  ] _________________________________________________ Party (Reserved Symbol)
[  ] An Independent Candidate on Free Symbol allotted by the Election Authority

I further declare that I have read / have had read out to me the Model Code of Conduct (MCC) prescribed by the State Election Commission, Andhra Pradesh, and I solemnly promise to abide by all provisions contained therein.

Date: ________________________                               Signature of Candidate

--------------------------------------------------------------------------------
RETURNING OFFICER'S ENDORSEMENT
Nomination Paper Serial Number: ________________________
This nomination paper was delivered to me at my office at ________ (hours) on ________ (date) by the Candidate / Proposer.

Date: ________________________                               Signature of Returning Officer / Authorized Person

--------------------------------------------------------------------------------
DECISION OF RETURNING OFFICER ACCEPTING OR REJECTING THE NOMINATION
I have examined this nomination paper in accordance with Rule 12 of the Andhra Pradesh Municipalities / Nagar Panchayats (Conduct of Election of Chairpersons and Ward Members) Rules, 2026, and decide as follows:

[  ] ACCEPTED (ఆమోదించబడినది)
[  ] REJECTED (తిరస్కరించబడినది) - Grounds: ______________________________________________

Date: ________________________                               Signature of Returning Officer

--------------------------------------------------------------------------------
RECEIPT FOR NOMINATION PAPER AND NOTICE OF SCRUTINY
(To be handed over to the person presenting the nomination paper)

Serial No. of Nomination Paper: ________________________
The nomination paper of Sri / Smt / Kum __________________________________________________,
a candidate for election as Chairperson / Ward Member from Ward No. ________ of Srikalahasti Municipality, was delivered to me at my office at ________ (hours) on ________ (date) by the Candidate / Proposer.

All nomination papers will be taken up for scrutiny on:
Date: ________________________ Time: ________ AM/PM Venue: ______________________________

Date: ________________________                               Signature of Returning Officer / Authorized Person""",
    "content_te": """ఫారం - I
అభ్యర్థి పూరించవలసిన నామినేషన్ పత్రము
[నియమం 8(1) చూడుము]

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్ పదవికి (లేదా)
శ్రీకాళహస్తి మునిసిపాలిటీలోని వార్డు నెం. _______ వార్డు సభ్యుని పదవికి ఎన్నిక.

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్‌గా (లేదా) _______ వార్డు సభ్యునిగా ఎన్నికకు నామినేషన్.

1. అభ్యర్థి పూర్తి పేరు: (పెద్ద అక్షరాలలో) : _____________________________________________
2. ఓటర్ల జాబితాలో అభ్యర్థి వరుస సంఖ్య : వార్డు నెం. _______, క్రమ సంఖ్య ____________________
3. తండ్రి లేదా భర్త పేరు : ___________________________________________________________
4. వయస్సు : _______ సంవత్సరాలు
5. లింగము : [  ] పురుషుడు    [  ] మహిళ    [  ] ఇతరులు
6. వృత్తి మరియు చిరునామా : _____________________________________________________
   ___________________________________________________________________________
7. సామాజిక వర్గము : [  ] ఓసీ    [  ] ఎస్సీ    [  ] ఎస్టీ    [  ] బీసీ
8. ప్రతిపాదకుని పూర్తి పేరు : ______________________________________________________________
9. ఓటర్ల జాబితాలో ప్రతిపాదకుని వరుస సంఖ్య : వార్డు నెం. _______, క్రమ సంఖ్య ____________________
10. ప్రతిపాదకుని సంతకము : _________________________________ తేదీ: ___________________

--------------------------------------------------------------------------------
(అభ్యర్థి పూరించవలెను)
రాష్ట్ర ఎన్నికల సంఘం ఆదేశాల మేరకు, ____________________________ పార్టీ గుర్తుపై / ఎన్నికల అధికారి కేటాయించు స్వేచ్ఛా గుర్తుపై, శ్రీకాళహస్తి మునిసిపాలిటీ ________ వార్డు నుండి వార్డు సభ్యునిగా / చైర్‌పర్సన్‌గా ఎన్నికలో పోటీ చేయుటకు నేను సముఖంగా ఉన్నానని ప్రకటించుచున్నాను.

రాష్ట్ర ఎన్నికల సంఘం నిర్దేశించిన ప్రవర్తనా నియమావళిని (MCC) నేను చదివితిని / నాకు చదివి వినిపించబడినది అని, అందులో నిర్దేశించిన నిబంధనలకు నేను కట్టుబడి ఉంటానని ఇంకను ప్రకటించుచున్నాను.

తేదీ: ________________________                               అభ్యర్థి సంతకము

--------------------------------------------------------------------------------
(ఎన్నికల అధికారి పూరించవలెను)
నామినేషన్ పత్రము వరుస సంఖ్య: ________________________
ఈ నామినేషన్ పత్రమును అభ్యర్థి / ప్రతిపాదకుడు ________________________ (తేదీ)న ________________ (గంటలకు) నా కార్యాలయములో నాకు అందజేసినారు.

గమనిక: చైర్‌పర్సన్ / వార్డు సభ్యుని పదవి ఎస్టీలు / ఎస్సీలు / బీసీలకు రిజర్వు చేయబడిన మునిసిపాలిటీ / వార్డుల విషయంలో, నియమం 8(8) లో నిర్దేశించిన ధృవపత్రమును జతపరచవలెను.

తేదీ: ________________________                               ఎన్నికల అధికారి లేదా అధికృత వ్యక్తి

--------------------------------------------------------------------------------
నామినేషన్ పత్రమును ఆమోదించుట లేదా తిరస్కరించుటపై ఎన్నికల అధికారి నిర్ణయము
ఆంధ్రప్రదేశ్ పురపాలక సంఘాల (చైర్‌పర్సన్ మరియు వార్డు సభ్యుల ఎన్నికల నిర్వహణ) నియమాలు, 2026 లోని నియమం 12 ప్రకారం ఈ నామినేషన్ పత్రమును నేను పరిశీలించి ఈ క్రింది విధంగా నిర్ణయించితిని: -

[  ] ఆమోదించబడినది (ACCEPTED)
[  ] తిరస్కరించబడినది (REJECTED) - కారణములు: _____________________________________________

తేదీ: ________________________                               ఎన్నికల అధికారి సంతకం

--------------------------------------------------------------------------------
నామినేషన్ పత్రము రశీదు మరియు పరిశీలన నోటీసు
(నామినేషన్ పత్రమును సమర్పించిన వ్యక్తికి అందజేయవలెను)

నామినేషన్ పత్రము వరుస సంఖ్య: ________________________
శ్రీకాళహస్తి మునిసిపాలిటీ వార్డు నెం. ________ వార్డు నుండి చైర్‌పర్సన్ / వార్డు సభ్యుని ఎన్నికకు అభ్యర్థి అయిన శ్రీ / శ్రీమతి / కుమారి __________________________________ యొక్క నామినేషన్ పత్రమును అభ్యర్థి / ప్రతిపాదకుడు ________________________ (తేదీ)న ________________ (గంటలకు) నా కార్యాలయములో నాకు అందజేసినారు.

అన్ని నామినేషన్ పత్రములు ________________ (స్థలము) వద్ద ________________________ (తేదీ)న ________________ (గంటలకు) పరిశీలనకు తీసుకొనబడును.

తేదీ: ________________________                               ఎన్నికల అధికారి లేదా ఇతర అధికృత వ్యక్తి

*వర్తించని ప్రత్యామ్నాయమును కొట్టివేయవలెను."""
  },
  {
    "code": "Form-II",
    "rule": "Rule 8(8)",
    "title_en": "Form - II: Declaration by SC / ST / BC Candidate",
    "title_te": "ఫారం - II: ఎస్టీ / ఎస్సీ / బీసీ అభ్యర్థి విషయంలో డిక్లరేషన్",
    "desc_en": "Statutory declaration [Rule 8(8)] required for candidates contesting seats reserved for SC, ST, or BC. Must be solemnly affirmed and certified by an officer not below the rank of Deputy Tahsildar.",
    "desc_te": "ఎస్సీ, ఎస్టీ లేదా బీసీలకు రిజర్వు చేసిన స్థానాల్లో పోటీ చేసే అభ్యర్థులు దాఖలు చేయవలసిన చట్టబద్ధ డిక్లరేషన్ [నియమం 8(8)]. డిప్యూటీ తహశీల్దారు హోదాకు తగ్గని రెవెన్యూ అధికారి చేత ధృవీకరించబడాలి.",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Page 3)",
    "content_en": """FORM - II
DECLARATION BY SC / ST / BC CANDIDATE
[See Rule 8(8)]

Election to the office of Chairperson of SRIKALAHASTI Municipality
(OR)
Election as Ward Member to Ward No. ________ of SRIKALAHASTI Municipality

DECLARATION IN RESPECT OF CANDIDATE BELONGING TO SCHEDULED CASTE / SCHEDULED TRIBE / BACKWARD CLASS

I hereby declare that I am a member of the __________________________________ Caste / Tribe / Community, which is recognized as a Scheduled Tribe / Scheduled Caste / Backward Class in relation to the State of Andhra Pradesh, in __________________________________ District / Area.

Date: ________________________                               Signature of Candidate

--------------------------------------------------------------------------------
ATTESTATION / CERTIFICATE BY REVENUE OFFICER
(To be attested by an officer of the Revenue Department not below the rank of Deputy Tahsildar)

The above declaration was solemnly affirmed before me by Sri / Smt / Kum __________________________________, who is personally known to me / identified to my satisfaction by __________________________________.

Office Seal:

Date: ________________________                               Signature of Revenue Officer Not Below
                                                             the Rank of Deputy Tahsildar
                                                             Full Designation: __________________________

*Strike out words which are not applicable.""",
    "content_te": """ఫారం - II
[నియమం 8(8) చూడుము]

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్ పదవికి (లేదా)
శ్రీకాళహస్తి మునిసిపాలిటీలోని వార్డు నెం. _______ వార్డు సభ్యుని పదవికి ఎన్నిక.

షెడ్యూల్డు తెగ / షెడ్యూల్డు కులము / వెనుకబడిన తరగతికి చెందిన అభ్యర్థి విషయంలో ప్రకటన

ఆంధ్రప్రదేశ్ రాష్ట్రంలోని ________________________ జిల్లా లేదా ప్రాంతమునకు సంబంధించి ఆంధ్రప్రదేశ్‌లో షెడ్యూల్డు తెగ / కులము / వెనుకబడిన తరగతిగా గుర్తించబడిన __________________________________ షెడ్యూల్డు తెగ / కులము / వెనుకబడిన తరగతికి చెందిన సభ్యుడనని ఇందుమూలముగా ప్రకటించుచున్నాను.

తేదీ: ________________________                               అభ్యర్థి సంతకము

--------------------------------------------------------------------------------
పై ప్రకటనను శ్రీ / శ్రీమతి / కుమారి __________________________________ నా సమక్షంలో ప్రమాణపూర్వకంగా ధృవీకరించినారు. వారు నాకు వ్యక్తిగతంగా తెలిసినవారు / __________________________________ ద్వారా నా సంతృప్తి మేరకు గుర్తించబడినవారు.

(కార్యాలయ ముద్ర)

తేదీ: ________________________                               డిప్యూటీ తహశీల్దారు హోదాకు తగ్గని
                                                             రెవెన్యూ శాఖ అధికారి సంతకము
                                                             పూర్తి హోదా: __________________________

*వర్తించని ప్రత్యామ్నాయమును కొట్టివేయవలెను."""
  },
  {
    "code": "Form-IA",
    "rule": "Rule 8(9)",
    "title_en": "Form - I A: Declaration on Choice of Symbols",
    "title_te": "ఫారం - I A: గుర్తుల ఎంపికపై ప్రకటన",
    "desc_en": "Statutory declaration [Rule 8(9)] regarding party symbol authorization (Form-B) or indication of three preferred free symbols in order of priority for independent candidates.",
    "desc_te": "రాజకీయ పార్టీ రిజర్వు గుర్తు లేదా స్వతంత్ర అభ్యర్థుల కోసం ప్రాధాన్యతా క్రమంలో మూడు స్వేచ్ఛా గుర్తులలో ఒకదానిని ఎంపిక చేసుకోవడానికి దాఖలు చేయవలసిన ఫారం [నియమం 8(9)].",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Page 4)",
    "content_en": """FORM - I A
DECLARATION ON CHOICE OF SYMBOLS
[See Rule 8(9)]

Election to the office of Chairperson of SRIKALAHASTI Municipality
(OR)
Election as Ward Member to Ward No. ________ of SRIKALAHASTI Municipality

(i) I am set up at this election by the __________________________________ Party, which is a recognized National Party / recognized State Party in the State of Andhra Pradesh / recognized State Party in other States / registered political party with a reserved symbol.
(OR)
(ii) I am set up at this election by the __________________________________ Party, which is a registered political party without a reserved symbol / I am contesting this election as an Independent candidate (strike out which is not applicable), and the symbols I have chosen, in order of preference, are:

1. __________________________________________________________________
2. __________________________________________________________________
3. __________________________________________________________________

Date: ________________________                               Signature of Candidate
                                                             Name: _______________________________

*Strike out whichever is not applicable.""",
    "content_te": """ఫారం - I A
[నియమం 8(9) చూడుము]
గుర్తుల ఎంపికపై ప్రకటన

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్ పదవికి (లేదా)
శ్రీకాళహస్తి మునిసిపాలిటీలోని వార్డు నెం. _______ వార్డు సభ్యుని పదవికి ఎన్నిక.

(i) గుర్తింపు పొందిన జాతీయ పార్టీ / ఆంధ్రప్రదేశ్ రాష్ట్రంలో గుర్తింపు పొందిన రాష్ట్ర పార్టీ / ఇతర రాష్ట్రాలలో గుర్తింపు పొందిన రాష్ట్ర పార్టీ / రిజర్వు చేయబడిన గుర్తు కలిగిన నమోదిత రాజకీయ పార్టీ అయిన __________________________________ పార్టీ ఈ ఎన్నికలో ఈ పదవికి నన్ను అభ్యర్థిగా నిలబెట్టినది.
లేదా
(ii) రిజర్వు చేయబడిన గుర్తు లేని నమోదిత రాజకీయ పార్టీ అయిన __________________________________ పార్టీ ఈ ఎన్నికలో ఈ పదవికి నన్ను అభ్యర్థిగా నిలబెట్టినది / నేను స్వతంత్ర అభ్యర్థిగా ఎన్నికలో పోటీ చేయుచున్నాను (వర్తించని దానిని కొట్టివేయవలెను) మరియు నేను ఎంచుకొనిన గుర్తులు, ప్రాధాన్యతా క్రమంలో, ఈ క్రింద సూచించబడినవి: -

1. __________________________________________________________________
2. __________________________________________________________________
3. __________________________________________________________________

తేదీ: ________________________                               అభ్యర్థి సంతకము
                                                             పేరు: _______________________________

*వర్తించని ప్రత్యామ్నాయమును కొట్టివేయవలెను."""
  },
  {
    "code": "Reg-Deposit",
    "rule": "Statutory Register",
    "title_en": "Nomination Deposit Register (14 Columns)",
    "title_te": "నామినేషన్ ధరావతు డిపాజిట్ల రిజిస్టరు (14 కాలమ్స్)",
    "desc_en": "Statutory 14-column register to account for nomination security deposits (General: ₹3,000, SC/ST/BC: ₹1,500), treasury remittance, and refunds/forfeiture.",
    "desc_te": "నామినేషన్ సెక్యూరిటీ డిపాజిట్ల (జనరల్: ₹3,000, ఎస్సీ/ఎస్టీ/బీసీ: ₹1,500) నిర్వహణ, ప్రభుత్వ ఖజానా/SBI జమ మరియు వాపసు/జప్తు వివరాల 14 కాలమ్‌ల చట్టబద్ధ రిజిస్టరు.",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 5)",
    "content_en": """STATUTORY REGISTER OF NOMINATION DEPOSITS
[Srikalahasti Municipality Phase 2 Ordinary Elections, 2026]

1. Serial Number (క్రమ సంఖ్య): ________________________
2. Candidate's Name & Full Address (అభ్యర్థి పేరు మరియు చిరునామా): __________________________________________________
3. Whether Candidate belongs to SC / ST? (అభ్యర్థి షెడ్యూల్డు కులము / షెడ్యూల్డు తెగ నకు చెందిన వారా ?): [  ] Yes  [  ] No
4. Amount Deposited (డిపాజిట్ చేయబడిన మొత్తము): Rs. _________ (₹3,000 for General / ₹1,500 for SC/ST/BC)
5. Name of Person Depositing (డిపాజిట్ జమ చేసిన వారు): __________________________________________________
6. Whether deposited in Cash or Treasury Chalan? (డిపాజిట్ నగదు రూపములో చేయబడినదా? లేదా ప్రభుత్వ ఖజానాకు జమ చేయబడినదా?):
   Mode: [  ] Cash    [  ] Treasury Chalan No: ________________________ Date: ________________________
7. Date of Deposit (డిపాజిట్ చేసిన తేది): ________________________
8. Date of Remittance to nearby Govt Treasury / SBI by RO (ఎన్నికల అధికారిచే సమిప ప్రభుత్వ ఖజానా లేదా SBI నందు డిపాజిట్ మొత్తము జమ చేయబడిన తేది): ________________________
9. Signature of Assistant Election Officer (సహాయ ఎలక్షన్ అధికారి సంతకము): ________________________
10. Date of Refund or Forfeiture to Govt (డిపాజిట్ మొత్తము జమ చేయబడిన / తిరిగి వాపసు చేయబడిన తేది): ________________________
11. Details of Person Receiving Refund (డిపాజిట్ వాపసు తీసుకున్న వ్యక్తి వివరాలు): __________________________________________________
12. Receipt of Person Receiving Refund (డిపాజిట్ వాపసు తీసుకున్న వ్యక్తి యొక్క రశీదు): __________________________________________________
13. Signature of Election Officer (ఎన్నికల అధికారి సంతకము): ________________________
14. Remarks (రిమార్కులు): __________________________________________________

NOTE: If the deposit amount is paid into the Government Treasury or State Bank, the Chalan Number and Date must be specifically noted in Column No. 6 above.""",
    "content_te": """డిపాజిట్ల రిజిస్టరు
[శ్రీకాళహస్తి పురపాలక సంఘం సాధారణ ఎన్నికలు - 2026]

1. క్రమ సంఖ్య: ________________________
2. అభ్యర్థి పేరు మరియు చిరునామా: __________________________________________________
3. అభ్యర్థి షెడ్యూల్డు కులము / షెడ్యూల్డు తెగ నకు చెందిన వారా ?: [  ] అవును  [  ] కాదు
4. డిపాజిట్ చేయబడిన మొత్తము: రూ. _________ (జనరల్: ₹3,000 / ఎస్సీ, ఎస్టీ, బీసీ: ₹1,500)
5. డిపాజిట్ జమ చేసిన వారు: __________________________________________________
6. డిపాజిట్ నగదు రూపములో చేయబడినదా? లేదా ప్రభుత్వ ఖజానాకు జమ చేయబడినదా?:
   విధానం: [  ] నగదు    [  ] ఖజానా చలానా నెం: ________________________ తేదీ: ________________________
7. డిపాజిట్ చేసిన తేది: ________________________
8. ఎన్నికల అధికారిచే సమిప ప్రభుత్వ ఖజానా లేదా భారతీయ స్టేట్ బ్యాంక్ (SBI) నందు డిపాజిట్ మొత్తము జమ చేయబడిన తేది: ________________________
9. సహాయ ఎలక్షన్ అధికారి సంతకము: ________________________
10. డిపాజిట్ మొత్తము ప్రభుత్వానికి జమ చేయబడిన / తిరిగి వాపసు చేయబడిన తేది: ________________________
11. డిపాజిట్ వాపసు తీసుకున్న వ్యక్తి వివరాలు: __________________________________________________
12. డిపాజిట్ వాపసు తీసుకున్న వ్యక్తి యొక్క రశీదు: __________________________________________________
13. ఎన్నికల అధికారి సంతకము: ________________________
14. రిమార్కులు: __________________________________________________

గమనిక: ఒకవేళ డిపాజిట్ మొత్తాన్ని ప్రభుత్వ ఖజానాలో గాని లేదా బ్యాంకు నందు గాని చెల్లించి నట్లయితే దాని యొక్క చలానా నెంబరు మరియు తేదిని పై గడి సంఖ్య 6 లో సూచించాలి."""
  },
  {
    "code": "Chk-Nomination",
    "rule": "Statutory Checklist",
    "title_en": "Nomination Verification Checklist (Original / Duplicate)",
    "title_te": "నామినేషన్ పత్రాల తనిఖీ నిమిత్తం చెక్ లిస్టు (ఒరిజినల్/డూప్లికేట్)",
    "desc_en": "Mandatory checklist for scrutinizing nominations, verifying Form 1-A symbols, Form-II caste verification, deposit payment, asset/criminal self-declaration, and expenditure declaration.",
    "desc_te": "నామినేషన్ల పరిశీలన చెక్‌లిస్టు. ఫారం 1-A గుర్తుల ఎంపిక, ఫారం-II కుల ధృవీకరణ, డిపాజిట్ రశీదు, ఆస్తులు/నేరచరిత్ర అఫిడవిట్, ఎన్నికల వ్యయ నిర్వహణ డిక్లరేషన్ తనిఖీ కోసం తప్పనిసరి.",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Pages 7 & 8)",
    "content_en": """NOMINATION VERIFICATION CHECKLIST
(Original / Duplicate)
[Original to be attached to Nomination Paper; Duplicate to be handed over to Candidate]

Candidate's Name: __________________________________________________________________
Ward Number & Name: Ward No. _______, _____________________________________________
Municipality: SRIKALAHASTI MUNICIPALITY
Contesting Office: [  ] Chairperson    [  ] Ward Member
Date & Time of Filing Nomination: Date: ________________________ Time: ________ AM/PM
Nomination Paper Serial Number: ________________________

VERIFICATION OF ATTACHED DOCUMENTS:
1. Is Declaration on Choice of Symbols in 'Form 1-A' attached?
   [  ] YES    [  ] NO    Deficiencies/Remarks: _________________________________________

2. For SC / ST / BC candidates, is Declaration in Form-II attested by Revenue Officer not below the rank of Deputy Tahsildar (OR) valid Caste Certificate issued by competent authority attached?
   [  ] YES    [  ] NO    [  ] NOT APPLICABLE (OC)    Deficiencies/Remarks: __________________

3. Has the Security Deposit been paid in accordance with the rules prescribed by State Election Commission?
   [  ] YES    [  ] NO    Receipt / Chalan No: ________________________ Amount: Rs. _________

4. Has Self-Declaration on Criminal Antecedents, Assets, Liabilities, and Educational Qualifications verified by signatures of two witnesses been submitted?
   (a) Are all columns completely filled? [  ] YES    [  ] NO
   (b) If not, details of incomplete columns: _____________________________________________

5. Has declaration undertaking to maintain day-to-day accounts of election expenditure before the Election Officer been submitted?
   [  ] YES    [  ] NO    Deficiencies/Remarks: _________________________________________

6. Has declaration of no disqualifications under AP Municipalities Act, 1965 been submitted?
   [  ] YES    [  ] NO    Deficiencies/Remarks: _________________________________________

--------------------------------------------------------------------------------
NOTICE OF DEFICIENT DOCUMENTS TO BE SUBMITTED BY CANDIDATE:
The following documents were not attached with the nomination paper and must be submitted:
(a) __________________________________________________ Must be submitted before: ___________
(b) __________________________________________________ Must be submitted before: ___________
(c) __________________________________________________ Must be submitted before: ___________

Received by: __________________________________________________
(Signature of Candidate)

Date & Time: ________________________                        Signature of Returning / Assistant
Place: _______________________________                       Returning Officer

MANDATORY STATUTORY NOTES:
1. All forms, documents, and certificates must be strictly filed before 3:00 PM on the last date of nominations.
2. The Self-Declaration on criminal history, assets, liabilities, and education, verified by two witnesses with all columns filled, must be filed before 3:00 PM on the last date of nominations.
3. Security deposit must be paid prior to or at the time of presenting nomination paper. No separate notice will be issued for non-payment of deposit.""",
    "content_te": """నామినేషన్ పత్రాలను తనిఖీ నిమిత్తం చెక్ లిస్టు
(Original / Duplicate)
(ఒరిజినల్ ప్రతి నామినేషన్ పత్రానికి జతపరచాలి. డూప్లికేట్ ప్రతి అభ్యర్థికి ఇవ్వవలసి ఉంటుంది.)

మున్సిపాలిటీలు/ నగర పంచాయితి వార్డు సభ్యుల ఎన్నికలు

అభ్యర్థి పేరు: __________________________________________________________________
ఎన్నిక జరుగు వార్డు నెంబరు మరియు పేరు: వార్డు నెం. _______, ______________________________
మున్సిపాలిటీ పేరు: శ్రీకాళహస్తి పురపాలక సంఘం
పోటీ చేయు పదవి పేరు: [  ] చైర్‌పర్సన్    [  ] వార్డు సభ్యుడు
నామినేషన్ పత్రము దాఖలు చేసిన తేది మరియు సమయము: తేదీ: ________________________ సమయం: ________
నామినేషన్ పత్రము క్రమ సంఖ్య: ________________________

తనిఖీ పట్టిక:
1. గుర్తుల (చిహ్నాల) ఎంపిక పై “ఫారం 1-A” లో చేయు ప్రకటన జత చేసినారా?
   [  ] అవును    [  ] కాదు    లోపాలు/వివరాలు: _________________________________________

2. యస్.సి. / యస్.టి. / బి.సి. అభ్యర్థులు ఫారం-II లో రెవెన్యూ శాఖకు చెందిన డిప్యూటీ తహశీల్దారు స్థాయికి తక్కువ కాని అధికారి సమక్షంలో చేసిన ప్రకటనను గాని (లేదా) అర్హత గల అధికారి ద్వారా జారీ చేయబడిన కుల ధృవీకరణ పత్రము జత చేసినారా?
   [  ] అవును    [  ] కాదు    [  ] వర్తించదు (OC)    లోపాలు/వివరాలు: __________________

3. రాష్ట్ర ఎన్నికల సంఘం నిర్దిష్టపరచిన విధంగా ధరావతుతో (డిపాజిట్) చెల్లించినారా ?
   [  ] అవును    [  ] కాదు    రశీదు / చలానా నెం: ________________________ మొత్తం: రూ. _________

4. అభ్యర్థి యొక్క నేర చరిత్ర, ఆస్తులు, అప్పులు, విద్యార్హతలకు సంబంధించి, ఇద్దరు సాక్షుల సంతకాలతో ధృవీకరించిన స్వీయ ప్రకటన చేసినారా?
   (a) అన్ని గడులు పూర్తి చేయబడినవా? [  ] అవును    [  ] కాదు
   (b) లేనిచో, అసంపూర్తిగా ఉన్న గడుల వివరాలు: _____________________________________________

5. ఎన్నికల ఖర్చుల ఖాతాను నిర్వహిస్తానని నిర్ధిత నమూనాలో అభ్యర్థి ఎలక్షన్ అధికారి సమక్షంలో చేసిన డిక్లరేషను దాఖలు చేసినారా?
   [  ] అవును    [  ] కాదు    లోపాలు/వివరాలు: _________________________________________

6. అనర్హతలకు సంబంధించి డిక్లరేషను చేసినారా?
   [  ] అవును    [  ] కాదు    లోపాలు/వివరాలు: _________________________________________

--------------------------------------------------------------------------------
నామినేషన్ పత్రముతో జతపరచని ఈ క్రింద తెలిపినటువంటి దాఖలు పరచవలసిన పత్రాలు:
(a) __________________________________________________ ఈ తేది లోగా సమర్పించవలెను: ___________
(b) __________________________________________________ ఈ తేది లోగా సమర్పించవలెను: ___________
(c) __________________________________________________ ఈ తేది లోగా సమర్పించవలెను: ___________

అందినది: __________________________________________________
(అభ్యర్థి సంతకము)

తేది & సమయము: ________________________                     ఎన్నికల / సహాయ ఎన్నికల అధికారి సంతకము
స్థలము: _______________________________

గమనిక:
1. అన్ని ఫారాలు, పత్రాలు మరియు సర్టిఫికెట్స్ మొదలైనవి నామినేషన్ చేయుటకు గల గడువు ఆఖరి తేదిన మధ్యాహ్నం 3.00 గంటల లోపు తప్పని సరిగా దాఖలు చేయాల్సి ఉంటుంది.
2. అభ్యర్థికి చెందిన నేర చరిత్ర, ఆస్తులు, రుణాలు (అప్పులు) విద్యార్హతలకు సంబంధించి, ఇద్దరు సాక్షుల ద్వారా ధృవీకరించి మరియు అన్ని గడులను పూరించినట్టి స్వీయ ప్రకటన నామినేషన్ చేయుటకు గల గడువు ఆఖరి తేదిని మధ్యాహ్నం 3.00 గంటల లోపు తప్పని సరిగా దాఖలు చేయాల్సి ఉంటుంది.
3. అభ్యర్థి చెల్లించవలసిన ఎన్నికల డిపాజిట్ మొత్తాన్ని నామినేషన్ దాఖలు పరిచే ముందు గాని లేదా నామినేషన్ పత్రము దాఖలు పరిచే సమయము నందు గాని చెల్లించాలి, కనుక, డిపాజిట్ చెల్లించ లేదని నోటీసు ఇవ్వవలసిన అవసరము లేదు."""
  },
  {
    "code": "Affidavit-SEC191",
    "rule": "SEC Order 191/2026",
    "title_en": "Self-Declaration Affidavit: Assets, Liabilities & Criminal Background",
    "title_te": "స్వీయ ప్రకటన పత్రం / అఫిడవిట్: ఆస్తులు, అప్పులు & నేర చరిత్ర",
    "desc_en": "Mandatory 7-page Self-Declaration under SEC Order No. 191/SEC-F2/2026. Covers PAN, IT returns, court cases, movable & immovable assets, loans & govt dues, education, and 2-witness verification.",
    "desc_te": "రాష్ట్ర ఎన్నికల సంఘం ఉత్తరువు నెం. 191/ఎస్.ఇ.సి-ఎఫ్2/2026 ప్రకారం నామినేషన్‌తో దాఖలు చేయవలసిన సమగ్ర 7 పుటల స్వీయ ప్రకటన పత్రం. పాన్, ఆదాయపు పన్ను, కేసులు, చర-స్థిరాస్తులు, అప్పులు, విద్యార్హతలు మరియు ఇద్దరు సాక్షుల రూఢి ప్రకటన.",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Pages 9 to 15)",
    "content_en": """SELF-DECLARATION AFFIDAVIT BY CANDIDATE
[Annexure to SEC Order No. 191/SEC-F2/2026, Dated: 26-03-2026]
(To be submitted along with Nomination Paper, attested by Two Witnesses)

Election to Ward Member of Ward No. ________ / Chairperson of SRIKALAHASTI Municipality

I, ____________________________________________________, Son/Daughter/Wife of ____________________________________________________,
Aged: ________ years, Resident of: ____________________________________________________________________________________
(give full postal address), a candidate at the above election, do hereby solemnly affirm and declare as under:

1. I am a candidate set up by __________________________________ Party / contesting as an Independent candidate.

2. DETAILS OF PAN AND STATUS OF FILING OF INCOME TAX RETURNS:
   Sl | Name                  | PAN No.    | Last FY for which ITR filed | Total Income shown in ITR (Rs.)
   ---+-----------------------+------------+-----------------------------+--------------------------------
   1. | Candidate:            |            |                             |
   2. | Spouse:               |            |                             |
   3. | Dependent-1:          |            |                             |
   4. | Dependent-2:          |            |                             |
   5. | Dependent-3:          |            |                             |

3. DETAILS OF PENDING CRIMINAL CASES IN WHICH COGNIZANCE HAS BEEN TAKEN BY COURT:
   Sl | Case Details, Sections & Act | Court Name, Case No & Date of Cognizance | Details of Appeal/Revision filed
   ---+------------------------------+------------------------------------------+---------------------------------
   1. |                              |                                          |

4. DETAILS OF CONVICTIONS BY A COURT OF LAW AND SENTENCE IMPOSED:
   Sl | Offence Description & Section | Court Name, Case No & Date of Order | Punishment / Sentence Imposed
   ---+-------------------------------+-------------------------------------+------------------------------
   1. |                               |                                     |

5. DETAILS OF ASSETS (MOVABLE AND IMMOVABLE) OF MYSELF, SPOUSE AND DEPENDENTS:
   (A) MOVABLE ASSETS:
   (i) Cash in hand
   (ii) Bank accounts & deposits (FDRs, Term Deposits, Savings)
   (iii) Investments in Bonds, Debentures, Shares, Mutual Funds
   (iv) NSS, Postal Savings, Insurance Policies
   (v) Personal loans / advances given
   (vi) Motor Vehicles, Aircrafts, Yachts/Boats (Make, Regn No, Year, Value)
   (vii) Jewellery, Bullion, Valuables (Weight, Value)
   (viii) Other claims / interests
   (ix) Gross Total Value (Rs.)

   (B) IMMOVABLE ASSETS:
   (i) Agricultural Land (Location, Survey No, Extent in Acres, Inherited/Self-Acquired, Purchase Cost, Current Market Value)
   (ii) Non-Agricultural Land
   (iii) Commercial Buildings (Built-up area in sq. ft., Current Market Value)
   (iv) Residential Buildings (Built-up area in sq. ft., Current Market Value)
   (v) Total Current Market Value (Rs.)

6. DETAILS OF LIABILITIES AND DUES TO PUBLIC FINANCIAL INSTITUTIONS AND GOVERNMENT:
   (i) Loans from Banks / Financial Institutions
   (ii) Loans from Individuals / Entities
   (iii) Government Dues:
        - Dues to departments dealing with Govt accommodation
        - Dues to departments dealing with water supply
        - Dues to departments dealing with electricity
        - Dues to departments dealing with telephones / mobiles
        - Dues to departments dealing with transport (including aircrafts/helicopters)
        - Income Tax dues, Wealth Tax, Service Tax, Municipal Property Tax, Sales Tax
        - Grand Total of all Government Dues (Rs.)

7. OCCUPATION / PROFESSION:
   (a) Candidate: __________________________________________________
   (b) Spouse: _____________________________________________________

8. EDUCATIONAL QUALIFICATIONS:
   (Highest educational certificate/diploma/degree, School/College/University, Year of completion)
   Sl | Qualification Degree/Course | School / College / University | Year Completed | Remarks
   ---+---------------------------+-------------------------------+----------------+--------
   1. |                           |                               |                |

--------------------------------------------------------------------------------
VERIFICATION (రూఢి ప్రకటన)
I, the deponent above named, do hereby verify and declare that the contents of this declaration are true and correct to the best of my knowledge and belief, that no part of it is false and nothing material has been concealed therefrom.

Verified at ________________________ on this the ________ day of ________________________, 2026.

                                                             Signature of Deponent / Candidate

WITNESSES (Name, Address & Signature):
1. Signature: _______________________ Name: ________________________________ Address: ___________________________
2. Signature: _______________________ Name: ________________________________ Address: ___________________________""",
    "content_te": """స్వీయ ప్రకటన పత్రం (AFFIDAVIT)
(26-03-2026 తేది గల ఉత్తరువు నెం. 191/యస్.ఇ.సి-ఎఫ్2/2026 యొక్క అనుబంధం)
(మున్సిపాలిటీ వార్డు సభ్యుల / చైర్‌పర్సన్ ఎన్నికల్లో పోటీచేయు అభ్యర్థి తన నామినేషన్ పత్రంతో పాటుగా ఎలెక్షన్ అధికారికి సమర్పించవలసిన, ఇద్దరు సాక్షుల సంతకాలతో కూడిన, స్వీయ ప్రకటన పత్రం)

శ్రీకాళహస్తి మున్సిపాలిటీ లోని వార్డు నెం. _______ వార్డు సభ్యుని / చైర్‌పర్సన్ పదవికి ఎన్నిక.

నేను ____________________________________________________, తండ్రి / భర్త పేరు: ____________________________________________________,
వయస్సు: _______ సంవత్సరాలు, చిరునామా: ____________________________________________________________________________________
(పూర్తి తపాలా చిరునామాను పేర్కొనండి), పైన తెలిపిన ఎన్నికలో ఒక అభ్యర్థిగా రూఢిగా ధృవీకరించి మరియు ప్రమాణపూర్వకంగా ఈక్రింది సమాచారాన్ని తెలియజేయుచున్నాను.

1) నేను __________________________________ పార్టీ అభ్యర్థిగా పోటీ చేయుచున్నాను / నేను స్వతంత్ర అభ్యర్థిగా పోటీ చేయుచున్నాను.

2) పాన్ నంబరు (Permanent Account Number) వివరాలు మరియు ఆదాయపు పన్ను రిటర్నుల ఫైలింగ్ వివరాలు:
   క్ర.సం | పేర్లు               | శాశ్వత ఖాతా నంబరు (PAN) | ఐటీ రిటర్న్ దాఖలు చేసిన ఆఖరి ఆర్థిక సంవత్సరం | ఐటీ రిటర్నులలో చూపిన మొత్తం ఆదాయం (రూ.)
   ------+---------------------+-----------------------+------------------------------------------+---------------------------------------
   1.    | అభ్యర్థి పేరు:       |                       |                                          |
   2.    | భార్య / భర్త పేరు:   |                       |                                          |
   3.    | ఆధారపడిన వ్యక్తి-1: |                       |                                          |
   4.    | ఆధారపడిన వ్యక్తి-2: |                       |                                          |
   5.    | ఆధారపడిన వ్యక్తి-3: |                       |                                          |

3) నాపై కోర్టు చేపట్టిన విచారణలో గల కేసు(లు) మరియు పెండింగులో ఉన్న కేసులు:
   క్ర.సం | కేసుల వివరాలు, చట్టంలోని విభాగాలు, నేరం వివరణ | కోర్టు పేరు, కేసు నంబరు మరియు విచారణకు స్వీకరించిన తేది | ఉత్తర్వులపై అప్పీలు/రివిజన్ వివరాలు
   ------+--------------------------------------------+------------------------------------------------------+---------------------------------
   1.    |                                            |                                                      |

4) కోర్టు ద్వారా శిక్ష పడినటువంటి నాపై గల కేసుల వివరాలు:
   క్ర.సం | నేర విచారణ, చట్టంలోని విభాగాలు | కోర్టు పేరు, కేసు నంబరు, ఉత్తరువు తేది | విధించబడినటువంటి శిక్ష
   ------+--------------------------------+-------------------------------------+----------------------
   1.    |                                |                                     |

5) నాకు, నా భాగస్వామికి, నాపై ఆధారపడిన వారి ఆస్తులకు (చర, స్థిర మున్నగునవి) సంబంధించిన వివరాలు:
   (ఎ) చరాస్తుల వివరాలు:
   (i) చేతిలో వున్న నగదు (రూపాయలలో)
   (ii) బ్యాంకులలో జమచేసిన ఖాతాల వివరాలు (FDRs, టర్మ్ డిపాజిట్లు, సేవింగ్ ఖాతాలు)
   (iii) బాండ్లలో, డిబెంచర్లలో ఉన్న పెట్టుబడి వివరాలు / షేర్లు మరియు మ్యూచువల్ ఫండ్స్
   (iv) NSS, పోస్టల్ సేవింగ్స్, ఇన్సూరెన్స్ పాలసీలు
   (v) వ్యక్తిగత రుణాలుగా / అడ్వాన్సుగా ఇచ్చినటువంటి మొత్తం సొమ్ము
   (vi) మోటారు వాహనాలు / విమానాలు / పడవలు (తయారీ, రిజిస్ట్రేషన్ నెం, కొనుగోలు సంవత్సరం, విలువ)
   (vii) నగలు, బులియన్, ఇతర విలువైన వస్తువులు (బరువు, విలువ)
   (viii) క్లయింలు / వడ్డీలు గల ఇతర విలువైన ఆస్తులు
   (ix) స్థూల విలువ మొత్తం (రూ||లలో) (i-viii)

   (బి) స్థిరాస్తుల వివరాలు:
   (i) వ్యవసాయ భూమి (ప్రాంతము, సర్వే నెం, విస్తీర్ణం ఎకరాలలో, వారసత్వ/స్వయం సంపాదన, ప్రస్తుత మార్కెట్ విలువ)
   (ii) వ్యవసాయేతర భూమి (ప్రాంతము, సర్వే నెం, విస్తీర్ణం, కొనుగోలు తేదీ, మార్కెట్ విలువ)
   (iii) వాణిజ్యపరమైన భవనాలు (అపార్టుమెంట్లు, విస్తీర్ణం Built up area, ప్రస్తుత మార్కెట్ విలువ)
   (iv) నివాసిత భవనాలు (విస్తీర్ణం Built up area, ప్రస్తుత మార్కెట్ విలువ)
   (v) ఇతర ఆస్తుల వివరాలు
   (vi) మొత్తం ఆస్తుల ప్రస్తుత మార్కెట్ విలువ మొత్తం (రూ.)

6) వివిధ ప్రభుత్వ ఆర్థిక సంస్థలు, ప్రభుత్వము నుండి తీసుకున్న అప్పులు / బకాయిల వివరాలు:
   (i) బ్యాంకులు / ఆర్థిక సంస్థలకు ఉన్న బాకీలు
   (ii) ఇతర వ్యక్తులకు / సంస్థలకు రుణపడి ఉన్న వివరాలు
   (iii) ప్రభుత్వ బకాయిలు:
        - గృహ వసతి కల్పనకు గాను ప్రభుత్వ శాఖలకు చెల్లించవలసిన బకాయిలు
        - నీటి సరఫరాతో సంబంధమున్న శాఖలకు బకాయిలు
        - విద్యుత్తు సరఫరాతో సంబంధమున్న శాఖలకు బకాయిలు
        - టెలిఫోనులు / మొబైల్ ఫోన్ల సేవల బకాయిలు
        - ప్రభుత్వ రవాణా శాఖకు చెల్లించవలసిన బకాయిలు (విమానాలు, హెలికాప్టర్లతో సహా)
        - ఆదాయ పన్ను, ఆస్తి పన్ను, సర్వీసు పన్ను, మునిసిపల్ పన్ను, అమ్మకం పన్ను బకాయిలు
        - అన్ని ప్రభుత్వ శాఖలకు చెల్లించవలసిన బకాయిలు వెరసి మొత్తం (రూ.)

7) వృత్తి లేదా వ్యాపార వివరాలు:
   ఎ) వ్యక్తిగతంగా: __________________________________________________
   బి) భార్య / భర్త: __________________________________________________

8) నా విద్యార్హతలు ఈ క్రింద విధంగా ఉన్నాయి:
   (సర్టిఫికెట్ / డిప్లొమా / డిగ్రీ, పాఠశాల / కళాశాల / విశ్వవిద్యాలయం, పూర్తి చేసిన సంవత్సరం)
   క్ర.సం | సర్టిఫికెట్ / డిగ్రీ వివరాలు | చదివిన పాఠశాల / కళాశాల / విశ్వవిద్యాలయం పేరు | కోర్సు పూర్తి చేసిన సంవత్సరం | రిమార్కులు
   ------+----------------------------+-------------------------------------------+----------------------------+----------
   1.    |                            |                                           |                            |

--------------------------------------------------------------------------------
రూఢి ప్రకటన
పైన స్వీయ ప్రకటన ద్వారా తెలిపిన వివరాలు నాకు తెలిసినంత మేరకు మరియు నేను విశ్వసించినంత మేరకు వాస్తవమైనవి మరియు సరైనవని, ఇందులో ఏ భాగం అవాస్తవం కాదని, దాని నుండి ఏదియూ రహస్యంగా ఉంచబడలేదని ఇందుమూలముగా ప్రకటిస్తున్నాను.

ఈ ప్రకటన ________________________ తేదిన చేయడమైనది.

                                                             రూఢి ప్రకటన చేయు వ్యక్తి సంతకం

సాక్షులు (సంతకం, పేరు మరియు చిరునామా):
1. సంతకం: _______________________ పేరు: ________________________________ చిరునామా: ___________________________
2. సంతకం: _______________________ పేరు: ________________________________ చిరునామా: ___________________________

గమనిక:
1. ఇద్దరు సాక్షుల సంతకాలతో కూడిన స్వీయ ప్రకటనను (Self-Declaration) అభ్యర్థి తన నామినేషన్ పత్రంతో పాటుగా దాఖలు చేయవలసి ఉంటుంది. నామినేషన్లు దాఖలు చేసేందుకు గల ఆఖరి తేదీన మధ్యాహ్నం 3 గంటల లోపు తప్పనిసరిగా స్వీయ ప్రకటనను దాఖలు చేయవలసి ఉంటుంది.
2. స్వీయ ప్రకటన పత్రంలో అన్ని గడులను పూరించాలి. ఏ గడిని ఖాళీగా వదలి వేయరాదు. సమాచారం లేనిచో 'ఏమీ లేదు' లేదా 'వర్తించదు' అని తెలియజేయాలి."""
  },
  {
    "code": "Dec-NoDisqual",
    "rule": "Sec 13-16, APM Act",
    "title_en": "Declaration of No Disqualification (AP Municipalities Act, 1965)",
    "title_te": "పోటీ చేయుటకు అనర్హతలు లేవని తెలియజేసే డిక్లరేషను",
    "desc_en": "Solemn declaration by contesting candidate affirming that they suffer from no disqualifications under Section 13-A, 13-B, 14, 15, or 16 of the AP Municipalities Act, 1965.",
    "desc_te": "1965 ఆంధ్రప్రదేశ్ మున్సిపాలిటీల చట్టం నిబంధనల క్రింద మున్సిపాలిటీ చైర్‌పర్సన్ లేదా వార్డు సభ్యునిగా ఎన్నికవడానికి తనకు ఎలాంటి చట్టపరమైన అనర్హతలు లేవని అభ్యర్థి ఇచ్చే డిక్లరేషన్.",
    "category": "Nomination",
    "category_te": "నామినేషన్",
    "authority": "Election-Officers-Forms.pdf (Page 16)",
    "content_en": """DECLARATION OF NO DISQUALIFICATION
[To be filed by the candidate along with Nomination Papers]
(Under provisions of the Andhra Pradesh Municipalities Act, 1965)

I, ____________________________________________________, Son/Daughter/Wife of ____________________________________________________,
Resident of: ____________________________________________________________________________________,
do hereby solemnly declare that to the best of my knowledge and belief, I am not disqualified for being chosen as a Chairperson / Member of SRIKALAHASTI Municipality under any of the provisions of the Andhra Pradesh Municipalities Act, 1965 (Act No. 6 of 1965), including:

1. I am an elector of Srikalahasti Municipality and have completed 21 years of age.
2. I am not of unsound mind and not an undischarged insolvent.
3. I am not an employee of the Central or State Government or any Local Authority or statutory corporation.
4. I am not in arrears of any kind due by me to the Srikalahasti Municipality.
5. I have not been disqualified for corrupt election practices or sentenced for any penal offences.

Date: ________________________                               Signature of Candidate

--------------------------------------------------------------------------------
ATTESTATION
Signed in my presence on this the ________ day of ________________________, 2026.

Date: ________________________                               Signature of Returning Officer / Authorized Person
                                                             Designation: __________________________""",
    "content_te": """డిక్లరేషన్
(పోటీ చేయుటకు అనర్హతలు లేవని తెలియజేసే డిక్లరేషను)
(నామినేషను పత్రాలతో పాటు పోటీ చేయు అభ్యర్థి దాఖలు చేయవలసి ఉండును)

____________________________________________________ గారి కుమారుడనైన / కుమార్తెనైన / భార్యనైన ____________________________________________________ అను నేను, 1965 ఆంధ్రప్రదేశ్ మున్సిపాలిటీల చట్టం నిబంధనల క్రింద, శ్రీకాళహస్తి మున్సిపాలిటీ యొక్క చైర్‌పర్సన్ / వార్డు సభ్యునిగా ఎంపిక చేసుకొనబడుటకు నాకు తెలిసినంతవరకు మరియు నా విశ్వాసం మేరకు నేను అనర్హుడను కానని ఇందుమూలంగా ప్రకటించుచున్నాను:

1. నేను శ్రీకాళహస్తి పురపాలక సంఘంలో ఓటరుగా నమోదై ఉన్నాను మరియు 21 సంవత్సరముల వయస్సు పూర్తి చేసుకున్నాను.
2. నేను మతిస్థిమితం లేని వ్యక్తిని కాను మరియు దివాళా తీసిన వ్యక్తిని కాను.
3. నేను కేంద్ర, రాష్ట్ర ప్రభుత్వాలలో గాని, లేదా స్థానిక సంస్థలలో గాని ఎటువంటి లాభదాయక పదవిలో లేను.
4. నేను శ్రీకాళహస్తి మునిసిపాలిటీకి ఎటువంటి పన్నులు లేదా బకాయిలు చెల్లించవలసి లేను.
5. నేను ఎన్నికల అక్రమ పద్ధతుల వల్ల గాని లేదా క్రిమినల్ నేరాల శిక్ష వల్ల గాని అనర్హత పొందలేదని ప్రమాణపూర్వకంగా తెలియజేస్తున్నాను.

తేదీ: ________________________                               అభ్యర్థి సంతకం

--------------------------------------------------------------------------------
తేది: ________________________ నెల 2026 సంవత్సరం నాడు నా సమక్షంలో సంతకం చేయడం జరిగింది.

తేదీ: ________________________                               ఎన్నికల అధికారి సంతకము
                                                             హోదా: __________________________"""
  },
  {
    "code": "Dec-ExpLimit",
    "rule": "SEC Order 197 & 177",
    "title_en": "Declaration of Election Expenditure Limits & Daily Accounting",
    "title_te": "ఎన్నికల ఖర్చుల లెక్కల నిర్వహణపై అభ్యర్థి దాఖలు చేయవలసిన డిక్లరేషను",
    "desc_en": "Candidate undertaking affirming receipt of SEC Order No. 197/SEC-F2/2026 & Notification No. 177/SEC-F1/2026, promising to maintain day-to-day accounts within statutory ceilings (₹20L Chairperson / ₹7.5L Member).",
    "desc_te": "రాష్ట్ర ఎన్నికల సంఘం ఉత్తరువు నెం. 197 & 177/2026 నిబంధనల ప్రకారం చట్టబద్ధ పరిమితి లోపు (చైర్‌పర్సన్: ₹20 లక్షలు, వార్డు సభ్యులు: ₹7.50 లక్షలు) రోజువారీ ఖర్చుల ఖాతాలను క్రమం తప్పక నిర్వహిస్తానని అభ్యర్థి ఇచ్చే డిక్లరేషన్.",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 17)",
    "content_en": """DECLARATION ON MAINTENANCE OF ELECTION EXPENDITURE ACCOUNTS
[SEC Order No. 197/SEC-F2/2026 & Notification No. 177/SEC-F1/2026]

I, ____________________________________________________, Son/Daughter/Wife of ____________________________________________________,
Resident of: ____________________________________________________________________________________,
having filed nomination as a candidate for the office of Chairperson / Ward Member of Ward No. ________ of SRIKALAHASTI Municipality, do hereby declare that:

1. I have received a copy of the State Election Commission Order No. 197/SEC-F2/2026, Dated: 26.03.2026 regarding maintenance of election accounts, and Notification No. 177/SEC-F1/2026, Dated: 26.03.2026 intimating the maximum expenditure ceiling (Rs. 20,00,000/- for Chairperson / Rs. 7,50,000/- for Ward Member).

2. I solemnly affirm that I shall maintain day-to-day accounts of all expenditure incurred or authorized by me or by my election agent, in the prescribed registers (Proforma I, II, III).

3. I shall produce the expenditure register for inspection before the Election Officer, Expenditure Observer, or designated team whenever summoned, and lodge the final true account within 45 days of the declaration of election results.

4. I declare that I have fully acquainted myself with all statutory provisions under the AP Municipalities Act, 1965 and Conduct of Election Rules, 2026, and shall strictly abide by all democratic norms.

Date: ________________________                               Signature of Contesting Candidate

--------------------------------------------------------------------------------
Signed in my presence on this ________ day of ________________________, 2026.

Date: ________________________                               Signature of Election Officer
                                                             Seal & Designation: __________________________""",
    "content_te": """ఎన్నికల ఖర్చుల లెక్కల నిర్వహణపై అభ్యర్థి దాఖలు చేయవలసిన డిక్లరేషను

శ్రీకాళహస్తి మున్సిపాలిటీ / నగర పంచాయతీ యొక్క చైర్‌పర్సన్ / వార్డు నెం. _______ వార్డు సభ్యుని పదవికి నామినేషన్ పత్రం దాఖలు చేసిన నాకు, అనగా ____________________________________________________, తండ్రి / భర్త: ____________________________________________________, నివాసము: ____________________________________________________________________________________

ఎన్నిక వ్యయ ఖాతాల నిర్వహణకు సంబంధించిన రాష్ట్ర ఎన్నికల సంఘం ఉత్తరువు నెం.197/ఎస్.ఇ.సి.-ఎఫ్2/2026, తేది:26.03.2026 ప్రతిని మరియు సదరు పదవులకు పోటీ చేస్తున్న అభ్యర్థులు ఖర్చు పెట్టదగిన గరిష్ట పరిమితిని తెలియజేసే ప్రకటన నెం. 177/ఎస్.ఇ.సి.-ఎఫ్1/2026, తేది.26.03.2026 (చైర్‌పర్సన్: రూ. 20.00 లక్షలు / వార్డు సభ్యుడు: రూ. 7.50 లక్షలు) అందచేశారని, ఇందుమూలంగా తెలియచేస్తున్నాను.

నిర్ణయించిన పరిమితి లోపల ఎన్నిక వ్యయాన్ని ఉంచుతానని, వాటిని వాస్తవంగా నిర్వహిస్తానని, రోజువారి వ్యయం తాలూకు లెక్కలను నిర్ణీత నమూనాలో నిర్ణీత సమయంలో తెలియ చేస్తానని, ఇందు మూలంగా ప్రకటిస్తున్నాను.

ఆంధ్ర ప్రదేశ్ మున్సిపాలిటీ / నగర పంచాయతీ చట్టం -1965 మరియు దాని క్రింద జారీచేసిన నియమాలలో పొందుపరచిన న్యాయ నిబంధనలను నేను పూర్తిగా తెలుసుకున్నానని మరియు చట్టంలోని ఈ నిబంధనలతో మరియు దాని ప్రకారము చేసిన నియమాలను అనుసరించి నడుచుకుంటానని మరియు పైన తెలిపిన ఎన్నికలో పోటీ చేయు అభ్యర్థిగా పూర్తి ప్రజాస్వామ్యబద్ధంగా నడుచుకుంటానని నేను ఇందుమూలంగా ప్రకటిస్తున్నాను.

తేదీ: ________________________                               పోటీ చేస్తున్న అభ్యర్థి సంతకం.

--------------------------------------------------------------------------------
నా సమక్షంలో పై డిక్లరేషను పై సంతకం చేయడమైనది.

తేదీ: ________________________                               ఎన్నికల అధికారి సంతకము
                                                             ముద్ర & హోదా: __________________________"""
  },
  {
    "code": "Proforma-I",
    "rule": "SEC Exp Guidelines",
    "title_en": "Proforma - I: Election Expenditure Register Cover Page",
    "title_te": "ప్రోఫార్మా - I: అభ్యర్థుల ఎన్నికల వ్యయ ఖాతా నిర్వహణ రిజిస్టరు కవరు పేజి",
    "desc_en": "Mandatory cover page of the daily election expenditure register provided to every contesting candidate to record identity, office, dates, and final total expenditure.",
    "desc_te": "పోటీ చేయు అభ్యర్థులకు అందజేసే ఎన్నికల వ్యయ ఖాతా రిజిస్టరు కవరు పేజీ. అభ్యర్థి పేరు, వార్డు, నామినేషన్ తేదీ, ఫలితాల తేదీ మరియు మొత్తం వ్యయం వివరాలను నమోదు చేయడానికి.",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 18)",
    "content_en": """PROFORMA - I (COVER PAGE)
MUNICIPAL ORDINARY ELECTIONS - 2026
REGISTER FOR MAINTENANCE OF DAY-TO-DAY ACCOUNTS OF ELECTION EXPENDITURE BY CONTESTING CANDIDATES

(a) Name of the Election (Ordinary / Casual) & Year: Ordinary Municipal Elections, 2026
(b) Name of Contesting Candidate: __________________________________________________________________
(c) Serial Number of the Candidate in the List of Contesting Candidates: ________________________
(d) Office Contested:
    [  ] Chairperson, Srikalahasti Municipality
    [  ] Ward Member, Ward No. ________ of Srikalahasti Municipality
(e) Date of Nomination: ________________________
(f) Date of Declaration of Result: ________________________
(g) Total Election Expenditure Incurred / Authorized: Rs. ________________________
    (in words: Rupees __________________________________________________________________________)

Date: ________________________                               Signature of Contesting Candidate

*Strike out whichever is not applicable.""",
    "content_te": """ప్రోఫార్మా - I (కవరు పేజి)
మున్సిపాలిటీ / నగర పంచాయితి వార్డు మెంబర్ల ఎన్నికలు – 2026
పోటీ చేయు అభ్యర్థుల ఎన్నికల వ్యయముల ఖాతా నిర్వహణ రిజిస్టరు

(a) ఎన్నిక పేరు (సాధారణ / ఆకస్మిక) మరియు సంవత్సరము: సాధారణ పురపాలక ఎన్నికలు, 2026
(b) పోటీ చేయు అభ్యర్థి పేరు: __________________________________________________________________
(c) పోటీ చేయు అభ్యర్థుల జాబితాలో సదరు అభ్యర్థి క్రమ సంఖ్య: ________________________
(d) పోటీ చేయుచున్న పదవి *:
    [  ] చైర్‌పర్సన్, శ్రీకాళహస్తి పురపాలక సంఘం
    [  ] వార్డు సభ్యుడు, వార్డు నెం. ________, శ్రీకాళహస్తి మున్సిపాలిటీ
(e) నామినేషను తేదీ: ________________________
(f) ఫలితాల తేదీ: ________________________
(g) ఎన్నికలలో అభ్యర్థి చేసిన మొత్తం వ్యయం (ఖర్చు): రూ. ________________________
    (అక్షరాలలో: రూపాయలు __________________________________________________________________________)

తేదీ: ________________________                               పోటీ చేయు అభ్యర్థి సంతకం

* వర్తించని వాటిని కొట్టివేయండి."""
  },
  {
    "code": "Proforma-II",
    "rule": "SEC Exp Guidelines",
    "title_en": "Proforma - II: Day-to-Day Expenditure Register Index",
    "title_te": "ప్రోఫార్మా - II: విషయ సూచిక (దినసరి వ్యయము తనిఖీ రిజిస్టరు)",
    "desc_en": "Statutory 6-column index of daily expenses, tracking voucher counts, daily expenditure totals, election officer/observer inspections, and page references in Proforma-III.",
    "desc_te": "దినసరి ఎన్నికల వ్యయాల 6 కాలమ్‌ల విషయ సూచిక. రోజువారీ వోచర్ల సంఖ్య, రోజువారీ ఖర్చు మొత్తం, ఎన్నికల పరిశీలకుల తనిఖీ మరియు ప్రోఫార్మా-III పేజీ నంబర్ల నమోదు కోసం.",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 19)",
    "content_en": """PROFORMA - II (INDEX SHEET)
INDEX OF DAY-TO-DAY EXPENDITURE REGISTER

Name of Contesting Candidate: __________________________________________________
Office Contested: Chairperson / Ward Member (Ward No. _______)

Sl | Date       | No. of Expense Vouchers on this date | Total Daily Expenditure Incurred (Rs.) | Inspected by Election Officer / Observer? (Yes / No) | Page Nos. in Proforma-III showing expenses
---+------------+-------------------------------------+----------------------------------------+------------------------------------------------------+-------------------------------------------
1  | 2          | 3                                   | 4                                      | 5                                                    | 6
---+------------+-------------------------------------+----------------------------------------+------------------------------------------------------+-------------------------------------------
1. |            |                                     |                                        |                                                      |
2. |            |                                     |                                        |                                                      |
3. |            |                                     |                                        |                                                      |
4. |            |                                     |                                        |                                                      |
5. |            |                                     |                                        |                                                      |
6. |            |                                     |                                        |                                                      |
7. |            |                                     |                                        |                                                      |
8. |            |                                     |                                        |                                                      |
9. |            |                                     |                                        |                                                      |
10 |            |                                     |                                        |                                                      |

Total Cumulative Expenditure to Date: Rs. ________________________

Date: ________________________                               Signature of Contesting Candidate""",
    "content_te": """ప్రోఫార్మా — II (విషయ సూచిక)

పోటీ చేయు అభ్యర్థి పేరు: __________________________________________________
పోటీ చేయు పదవి: చైర్‌పర్సన్ / వార్డు సభ్యుడు (వార్డు నెం. _______)

క్ర.సం. | తేది       | ఈ తేది నాటి ఖర్చు పద్దుల సంఖ్య | ఈ తేది నాడు చేసిన మొత్తం వ్యయము (రూ.లలో) | ఈ తేది నాడు ఎన్నికల అధికారి / పరిశీలకుని చేత తనిఖీ చేయబడినదా? లేదా? (అవును/ కాదు) | ప్రోఫార్మా-III లో ఈ తేది నాటి వ్యయము చూపించు పుటల (పేజీల) సంఖ్యలు
-------+------------+-------------------------------+---------------------------------------+------------------------------------------------------------------------------------+------------------------------------------------------------------
1      | 2          | 3                             | 4                                     | 5                                                                                  | 6
-------+------------+-------------------------------+---------------------------------------+------------------------------------------------------------------------------------+------------------------------------------------------------------
1.     |            |                               |                                       |                                                                                    |
2.     |            |                               |                                       |                                                                                    |
3.     |            |                               |                                       |                                                                                    |
4.     |            |                               |                                       |                                                                                    |
5.     |            |                               |                                       |                                                                                    |
6.     |            |                               |                                       |                                                                                    |
7.     |            |                               |                                       |                                                                                    |
8.     |            |                               |                                       |                                                                                    |
9.     |            |                               |                                       |                                                                                    |
10.    |            |                               |                                       |                                                                                    |

ఈ నాటికి అయిన మొత్తం ఎన్నికల వ్యయం: రూ. ________________________

తేదీ: ________________________                               పోటీ చేయు అభ్యర్థి సంతకం"""
  },
  {
    "code": "Proforma-III",
    "rule": "SEC Exp Guidelines",
    "title_en": "Proforma - III: Daily Itemized Expenditure Account",
    "title_te": "ప్రోఫార్మా - III: పద్దుల వారి ఎన్నికల వ్యయ వివరాలు (ప్రధాన పేజీలు)",
    "desc_en": "7-column itemized daily expenditure sheet with candidate legal verification. Itemizes nature, quantity, unit cost, voucher numbers, authorized spenders, and remarks.",
    "desc_te": "పద్దుల వారీ దినసరి ఎన్నికల వ్యయ వివరాల 7 కాలమ్‌ల ప్రధాన పట్టిక. వస్తువుల వివరాలు, పరిమాణం, ఖర్చు మొత్తం, ఓచర్ల సంఖ్య, వ్యయం చేసిన వారి వివరాలు మరియు అభ్యర్థి డిక్లరేషన్.",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 20)",
    "content_en": """PROFORMA - III (MAIN ACCOUNT SHEETS)
ITEMIZED ACCOUNT OF DAILY ELECTION EXPENDITURE

Name of Contesting Candidate: __________________________________________________ Page Number: _________
Office Contested: Chairperson / Ward Member (Ward No. _______)

Sl | Date       | Nature & Description of Expenditure (Quantity, Units, etc.) | Amount Incurred (Rs.) | Voucher / Bill Serial Number | Incurred / Authorized By: Candidate / Agent / Party / Others* | Remarks
---+------------+-------------------------------------------------------------+-----------------------+------------------------------+---------------------------------------------------------------+--------
1  | 2          | 3                                                           | 4                     | 5                            | 6                                                             | 7
---+------------+-------------------------------------------------------------+-----------------------+------------------------------+---------------------------------------------------------------+--------
1. |            |                                                             |                       |                              |                                                               |
2. |            |                                                             |                       |                              |                                                               |
3. |            |                                                             |                       |                              |                                                               |
4. |            |                                                             |                       |                              |                                                               |
5. |            |                                                             |                       |                              |                                                               |
6. |            |                                                             |                       |                              |                                                               |
7. |            |                                                             |                       |                              |                                                               |
8. |            |                                                             |                       |                              |                                                               |

* Candidate / Election Agent / Political Party / Others

DECLARATION:
I do hereby solemnly certify that the information given above is true and correct to the best of my knowledge and belief.

Date: ________________________                               Signature of Contesting Candidate""",
    "content_te": """ప్రోఫార్మా — III (ప్రధాన పేజీలు)
పద్దుల వారి ఎన్నికల వ్యయ వివరాలు

పోటీ చేయు అభ్యర్థి పేరు: __________________________________________________ పేజి నెంబరు: _________
పోటీ చేయు పదవి: చైర్‌పర్సన్ / వార్డు సభ్యుడు (వార్డు నెం. _______)

క్ర.సం. | తేది       | ఖర్చు పద్దు మరియు దాని వివరములు (పరిమాణం, సంఖ్య మొదలగునవి) | పద్దు వారి చేసిన వ్యయము (రూ.లలో) | ఓచరు/ బిల్లు యొక్క క్రమ సంఖ్య | వ్యయము(ఖర్చు) చేసిన వారు: అభ్యర్థి / ఎన్నికల ఏజెంటు / పార్టీ / ఇతరులు * | రిమార్కులు
-------+------------+---------------------------------------------------------+---------------------------------+------------------------------+------------------------------------------------------------------------+----------
1      | 2          | 3                                                       | 4                               | 5                            | 6                                                                      | 7
-------+------------+---------------------------------------------------------+---------------------------------+------------------------------+------------------------------------------------------------------------+----------
1.     |            |                                                         |                                 |                              |                                                                        |
2.     |            |                                                         |                                 |                              |                                                                        |
3.     |            |                                                         |                                 |                              |                                                                        |
4.     |            |                                                         |                                 |                              |                                                                        |
5.     |            |                                                         |                                 |                              |                                                                        |
6.     |            |                                                         |                                 |                              |                                                                        |
7.     |            |                                                         |                                 |                              |                                                                        |
8.     |            |                                                         |                                 |                              |                                                                        |

* అభ్యర్థి / ఎన్నికల ఏజెంటు / పార్టీ / ఇతరులు

డిక్లరేషను:
పైన ఇవ్వబడిన సమాచారము నాకు తెలిసినంత వరకు సరియైనది మరియు నిజమైనదని దృవీకరించనైనది.

తేదీ: ________________________                               పోటీ చేయు అభ్యర్థి సంతకం"""
  },
  {
    "code": "Proforma-IV",
    "rule": "SEC Exp Guidelines",
    "title_en": "Proforma - IV: Acknowledgment Receipt for Submission of Election Accounts",
    "title_te": "ప్రోఫార్మా - IV: ఎన్నికల వ్యయ వివరాల దాఖలు రశీదు",
    "desc_en": "Official statutory acknowledgment receipt issued by the Municipal Commissioner / District Election Authority upon receiving the final election expenditure accounts from candidate.",
    "desc_te": "అభ్యర్థి ఎన్నికల వ్యయాల ఖాతాలను సమర్పించినప్పుడు మునిసిపల్ కమీషనర్ / జిల్లా ఎన్నికల అథారిటీ జారీ చేయవలసిన అధికారిక రశీదు (అసలు ప్రతి అభ్యర్థికి, కాపీ ఆఫీసు రికార్డులో).",
    "category": "Accounts",
    "category_te": "ఖాతాలు & డిపాజిట్లు",
    "authority": "Election-Officers-Forms.pdf (Page 21)",
    "content_en": """PROFORMA - IV: ACKNOWLEDGMENT RECEIPT
(Original to be given to the Candidate; Duplicate Copy to be retained in Office)

ACKNOWLEDGMENT RECEIPT (ORIGINAL / OFFICE COPY)

In the month of ________________________, Year 2026, in the elections held for the office of Chairperson / Ward Member of Ward No. ________ of SRIKALAHASTI Municipality, the accounts of election expenses of Sri / Smt / Kum ____________________________________________________, holding Serial Number ________ in the List of Contesting Candidates, have been duly submitted to me today, i.e. on ________________________ (date) by Sri / Smt / Kum ____________________________________________________.

Office Seal:

Date: ________________________                               Signature of Authorized Officer
                                                             Designation: Municipal Commissioner /
                                                             District Election Authority""",
    "content_te": """ప్రోఫార్మా - IV - రశీదు
(అసలు ప్రతి అభ్యర్థికి ఇచ్చి, ఒక కాపీని కార్యాలయంలో భద్రపర్చవలెను)

రశీదు (అసలు ప్రతి / కార్యాలయపు కాపీ)

________________________ నెల 2026 సంవత్సరములో శ్రీకాళహస్తి మున్సిపాలిటీ / నగర పంచాయితి లోని చైర్‌పర్సన్ / వార్డు నెం. _______ వార్డు సభ్యుని పదవికి జరిగిన ఎన్నికలో పోటీ చేయు అభ్యర్థుల జాబితాలోని క్రమ సంఖ్య ________ కలిగిన శ్రీ / శ్రీమతి / కుమారి ____________________________________________________ గారి యొక్క ఎన్నికల వ్యయ వివరాలు ఈ రోజు అనగా ________________________ తేదిన శ్రీ / శ్రీమతి / కుమారి ____________________________________________________ గారు నాకు సమర్పించినారు.

కార్యాలయ సీలు:

తేదీ: ________________________                               అధికృత అధికారి సంతకం
                                                             హోదా: మున్సిపల్ కమీషనర్ / జిల్లా ఎన్నికల అథారిటీ"""
  },
  {
    "code": "Form-1",
    "rule": "Rule 4 & Sec 20",
    "title_en": "Form - 1: Notice of Election",
    "title_te": "ఫారం - 1: ఎన్నికల నోటీసు",
    "desc_en": "Statutory notice of election published by the Election Officer under Rule 4, specifying ward reservations, nomination dates (16-11-2026 to 18-11-2026), scrutiny (19-11-2026), withdrawal (22-11-2026), and poll date (29-11-2026).",
    "desc_te": "ఎన్నికల అధికారి జారీ చేసే చట్టబద్ధ ఎన్నికల నోటీసు. నామినేషన్ల స్వీకరణ తేదీలు, పరిశీలన, ఉపసంహరణ మరియు పోలింగ్ వివరాలను తెలియజేస్తుంది.",
    "category": "Statutory",
    "category_te": "చట్టబద్ధ ఫారాలు",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - 1
NOTICE OF ELECTION
[See Rule 4]

Notice is hereby given that:
1. An ordinary election is to be held to elect Chairperson and Ward Members for 44 Wards of Srikalahasti Municipality.
2. Nomination papers may be delivered by a candidate or proposer to the Election Officer / Assistant Election Officer at the Municipal Office, Srikalahasti between 11:00 AM and 3:00 PM on any day (other than public holiday) not later than 18.11.2026.
3. Scrutiny of nomination papers will take place at the Municipal Office on 19.11.2026 at 11:00 AM.
4. Notice of withdrawal of candidature may be delivered either by candidate or authorized agent up to 3:00 PM on 22.11.2026.
5. In the event of election being contested, the poll will be taken on 29.11.2026 between 7:00 AM and 5:00 PM.

Date: 16.11.2026                                             Election Officer / Commissioner
Place: Srikalahasti                                          Srikalahasti Municipality""",
    "content_te": """ఫారం - 1
ఎన్నికల నోటీసు
[నియమం 4 చూడుము]

ఇందుమూలంగా నోటీసు ఇవ్వడమైనది:
1. శ్రీకాళహస్తి పురపాలక సంఘం చైర్‌పర్సన్ మరియు 44 వార్డుల సభ్యుల పదవులకు సాధారణ ఎన్నికలు నిర్వహించబడును.
2. నామినేషన్ పత్రాలను అభ్యర్థి లేదా ప్రతిపాదకుడు శ్రీకాళహస్తి పురపాలక కార్యాలయంలోని ఎన్నికల అధికారి / సహాయ ఎన్నికల అధికారికి ఉదయం 11:00 నుండి మధ్యాహ్నం 3:00 గంటల మధ్య 18.11.2026 లోపు అందజేయవచ్చును.
3. నామినేషన్ పత్రాల పరిశీలన 19.11.2026 న ఉదయం 11:00 గంటలకు మునిసిపల్ కార్యాలయంలో జరుగును.
4. అభ్యర్థిత్వాన్ని ఉపసంహరించుకునే నోటీసును 22.11.2026 మధ్యాహ్నం 3:00 గంటల లోపు దాఖలు చేయవచ్చును.
5. ఎన్నికలలో పోటీ ఉన్నచో, పోలింగ్ 29.11.2026 న ఉదయం 7:00 గంటల నుండి సాయంత్రం 5:00 గంటల వరకు జరుగును.

తేదీ: 16.11.2026                                             ఎన్నికల అధికారి / మున్సిపల్ కమీషనర్
స్థలము: శ్రీకాళహస్తి                                          శ్రీకాళహస్తి పురపాలక సంఘం"""
  },
  {
    "code": "Form-VII",
    "rule": "Rule 14(1)",
    "title_en": "Form - VII: List of Contesting Candidates",
    "title_te": "ఫారం - VII: పోటీ చేయు అభ్యర్థుల జాబితా",
    "desc_en": "List of validly nominated contesting candidates arranged alphabetically, showing candidate address, party affiliation, and allotted election symbol.",
    "desc_te": "అక్షర క్రమంలో రూపొందించబడిన పోటీ చేయు అభ్యర్థుల జాబితా, వారి చిరునామా, పార్టీ అనుబంధం మరియు కేటాయించబడిన ఎన్నికల గుర్తుల వివరాలు.",
    "category": "Statutory",
    "category_te": "చట్టబద్ధ ఫారాలు",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - VII
LIST OF CONTESTING CANDIDATES
[See Rule 14(1)]

Election to the Chairperson / Ward Member of Ward No. ________ of Srikalahasti Municipality

Sl | Name of Candidate | Address of Candidate | Party Affiliation | Symbol Allotted
---+-------------------+----------------------+-------------------+----------------
1. |                   |                      |                   |
2. |                   |                      |                   |
3. |                   |                      |                   |
4. |                   |                      |                   |

Date: 22.11.2026                                             Election Officer
Place: Srikalahasti                                          Srikalahasti Municipality""",
    "content_te": """ఫారం - VII
పోటీ చేయు అభ్యర్థుల జాబితా
[నియమం 14(1) చూడుము]

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్ / వార్డు నెం. ________ సభ్యుని పదవికి ఎన్నిక

క్ర.సం | అభ్యర్థి పేరు | అభ్యర్థి చిరునామా | పార్టీ అనుబంధం | కేటాయించిన గుర్తు
------+---------------+------------------+----------------+------------------
1.    |               |                  |                |
2.    |               |                  |                |
3.    |               |                  |                |
4.    |               |                  |                |

తేదీ: 22.11.2026                                             ఎన్నికల అధికారి
స్థలము: శ్రీకాళహస్తి                                          శ్రీకాళహస్తి మునిసిపాలిటీ"""
  },
  {
    "code": "Form-X-C",
    "rule": "Rule 18(1)",
    "title_en": "Form - X-C: Appointment of Polling Agent",
    "title_te": "ఫారం - X-C: పోలింగ్ ఏజెంటు నియామక పత్రము",
    "desc_en": "Statutory appointment of polling agent for a designated polling station, complete with candidate authorization and agent's solemn declaration before the Presiding Officer.",
    "desc_te": "నిర్దేశిత పోలింగ్ కేంద్రం వద్ద అభ్యర్థి తరఫున హాజరయ్యే పోలింగ్ ఏజెంటు నియామక పత్రము మరియు ప్రిసైడింగ్ అధికారి సమక్షంలో ఏజెంటు చేసే డిక్లరేషన్.",
    "category": "Polling Day",
    "category_te": "పోలింగ్ రోజు",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - X-C
APPOINTMENT OF POLLING AGENT
[See Rule 18(1)]

Election to Chairperson / Ward Member of Ward No. ________ of Srikalahasti Municipality

I, ____________________________________________________, a candidate at the above election, do hereby appoint Sri / Smt / Kum ____________________________________________________, resident of ____________________________________________________, as Polling Agent to attend Polling Station No. ________ situated at ____________________________________________________.

Date: ________________________                               Signature of Candidate / Election Agent

DECLARATION OF POLLING AGENT
I agree to act as Polling Agent and promise to maintain secrecy of voting.

Date: ________________________                               Signature of Polling Agent
Signed before me at the Polling Station:                     Signature of Presiding Officer""",
    "content_te": """ఫారం - X-C
పోలింగ్ ఏజెంటు నియామక పత్రము
[నియమం 18(1) చూడుము]

శ్రీకాళహస్తి మునిసిపాలిటీ చైర్‌పర్సన్ / వార్డు నెం. ________ సభ్యుని పదవికి ఎన్నిక

పైన పేర్కొన్న ఎన్నికలో అభ్యర్థినైన నేను, ____________________________________________________ నివాసి అయిన శ్రీ / శ్రీమతి / కుమారి ____________________________________________________ గారిని, ____________________________________________________ వద్ద ఉన్న పోలింగ్ కేంద్రం నెం. ________ వద్ద పోలింగ్ ఏజెంటుగా నియమించుచున్నాను.

తేదీ: ________________________                               అభ్యర్థి / ఎన్నికల ఏజెంటు సంతకము

పోలింగ్ ఏజెంటు ప్రకటన
నేను పోలింగ్ ఏజెంటుగా పనిచేయుటకు అంగీకరిస్తున్నాను మరియు ఓటింగు గోప్యతను కాపాడగలనని వాగ్దానం చేస్తున్నాను.

తేదీ: ________________________                               పోలింగ్ ఏజెంటు సంతకము
నా సమక్షంలో సంతకం చేయబడినది:                                  ప్రిసైడింగ్ అధికారి సంతకము"""
  },
  {
    "code": "Form-XVIII",
    "rule": "Rule 38",
    "title_en": "Form - XVIII: Ballot Paper Account",
    "title_te": "ఫారం - XVIII: బ్యాలెట్ పేపర్ల లెక్కల పత్రము",
    "desc_en": "Critical statutory ballot paper account (Part-I) prepared by Presiding Officer at poll close, recording total ballots received, issued, cancelled, tendered, and inserted into ballot boxes. Part-II records counting.",
    "desc_te": "పోలింగ్ ముగింపులో ప్రిసైడింగ్ అధికారి తయారు చేయవలసిన అత్యంత కీలకమైన బ్యాలెట్ పేపర్ల లెక్కల పత్రము (భాగము-I). అందినవి, జారీచేసినవి, రద్దుచేసినవి మరియు బ్యాలెట్ పెట్టెలో వేయబడిన ఓట్ల సమగ్ర లెక్క.",
    "category": "Polling Day",
    "category_te": "పోలింగ్ రోజు",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - XVIII: BALLOT PAPER ACCOUNT
[See Rule 38]
PART - I: BALLOT PAPER ACCOUNT

Election to Chairperson / Ward Member of Ward No. ________ of Srikalahasti Municipality
Polling Station No: ________ Building: __________________________________________________

1. Ballot papers received: From Sl. No. ____________ to Sl. No. ____________ Total: _________
2. Ballot papers unused (returned):
   (a) Undamaged: Total: _________
   (b) Damaged with cancelled signature: Total: _________
3. Ballot papers used at polling station (1 minus 2): Total: _________
4. Ballot papers cancelled under Rule 35 (voting procedure violation): Total: _________
5. Tendered Ballot papers used (Rule 36): Total: _________
6. BALLOT PAPERS TO BE FOUND IN BALLOT BOX (Item 3 minus Items 4 and 5): TOTAL: _________

Date: 29.11.2026                                             Signature of Presiding Officer
Time: _________________                                      Polling Station No: ________""",
    "content_te": """ఫారం - XVIII: బ్యాలెట్ పేపర్ల లెక్కల పత్రము
[నియమం 38 చూడుము]
భాగము - I: బ్యాలెట్ పేపర్ల లెక్క

శ్రీకాళహస్తి పురపాలక సంఘం చైర్‌పర్సన్ / వార్డు నెం. ________ వార్డు సభ్యుని పదవికి ఎన్నిక
పోలింగ్ కేంద్రం నెం: ________ భవనం: __________________________________________________

1. ప్రిసైడింగ్ అధికారికి అందిన బ్యాలెట్ పేపర్లు: క్ర.సం. ____________ నుండి ____________ వరకు మొత్తం: _________
2. ఉపయోగించని బ్యాలెట్ పేపర్లు (వాపసు ఇచ్చినవి):
   (a) చెక్కుచెదరనివి: మొత్తం: _________
   (b) ప్రిసైడింగ్ అధికారి సంతకం ఉండి రద్దు చేసినవి: మొత్తం: _________
3. పోలింగ్ కేంద్రం వద్ద ఉపయోగించిన బ్యాలెట్ పేపర్లు (1 లోంచి 2 తీసివేయగా): మొత్తం: _________
4. ఓటింగ్ నియమావళి ఉల్లంఘన వల్ల రద్దు చేయబడినవి (నియమం 35): మొత్తం: _________
5. టెండర్డు బ్యాలెట్ పేపర్లుగా ఉపయోగించినవి (నియమం 36): మొత్తం: _________
6. బ్యాలెట్ పెట్టెలో ఉండవలసిన బ్యాలెట్ పేపర్లు (గడి 3 లోంచి 4 మరియు 5 తీసివేయగా): మొత్తం: _________

తేదీ: 29.11.2026                                             ప్రిసైడింగ్ అధికారి సంతకము
సమయము: _________________                                    పోలింగ్ కేంద్రం నెం: ________"""
  },
  {
    "code": "Form-XX-P1",
    "rule": "Rule 48(1)",
    "title_en": "Form - XX (Part-I): Counting Sheet & Result of Voting",
    "title_te": "ఫారం - XX (భాగము-I): ఓట్ల లెక్కింపు రికార్డు & ఫలితాల పత్రం",
    "desc_en": "Statutory result sheet of counting under Rule 48(1). Records valid votes polled by each candidate, rejected votes, total votes found in boxes, and provides mandatory 15-minute recount window before signing.",
    "desc_te": "ఓట్ల లెక్కింపు ఫలితాల చట్టబద్ధ రికార్డు [నియమం 48(1)]. ప్రతి అభ్యర్థికి వచ్చిన చెల్లుబాటైన ఓట్లు, తిరస్కరించిన ఓట్లు మరియు రీకౌంటింగ్ కోరడానికి 15 నిమిషాల వ్యవధి నమోదు.",
    "category": "Counting",
    "category_te": "కౌంటింగ్",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - XX: RECORD OF COUNTING OF VOTES
[See Rule 48(1)]
PART - I: RESULT OF COUNTING

Election to Chairperson / Ward Member of Ward No. ________ of Srikalahasti Municipality
Counting Table No: ________ Round No: ________

Sl | Name of Candidate | Valid Votes Polled in Ballot Boxes | Postal Votes Polled | Total Valid Votes
---+-------------------+------------------------------------+---------------------+------------------
1. |                   |                                    |                     |
2. |                   |                                    |                     |
3. |                   |                                    |                     |
4. |                   |                                    |                     |

A. Total Number of Valid Votes: ________________________
B. Total Number of Rejected Votes: ________________________
C. Total Number of Tendered Votes: ________________________
D. TOTAL VOTES FOUND IN BALLOT BOXES (A + B): ________________________

ANNOUNCEMENT & MANDATORY 15-MINUTE RECOUNT WINDOW:
Announced to all candidates and counting agents present at: ________ (hours/minutes).
A mandatory interval of 15 minutes is allowed to submit written application for recount under Rule 49.
Recount requested: [  ] YES    [  ] NO

Date: 03.12.2026                                             Signature of Returning Officer /
Time: _________________                                      Assistant Returning Officer""",
    "content_te": """ఫారం - XX: ఓట్ల లెక్కింపు రికార్డు
[నియమం 48(1) చూడుము]
భాగము - I: లెక్కింపు ఫలితాలు

శ్రీకాళహస్తి పురపాలక సంఘం చైర్‌పర్సన్ / వార్డు నెం. ________ సభ్యుని పదవికి ఎన్నిక
కౌంటింగ్ టేబుల్ నెం: ________ రౌండ్ నెం: ________

క్ర.సం | అభ్యర్థి పేరు | బ్యాలెట్ పెట్టెలలో వచ్చిన చెల్లుబాటైన ఓట్లు | పోస్టల్ ఓట్లు | మొత్తం చెల్లుబాటైన ఓట్లు
------+---------------+------------------------------------------+--------------+-----------------------
1.    |               |                                          |              |
2.    |               |                                          |              |
3.    |               |                                          |              |
4.    |               |                                          |              |

A. మొత్తం చెల్లుబాటైన ఓట్ల సంఖ్య: ________________________
B. మొత్తం తిరస్కరించబడిన చెల్లని ఓట్ల సంఖ్య: ________________________
C. మొత్తం టెండర్డు ఓట్ల సంఖ్య: ________________________
D. బ్యాలెట్ పెట్టెలలో లభించిన మొత్తం ఓట్లు (A + B): ________________________

ప్రకటన & తప్పనిసరి 15 నిమిషాల రీకౌంటింగ్ సమయం:
హాజరైన అభ్యర్థులు మరియు కౌంటింగ్ ఏజెంట్లకు ఫలితాలు వినిపించిన సమయం: ________ గంటలకు.
నియమం 49 ప్రకారం రీకౌంటింగ్ దరఖాస్తు చేసుకోవడానికి 15 నిమిషాల వ్యవధి ఇవ్వడమైనది.
రీకౌంటింగ్ కోరబడినదా: [  ] అవును    [  ] లేదు

తేదీ: 03.12.2026                                             ఎన్నికల అధికారి సంతకము /
సమయము: _________________                                    సహాయ ఎన్నికల అధికారి"""
  },
  {
    "code": "Form-XX-P2",
    "rule": "Rule 51",
    "title_en": "Form - XX (Part-II): Declaration of Election Result & Return",
    "title_te": "ఫారం - XX (భాగము-II): ఎన్నికల ఫలితాల అధికారిక ప్రకటన పత్రము",
    "desc_en": "Statutory certificate of election issued under Rule 51 declaring the returned candidate as duly elected Chairperson or Ward Member of Srikalahasti Municipality.",
    "desc_te": "ఎన్నికైన అభ్యర్థిని శ్రీకాళహస్తి పురపాలక సంఘం చైర్‌పర్సన్ లేదా వార్డు సభ్యునిగా అధికారికంగా ప్రకటిస్తూ ఎన్నికల అధికారి జారీ చేసే చట్టబద్ధ ప్రకటన పత్రము [నియమం 51].",
    "category": "Counting",
    "category_te": "కౌంటింగ్",
    "authority": "Conduct of Election Rules, 2026",
    "content_en": """FORM - XX: DECLARATION OF RESULT
[See Rule 51]
PART - II: DECLARATION OF ELECTION

In accordance with Rule 51 of the Andhra Pradesh Municipalities / Nagar Panchayats (Conduct of Election of Chairpersons and Ward Members) Rules, 2026, I hereby declare that:

Sri / Smt / Kum: __________________________________________________________________
Address: _________________________________________________________________________
Sponsored by: __________________________________ Political Party / Independent

has been duly elected as:
[  ] CHAIRPERSON of SRIKALAHASTI MUNICIPALITY
[  ] WARD MEMBER for WARD NO. ________ of SRIKALAHASTI MUNICIPALITY

Date: 03.12.2026                                             Returning Officer /
Place: Srikalahasti                                          Municipal Commissioner
                                                             Srikalahasti Municipality""",
    "content_te": """ఫారం - XX: ఎన్నికల ఫలితాల అధికారిక ప్రకటన
[నియమం 51 చూడుము]
భాగము - II: ఎన్నికైనట్లు ప్రకటన

ఆంధ్రప్రదేశ్ పురపాలక సంఘాల (చైర్‌పర్సన్ మరియు వార్డు సభ్యుల ఎన్నికల నిర్వహణ) నియమాలు, 2026 లోని నియమం 51 ప్రకారం, నేను ఇందుమూలంగా ప్రకటించుచున్నాను:

శ్రీ / శ్రీమతి / కుమారి: __________________________________________________________________
చిరునామా: _________________________________________________________________________
పార్టీ: __________________________________ పార్టీ / స్వతంత్ర అభ్యర్థి

శ్రీకాళహస్తి పురపాలక సంఘానికి:
[  ] చైర్‌పర్సన్‌గా (CHAIRPERSON)
[  ] వార్డు నెం. ________ వార్డు సభ్యునిగా (WARD MEMBER)

సక్రమముగా ఎన్నుకోబడినట్లు ఇందుమూలముగా ప్రకటించడమైనది.

తేదీ: 03.12.2026                                             ఎన్నికల అధికారి /
స్థలము: శ్రీకాళహస్తి                                          మునిసిపల్ కమీషనర్
                                                             శ్రీకాళహస్తి మునిసిపాలిటీ"""
  }
]

with open('portal_forms_full.json', 'w', encoding='utf-8') as f:
    json.dump(forms, f, ensure_ascii=False, indent=2)

print(f"Generated {len(forms)} comprehensive forms in portal_forms_full.json.")
