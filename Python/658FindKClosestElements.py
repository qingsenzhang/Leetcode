from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            if len(heap) < k:
                heappush(heap, (-abs(num - x), -num))
            else:
                heappushpop(heap, (-abs(num - x), -num))
        
        ans = sorted([-num for _, num in heap])
        
        return ans
