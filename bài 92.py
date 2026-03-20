import random

# Nhập n
n = int(input("Nhap bac ma tran: "))

# Tạo ma trận
A = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]

# Xuất ma trận
for row in A:
    for x in row:
        print(f"{x:4}", end="")
    print()

# 🔹 Tìm đường chéo song song có tổng lớn nhất
max_sum = -10**9
best_diag = []

# d = i - j
for d in range(-(n-1), n):
    diag = []
    s = 0
    for i in range(n):
        j = i - d
        if 0 <= j < n:
            diag.append(A[i][j])
            s += A[i][j]

    if s > max_sum:
        max_sum = s
        best_diag = diag

# In kết quả
print("Duong cheo co tong lon nhat:")
print(*best_diag, ":", max_sum)
