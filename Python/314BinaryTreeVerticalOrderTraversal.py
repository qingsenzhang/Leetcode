# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        self.nodes = []
        self.dfs(root, 0, 0)
        self.nodes = sorted(self.nodes, key=lambda node: (node[1], node[2]))
        i = 0
        while i < len(self.nodes):
            level_nodes = []
            level = self.nodes[i][1]
            while i < len(self.nodes) and self.nodes[i][1] == level:
                level_nodes.append(self.nodes[i][0])
                i += 1
            ans.append(level_nodes)
        return ans
        
    def dfs(self, node, ver_level, hor_level):
        if not node:
            return 
        self.nodes.append([node.val, ver_level, hor_level])
        if node.left:
            self.dfs(node.left, ver_level - 1, hor_level + 1)
        if node.right:
            self.dfs(node.right, ver_level + 1, hor_level + 1)
