class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_len = 1
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[right] > nums[right - 1]:
                right += 1
            
            max_len = max(max_len, right - left)
            left = right
            right += 1
            
        return max_len
        
