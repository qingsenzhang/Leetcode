# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if not node:
                break
            dq.append(node.left)
            dq.append(node.right)
            
        for node in dq:
            if node:
                return False
            
        return True
            
        
