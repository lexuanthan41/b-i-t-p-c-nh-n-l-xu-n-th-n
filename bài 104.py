import random

# Nhập n
n = int(input("Nhap bac ma tran: "))

# Tạo ma trận A
A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

# Xuất ma trận A
for row in A:
    for x in row:
        print(f"{x:4}", end="")
    print()

# Tạo ma trận B
B = [[0]*n for _ in range(n)]

# Tiền xử lý: max đường chéo chính (i - j)
diag1 = {}
for d in range(-(n-1), n):
    max_val = -10**9
    for i in range(n):
        j = i - d
        if 0 <= j < n:
            max_val = max(max_val, A[i][j])
    diag1[d] = max_val

# Tiền xử lý: max đường chéo phụ (i + j)
diag2 = {}
for s in range(2*n - 1):
    max_val = -10**9
    for i in range(n):
        j = s - i
        if 0 <= j < n:
            max_val = max(max_val, A[i][j])
    diag2[s] = max_val

# Tạo B
for i in range(n):
    for j in range(n):
        B[i][j] = max(diag1[i - j], diag2[i + j])

# Xuất ma trận B
print("Ma tran B:")
for row in B:
    for x in row:
        print(f"{x:4}", end="")
    print()
