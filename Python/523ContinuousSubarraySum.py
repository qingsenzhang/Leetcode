class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return 0
        
        k = abs(k)
        if k == 1 and len(nums) > 1:
            return True
        
        prefix_sum = collections.Counter()
        prefix_sum[0] = -1
        modulo_sum = collections.Counter()
        sum = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            if i > 0 and sum == k:
                return True
            if sum not in prefix_sum:
                prefix_sum[sum] = i
            if k != 0 and sum % k not in modulo_sum:
                modulo_sum[sum % k] = i
            elif k == 0:
                if i - prefix_sum[sum] >= 2:
                    return True
            else:
                if i - modulo_sum[sum % k] >= 2:
                    return True
        
        return False
