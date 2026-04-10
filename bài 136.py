import tkinter as tk
from tkinter import scrolledtext
import string

def analyze_text():
    text = input_text.get("1.0", tk.END)

    lines = text.strip().split("\n")
    line_count = len(lines) if text.strip() else 0

    words = text.split()
    word_count = len(words)

    freq = {ch: 0 for ch in string.ascii_uppercase}

    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            if ch in freq:
                freq[ch] += 1

    # Hiển thị kết quả
    result = f"{line_count} dòng, {word_count} từ\n\nTần số ký tự:\n"

    count = 0
    for ch in string.ascii_uppercase:
        result += f"{ch}: {freq[ch]}  "
        count += 1
        if count % 7 == 0:
            result += "\n"

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


# Tạo cửa sổ
root = tk.Tk()
root.title("Phân tích văn bản")
root.geometry("600x500")

# Ô nhập văn bản
tk.Label(root, text="Nhập văn bản:").pack()
input_text = scrolledtext.ScrolledText(root, height=10)
input_text.pack(fill="both", padx=10, pady=5)

# Nút phân tích
tk.Button(root, text="Phân tích", command=analyze_text).pack(pady=10)

# Ô hiển thị kết quả
tk.Label(root, text="Kết quả:").pack()
output_text = scrolledtext.ScrolledText(root, height=10)
output_text.pack(fill="both", padx=10, pady=5)

# Chạy chương trình
root.mainloop()
