class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Chèn node vào BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# In BST theo thứ tự tăng (inorder)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Tìm node nhỏ nhất trong cây con
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Xóa node trong BST
def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # Node có 1 hoặc 0 con
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node có 2 con: thay bằng giá trị nhỏ nhất bên phải
        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root

# Nhập dữ liệu
root = None
print("Nhap cac gia tri (0 de dung):")
while True:
    x = int(input())
    if x == 0:
        break
    root = insert(root, x)

print("In BST theo thu tu tang:", end=" ")
inorder(root)
print()

# Nhập giá trị cần xóa
k = int(input("Nhap k: "))
root = delete_node(root, k)

print("Sau khi xoa:", end=" ")
inorder(root)
print()
