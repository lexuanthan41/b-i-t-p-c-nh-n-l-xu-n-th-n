n = int(input("Nhap n: "))

if n % 2 == 0:
    S = (n // 2) * (n // 2 + 1)
else:
    S = n * (n + 1) // 2

print("S =", S)
