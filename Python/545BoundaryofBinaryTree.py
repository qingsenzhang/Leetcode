# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.root = root
        if not root:
            return self.ans
        
        self.ans.append(root.val)
        self.left_dfs(root.left)
        self.boundary(root)
        self.right_dfs(root.right)
        
        return self.ans
        
    def left_dfs(self, root):
        if not root or not root.left and not root.right:
            return 
        
        self.ans.append(root.val)
        if root.left:
            self.left_dfs(root.left)
        else:
            self.left_dfs(root.right)
        
    def boundary(self, root):
        if not root:
            return 
        
        if root != self.root and not root.left and not root.right:
            self.ans.append(root.val)
            
        self.boundary(root.left)
        self.boundary(root.right)
        
    def right_dfs(self, root):
        if not root or not root.left and not root.right:
            return
        
        if root.right:
            self.right_dfs(root.right)
        else:
            self.right_dfs(root.left)
            
        self.ans.append(root.val)
