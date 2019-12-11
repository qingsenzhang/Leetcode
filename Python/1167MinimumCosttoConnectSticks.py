from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks or len(sticks) == 1:
            return 0
        
        heapify(sticks)
        
        cost = 0
        while len(sticks) > 1:
            x, y = heappop(sticks), heappop(sticks)
            cost += x + y
            heappush(sticks, x + y)
            
        return cost
