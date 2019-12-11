class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        volume = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    volume += max_left - height[left]      
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    volume += max_right - height[right]      
                right -= 1
            
        return volume
