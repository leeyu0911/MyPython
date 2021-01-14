'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, inverse_i in enumerate(reversed(range(len(digits)))):
            num += digits[inverse_i] * 10 ** i
        if num == 0:
            return [0 for i in range(len(digits) - 1)] + [1]
        num += 1
        output = []
        while num > 0:
            num, remainder = divmod(num, 10)
            output.append(remainder)
        output.reverse()
        return output



input = [0,0,0]
s = Solution()
output = s.plusOne(input)
print(output)


# Submission Detail
# 114 / 114 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14.2 MB
