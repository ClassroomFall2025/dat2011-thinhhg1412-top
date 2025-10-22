import random

# ==============================
# LỚP CHA: NHÂN VIÊN
# ==============================
class Nhanvien:
    def __init__(self, id, hoten, luong):
        self.id = id
        self.hoten = hoten
        self.luong = float(luong)

    def tong_luong(self):
        return self.luong

    def __str__(self):
        return f'ID: {self.id}, Họ tên: {self.hoten}, Lương: {self.luong:.0f}'


# ==============================
# LỚP CON: HÀNH CHÍNH
# ==============================
class Hanhchinh(Nhanvien):
    def tinh_thue(self):
        if self.luong <= 9000000:
            return 0
        elif self.luong <= 15000000:
            return (self.luong - 9000000) * 0.01
        else:
            return (self.luong - 15000000) * 0.12

    def tong_luong(self):
        return self.luong - self.tinh_thue()


# ==============================
# LỚP CON: TIẾP THỊ
# ==============================
class Tiepthi(Hanhchinh):
    def __init__(self, id, hoten, luong, doanhso, hoahong=0.05):
        super().__init__(id, hoten, luong)
        self.doanhso = doanhso
        self.hoahong = hoahong

    def tong_luong(self):
        tong_thunhap = self.luong + (self.doanhso * self.hoahong)
        return tong_thunhap - self.tinh_thue()


# ==============================
# LỚP CON: TRƯỞNG PHÒNG
# ==============================
class TruongPhong(Hanhchinh):
    def __init__(self, id, hoten, luong, luong_trachnhiem):
        super().__init__(id, hoten, luong)
        self.luong_trachnhiem = luong_trachnhiem

    def tong_luong(self):
        tong_thunhap = self.luong + self.luong_trachnhiem
        return tong_thunhap - self.tinh_thue()


# ==============================
# HÀM TỰ ĐỘNG TẠO NHÂN VIÊN
# ==============================
def tao_ngau_nhien_nhanvien(so_luong=5):
    ho_ten_mau = ["Nguyen Van A", "Le Thi B", "Tran Van C", "Pham Thi D", "Vo Van E"]
    nhanvien_list = []

    for i in range(so_luong):
        loai = random.choice(["hanhchinh", "tiepthi", "truongphong"])
        ma = f"NV{i+1:03d}"
        hoten = random.choice(ho_ten_mau)
        luong = random.randint(8000000, 20000000)

        if loai == "hanhchinh":
            nv = Hanhchinh(ma, hoten, luong)
        elif loai == "tiepthi":
            doanhso = random.randint(10000000, 100000000)
            hoahong = round(random.uniform(0.03, 0.07), 2)
            nv = Tiepthi(ma, hoten, luong, doanhso, hoahong)
        else:
            luong_trachnhiem = random.randint(2000000, 5000000)
            nv = TruongPhong(ma, hoten, luong, luong_trachnhiem)

        nhanvien_list.append(nv)

    return nhanvien_list


# ==============================
# HÀM NHẬP NHÂN VIÊN TỪ BÀN PHÍM
# ==============================
def nhap_nhanvien():
    nhanvien_list = []
    while True:
        print("\n-- Nhập thông tin nhân viên --")
        id = input("Mã nhân viên: ")
        hoten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        print("Chọn loại nhân viên:")
        print("1. Hành chính")
        print("2. Tiếp thị")
        print("3. Trưởng phòng")
        loai = input("Chọn (1-3): ")

        if loai == "1":
            nv = Hanhchinh(id, hoten, luong)
        elif loai == "2":
            doanhso = float(input("Nhập doanh số: "))
            hoahong = float(input("Nhập hoa hồng (vd 0.05 = 5%): "))
            nv = Tiepthi(id, hoten, luong, doanhso, hoahong)
        elif loai == "3":
            luong_trachnhiem = float(input("Nhập lương trách nhiệm: "))
            nv = TruongPhong(id, hoten, luong, luong_trachnhiem)
        else:
            print("❌ Loại không hợp lệ.")
            continue

        nhanvien_list.append(nv)
        tiep = input("Bạn có muốn nhập thêm (y/n)? ").lower()
        if tiep != "y":
            break
    return nhanvien_list


# ==============================
# GHI & ĐỌC FILE
# ==============================
def ghi_file(nhanvien_list, ten_file="Nhanvien.txt"):
    with open(ten_file, "w", encoding="utf-8") as f:
        for nv in nhanvien_list:
            f.write(str(nv) + "\n")
    print(f"✅ Đã ghi {len(nhanvien_list)} nhân viên vào file '{ten_file}'")


def doc_file(ten_file="Nhanvien.txt"):
    print("\n📄 Danh sách nhân viên trong file:")
    with open(ten_file, "r", encoding="utf-8") as f:
        print(f.read())


# ==============================
# MENU CHÍNH
# ==============================
def menu():
    ds = []
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1. Nhập nhân viên bằng tay")
        print("2. Tạo ngẫu nhiên danh sách nhân viên")
        print("3. Ghi danh sách ra file")
        print("4. Đọc danh sách từ file")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == "1":
            ds = nhap_nhanvien()
        elif chon == "2":
            so_luong = int(input("Nhập số lượng nhân viên muốn tạo: "))
            ds = tao_ngau_nhien_nhanvien(so_luong)
            print(f"✅ Đã tạo {so_luong} nhân viên ngẫu nhiên.")
        elif chon == "3":
            if ds:
                ghi_file(ds)
            else:
                print("⚠️ Chưa có danh sách nhân viên để ghi.")
        elif chon == "4":
            doc_file()
        elif chon == "0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")


# ==============================
# CHẠY CHƯƠNG TRÌNH
# ==============================
if __name__ == "__main__":
    menu()
