"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution1(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        elif not root.left and not root.right:
            root.left, root.right = root, root
            return root
        
        self.inorder = [] 
        self.inorder_dfs(root)
        self.inorder = [Node(val, None, None) for val in self.inorder]
        for i in range(len(self.inorder) - 1):
            self.inorder[i].right = self.inorder[i+1]
        for i in range(len(self.inorder) - 1, 0, -1):
            self.inorder[i].left = self.inorder[i-1]
        self.inorder[0].left = self.inorder[-1]
        self.inorder[-1].right = self.inorder[0]
        return self.inorder[0]
        
    def inorder_dfs(self, root):
        if not root:
            return 
        
        self.inorder_dfs(root.left)
        self.inorder.append(root.val)
        self.inorder_dfs(root.right)
        
