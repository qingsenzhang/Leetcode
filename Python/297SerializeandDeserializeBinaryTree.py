# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        if not root:
            return ans
        self.root = root
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if node:
                ans += str(node.val) + " "
                dq.append(node.left)
                dq.append(node.right)
            else:
                ans += "* "
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == "*":
            return None
        if len(data) == 1:
            return TreeNode(int(data[0]))
        
        nodes = []
        for val in data.split():
            if val != "*":
                nodes.append(TreeNode(int(val)))
            else:
                nodes.append(None)
                
        nodes = collections.deque(nodes)
        root = nodes.popleft()
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            left = nodes.popleft()
            right = nodes.popleft()
            node.left, node.right = left, right
            if left:
                dq.append(left)
            if right:
                dq.append(right)
                
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
