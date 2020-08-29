'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        shortist_str = strs[0]
        for s in strs:
            if len(s) < len(shortist_str):
                shortist_str = s

        count = 0
        flag = 1
        n = len(strs)
        for i, s in enumerate(shortist_str):
            for j in range(n):
                if s != strs[j][i]:
                    flag = 0
                    break
            if flag == 0:
                break
            elif j == n-1:
                count += 1

        return strs[0][:count] if count != 0 else ''


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(['pqwoe', 'diikdwo', 'sjjd']))
print(s.longestCommonPrefix([]))

'''
Runtime: 32 ms, faster than 85.93% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 15.92% of Python3 online submissions for Longest Common Prefix.
'''