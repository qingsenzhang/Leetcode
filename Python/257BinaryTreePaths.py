# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        if not root:
            return self.ans
        
        self.dfs(root, "")
        return self.ans
        
    def dfs(self, root, s):
        s += "->" + str(root.val)
        if not root.left and not root.right:
            self.ans.append(s[2:])
        else:
            if root.left:
                self.dfs(root.left, s)
            if root.right:
                self.dfs(root.right, s)
