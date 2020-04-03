'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        c = [0] * len(nums)
        
        for i in range(len(nums)):
            try:
                if (c[i-1] + nums[i]) > nums[i]:
                    c[i] = c[i-1] + nums[i]
                else:
                    c[i] = nums[i]
            except IndexError:
                c[i] = nums[i]

        return max(c)


print(Solution.maxSubArray(0, [-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray(0, [-2,-1]))
