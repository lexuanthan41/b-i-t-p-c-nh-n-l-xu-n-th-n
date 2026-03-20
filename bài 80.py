# Nhập n
while True:
    n = int(input("Nhap n [1, 99]: "))
    if 1 <= n <= 99:
        break

# Nhập mảng A
print(f"Nhap {n} phan tu mang A:")
A = list(map(int, input().split()))

# Nhập m
while True:
    m = int(input(f"Nhap m [1, {n}]: "))
    if 1 <= m <= n:
        break

# Nhập mảng B
print(f"Nhap {m} phan tu mang B:")
B = list(map(int, input().split()))

# 🔹 Tìm vị trí xuất hiện đầu tiên của B trong A
found = -1

for i in range(n - m + 1):
    if A[i:i+m] == B:
        found = i
        break

if found != -1:
    print(f"B co trong A tai: A[{found}]")
else:
    print("B khong co trong A")

# 🔹 Tìm số nguyên âm cuối cùng
so_am = None

for x in reversed(A):
    if x < 0:
        so_am = x
        break

if so_am is not None:
    print("So nguyen am cuoi:", so_am)
else:
    print("Khong co so am trong mang A")
