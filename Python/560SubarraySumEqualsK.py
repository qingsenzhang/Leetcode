 class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        if not nums:
            return count
        elif len(nums) == 1:
            return 1 if nums[0] == k else count
        
        preSum = {0 : 1}
        sum = 0
        for num in nums:
            sum += num
            if sum - k in preSum:
                count += preSum[sum - k]
            preSum[sum] = preSum.get(sum, 0) + 1
        return count
