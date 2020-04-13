'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

class Solution:
    def findMaxLength(self, nums: 'List[int]') -> 'int':
        dic = {0: -1}
        diff_of01 = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                diff_of01 -= 1
            else:
                diff_of01 += 1
            if diff_of01 in dic:
                res = max(res, i - dic[diff_of01])  # 如果01個數差值相同 index相減
            else:
                dic[diff_of01] = i   # 紀錄第一次 sum 值
        return res

print(Solution.findMaxLength(0, [0,1,0,1]))
print(Solution.findMaxLength(0, [0,1,1,0,1,1,1,0]))
print(Solution.findMaxLength(0, []))

import numpy as np 
for i in range(10):
    print(np.random.randint(2, size=10))