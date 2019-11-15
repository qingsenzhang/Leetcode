# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root or not root.left and not root.right:
            return True
        else:
            self.isValid = True
            self.dfs(root)
            return self.isValid
        
    def dfs(self, root):
        if not root.left and not root.right:
            return (root.val, root.val)
        
        if root.left:
            l_max, l_min = self.dfs(root.left)
            if l_max >= root.val:
                self.isValid = False
        if root.right:
            r_max, r_min = self.dfs(root.right)
            if r_min <= root.val:
                self.isValid = False
                
        if root.left and root.right:
            return (max(l_max, r_max, root.val), min(l_min, r_min, root.val))
        elif root.left:
            return (max(l_max, root.val), min(l_min, root.val))
        else:
            return (max(r_max, root.val), min(r_min, root.val))
