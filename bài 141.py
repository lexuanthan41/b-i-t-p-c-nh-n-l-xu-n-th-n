def dan_so(n):
    if n == 0:
        return 8_000_000_000  # 8 tỷ
    return dan_so(n - 1) * 1.025

# Tính năm 2010 (sau 10 năm)
result = dan_so(10)

print(int(result), "nguoi")
