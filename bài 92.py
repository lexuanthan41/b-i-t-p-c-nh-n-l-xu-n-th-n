import tkinter as tk
import random

def tao_ma_tran():
    global A, n
    try:
        n = int(entry_n.get())
        A = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]

        text_matrix.delete("1.0", tk.END)
        for row in A:
            text_matrix.insert(tk.END, " ".join(f"{x:4}" for x in row) + "\n")

    except:
        text_matrix.delete("1.0", tk.END)
        text_matrix.insert(tk.END, "Nhập n hợp lệ!")

def tim_duong_cheo():
    try:
        max_sum = -10**9
        best_diag = []

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

        result_label.config(text=f"Đường chéo max:\n{best_diag}\nTổng = {max_sum}")

    except:
        result_label.config(text="Hãy tạo ma trận trước!")

# Cửa sổ
root = tk.Tk()
root.title("Ma trận & đường chéo max")
root.geometry("450x400")

# Nhập n
tk.Label(root, text="Nhập bậc ma trận n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Nút tạo
tk.Button(root, text="Tạo ma trận", command=tao_ma_tran).pack(pady=5)

# Hiển thị ma trận
text_matrix = tk.Text(root, height=10)
text_matrix.pack()

# Nút tìm
tk.Button(root, text="Tìm đường chéo max", command=tim_duong_cheo).pack(pady=5)

# Kết quả
result_label = tk.Label(root, text="Kết quả:", fg="blue")
result_label.pack()

# Chạy
root.mainloop()
