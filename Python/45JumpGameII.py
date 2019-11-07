class Solution:
    def jump(self, nums: List[int]) -> int:
        count, curr_far, next_far = 0, 0, 0
        for i in range(len(nums) - 1):
            next_far = max(next_far, i + nums[i])
            if i == curr_far:
                curr_far = next_far
                count += 1
                
        return count
