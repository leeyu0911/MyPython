def Josephus_Problem(n, k):
    '''
    n=總人數
    k=間格人數
    index從0開始
    返回值為最後一個存活index
    '''
    if n == 1:
        return 0
    return (Josephus_Problem(n-1, k) + k) % n


print(Josephus_Problem(2, 9))
print(Josephus_Problem(30, 9))
print(Josephus_Problem(5, 2))
print()


# 修改自維基百科
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linkList(n):
    head = Node(1)
    pre = head
    for i in range(2, n+1):
        newNode = Node(i)
        pre.next = newNode
        pre = newNode
    pre.next = head
    return head


def Josephus_Problem_list(n, m):
    """
    印出所有次序
    index從1開始
    """
    killed_list = []
    if m == 1:  # 如果是1的話，直接輸出
        killed_list = [i for i in range(1, n)]
        print(killed_list)
    else:
        head = create_linkList(n)  # 起始位置
        pre = None
        cur = head  # 目前位置 數到哪裡的指標
        while cur.next != cur:  # 終止條件是節點的下一個節點指向本身 也就是只剩下最後一位
            for i in range(m-1):
                pre = cur
                cur = cur.next
            killed_list.append(cur.value)
            pre.next = cur.next
            cur.next = None
            cur = pre.next
        killed_list.append(cur.value)
        print(killed_list)


Josephus_Problem_list(5, 2)
Josephus_Problem_list(30, 9)
