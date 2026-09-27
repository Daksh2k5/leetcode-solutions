# Last updated: 9/19/2026, 1:58:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.i=0
10
11        def dfs(curr):
12            if not curr:
13                return 0
14            
15            left=dfs(curr.left)
16            right=dfs(curr.right)
17
18            self.i=max(self.i,(left+right))
19            return 1+ max(left,right)
20
21        dfs(root)
22        return self.i