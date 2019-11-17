class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        curr = 0
        while curr <= right:
            if nums[curr] == 0:
                self.swap(left, curr, nums)
                left += 1
                curr += 1
            elif nums[curr] == 2:
                self.swap(right, curr, nums)
                right -= 1
            else:
                curr += 1
    
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
