import tkinter as tk

def xu_ly():
    try:
        A = list(map(int, entry_A.get().split()))
        B = list(map(int, entry_B.get().split()))

        n = len(A)
        m = len(B)

        # 🔹 Tìm B trong A
        found = -1
        for i in range(n - m + 1):
            if A[i:i+m] == B:
                found = i
                break

        if found != -1:
            kq1 = f"B có trong A tại vị trí A[{found}]"
        else:
            kq1 = "B không có trong A"

        # 🔹 Tìm số âm cuối cùng
        so_am = None
        for x in reversed(A):
            if x < 0:
                so_am = x
                break

        if so_am is not None:
            kq2 = f"Số âm cuối: {so_am}"
        else:
            kq2 = "Không có số âm trong A"

        result_label.config(text=kq1 + "\n" + kq2)

    except:
        result_label.config(text="Nhập sai dữ liệu!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Xử lý mảng A và B")
root.geometry("400x250")

# Nhập A
tk.Label(root, text="Nhập mảng A (cách nhau bằng dấu cách):").pack()
entry_A = tk.Entry(root, width=40)
entry_A.pack()

# Nhập B
tk.Label(root, text="Nhập mảng B (cách nhau bằng dấu cách):").pack()
entry_B = tk.Entry(root, width=40)
entry_B.pack()

# Nút xử lý
tk.Button(root, text="Xử lý", command=xu_ly).pack(pady=10)

# Hiển thị kết quả
result_label = tk.Label(root, text="Kết quả:", fg="blue")
result_label.pack()

# Chạy chương trình
root.mainloop()
