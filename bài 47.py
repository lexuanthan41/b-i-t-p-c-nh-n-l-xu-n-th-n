import tkinter as tk

def tinh_tong():
    try:
        n = int(entry.get())
        S = n * (n + 1) // 2
        result_label.config(text=f"S = {S}")
    except:
        result_label.config(text="Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tính tổng từ 1 đến n")
root.geometry("300x200")

# Nhập n
label = tk.Label(root, text="Nhập n:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Nút tính
btn = tk.Button(root, text="Tính", command=tinh_tong)
btn.pack()

# Hiển thị kết quả
result_label = tk.Label(root, text="S = ")
result_label.pack()

# Chạy chương trình
root.mainloop()
