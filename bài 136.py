import sys
import string

line_count = 0
word_count = 0

# Tần số A-Z
freq = {ch: 0 for ch in string.ascii_uppercase}

print("Nhap van ban (Ctrl+Z de ket thuc):")

for line in sys.stdin:
    line_count += 1

    # Đếm từ
    words = line.split()
    word_count += len(words)

    # Đếm ký tự
    for ch in line:
        if ch.isalpha():
            freq[ch.upper()] += 1

# In kết quả
print(f"{line_count} hang, {word_count} tu, voi tan so cac ky tu:")

count = 0
for ch in string.ascii_uppercase:
    print(f"{ch}: {freq[ch]}", end=" ")
    count += 1
    if count % 7 == 0:
        print()
