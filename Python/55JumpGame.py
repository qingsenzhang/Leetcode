class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        if len(nums) == 1:
            return True
        
        curr_far, next_far = 0, 0
        for i in range(len(nums)):
            next_far = max(next_far, i + nums[i])
            if i == curr_far:
                if next_far == curr_far:
                    return False
                elif next_far >= len(nums) - 1:
                    return True
                else:
                    curr_far = next_far        
            
        
