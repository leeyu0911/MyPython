'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if len(grid) < 1:
            return 0

        def dfs(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n -1 or grid[i][j] == '0':  # 邊界條件 
                return
            
            grid[i][j] = '0'
            
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
                

        self.ans = 0
        m = len(grid)  # row
        n = len(grid[0])  # col

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.ans += 1
                    dfs(i, j)
                else:
                    continue

        return self.ans



l = [["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
print(Solution.numIslands(Solution,l))  





