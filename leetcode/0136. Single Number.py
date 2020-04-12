'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return nums[0]

        # count_arr = [0] * len(nums)

        # for i in nums:
        #     count_arr[i] += 1
        # print(count_arr)
        # return [count_arr.index(i) for i in count_arr if i == 1][0]

        dic = dict()
        dic2 = dict()
        for i in nums:
            dic[i] = 0
        for i in nums:
            dic[i] += 1
        for i, j in dic.items():
            dic2[j] = i
        return dic2.get(1)



print(Solution.singleNumber(0, [4,1,2,1,2]))
print(Solution.singleNumber(0, [1]))
print(Solution.singleNumber(0, [-1,-1,-2]))  

[i for i in range(3) if i ==1][0]