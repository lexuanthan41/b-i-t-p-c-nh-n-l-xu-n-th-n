import tkinter as tk

def phan_tich():
    try:
        n = int(entry.get())
        if n <= 1:
            result_label.config(text="Nhập n > 1")
            return

        temp = n
        i = 2
        result = ""

        while i * i <= temp:
            while temp % i == 0:
                result += str(i)
                temp //= i
                if temp > 1:
                    result += " * "
            i += 1

        if temp > 1:
            result += str(temp)

        result_label.config(text=f"{n} = {result}")

    except:
        result_label.config(text="Nhập số hợp lệ!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Phân tích số nguyên tố")
root.geometry("350x200")

# Nhập n
tk.Label(root, text="Nhập n:").pack()
entry = tk.Entry(root)
entry.pack()

# Nút thực hiện
tk.Button(root, text="Phân tích", command=phan_tich).pack(pady=10)

# Hiển thị kết quả
result_label = tk.Label(root, text="Kết quả:", fg="blue")
result_label.pack()

# Chạy chương trình
root.mainloop()
