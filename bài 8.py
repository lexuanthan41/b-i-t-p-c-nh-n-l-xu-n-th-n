import tkinter as tk
import math

def giai_pt():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            result_label.config(text="Đây không phải PT bậc 2")
            return

        delta = b*b - 4*a*c

        if delta < 0:
            result_label.config(text="Vô nghiệm")
        elif delta == 0:
            x = -b / (2*a)
            result_label.config(text=f"Nghiệm kép x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            result_label.config(text=f"x1 = {x1}\nx2 = {x2}")

    except:
        result_label.config(text="Nhập sai dữ liệu!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Giải phương trình bậc 2")
root.geometry("350x250")

# Nhập a
tk.Label(root, text="Nhập a:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

# Nhập b
tk.Label(root, text="Nhập b:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

# Nhập c
tk.Label(root, text="Nhập c:").pack()
entry_c = tk.Entry(root)
entry_c.pack()

# Nút giải
tk.Button(root, text="Giải", command=giai_pt).pack(pady=10)

# Hiển thị kết quả
result_label = tk.Label(root, text="Kết quả:", fg="blue")
result_label.pack()

# Chạy chương trình
root.mainloop()
