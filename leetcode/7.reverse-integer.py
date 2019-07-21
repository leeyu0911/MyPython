#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.39%)
# Likes:    2281
# Dislikes: 3500
# Total Accepted:    738.1K
# Total Submissions: 2.9M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        max_n = 2147483647
        min_n = -2147483648
        if x > max_n:
            return 0
        if x < min_n:
            return 0

        x = str(x)
        y = list(str(x))

        if y[0] == '-':
            if int(''.join(y[0]) + ''.join(y[:0:-1])) < min_n:
                return 0
            return int(''.join(y[0]) + ''.join(y[:0:-1]))
        if int(''.join(y[::-1])) > max_n:
            return 0

        else:
            return int(''.join(y[::-1]))
# ✔ Accepted
#   ✔ 1032/1032 cases passed (40 ms)
#   ✔ Your runtime beats 53.11 % of python3 submissions
#   ✔ Your memory usage beats 5.45 % of python3 submissions (14 MB)