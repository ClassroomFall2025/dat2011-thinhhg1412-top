# Lớp cha Nhanvien
class Nhanvien:
    def __init__(self, id, hoten, luong):
        self.id = id
        self.hoten = hoten
        self.luong = float(luong)

    def tong_luong(self):
        return self.luong

    def __str__(self):
        return f'ID: {self.id}, Name: {self.hoten}, Lương: {self.luong}'

# Lớp con Hanhchinh kế thừa từ Nhanvien
class Hanhchinh(Nhanvien):
    def __init__(self, id, hoten, luong):
        super().__init__(id, hoten, luong)

    def tinh_thue(self):
        if self.luong <= 9000000:
            return 0
        elif self.luong <= 15000000:
            return (self.luong - 9000000) * 0.01
        else:
            return (self.luong - 15000000) * 0.12

    def tong_luong(self):
        return self.luong - self.tinh_thue()

    def __str__(self):
        return f'ID: {self.id}, Name: {self.hoten}, Lương: {self.luong}, Thuế: {self.tinh_thue()}, Tổng Lương Sau khi trừ thuế: {self.tong_luong()}'

# Lớp con Tiepthi kế thừa từ Hanhchinh
class Tiepthi(Hanhchinh):
    def __init__(self, id, hoten, luong, doanhso, hoahong=0.05):
        super().__init__(id, hoten, luong)
        self.doanhso = float(doanhso)
        self.hoahong = float(hoahong)

    def tong_luong(self):
        tong_thunhap = self.luong + (self.doanhso * self.hoahong)
        return tong_thunhap - self.tinh_thue()

    def __str__(self):
        return f'ID: {self.id}, Name: {self.hoten}, Lương: {self.luong}, Doanh số: {self.doanhso}, Hoa hồng: {self.hoahong}, Tổng Thu Nhập: {self.tong_luong()}'

# Lớp con TruongPhong kế thừa từ Hanhchinh
class TruongPhong(Hanhchinh):
    def __init__(self, id, hoten, luong, luong_trachnhiem):
        super().__init__(id, hoten, luong)
        self.luong_trachnhiem = float(luong_trachnhiem)

    def tong_luong(self):
        tong_thunhap = self.luong + self.luong_trachnhiem
        return tong_thunhap - self.tinh_thue()

    def __str__(self):
        return f'ID: {self.id}, Name: {self.hoten}, Lương: {self.luong}, Lương trách nhiệm: {self.luong_trachnhiem}, Thuế: {self.tinh_thue()}, Tổng Thu Nhập: {self.tong_luong()}'

# Hàm nhập nhân viên
def nhap_nhanvien():
    nhanvien_list = []
    soluong = int(input('Nhập số lượng nhân viên: '))
    for _ in range(soluong):
        print('1. Nhân viên Hành chính')
        print('2. Nhân viên Tiếp Thị')
        print('3. Trưởng Phòng')
        loainhan_vien = int(input('Chọn loại nhân viên: '))
        if loainhan_vien == 1:
            ma = input('Nhập mã nhân viên: ')
            hoten = input('Nhập họ tên nhân viên: ')
            luong = float(input('Nhập lương: '))
            nhanvien = Hanhchinh(ma, hoten, luong)
            nhanvien_list.append(nhanvien)
        elif loainhan_vien == 2:
            ma = input('Nhập mã nhân viên: ')
            hoten = input('Nhập họ tên nhân viên: ')
            luong = float(input('Nhập lương: '))
            doanhso = float(input('Nhập doanh số: '))
            hoahong = float(input('Nhập hoa hồng: '))
            nhanvien = Tiepthi(ma, hoten, luong, doanhso, hoahong)
            nhanvien_list.append(nhanvien)
        elif loainhan_vien == 3:
            ma = input('Nhập mã nhân viên: ')
            hoten = input('Nhập họ tên nhân viên: ')
            luong = float(input('Nhập lương: '))
            luong_trachnhiem = float(input('Nhập lương trách nhiệm: '))
            nhanvien = TruongPhong(ma, hoten, luong, luong_trachnhiem)
            nhanvien_list.append(nhanvien)
        else:
            print('Nhân viên không hợp lệ!')
            continue
    with open('PS41941_NGUYENTHANHDAT_Assignment1/Nhanvien.txt', 'w', encoding='utf-8') as Filedoc:
        for nv in nhanvien_list:
            if isinstance(nv, Hanhchinh):
                Filedoc.write(f"Loại Nhân viên hành chính:, Mã: {nv.id}, Họ tên: {nv.hoten}, Lương: {nv.luong}\n")
            elif isinstance(nv, Tiepthi):
                Filedoc.write(f"Loại nhân viên tiếp thị: , Mã: {nv.id}, Họ tên: {nv.hoten}, Lương: {nv.luong}, Doanh số: {nv.doanhso}, Hoa hồng: {nv.hoahong}\n")
            elif isinstance(nv, TruongPhong):
                Filedoc.write(f" Loại nhân viên trưởng phòng: , Mã: {nv.id}, Họ tên: {nv.hoten}, Luơng: {nv.luong}, Lương trách nhiệm: {nv.luong_trachnhiem}\n")
        print('Danh sách đã được lưu vào file.')

    
# Hàm In ra nhân viên từ file

def doc_nhanvien_tu_file():
    nhanvien_list = []
    try:
        with open('PS41941_NGUYENTHANHDAT_Assignment1/Nhanvien.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if 'Loại Nhân viên hành chính' in line:
                    parts = line.split(',')
                    id = parts[1].split(':')[1].strip()  # Đổi từ ma thành id
                    hoten = parts[2].split(':')[1].strip()
                    luong = float(parts[3].split(':')[1].strip())
                    nhanvien = Hanhchinh(id, hoten, luong)
                    nhanvien_list.append(nhanvien)

        # Xuất danh sách nhân viên ra màn hình
        print("Danh sách nhân viên từ file:")
        for nv in nhanvien_list:
            print(f"Nhân viên Hành chính - ID: {nv.id}, Họ tên: {nv.hoten}, Lương: {nv.luong}")

    except FileNotFoundError:
        print("File không tồn tại, vui lòng nhập nhân viên trước!")
    except ValueError as ve:
        print(f"Lỗi chuyển đổi dữ liệu: {ve}")

# tìm thông tin nhân viên bằng id và in ra 

def tim_nhanvien_theo_ma():
    ma_tim_kiem = input("Nhập mã nhân viên cần tìm: ").strip()  # Nhập mã từ bàn phím và loại bỏ khoảng trắng
    nhanvien_tim_thay = None  # Biến để lưu kết quả tìm kiếm
    try:
        with open('Nhanvien.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if 'Loại Nhân viên hành chính' in line or 'Loại Nhân viên tiếp thị' in line or 'Loại Trưởng Phòng' in line:
                    parts = line.split(',')
                    id = parts[1].split(':')[1].strip()

                    # Kiểm tra nếu mã nhân viên trùng với mã tìm kiếm
                    if id == ma_tim_kiem:
                        nhanvien_tim_thay = line  # Lưu dòng thông tin nhân viên tìm được
                        break

        if nhanvien_tim_thay:
            print(f"Nhân viên tìm thấy: {nhanvien_tim_thay}")
        else:
            print(f"Không tìm thấy nhân viên với mã: {ma_tim_kiem}")

    except FileNotFoundError:
        print("File không tồn tại, vui lòng nhập nhân viên trước!")
    except Exception as e:
        print(f"Lỗi: {e}") 



# Hàm yêu cầu và lựa chọn chức năng
def yeucau():
    print('+-----------------------------------------------------------------------------+')
    print('1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file')
    print('2. Đọc thông tin nhân viên từ file và xuất nhân viên ra màn hình')
    print('3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím')
    print('4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.')
    print('5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.')
    print('6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.')
    print('7. Sắp xếp nhân viên theo họ và tên.')
    print('8. Sắp xếp nhân viên theo thu nhập.')
    print('9. Xuất 5 nhân viên có thu nhập cao nhất.')
    print('10. Kết thúc.')
    print('+-----------------------------------------------------------------------------+')

# Chương trình chính
if __name__ == "__main__": 
    while True: 
        yeucau()
        chon = int(input('Chọn chức năng: ')) 
        if chon == 1:
            nhap_nhanvien()
        elif chon == 2: 
            doc_nhanvien_tu_file()
        elif chon == 3: 
            tim_nhanvien_theo_ma()
        elif chon == 4: 
            pass 
        elif chon == 5: 
            pass 
        elif chon == 6: 
            pass 
        elif chon == 7: 
            pass 
        elif chon == 8: 
            pass 
        elif chon == 9: 
            pass 
        elif chon == 10:
            print('Kết thúc chương trình') 
            break 
            






