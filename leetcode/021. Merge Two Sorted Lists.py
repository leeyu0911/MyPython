'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode(0)
        t = new_list
        t1 = l1 
        t2 = l2
        while t1 != None and t2 != None:
            if t1.val > t2.val:
                t.next = t2
                t2 = t2.next
                t = t.next
            else:
                t.next = t1
                t1 = t1.next
                t = t.next

        while t1 != None:
            t.next = t1
            t1 = t1.next
            t = t.next
        while t2 != None:
            t.next = t2
            t2 = t2.next
            t = t.next

        return new_list.next


ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(4)

ll2 = ListNode(1)
ll2.next = ListNode(3)
ll2.next.next = ListNode(4)

t1 = ll1
t2 = ll2

print(Solution.mergeTwoLists(0, ll1, ll2))




        