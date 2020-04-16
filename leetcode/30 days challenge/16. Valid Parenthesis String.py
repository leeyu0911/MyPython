'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

# https://leetcode.com/articles/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []
        for i, ss in enumerate(s):
            if ss == '(':
                stack.append(i)  # 紀錄位置
            elif ss == '*':
                star_stack.append(i)  # 紀錄位置
            else:
                if ss == ')':
                    if not stack:
                        if not star_stack:
                            return False
                        else:
                            star_stack.pop()
                    else:
                        stack.pop()
        while stack and star_stack:
            if stack.pop() > star_stack.pop():
                return False
        return True




print(Solution.checkValidString(0, "(*))"))  # T
print(Solution.checkValidString(0, "(())"))  # T
print(Solution.checkValidString(0, "(*)("))  # F
print(Solution.checkValidString(0, "(*)"))  # T
print(Solution.checkValidString(0, ")"))  # F
print(Solution.checkValidString(0, "(*()"))  # T
print(Solution.checkValidString(0, "(((******))"))  # T
print(Solution.checkValidString(0, ")"))  # F
print(Solution.checkValidString(0, "((()))()(())(*()()())**(())()()()()((*()*))((*()*)"))  # T
print(Solution.checkValidString(0, "(((((()*)(*)*))())())(()())())))((**)))))(()())()"))  # F
print(Solution.checkValidString(0, "(())((())()()(*)(*()(())())())()()((()())((()))(*"))  # F
print(Solution.checkValidString(0, "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))  # T



class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:
                break
            lo = max(lo,0)

        return lo == 0