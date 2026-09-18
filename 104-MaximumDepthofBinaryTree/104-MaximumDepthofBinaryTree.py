# Last updated: 9/19/2026, 12:07:20 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: TreeNode | None) -> int:
9        if not root:
10            return 0
11        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))