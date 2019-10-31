class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        nums.sort()
        subset = []
        self.dfs(nums, 0, subset, ans)
        return ans
        
    def dfs(self, nums, index, subset, ans):
        ans.append(subset.copy())
        
        while index < len(nums):
            subset.append(nums[index])
            self.dfs(nums, index + 1, subset, ans)
            subset.pop()
            index += 1
