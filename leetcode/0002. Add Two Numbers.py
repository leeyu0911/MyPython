'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def tranform_to_int(l):
        # l 轉成正常數字
        n = ''
        p = l
        while p is not None:
            n += str(p.val)
            if p.val is not None:
                p = p.next

        return int(n[::-1])

    @staticmethod
    def int_to_ListNode(n):
        # 結果轉成ListNode
        n = list(str(n))
        ln = ListNode(n.pop())
        p = ln
        while n:
            p.next = ListNode(n.pop())
            p = p.next
        return ln

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.tranform_to_int(l1)
        n2 = self.tranform_to_int(l2)

        return self.int_to_ListNode(n1 + n2)


l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))

s = Solution()
l3 = s.addTwoNumbers(l1, l2)

# print test
p = l3
while p is not None:
    print(p.val)
    p = p.next

'''
Runtime: 60 ms, faster than 98.54% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 52.41% of Python3 online submissions for Add Two Numbers.
'''