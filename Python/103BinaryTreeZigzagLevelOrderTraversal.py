# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        ltr = True
        dq = collections.deque([root])
        while dq:
            level = []
            l = len(dq)
            for i in range(l):
                node = dq.popleft()
                if node:
                    dq.append(node.left)
                    dq.append(node.right)
                    level.append(node.val)
                
            if ltr:
                if level:
                    ans.append(level)
            else:
                if level:
                    level.reverse()
                    ans.append(level)
            ltr = not ltr
            
        return ans
