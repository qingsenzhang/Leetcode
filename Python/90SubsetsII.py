class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        nums = sorted(nums)
        subset = []
        self.dfs(nums, 0, subset, ans)
        return ans
        
    def dfs(self, nums, index, subset, ans):
        ans.append(subset.copy())
        
        i = index
        while i < len(nums):
            if i != 0 and nums[i] == nums[i - 1] and i > index:
                i += 1
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, ans)
            subset.pop()
            i += 1

