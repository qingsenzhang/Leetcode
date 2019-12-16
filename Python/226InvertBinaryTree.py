# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.right and not root.left):
            return root
        
        left, right = self.invertTree(root.left), self.invertTree(root.right)
        
        root.left, root.right = right, left
        return root
        
