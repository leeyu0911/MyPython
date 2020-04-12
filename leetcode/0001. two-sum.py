#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.30%)
# Likes:    11163
# Dislikes: 381
# Total Accepted:    1.9M
# Total Submissions: 4.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = dict()
        for i in nums:
            if target - i in nums:
                if nums.index(i) != nums.index(target - i):
                    return nums.index(i), nums.index(target - i)
                elif target - i == i and (nums.count(i) > 1):
                    return nums.index(i), nums.index(target - i, nums.index(i)+1)

        
# ✔ Accepted
#   ✔ 29/29 cases passed (800 ms)
#   ✔ Your runtime beats 33.35 % of python3 submissions
#   ✔ Your memory usage beats 74.57 % of python3 submissions (13.8 MB)
