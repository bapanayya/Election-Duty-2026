# -*- coding: utf-8 -*-
"""
Generates the complete index.html for Srikalahasti Municipality Phase 2 Ordinary Elections 2026.
"""

import json

with open('srikalahasti_88_polling_stations.json', 'r', encoding='utf-8') as f:
    ps_data = json.load(f)

from prepare_data import reservations, ward_summary

# Supporting staff to Election Officers
supporting_staff = [
    {"cluster": "Chairperson Office", "wards": "All 44 Wards (Direct Election)", "staff": [("G. Nithin Singh, WA", "9492831594"), ("A. Leela Krishna, WA", "7032027606")]},
    {"cluster": "Cluster 1", "wards": "Wards 1 – 4", "staff": [("B. Sreepathi, WEDPS", "8374252079"), ("E. Jhansi, WA", "9030881708")]},
    {"cluster": "Cluster 2", "wards": "Wards 5 – 8", "staff": [("K. Suresh, WEDPS", "9014566244"), ("K. Madhavi, WA", "7204695000")]},
    {"cluster": "Cluster 3", "wards": "Wards 9 – 12", "staff": [("T. Suresh, WEDPS", "8919170382"), ("K. Kalpana, WA", "8897890434")]},
    {"cluster": "Cluster 4", "wards": "Wards 13 – 16", "staff": [("R. Praveen, WEDPS", "9177203062"), ("S. Thasleem, WA", "7842246142")]},
    {"cluster": "Cluster 5", "wards": "Wards 17 – 20", "staff": [("D. Jayaprakash, WEDPS", "9966449310"), ("K. Siva Kumar, WA", "7207266773")]},
    {"cluster": "Cluster 6", "wards": "Wards 21 – 24", "staff": [("K. J. Bhaskar, WEDPS", "7893111073"), ("G. Sai Sunil Kumar, WA", "7013435085")]},
    {"cluster": "Cluster 7", "wards": "Wards 25 – 28", "staff": [("D. L. Dilli Priya, WEDPS", "8074332196"), ("Muni Chenchu Latha, WA", "9701786332")]},
    {"cluster": "Cluster 8", "wards": "Wards 29 – 32", "staff": [("N. Hema Madhuri, WA", "9912250707"), ("C. Yamini, WA", "8464077105")]},
    {"cluster": "Cluster 9", "wards": "Wards 33 – 36", "staff": [("K. Sravani, WEDPS", "9985340635"), ("G. Kameswara Rao, WA", "8328075402")]},
    {"cluster": "Cluster 10", "wards": "Wards 37 – 40", "staff": [("T. Chandra Reddy, WEDPS", "9640473306"), ("K. Bhanu Prakash, WA", "9154562184")]},
    {"cluster": "Cluster 11", "wards": "Wards 41 – 44", "staff": [("C. Murali, WEDPS", "9885743874"), ("Y. Yamuna, WA", "8897447071")]}
]

# Zonal Officers
zonal_officers = [
    {"zone": "Zone 01", "officer": "Dr. P. Venugopal", "desig": "Lecturer in Commerce", "phone": "9393887222", "routes": "Routes 1, 2, 3", "wards": "1, 2, 3, 4, 5, 6, 7; 33, 34, 35, 36, 37; 40, 41, 43, 44", "ps_count": 31},
    {"zone": "Zone 02", "officer": "K. Bhuvaneswari", "desig": "Mandal Education Officer", "phone": "9618415439 / 9441592631", "routes": "Routes 4, 6, 7", "wards": "38, 39, 40, 42; 11, 12, 13, 14; 8, 9, 10, 15, 16, 20", "ps_count": 27},
    {"zone": "Zone 03", "officer": "K. Bhagya Lakshmi", "desig": "Supervisor Grade-II, WD&CW Dept.", "phone": "9491000256", "routes": "Routes 5, 8, 9", "wards": "17, 18, 24, 26, 28, 29, 30; 19, 21, 22, 23, 25; 31, 32, 27", "ps_count": 30}
]

# Route Officers
route_officers = [
    {"route": 1, "name": "M. Pardhasaradhi", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "8686867365", "wards": "1, 2, 3, 4, 5, 6, 7", "ps_list": "1/1, 1/2, 2/1, 2/2, 3/1, 3/2, 4/1, 4/2, 5/1, 5/2, 6/1, 6/2, 7/1, 7/2 (14 PS)"},
    {"route": 2, "name": "K. Rajendra", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "7288936923", "wards": "33, 34, 35, 36, 37", "ps_list": "33/1, 33/2, 34/1, 34/2, 35/1, 35/2, 36/1, 36/2, 37/1, 37/2 (10 PS)"},
    {"route": 3, "name": "NB Prabhakar", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "9629297089", "wards": "40, 41, 43, 44", "ps_list": "40/1, 41/1, 41/2, 43/1, 43/2, 44/1, 44/2 (7 PS)"},
    {"route": 4, "name": "Shaik Sulthan Sharief", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "9966011817", "wards": "38, 39, 40, 42", "ps_list": "38/1, 38/2, 39/1, 39/2, 40/2, 42/1, 42/2 (7 PS)"},
    {"route": 5, "name": "B. Sai Prasad", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "9676006961", "wards": "17, 18, 24, 26, 28, 29, 30", "ps_list": "17/1, 17/2, 18/1, 18/2, 24/1, 24/2, 26/1, 26/2, 28/1, 28/2, 29/1, 29/2, 30/1, 30/2 (14 PS)"},
    {"route": 6, "name": "A. Gireesha", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "8919543675", "wards": "11, 12, 13, 14", "ps_list": "11/1, 11/2, 12/1, 12/2, 13/1, 13/2, 14/1, 14/2 (8 PS)"},
    {"route": 7, "name": "C. Pramila", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "7036375470", "wards": "8, 9, 10, 15, 16, 20", "ps_list": "8/1, 8/2, 9/1, 9/2, 10/1, 10/2, 15/1, 15/2, 16/1, 16/2, 20/1, 20/2 (12 PS)"},
    {"route": 8, "name": "Vinitha", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "7330746514", "wards": "19, 21, 22, 23, 25", "ps_list": "19/1, 19/2, 21/1, 21/2, 22/1, 22/2, 23/1, 23/2, 25/1, 25/2 (10 PS)"},
    {"route": 9, "name": "Chandana", "desig": "Ward Planning & Regulation Secretary (WPRS)", "phone": "8096610523", "wards": "31, 32, 27", "ps_list": "31/1, 31/2, 32/1, 32/2, 27/1, 27/2 (6 PS)"}
]

# MCC, FST, SST, VST, Expenditure Teams
surveillance_teams = {
    "mcc": [
        {"shift": "Shift 1 (08:00 AM – 08:00 PM)", "wards": "Wards 1 to 44", "members": [
            ("Dr. C. Narasimha Reddy (Incharge)", "Lecturer in Mathematics, SVA Govt College", "9441209500"),
            ("Deva Rajulu Vedagiri", "Senior Assistant, O/o EE NTR TGP Div", "7036371140"),
            ("K. Kranthi", "Head Constable 981", "9505354981")
        ]},
        {"shift": "Shift 2 (08:00 PM – 08:00 AM)", "wards": "Wards 1 to 44", "members": [
            ("D. Bhaskar (Incharge)", "Lecturer in Commerce, SVA Govt College", "9440095961"),
            ("Anil Kumar Reddy Dappili", "Senior Assistant, O/o EE NTR TGP Div", "9492320039"),
            ("U. Ramanaiah", "Head Constable 789", "9440846401")
        ]}
    ],
    "fst": [
        {"shift": "Shift 1 (08:00 AM – 08:00 PM)", "wards": "Wards 1 to 44", "members": [
            ("Bharathi (Incharge)", "Mandal Education Officer", "9441573295"),
            ("Narasimhulu Chindukuri", "Senior Assistant, O/o EE NTR TGP Div", "9989671658"),
            ("M. Ramanaiah", "Head Constable 844", "9449932821")
        ]},
        {"shift": "Shift 2 (08:00 PM – 08:00 AM)", "wards": "Wards 1 to 44", "members": [
            ("A. Balaiah (Incharge)", "Mandal Education Officer", "9440343503"),
            ("Srinivasulu Valluru", "Senior Assistant, O/o EE NTR TGP Div", "9441132420"),
            ("S. Subramanyam", "Head Constable 758", "8074660081")
        ]}
    ],
    "sst": [
        {"location": "SST-1: AP Tourism, Srikalahasti", "shifts": [
            {"timing": "Shift 1 (08:00 AM – 08:00 PM)", "members": [
                ("K. Vinith Kumar Reddy (AEO Gr-II)", "Panguru", "8919604708"),
                ("Venkata Subba Reddy Paleti", "Senior Assistant, EE NTR TGP Div", "8341337654"),
                ("M. Sankar", "Police Constable 858", "9985944940")
            ]},
            {"timing": "Shift 2 (08:00 PM – 08:00 AM)", "members": [
                ("P. Venkata Praveen (AEO Gr-II)", "Nalvai", "98499997550"),
                ("Malleswaraiah Obulam", "Junior Assistant, EE NTR TGP Div", "8297288918"),
                ("V. Mohan Babu", "Police Constable 2023", "9676572238")
            ]}
        ]},
        {"location": "SST-2: Nandi Circle, Naidupeta Road, Srikalahasti", "shifts": [
            {"timing": "Shift 1 (08:00 AM – 08:00 PM)", "members": [
                ("K. Jyothsna (AEO Gr-II)", "Muchivolu", "9515577377"),
                ("Siva Kundla", "Junior Assistant, EE NTR TGP Div", "6281525335"),
                ("V. Anil Kumar", "Police Constable 871", "8897837877")
            ]},
            {"timing": "Shift 2 (08:00 PM – 08:00 AM)", "members": [
                ("A. Ravi Prasad (AEO Gr-II)", "Arai", "9533910555"),
                ("Subba Reddy Koppula", "Junior Assistant, EE NTR TGP Div", "9551223998"),
                ("P. Hari", "Police Constable 1811", "9618664654")
            ]}
        ]}
    ],
    "expenditure": [
        {"team": "Team 1 (Wards 1 to 22)", "members": [
            ("Prabhakar", "AAO, Srikalahasti Municipality", "9440667769"),
            ("B. Priyanka", "Senior Accountant, Puttur Municipality", "7997423413")
        ]},
        {"team": "Team 2 (Wards 23 to 44)", "members": [
            ("B. Manohara", "JAO, Nagari Municipality", "9491781181"),
            ("C. Balaji", "Senior Accountant, Srikalahasti Municipality", "8008644256")
        ]}
    ],
    "vst": [
        {"team": "Video Surveillance Team (Municipal Limits)", "members": [
            ("Ramana", "Videographer", "9705518400"),
            ("Ch. Chalamaiah", "Head Constable 3898", "8985272119")
        ]}
    ]
}

print("Operational dataset assembled. Ready to write generator script.")
