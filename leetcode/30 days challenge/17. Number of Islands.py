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



l1 = [["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
print(Solution.numIslands(Solution,l1))  

l2 = \
[["0","1","0","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","1","0","0"]]
print(Solution.numIslands(Solution,l2)) 

# https://leetcode.com/problems/number-of-islands/discuss/584203/Python-3-implementation-99-faster
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        
        if nr==0  :
            return 0
        
        nc = len(grid[0])
        
        num_islands = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands+=1
                    self.dfs(grid, r,c)
                    
        return num_islands
    
    def dfs(self, grid: List[List[str]], r: int, c: int) :
        nr = len(grid)
        nc = len(grid[0])
        
        grid[r][c] = "0"
        
        if r-1 >= 0 and grid[r-1][c]=="1":
            self.dfs(grid, r-1, c)
        if r+1 <  nr and grid[r+1][c]=="1":   
            self.dfs(grid, r+1, c)
        if c-1 >= 0 and grid[r][c-1]=="1":   
            self.dfs(grid, r, c-1)
        if c+1 <  nc and grid[r][c+1]=="1":   
            self.dfs(grid, r, c+1)
