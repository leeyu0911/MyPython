'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i

        return i + 1


'''
Runtime: 48 ms, faster than 82.84% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.5 MB, less than 54.63% of Python3 online submissions for Search Insert Position.
'''

S = Solution()
print(S.searchInsert([1,3,5,6], 7))