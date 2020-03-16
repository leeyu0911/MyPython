class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_circular_linklist(n):
    # 創建連續整數n個環狀串列
    head = Node(1)
    pre = head
    for i in range(2, n+1):
        new_node = Node(i)
        pre.next = new_node
        pre = new_node
    pre.next = head
    return head

head = create_circular_linklist(3)
print(head.next.value)

