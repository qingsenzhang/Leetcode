# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        
        if self.compare(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def compare(self, s, t):
        if not s and not t:
            return True
        elif s and not t or t and not s or s.val != t.val:
            return False
        
        return self.compare(s.left, t.left) and self.compare(s.right, t.right)
