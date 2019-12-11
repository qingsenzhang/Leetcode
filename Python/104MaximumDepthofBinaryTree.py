# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
        
    def dfs(self, root):
        if not root:
            return 0
        
        return max(self.dfs(root.left), self.dfs(root.right)) + 1
