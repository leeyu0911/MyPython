'''
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print(s.addBinary("1010", "1011"))


# 294 / 294 test cases passed.
# Runtime: 24 ms, faster than 98.00% of Python3 online submissions for Add Binary.
# Memory Usage: 13.9 MB, less than 99.08% of Python3 online submissions for Add Binary.
