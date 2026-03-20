from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu không được bằng 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    # Rút gọn phân số và chuẩn hóa mẫu dương
    def rut_gon(self):
        g = gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g
        if self.mau < 0:
            self.tu = -self.tu
            self.mau = -self.mau

    # Phép cộng
    def __add__(self, other):
        return PhanSo(self.tu * other.mau + other.tu * self.mau,
                      self.mau * other.mau)

    # Phép trừ
    def __sub__(self, other):
        return PhanSo(self.tu * other.mau - other.tu * self.mau,
                      self.mau * other.mau)

    # Phép nhân
    def __mul__(self, other):
        return PhanSo(self.tu * other.tu, self.mau * other.mau)

    # Phép chia
    def __truediv__(self, other):
        if other.tu == 0:
            raise ValueError("Không thể chia cho 0")
        return PhanSo(self.tu * other.mau, self.mau * other.tu)

    # Xuất phân số
    def __str__(self):
        return f"{self.tu}/{self.mau}"


# Hàm nhập phân số
def nhap_phan_so():
    tu, mau = map(int, input("Nhap tu so va mau so: ").split())
    return PhanSo(tu, mau)


# Chương trình chính
a = nhap_phan_so()
b = nhap_phan_so()

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
