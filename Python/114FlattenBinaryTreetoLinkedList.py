# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        else:
            self.dfs(root)
        
    def dfs(self, root):
        if not root.left and not root.right:
            return root
        elif not root.left:
            root.right = self.dfs(root.right)
            return root
        elif not root.right:
            root.right = self.dfs(root.left)
            root.left = None
            return root
        else:
            right = root.right
            root.right = self.dfs(root.left)
            root.left = None
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = self.dfs(right)
            return root
            
        
