# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return node.val
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)
