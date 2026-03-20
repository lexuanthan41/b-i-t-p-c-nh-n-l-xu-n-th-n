import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("Vô nghiệm")
elif delta == 0:
    x = -b / (2*a)
    print("Nghiệm kép x =", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 =", x1)
    print("x2 =", x2)
