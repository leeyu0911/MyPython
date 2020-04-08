'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = [int(i) for i in str(n)]
        
        if n in (1, 7):
            return True
        elif n in (2, 3, 4, 5, 6, 8, 9):
            return False
        
        while len(arr) != 1:
            sum = 0
            for i in range(len(arr)):
                sum += arr.pop() ** 2
            arr = [int(i) for i in str(sum)]
            
        return True if sum in (1, 7) else False


print(Solution.isHappy(0, 19))
print(Solution.isHappy(0, 1))
print(Solution.isHappy(0, 2))
print(Solution.isHappy(0, 4))
print(Solution.isHappy(0, 1111111))