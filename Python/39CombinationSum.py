class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        candidates.sort()
        subset = []
        self.dfs(candidates, 0, subset, ans, target)
        return ans
        
    def dfs(self, nums, index, subset, ans, target):
        if target < 0:
            return 
        
        if target == 0:
            ans.append(subset.copy())
            return
        
        i = index 
        while i < len(nums):
            if i != 0 and nums[i] == nums[i - 1] and i > index:
                i += 1
                continue
            subset.append(nums[i])
            self.dfs(nums, i, subset, ans, target - nums[i])
            subset.pop()
            i += 1
