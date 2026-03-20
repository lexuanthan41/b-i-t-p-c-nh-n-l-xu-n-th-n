# Các hàm xử lý menu
def them():
    print("Ban da chon: Them sinh vien")

def doc():
    print("Ban da chon: Doc danh sach sinh vien")

def sua():
    print("Ban da chon: Sua thong tin sinh vien")

def thoat():
    print("Thoat chuong trinh")
    exit()

# Mảng (danh sách) các con trỏ hàm
menu_actions = [them, doc, sua, thoat]

# Chương trình chính
while True:
    print("\nMENU (File 'STUDENT.DAT')")
    print("----")
    print("[1]. Them")
    print("[2]. Doc")
    print("[3]. Sua")
    print("[4]. Thoat")
    
    try:
        choice = int(input("Chon tac vu: "))
        if 1 <= choice <= 4:
            # Gọi hàm tương ứng
            menu_actions[choice - 1]()
        else:
            print("Lua chon khong hop le. Vui long chon 1-4.")
    except ValueError:
        print("Vui long nhap so nguyen tu 1 den 4.")
