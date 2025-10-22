# def tinh_tien_nuoc(sanluongnuoc):
#     giabannuoc = (7500, 8800, 12000, 24000) # Kiểu dữ liệu Tuple
#     tongtien_nuoc = 0

#     # Tính tiền nước theo từng bậc
#     if sanluongnuoc <= 10:
#         tongtien_nuoc = sanluongnuoc * giabannuoc[0]
#     elif sanluongnuoc <= 20:
#         tongtien_nuoc = 10 * giabannuoc[0] + (sanluongnuoc - 10) * giabannuoc[2]
#     elif tongtien_nuoc <= 30:
#         tongtien_nuoc = 10 * giabannuoc[0] + 10 * giabannuoc[1] + (sanluongnuoc - 20) * giabannuoc[2]
#     else:
#         tongtien_nuoc = 10 * giabannuoc[0] + 10 * giabannuoc[1] + 10 * giabannuoc[2] + (sanluongnuoc - 30) * giabannuoc[3]

#     return tongtien_nuoc


# def tinh_nguyen_lieu_1(so_banh_dau_xanh, so_banh_thap_cam, so_banh_deo):
#     # Lưu lượng nguyên liệu cho từng loại bánh (sử dụng dictionary)
#     nguyen_lieu_banh = {
#         "banh_dau_xanh": {"đường": 0.04, "đậu": 0.07},
#         "banh_thap_cam": {"đường": 0.06, "đậu": 0},
#         "banh_deo": {"đường": 0.05, "đậu": 0.02}
#     }

#     # Tính tổng lượng đường
#     duong = (so_banh_dau_xanh * nguyen_lieu_banh["banh_dau_xanh"]["đường"] +
#              so_banh_thap_cam * nguyen_lieu_banh["banh_thap_cam"]["đường"] +
#              so_banh_deo * nguyen_lieu_banh["banh_deo"]["đường"])

#     # Tính tổng lượng đậu
#     dau = (so_banh_dau_xanh * nguyen_lieu_banh["banh_dau_xanh"]["đậu"] +
#            so_banh_thap_cam * nguyen_lieu_banh["banh_thap_cam"]["đậu"] +
#            so_banh_deo * nguyen_lieu_banh["banh_deo"]["đậu"])

#     # Trả về kết quả dưới dạng dictionary
#     return {"đường": duong, "đậu": dau}

# Tính tiền nước
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30: 
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

# Nguyên liệu làm bánh
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"đường":0.04, "đậu":0.07}
    banh_thap_cam = {"đường":0.06, "đậu":0}
    banh_deo = {"đường":0.05, "đậu":0.02}
    nguyen_lieu = {}
    duong_trong_banh = sl_bdx * banh_dau_xanh["đường"] + sl_btc * banh_thap_cam["đường"] + sl_bd * banh_deo["đường"]
    dau_trong_banh = sl_bdx * banh_dau_xanh["đậu"] + sl_btc * banh_thap_cam["đậu"] + sl_bd * banh_deo["đậu"]
    nguyen_lieu["đường"] = duong_trong_banh
    nguyen_lieu["đậu"] = dau_trong_banh
    return nguyen_lieu

