class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
            
        visited = set([1])
        heap = [1]
        ans = 1
        for i in range(n):
            ans = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if ans * factor not in visited:
                    visited.add(ans * factor)
                    heapq.heappush(heap, ans * factor)
                    
        return ans
