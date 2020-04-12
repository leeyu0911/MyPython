'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # self.depth = [0, 0] AttributeError: 'int' object has no attribute 'depth'

        '''
        想法：
        self.depth[0]代表左子樹之最長鍊（深度），self.depth[1]代表右子樹之最長鍊
        sum(self.depth)即經過該node之最長diameter
        '''

# You are here! Your runtime beats 96.53 % of python3 submissions.
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0

        def dfs_recode_depth(record_data, t):
            # 單邊為空
            if t == None:
                return [-1, -1]    # 不知為啥賽出來的值

            # 雙邊為空
            if t.left == None and t.right == None:
                return [0, 0]
            
            l = dfs_recode_depth(record_list, t.left)
            r = dfs_recode_depth(record_list, t.right)
            record_data.append(sum([max(l) + 1, max(r) + 1]))  # 紀錄每個 node 之非0 diameter
            return [max(l) + 1, max(r) + 1]

        record_list = [0]  # 如果為空樹 先塞0預防list為空
        dfs_recode_depth(record_list, root)
        return max(record_list) # 整棵樹最長diameter

            
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
print(Solution.diameterOfBinaryTree(0, t1))

t0 = TreeNode(None)
print(Solution.diameterOfBinaryTree(0, None))

[1,2]
t1 = TreeNode(1)
t2 = TreeNode(2)
t1.left = t2
print(Solution.diameterOfBinaryTree(0, t1))


# Approach #1: Depth-First Search [Accepted] Analysis written by: @awice.
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1