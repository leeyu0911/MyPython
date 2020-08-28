'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                try:
                    p = stack.pop()
                except IndexError:
                    return False
                if i == ')':
                    if p != '(':
                        return False
                elif i == ']':
                    if p != '[':
                        return False
                elif i == '}':
                    if p != '{':
                        return False

        return True if stack == [] else False

S = Solution()
print(S.isValid("["))


'''
Runtime: 24 ms, faster than 95.28% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 58.65% of Python3 online submissions for Valid Parentheses.
'''
