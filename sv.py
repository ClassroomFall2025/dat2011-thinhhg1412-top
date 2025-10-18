class SinhVien:

    def __init__(self, tensv, namsinh, truonghoc):
        self.ten_sinh_vien = tensv
        self.nam_sinh = namsinh
        self.truong = truonghoc
    

    def __str__(self):
        return f"sinh viên (self.__ten_sinh_vien) sinh năm "