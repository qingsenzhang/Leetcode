import heapq
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        i = 0
        while i < k - 1:
            heapq.heappop(heap)
            i += 1
        
        return -heapq.heappop(heap)
       
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(0, len(nums) - 1, nums, len(nums) - k)

    def quickSelect(self, start, end, nums, k):
        if start > end:
            return
        elif start == end:
            return nums[start]

        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        if k <= right:
            self.quickSelect(start, right, nums, k)
        elif k >= left:
            self.quickSelect(left, end, nums, k)

        return nums[k]
