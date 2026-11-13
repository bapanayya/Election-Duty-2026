import json

national_data = [
    {
        "sl": 1,
        "name_en": "Aam Aadmi Party",
        "name_te": "ఆమ్ ఆద్మీ పార్టీ",
        "symbol_en": "Broom",
        "symbol_te": "చీపురు",
        "category": "National",
        "category_te": "గుర్తింపు పొందిన జాతీయ పార్టీ",
        "abbr": "AAP",
        "img": "symbols_bw/nat_1_aap_broom.png"
    },
    {
        "sl": 2,
        "name_en": "Bahujan Samaj Party",
        "name_te": "బహుజన్ సమాజ్ పార్టీ",
        "symbol_en": "Elephant",
        "symbol_te": "ఏనుగు",
        "category": "National",
        "category_te": "గుర్తింపు పొందిన జాతీయ పార్టీ",
        "abbr": "BSP",
        "img": "symbols_bw/nat_2_bsp_elephant.png"
    },
    {
        "sl": 3,
        "name_en": "Bharatiya Janata Party",
        "name_te": "భారతీయ జనతా పార్టీ",
        "symbol_en": "Lotus",
        "symbol_te": "కమలము",
        "category": "National",
        "category_te": "గుర్తింపు పొందిన జాతీయ పార్టీ",
        "abbr": "BJP",
        "img": "symbols_bw/nat_3_bjp_lotus.png"
    },
    {
        "sl": 4,
        "name_en": "Communist Party of India (Marxist)",
        "name_te": "కమ్యూనిస్ట్ పార్టీ ఆఫ్ ఇండియా (మార్క్సిస్ట్)",
        "symbol_en": "Hammer, Sickle & Star",
        "symbol_te": "సుత్తి, కొడవలి మరియు నక్షత్రం",
        "category": "National",
        "category_te": "గుర్తింపు పొందిన జాతీయ పార్టీ",
        "abbr": "CPI(M)",
        "img": "symbols_bw/nat_4_cpim_hammer_sickle_star.png"
    },
    {
        "sl": 5,
        "name_en": "Indian National Congress",
        "name_te": "భారత జాతీయ కాంగ్రెస్",
        "symbol_en": "Hand",
        "symbol_te": "చేయి",
        "category": "National",
        "category_te": "గుర్తింపు పొందిన జాతీయ పార్టీ",
        "abbr": "INC",
        "img": "symbols_bw/nat_5_inc_hand.png"
    }
]

ap_state_data = [
    {
        "sl": 1,
        "name_en": "Janasena Party",
        "name_te": "జనసేన పార్టీ",
        "symbol_en": "Glass Tumbler",
        "symbol_te": "గాజు గ్లాసు",
        "category": "State (AP)",
        "category_te": "ఆంధ్రప్రదేశ్ గుర్తింపు పొందిన రాష్ట్ర పార్టీ",
        "abbr": "JSP",
        "img": "symbols_bw/state_1_jsp_glass_tumbler.png"
    },
    {
        "sl": 2,
        "name_en": "Telugu Desam Party",
        "name_te": "తెలుగుదేశం పార్టీ",
        "symbol_en": "Bicycle",
        "symbol_te": "సైకిల్",
        "category": "State (AP)",
        "category_te": "ఆంధ్రప్రదేశ్ గుర్తింపు పొందిన రాష్ట్ర పార్టీ",
        "abbr": "TDP",
        "img": "symbols_bw/state_2_tdp_bicycle.png"
    },
    {
        "sl": 3,
        "name_en": "Yuvajana Sramika Rythu Congress Party",
        "name_te": "యువజన శ్రామిక రైతు కాంగ్రెస్ పార్టీ (వైఎస్సార్‌సీపీ)",
        "symbol_en": "Ceiling Fan",
        "symbol_te": "సీలింగ్ ఫ్యాన్",
        "category": "State (AP)",
        "category_te": "ఆంధ్రప్రదేశ్ గుర్తింపు పొందిన రాష్ట్ర పార్టీ",
        "abbr": "YSRCP",
        "img": "symbols_bw/state_3_ysrcp_ceiling_fan.png"
    }
]

other_state_data = [
    {
        "sl": 1,
        "name_en": "All India Anna Dravida Munnetra Kazhagam",
        "name_te": "ఆల్ ఇండియా అన్నా ద్రవిడ మున్నేట్ర కజగం",
        "symbol_en": "Two Leaves",
        "symbol_te": "రెండు ఆకులు",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (తమిళనాడు)",
        "abbr": "AIADMK",
        "img": "symbols_bw/other_1_aiadmk_two_leaves.png"
    },
    {
        "sl": 2,
        "name_en": "All India Forward Bloc",
        "name_te": "ఆల్ ఇండియా ఫార్వర్డ్ బ్లాక్",
        "symbol_en": "Lion",
        "symbol_te": "సింహం",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (పశ్చిమ బెంగాల్)",
        "abbr": "AIFB",
        "img": "symbols_bw/other_2_aifb_lion.png"
    },
    {
        "sl": 3,
        "name_en": "All India Majlis-E-Ittehadul-Muslimeen",
        "name_te": "ఆల్ ఇండియా మజ్లిస్-ఎ-ఇత్తెహాదుల్ ముస్లిమీన్",
        "symbol_en": "Kite",
        "symbol_te": "గాలిపటం",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (తెలంగాణ)",
        "abbr": "AIMIM",
        "img": "symbols_bw/other_3_aimim_kite.png"
    },
    {
        "sl": 4,
        "name_en": "Bharat Rashtra Samithi",
        "name_te": "భారత్ రాష్ట్ర సమితి",
        "symbol_en": "Car",
        "symbol_te": "కారు",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (తెలంగాణ)",
        "abbr": "BRS",
        "img": "symbols_bw/other_4_brs_car.png"
    },
    {
        "sl": 5,
        "name_en": "Communist Party of India",
        "name_te": "కమ్యూనిస్ట్ పార్టీ ఆఫ్ ఇండియా",
        "symbol_en": "Ears of Corn & Sickle",
        "symbol_te": "కంకులు మరియు కొడవలి",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (కేరళ)",
        "abbr": "CPI",
        "img": "symbols_bw/other_5_cpi_corn_sickle.png"
    },
    {
        "sl": 6,
        "name_en": "Communist Party of India (Marxist-Leninist) (Liberation)",
        "name_te": "కమ్యూనిస్ట్ పార్టీ ఆఫ్ ఇండియా (మార్క్సిస్ట్-లెనినిస్ట్) (లిబరేషన్)",
        "symbol_en": "Flag with three Stars",
        "symbol_te": "మూడు నక్షత్రాలతో కూడిన జెండా",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (బీహార్)",
        "abbr": "CPI(ML)L",
        "img": "symbols_bw/other_6_cpiml_flag_3_stars.png"
    },
    {
        "sl": 7,
        "name_en": "Indian Union Muslim League",
        "name_te": "ఇండియన్ యూనియన్ ముస్లిం లీగ్",
        "symbol_en": "Ladder",
        "symbol_te": "నిచ్చెన",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (కేరళ)",
        "abbr": "IUML",
        "img": "symbols_bw/other_7_iuml_ladder.png"
    },
    {
        "sl": 8,
        "name_en": "Janata Dal (Secular)",
        "name_te": "జనతాదళ్ (సెక్యులర్)",
        "symbol_en": "A lady farmer carrying paddy on her head",
        "symbol_te": "వరి మోపు తలపై మోస్తున్న మహిళా రైతు",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (కర్ణాటక)",
        "abbr": "JD(S)",
        "img": "symbols_bw/other_8_jds_farmer_lady.png"
    },
    {
        "sl": 9,
        "name_en": "Janata Dal (United)",
        "name_te": "జనతాదళ్ (యునైటెడ్)",
        "symbol_en": "Arrow",
        "symbol_te": "బాణం",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (బీహార్)",
        "abbr": "JD(U)",
        "img": "symbols_bw/other_9_jdu_arrow.png"
    },
    {
        "sl": 10,
        "name_en": "Nationalist Congress Party",
        "name_te": "నేషనలిస్ట్ కాంగ్రెస్ పార్టీ",
        "symbol_en": "Clock",
        "symbol_te": "గడియారం",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (మహారాష్ట్ర)",
        "abbr": "NCP",
        "img": "symbols_bw/other_10_ncp_clock.png"
    },
    {
        "sl": 11,
        "name_en": "Revolutionary Socialist Party",
        "name_te": "రివల్యూషనరీ సోషలిస్ట్ పార్టీ",
        "symbol_en": "Spade & Stoker",
        "symbol_te": "పార మరియు స్టోకర్",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (పశ్చిమ బెంగాల్ / కేరళ)",
        "abbr": "RSP",
        "img": "symbols_bw/other_11_rsp_spade_stoker.png"
    },
    {
        "sl": 12,
        "name_en": "Samajwadi Party",
        "name_te": "సమాజ్‌వాదీ పార్టీ",
        "symbol_en": "Banyan Tree",
        "symbol_te": "మర్రి చెట్టు",
        "category": "State (Other)",
        "category_te": "ఇతర రాష్ట్ర గుర్తింపు పొందిన పార్టీ (ఉత్తర ప్రదేశ్)",
        "abbr": "SP",
        "img": "symbols_bw/other_12_sp_banyan_tree.png"
    }
]

free_symbols_data = [
    {"sl": 1, "name_en": "Air conditioner", "name_te": "ఎయిర్ కండీషనర్", "img": "symbols_bw/free_1_air_conditioner.png"},
    {"sl": 2, "name_en": "Almirah", "name_te": "బీరువా (అల్మారా)", "img": "symbols_bw/free_2_almirah.png"},
    {"sl": 3, "name_en": "Balloon", "name_te": "బెలూన్", "img": "symbols_bw/free_3_balloon.png"},
    {"sl": 4, "name_en": "Basket containing fruits", "name_te": "పండ్లతో కూడిన బుట్ట", "img": "symbols_bw/free_4_basket_fruits.png"},
    {"sl": 5, "name_en": "Bat", "name_te": "బ్యాట్", "img": "symbols_bw/free_5_bat.png"},
    {"sl": 6, "name_en": "Batsman", "name_te": "బ్యాట్స్‌మెన్", "img": "symbols_bw/free_6_batsman.png"},
    {"sl": 7, "name_en": "Battery torch", "name_te": "బ్యాటరీ టార్చ్", "img": "symbols_bw/free_7_battery_torch.png"},
    {"sl": 8, "name_en": "Belt", "name_te": "బెల్ట్", "img": "symbols_bw/free_8_belt.png"},
    {"sl": 9, "name_en": "Black Board", "name_te": "బ్లాక్ బోర్డ్ (నల్లబల్ల)", "img": "symbols_bw/free_9_black_board.png"},
    {"sl": 10, "name_en": "Bottle", "name_te": "సీసా (బాటిల్)", "img": "symbols_bw/free_10_bottle.png"},
    {"sl": 11, "name_en": "Bread", "name_te": "రొట్టె (బ్రెడ్)", "img": "symbols_bw/free_11_bread.png"},
    {"sl": 12, "name_en": "Brief case", "name_te": "బ్రీఫ్ కేసు", "img": "symbols_bw/free_12_brief_case.png"},
    {"sl": 13, "name_en": "Brush", "name_te": "బ్రష్", "img": "symbols_bw/free_13_brush.png"},
    {"sl": 14, "name_en": "Cake", "name_te": "కేక్", "img": "symbols_bw/free_14_cake.png"},
    {"sl": 15, "name_en": "Calculator", "name_te": "కాలిక్యులేటర్", "img": "symbols_bw/free_15_calculator.png"},
    {"sl": 16, "name_en": "Camera", "name_te": "కెమెరా", "img": "symbols_bw/free_16_camera.png"},
    {"sl": 17, "name_en": "Candles", "name_te": "కొవ్వొత్తులు", "img": "symbols_bw/free_17_candles.png"},
    {"sl": 18, "name_en": "Carom Board", "name_te": "క్యారమ్ బోర్డు", "img": "symbols_bw/free_18_carom_board.png"},
    {"sl": 19, "name_en": "Carpet", "name_te": "కార్పెట్", "img": "symbols_bw/free_19_carpet.png"},
    {"sl": 20, "name_en": "Cauliflower", "name_te": "కాలీఫ్లవర్", "img": "symbols_bw/free_20_cauliflower.png"},
    {"sl": 21, "name_en": "Chappals", "name_te": "చెప్పులు", "img": "symbols_bw/free_21_chappals.png"},
    {"sl": 22, "name_en": "Chess Board", "name_te": "చదరంగం బోర్డు", "img": "symbols_bw/free_22_chess_board.png"},
    {"sl": 23, "name_en": "Coat", "name_te": "కోటు", "img": "symbols_bw/free_23_coat.png"},
    {"sl": 24, "name_en": "Coconut", "name_te": "కొబ్బరికాయ", "img": "symbols_bw/free_24_coconut.png"},
    {"sl": 25, "name_en": "Cot", "name_te": "మంచం", "img": "symbols_bw/free_25_cot.png"},
    {"sl": 26, "name_en": "Cup and saucer", "name_te": "కప్పు మరియు సాసర్", "img": "symbols_bw/free_26_cup_and_saucer.png"},
    {"sl": 27, "name_en": "Cutting Plier", "name_te": "కట్టింగ్ ప్లయర్", "img": "symbols_bw/free_27_cutting_plier.png"},
    {"sl": 28, "name_en": "Dao", "name_te": "దావో (కత్తి)", "img": "symbols_bw/free_28_dao.png"},
    {"sl": 29, "name_en": "Diesel Pump", "name_te": "డీజిల్ పంపు", "img": "symbols_bw/free_29_diesel_pump.png"},
    {"sl": 30, "name_en": "Dish Antenna", "name_te": "డిష్ యాంటెన్నా", "img": "symbols_bw/free_30_dish_antenna.png"},
    {"sl": 31, "name_en": "Dolli", "name_te": "డోలి", "img": "symbols_bw/free_31_dolli.png"},
    {"sl": 32, "name_en": "Electric Pole", "name_te": "విద్యుత్ స్తంభం", "img": "symbols_bw/free_32_electric_pole.png"},
    {"sl": 33, "name_en": "Envelop", "name_te": "కవరు (ఎన్వలప్)", "img": "symbols_bw/free_33_envelop.png"},
    {"sl": 34, "name_en": "Flute", "name_te": "పిల్లనగ్రోవి (ఫ్లూట్)", "img": "symbols_bw/free_34_flute.png"},
    {"sl": 35, "name_en": "Frock", "name_te": "ఫ్రాక్", "img": "symbols_bw/free_35_frock.png"},
    {"sl": 36, "name_en": "Frying Pan", "name_te": "బాణలి (ఫ్రైయింగ్ పాన్)", "img": "symbols_bw/free_36_frying_pan.png"},
    {"sl": 37, "name_en": "Funnel", "name_te": "గరాటు (ఫన్నెల్)", "img": "symbols_bw/free_37_funnel.png"},
    {"sl": 38, "name_en": "Gas Cylinder", "name_te": "గ్యాస్ సిలిండర్", "img": "symbols_bw/free_38_gas_cylinder.png"},
    {"sl": 39, "name_en": "Gas Stove", "name_te": "గ్యాస్ స్టవ్", "img": "symbols_bw/free_39_gas_stove.png"},
    {"sl": 40, "name_en": "Grapes", "name_te": "ద్రాక్ష", "img": "symbols_bw/free_40_grapes.png"},
    {"sl": 41, "name_en": "Harmonium", "name_te": "హార్మోనియం", "img": "symbols_bw/free_41_harmonium.png"},
    {"sl": 42, "name_en": "Helmet", "name_te": "హెల్మెట్", "img": "symbols_bw/free_42_helmet.png"},
    {"sl": 43, "name_en": "Hockey Ball and Stick", "name_te": "హాకీ బాల్ మరియు స్టిక్", "img": "symbols_bw/free_43_hockey_ball_and_stick.png"},
    {"sl": 44, "name_en": "Ice Cream", "name_te": "ఐస్ క్రీమ్", "img": "symbols_bw/free_44_ice_cream.png"},
    {"sl": 45, "name_en": "Letter Box", "name_te": "లెటర్ బాక్స్ (తపాలా పెట్టె)", "img": "symbols_bw/free_45_letter_box.png"},
    {"sl": 46, "name_en": "Mixee", "name_te": "మిక్సీ", "img": "symbols_bw/free_46_mixee.png"},
    {"sl": 47, "name_en": "Nail Cutter", "name_te": "నెయిల్ కట్టర్", "img": "symbols_bw/free_47_nail_cutter.png"},
    {"sl": 48, "name_en": "Neck Tie", "name_te": "నెక్ టై", "img": "symbols_bw/free_48_neck_tie.png"},
    {"sl": 49, "name_en": "Pencil Sharpner", "name_te": "పెన్సిల్ షార్ప్‌నర్", "img": "symbols_bw/free_49_pencil_sharpner.png"},
    {"sl": 50, "name_en": "Pot", "name_te": "కుండ", "img": "symbols_bw/free_50_pot.png"},
    {"sl": 51, "name_en": "Pressure Cooker", "name_te": "ప్రెషర్ కుక్కర్", "img": "symbols_bw/free_51_pressure_cooker.png"},
    {"sl": 52, "name_en": "Razor", "name_te": "రేజర్ (బ్లేడు)", "img": "symbols_bw/free_52_razor.png"},
    {"sl": 53, "name_en": "Refrigerator", "name_te": "రిఫ్రిజిరేటర్", "img": "symbols_bw/free_53_refrigerator.png"},
    {"sl": 54, "name_en": "Ring", "name_te": "ఉంగరం", "img": "symbols_bw/free_54_ring.png"},
    {"sl": 55, "name_en": "Saw", "name_te": "రంపం", "img": "symbols_bw/free_55_saw.png"},
    {"sl": 56, "name_en": "School Bag", "name_te": "స్కూల్ బ్యాగ్", "img": "symbols_bw/free_56_school_bag.png"},
    {"sl": 57, "name_en": "Scissors", "name_te": "కత్తెర", "img": "symbols_bw/free_57_scissors.png"},
    {"sl": 58, "name_en": "Sewing Machine", "name_te": "కుట్టు మిషన్", "img": "symbols_bw/free_58_sewing_machine.png"}
]

nota_data = {
    "name_en": "None of the Above (NOTA)",
    "name_te": "పైవారెవరూ కాదు (నోటా)",
    "rule": "Rule 75(1) & (2) of AP Municipalities Rules, 2026",
    "symbol_desc_en": "Statutory ballot paper cross mark with NOTA lettering",
    "symbol_desc_te": "నోటా అక్షరాలతో కూడిన చట్టబద్ధ బ్యాలెట్ క్రాస్ మార్క్",
    "placement_en": "Printed in the LAST panel of every ballot paper (Pink for Chairperson, White for Ward Members)",
    "placement_te": "ప్రతి బ్యాలెట్ పత్రం యొక్క చిట్టచివరి ప్యానెల్‌లో ముద్రించాలి (ఛైర్‌పర్సన్‌కు గులాబీ రంగు, వార్డు సభ్యులకు తెలుపు రంగు)",
    "img": "symbols_bw/table_v_nota.png"
}

# Verify that all referenced images exist on disk!
all_images = (
    [x["img"] for x in national_data] +
    [x["img"] for x in ap_state_data] +
    [x["img"] for x in other_state_data] +
    [x["img"] for x in free_symbols_data] +
    [nota_data["img"]]
)

import os
missing = [img for img in all_images if not os.path.exists(img)]
print(f"Total symbol image references: {len(all_images)}")
if missing:
    print(f"MISSING IMAGES: {missing}")
else:
    print("ALL 79 REFERENCED IMAGE FILES EXIST ON DISK!")
