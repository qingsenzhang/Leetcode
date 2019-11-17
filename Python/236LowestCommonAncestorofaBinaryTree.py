# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _, _, ans = self.dfs(root, p, q)
        return ans
    
    def dfs(self, root, p, q):
        if not root:
            return (False, False, None)
        
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        
        if left[2]:
            return left
        elif right[2]:
            return right
        
        found_p = left[0] or right[0] or root == p
        found_q = left[1] or right[1] or root == q
        if found_p and found_q:
            return (True, True, root)
        else:
            return (found_p, found_q, None)
        
        
        
        
        
        
        
        
