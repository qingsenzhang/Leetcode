# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_sum = -sys.maxsize
        self.dfs(root)
        return self.max_sum
        
    def dfs(self, root):
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.max_sum = max(self.max_sum, left + right + root.val, root.val)
        return root.val + max(left, right)
        
