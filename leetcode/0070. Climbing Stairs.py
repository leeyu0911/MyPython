'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Limit Exceeded
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # elif n == 3:
        #     return 3
        # return self.climbStairs(n-1) + self.climbStairs(n-2)


        # Runtime: 28 ms, faster than 81.74% of Python3 online submissions for Climbing Stairs.
        # Memory Usage: 14.1 MB, less than 90.95% of Python3 online submissions for Climbing Stairs.
        dp_list = [1, 2, 3]
        for i in range(3, n):
            dp_list.append(dp_list[-2] + dp_list[-1])
        return dp_list[n-1]


        # cn_2 = 1  # 上兩個
        # cn_1 = 2  # 上一個
        # if n == 1:
        #     return cn_2
        # elif n == 2:
        #     return cn_1
        #
        # for i in range(2, n):
        #     cn = cn_2 + cn_1
        #     cn_2, cn_1 = cn_1, cn
        # return cn


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(44))
