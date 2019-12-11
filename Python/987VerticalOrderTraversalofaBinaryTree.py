# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        if not root:
            return self.ans
        
        self.dfs(root, 0, 0)
        self.ans = sorted(self.ans, key=lambda node: (node[0],node[1],node[2]))
        
        ptr = 0
        ans = []
        while ptr < len(self.ans):
            toAdd = []
            level = self.ans[ptr][0]
            while ptr < len(self.ans) and self.ans[ptr][0] == level:
                toAdd.append(self.ans[ptr][2])
                ptr += 1
            ans.append(toAdd)
        return ans
            
    def dfs(self, root, level, depth):
        if not root:
            return 
        
        self.ans.append([level, depth, root.val])
            
        self.dfs(root.left, level - 1, depth + 1)
        self.dfs(root.right, level + 1, depth + 1)
