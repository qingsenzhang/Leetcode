class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = reversed(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        return
    
        nums.reverse()
        
