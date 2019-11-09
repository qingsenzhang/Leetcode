class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            max_vol = max(min(height[left], height[right]) * (right - left), max_vol)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_vol
