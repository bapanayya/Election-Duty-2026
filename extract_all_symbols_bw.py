import os
from PIL import Image
import numpy as np

os.makedirs('symbols_bw', exist_ok=True)

def clean_and_square(crop_im, pad=18, out_size=(200, 200), thresh=175, mask_lr=28, mask_tb=16):
    gray = crop_im.convert('L')
    arr = np.array(gray)
    h, w = arr.shape
    
    clean = arr.copy()
    clean[:mask_tb, :] = 255
    clean[-mask_tb:, :] = 255
    clean[:, :mask_lr] = 255
    clean[:, -mask_lr:] = 255
    
    mask = clean < thresh
    if mask.sum() == 0:
        return None
    
    ys, xs = np.where(mask)
    y1, y2 = ys.min(), ys.max()
    x1, x2 = xs.min(), xs.max()
    
    symbol_crop = gray.crop((x1, y1, x2 + 1, y2 + 1))
    sw, sh = symbol_crop.size
    
    dim = max(sw, sh) + pad * 2
    canvas = Image.new('L', (dim, dim), 255)
    canvas.paste(symbol_crop, ((dim - sw) // 2, (dim - sh) // 2))
    
    final_im = canvas.resize(out_size, Image.Resampling.LANCZOS)
    return final_im

# Master list of all 79 symbols to extract
# Format: (page_png, y1_pt, y2_pt, x1_px, x2_px, filename, mask_lr, mask_tb)

symbols_defs = []

# --- 1. Page 3: National Parties (1-5) ---
# x: 1225 to 1515
p3_nat = [
    (150, 210, 'nat_1_aap_broom.png'),
    (210, 270, 'nat_2_bsp_elephant.png'),
    (270, 335, 'nat_3_bjp_lotus.png'),
    (335, 405, 'nat_4_cpim_hammer_sickle_star.png'),
    (405, 475, 'nat_5_inc_hand.png'),
]
for y1, y2, fname in p3_nat:
    symbols_defs.append(('page_3.png', y1, y2, 1225, 1515, fname, 12, 8))

# --- 2. Page 3: AP State Parties (1-3) ---
p3_state = [
    (560, 625, 'state_1_jsp_glass_tumbler.png'),
    (625, 690, 'state_2_tdp_bicycle.png'),
    (690, 760, 'state_3_ysrcp_ceiling_fan.png'),
]
for y1, y2, fname in p3_state:
    symbols_defs.append(('page_3.png', y1, y2, 1225, 1515, fname, 12, 8))

# --- 3. Page 4: Other State Parties (1-9) ---
# x: 1120 to 1460
p4_other = [
    (105, 165, 'other_1_aiadmk_two_leaves.png'),
    (165, 225, 'other_2_aifb_lion.png'),
    (225, 280, 'other_3_aimim_kite.png'),
    (280, 340, 'other_4_brs_car.png'),
    (340, 410, 'other_5_cpi_corn_sickle.png'),
    (410, 480, 'other_6_cpiml_flag_3_stars.png'),
    (480, 550, 'other_7_iuml_ladder.png'),
    (550, 650, 'other_8_jds_farmer_lady.png'),
    (650, 720, 'other_9_jdu_arrow.png'),
]
for y1, y2, fname in p4_other:
    symbols_defs.append(('page_4.png', y1, y2, 1120, 1460, fname, 15, 8))

# --- 4. Page 5: Other State Parties (10-12) ---
p5_other = [
    (50, 115, 'other_10_ncp_clock.png'),
    (115, 185, 'other_11_rsp_spade_stoker.png'),
    (185, 255, 'other_12_sp_banyan_tree.png'),
]
for y1, y2, fname in p5_other:
    symbols_defs.append(('page_5.png', y1, y2, 1120, 1460, fname, 15, 8))

# --- 5. Page 7: Free Symbols (1-3) ---
# x: 1050 to 1500
p7_free = [
    (535, 605, 'free_1_air_conditioner.png'),
    (605, 675, 'free_2_almirah.png'),
    (675, 745, 'free_3_balloon.png'),
]
for y1, y2, fname in p7_free:
    symbols_defs.append(('page_7.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 6. Page 8: Free Symbols (4-13) ---
p8_free = [
    (45, 110, 'free_4_basket_fruits.png'),
    (110, 175, 'free_5_bat.png'),
    (175, 240, 'free_6_batsman.png'),
    (240, 305, 'free_7_battery_torch.png'),
    (305, 370, 'free_8_belt.png'),
    (370, 435, 'free_9_black_board.png'),
    (435, 505, 'free_10_bottle.png'),
    (505, 570, 'free_11_bread.png'),
    (570, 635, 'free_12_brief_case.png'),
    (635, 705, 'free_13_brush.png'),
]
for y1, y2, fname in p8_free:
    symbols_defs.append(('page_8.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 7. Page 9: Free Symbols (14-24) ---
p9_free = [
    (45, 105, 'free_14_cake.png'),
    (105, 170, 'free_15_calculator.png'),
    (170, 235, 'free_16_camera.png'),
    (235, 300, 'free_17_candles.png'),
    (300, 365, 'free_18_carom_board.png'),
    (365, 430, 'free_19_carpet.png'),
    (430, 495, 'free_20_cauliflower.png'),
    (495, 560, 'free_21_chappals.png'),
    (560, 625, 'free_22_chess_board.png'),
    (625, 690, 'free_23_coat.png'),
    (690, 755, 'free_24_coconut.png'),
]
for y1, y2, fname in p9_free:
    symbols_defs.append(('page_9.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 8. Page 10: Free Symbols (25-35) ---
p10_free = [
    (45, 105, 'free_25_cot.png'),
    (105, 170, 'free_26_cup_and_saucer.png'),
    (170, 235, 'free_27_cutting_plier.png'),
    (235, 300, 'free_28_dao.png'),
    (300, 365, 'free_29_diesel_pump.png'),
    (365, 430, 'free_30_dish_antenna.png'),
    (430, 495, 'free_31_dolli.png'),
    (495, 560, 'free_32_electric_pole.png'),
    (560, 625, 'free_33_envelop.png'),
    (625, 690, 'free_34_flute.png'),
    (690, 755, 'free_35_frock.png'),
]
for y1, y2, fname in p10_free:
    symbols_defs.append(('page_10.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 9. Page 11: Free Symbols (36-46) ---
p11_free = [
    (45, 105, 'free_36_frying_pan.png'),
    (105, 170, 'free_37_funnel.png'),
    (170, 235, 'free_38_gas_cylinder.png'),
    (235, 300, 'free_39_gas_stove.png'),
    (300, 365, 'free_40_grapes.png'),
    (365, 430, 'free_41_harmonium.png'),
    (430, 495, 'free_42_helmet.png'),
    (495, 560, 'free_43_hockey_ball_and_stick.png'),
    (560, 625, 'free_44_ice_cream.png'),
    (625, 690, 'free_45_letter_box.png'),
    (690, 755, 'free_46_mixee.png'),
]
for y1, y2, fname in p11_free:
    symbols_defs.append(('page_11.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 10. Page 12: Free Symbols (47-57) ---
p12_free = [
    (45, 105, 'free_47_nail_cutter.png'),
    (105, 170, 'free_48_neck_tie.png'),
    (170, 235, 'free_49_pencil_sharpner.png'),
    (235, 300, 'free_50_pot.png'),
    (300, 365, 'free_51_pressure_cooker.png'),
    (365, 430, 'free_52_razor.png'),
    (430, 495, 'free_53_refrigerator.png'),
    (495, 560, 'free_54_ring.png'),
    (560, 625, 'free_55_saw.png'),
    (625, 690, 'free_56_school_bag.png'),
    (690, 755, 'free_57_scissors.png'),
]
for y1, y2, fname in p12_free:
    symbols_defs.append(('page_12.png', y1, y2, 1050, 1500, fname, 26, 12))

# --- 11. Page 13: Free Symbol 58 & NOTA ---
symbols_defs.append(('page_13.png', 45, 110, 1050, 1500, 'free_58_sewing_machine.png', 26, 12))
symbols_defs.append(('page_13.png', 230, 310, 1050, 1500, 'table_v_nota.png', 26, 12))

print(f"Total symbol definitions: {len(symbols_defs)}")

# Cache loaded images
page_images = {}

success_count = 0
failed = []

for pfile, y1_pt, y2_pt, x1_px, x2_px, fname, mlr, mtb in symbols_defs:
    if pfile not in page_images:
        page_images[pfile] = Image.open('sec_symbol_pages/' + pfile)
    p_im = page_images[pfile]
    
    sy = p_im.height / 841.5
    crop_im = p_im.crop((x1_px, int(y1_pt * sy), x2_px, int(y2_pt * sy)))
    
    cleaned = clean_and_square(crop_im, pad=18, out_size=(200, 200), thresh=175, mask_lr=mlr, mask_tb=mtb)
    if cleaned is not None:
        out_path = os.path.join('symbols_bw', fname)
        cleaned.save(out_path, optimize=True)
        success_count += 1
    else:
        print(f"FAILED: {fname}")
        failed.append(fname)

print(f"Extraction completed: {success_count}/{len(symbols_defs)} succeeded.")
if failed:
    print(f"Failed symbols: {failed}")
