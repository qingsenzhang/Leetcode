class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        ans = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), ans, target)
        return ans
        
    def dfs(self, nums, tmp, curr, last, ans, target):
        if not nums:
            if curr == target:
                ans.append(tmp)
            return
        else:
            for i in range(1, len(nums) + 1):
                val = nums[:i]
                if i == 1 or (i > 1 and nums[0] != '0'):
                    self.dfs(nums[i:], tmp + '+' + val, curr + int(val), int(val), ans, target)
                    self.dfs(nums[i:], tmp + '-' + val, curr - int(val), -int(val), ans, target)
                    self.dfs(nums[i:], tmp + '*' + val, curr - last + last * int(val), last * int(val), ans, target)
