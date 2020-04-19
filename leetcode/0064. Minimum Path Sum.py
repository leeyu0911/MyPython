'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

import numpy as np

class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        g = np.array(grid)  # path
        Q = np.zeros(g.shape, 'int32') # vertex
        m = g.shape[0]
        n = g.shape[1]

        Q[0][0] = g[0][0]
        for i in range(1, n):
            Q[0][i] = Q[0][i-1] + g[0][i]

        for i in range(1, m):
            Q[i][0] = Q[i-1][0] + g[i][0]

        for i in range(1, m):
            for j in range(1, n):
                Q[i][j] = min(Q[i-1][j], Q[i][j-1]) + g[i][j]

        return Q[-1][-1]


l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
l1 = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution.minPathSum(Solution, l1))