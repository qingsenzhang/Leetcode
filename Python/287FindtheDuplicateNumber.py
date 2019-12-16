class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[1]
        
        slow, fast = nums[0], nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
