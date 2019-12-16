from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        heap = []
        for num, count in count.items():
            if len(heap) < k:
                heappush(heap, (count, num))
            else:
                heappushpop(heap, (count, num))
            
        ans = [num for _, num in sorted(heap, key=lambda pair:-pair[0])]
        return ans
