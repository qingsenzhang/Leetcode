class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if not nums or target < nums[0] or target > nums[-1]:
            return ans
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        if target == nums[start]:
            ans[0] = start
        elif target == nums[end]:
            ans[0] = end
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                start = mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        if target == nums[end]:
            ans[1] = end 
        elif target == nums[start]:
            ans[1] = start
            
        return ans
            
        
