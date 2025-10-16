# class SanPham:
#     def __init__(self, ten_san_pham, gia, giam_gia):
#         self.ten_san_pham = ten_san_pham
#         self.gia = gia
#         self.giam_gia = giam_gia
#     def thue_nhap_khau(self):
#         return self.gia * 0.1
#     def nhap_sp(self):
#         self.ten_san_pham = input("tên sản phẩm:")
#         self.gia = float(input("gia"))
#         self.giam_gia = float(input("giam gia"))
        
#     def xuat_tt_sp(self):
#         print(f"sản phẩm {self.ten_san_pham} có giá{self.gia} và được giảm giá {self.giam_gia}")


class SanPham:
    # Hàm khởi tạo __init__ đã được sửa ở bước trước
    def __init__(self, ten_san_pham="", gia=0, giam_gia=0):
        self._ten = ten_san_pham
        self._gia = gia
        self._giam_gia = giam_gia
    
    # PHƯƠNG THỨC XUAT (Bạn cần thêm phần này)
    def xuat(self):
        # In ra thông tin của sản phẩm
        print(f"Tên sản phẩm: {self._ten}")
        print(f"Giá: {self._gia:,.0f} VNĐ")
        print(f"Giảm giá: {self._giam_gia * 100}%")
        # Hoặc bất kỳ thông tin nào khác bạn muốn hiển thị
        
    # Các phương thức và thuộc tính khác (nếu có)
    def get_ten(self):
        return self._ten
    def get_gia(self):
        return self._gia
    def get_giam_gia(self):
        return self._giam_gia   
      
    def set_ten(self, ten):
        self._ten = ten
    def set_gia(self, gia):
        if gia < 0:
            raise ValueError("Gia phai lon hon 0")
        else:
            self._gia = gia
    def set_giam_gia(self, giam_gia):
        self._giam_gia = giam_gia 