'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.



Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
countAndSay(5) = say "1211" = one 1 + one 2 + two 1 = "11" + "12" + "21" = "111221"


Constraints:

1 <= n <= 30
'''


class Solution:
    def sub_func(self, n):
        s = ''
        c = 1
        point = n[0]
        for i in range(1, len(n)):
            if n[i] == point:
                c += 1
            else:
                s += str(c) + n[i-1]
                # 重置
                point = n[i]
                c = 1

        s += str(c) + n[i]
        return s

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            return self.sub_func(self.countAndSay(n-1))


input_str = '1'
s = Solution()
print(s.sub_func(input_str))
print(s.countAndSay(5))


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.3 MB

# Runtime: 36 ms, faster than 96.02% of Python3 online submissions for Count and Say.
# Memory Usage: 14.3 MB, less than 51.72% of Python3 online submissions for Count and Say.

