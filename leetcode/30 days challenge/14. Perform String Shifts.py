'''
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
'''

class Solution:
    def stringShift(self, s: str, shift: 'List[List[int]]') -> 'str':
        count = 0
        for i, j in shift:
            if i == 0:
                count -= j
            else:
                count += j
        print(count)
        count = count % len(s) # 右移 x 單位等於左移 len(s) - x 單位，又python mod後皆為正數，所以左移會被轉成右移
        s = s[-count:] + s[0:-count]
        return s
        

print(Solution.stringShift(0, 'abc', [[0,1],[1,2]]))
print(Solution.stringShift(0, 'abc', [[0,3],[1,2]]))
print(Solution.stringShift(0, 'abcde', [[0,4],[1,5]]))
print(Solution.stringShift(0, 'abcdef', [[0,4],[1,6]]))
print(Solution.stringShift(0, 'abcdef', [[0,4],[1,0]]))
        
        

