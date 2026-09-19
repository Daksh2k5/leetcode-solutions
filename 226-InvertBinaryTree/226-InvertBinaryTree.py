# Last updated: 9/19/2026, 11:25:44 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
9        if not root:
10            return None
11        
12        temp=root.left
13        root.left=root.right
14        root.right=temp
15
16        self.invertTree(root.left)
17        self.invertTree(root.right)
18
19        return root