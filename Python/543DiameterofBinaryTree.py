# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
        
        
    def depth(self, root):
        if not root:
            return 0
        
        left, right = self.depth(root.left), self.depth(root.right)
        self.diameter = max(self.diameter, left + right)
        
        return max(left, right) + 1
        
        
