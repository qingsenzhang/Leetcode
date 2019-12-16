# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, TreeNode(-sys.maxsize)
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            
            if not self.first and self.prev.val >= root.val:
                self.first = self.prev
            if self.first and self.prev.val >= root.val:
                self.second = root
                
            self.prev = root
            dfs(root.right)
            
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
