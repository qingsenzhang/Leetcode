class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums or len(nums) == 0:
            return [[]]
            
        permutation = []
        visited = [False for i in nums]
        self.permutations(nums, visited, permutation, ans)
        return ans
        
    def permutations(self, nums, visited, permutation, ans):
        if len(permutation) == len(nums):
            ans.append(permutation.copy())
            return
        
        i = 0
        while i < len(nums):
            if visited[i]:
                i += 1
                continue
            permutation.append(nums[i])
            visited[i] = True
            self.permutations(nums, visited, permutation, ans)
            permutation.pop()
            visited[i] = False
            i += 1

        
