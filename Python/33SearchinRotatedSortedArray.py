class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1
         
        min_idx = self.findMin(nums)
        if nums[min_idx] <= target <= nums[-1]:
            return self.binarySearch(nums, min_idx, len(nums) - 1, target)
        else:
            return self.binarySearch(nums, 0, min_idx - 1, target)
        
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
                
        if nums[start] <= end:
            return start
        else:
            return end
        
    def binarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
        
