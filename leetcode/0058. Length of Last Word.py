'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_list = s.split(' ')
        new_list = [ss for ss in new_list if ss != '']
        return len(new_list[-1]) if len(new_list) != 0 else 0


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord(" "))
print(s.lengthOfLastWord("b   a    "))


# 58 / 58 test cases passed.
# Runtime: 20 ms, faster than 98.70% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.5 MB, less than 7.28% of Python3 online submissions for Length of Last Word.
