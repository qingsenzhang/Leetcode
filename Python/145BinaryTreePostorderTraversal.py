class PostOrderTraversal:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
               
        ans.reverse()
        return ans# Definition for a binary tree node.
