'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        temp = ListNode(head.val)
        temp_head = temp

        while head.next is not None:
            if head.val != head.next.val:
                temp.next = head.next
                temp = temp.next
                head = head.next
            else:
                head = head.next
        temp.next = None
        return temp_head
        # Runtime: 40 ms, faster than 80.61% of Python3 online submissions for Remove Duplicates from Sorted List.
        # Memory Usage: 14.4 MB, less than 28.05% of Python3 online submissions for Remove Duplicates from Sorted List.




head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

s = Solution()
answer1 = s.deleteDuplicates(head)


