'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        # dp = [[0] * n] * m  # 這樣宣告在 dp[i][j] = dp[i - 1][j - 1] + 1 時會一次改掉一整個column
        dp = [[0 for i in range(n)] for j in range(m)]  # 其實只要開兩行就可以

        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]



s = Solution()
t1 = 'bl'
t2 = 'yby'
print(s.longestCommonSubsequence(t1, t2))

t1 = 'pmjghexybyrgzczy'
t2 = 'hafcdqbgncrcbihkd'
print(s.longestCommonSubsequence(t1, t2))


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)  # n > m
        table = [0] * (m + 1)
        prev_table = [0] * (m + 1)
        for c1 in text1:
            for i, c2 in enumerate(text2):
                table[i + 1] = max(prev_table[i] + 1 if c1 == c2 else prev_table[i + 1], table[i])
            table, prev_table = prev_table, table
        return prev_table[-1]