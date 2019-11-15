class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : -1}
        sum = 0
        max_len = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum not in prefix_sum:
                prefix_sum[sum] = i
            if sum - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[sum - k])
        return max_len
        
