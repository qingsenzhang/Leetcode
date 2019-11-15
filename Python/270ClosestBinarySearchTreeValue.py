# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = root.val
        while root:
            ans = root.val if abs(root.val - target) < abs(target - ans) else ans
            root = root.right if target > root.val else root.left
            
        return ans
