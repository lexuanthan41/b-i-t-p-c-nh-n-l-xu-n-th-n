# Định nghĩa Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Hàm chèn node vào danh sách tăng dần
def insert_sorted(head, value):
    new_node = Node(value)
    # Nếu danh sách rỗng hoặc giá trị nhỏ hơn head
    if head is None or value < head.data:
        new_node.next = head
        return new_node

    # Duyệt tìm vị trí thích hợp
    current = head
    while current.next and current.next.data < value:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

# Hàm hiển thị danh sách
def print_list(head):
    current = head
    while current:
        print(f"[{current.data}]", end="")
        current = current.next
    print()

# Nhập danh sách ban đầu
head = None
print("Nhap cac gia tri (0 de dung):")
while True:
    x = int(input())
    if x == 0:
        break
    head = insert_sorted(head, x)

print("List goc:", end=" ")
print_list(head)

# Nhập giá trị mới
value = int(input("Nhap tri moi: "))
head = insert_sorted(head, value)

print("List moi:", end=" ")
print_list(head)
