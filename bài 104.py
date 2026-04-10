import tkinter as tk
import random

def tao_ma_tran():
    global A, n
    try:
        n = int(entry_n.get())
        A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]

        text_A.delete("1.0", tk.END)
        for row in A:
            text_A.insert(tk.END, " ".join(f"{x:4}" for x in row) + "\n")

    except:
        text_A.delete("1.0", tk.END)
        text_A.insert(tk.END, "Nhập n hợp lệ!")

def tao_B():
    try:
        B = [[0]*n for _ in range(n)]

        # đường chéo chính
        diag1 = {}
        for d in range(-(n-1), n):
            max_val = -10**9
            for i in range(n):
                j = i - d
                if 0 <= j < n:
                    max_val = max(max_val, A[i][j])
            diag1[d] = max_val

        # đường chéo phụ
        diag2 = {}
        for s in range(2*n - 1):
            max_val = -10**9
            for i in range(n):
                j = s - i
                if 0 <= j < n:
                    max_val = max(max_val, A[i][j])
            diag2[s] = max_val

        # tạo B
        for i in range(n):
            for j in range(n):
                B[i][j] = max(diag1[i - j], diag2[i + j])

        text_B.delete("1.0", tk.END)
        for row in B:
            text_B.insert(tk.END, " ".join(f"{x:4}" for x in row) + "\n")

    except:
        text_B.delete("1.0", tk.END)
        text_B.insert(tk.END, "Hãy tạo ma trận A trước!")

# Cửa sổ
root = tk.Tk()
root.title("Ma trận A → B")
root.geometry("500x450")

# Nhập n
tk.Label(root, text="Nhập bậc ma trận n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Nút tạo A
tk.Button(root, text="Tạo ma trận A", command=tao_ma_tran).pack(pady=5)

# Hiển thị A
tk.Label(root, text="Ma trận A:").pack()
text_A = tk.Text(root, height=8)
text_A.pack()

# Nút tạo B
tk.Button(root, text="Tạo ma trận B", command=tao_B).pack(pady=5)

# Hiển thị B
tk.Label(root, text="Ma trận B:").pack()
text_B = tk.Text(root, height=8)
text_B.pack()

# Chạy
root.mainloop()
