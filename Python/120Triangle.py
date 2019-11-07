class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.divideAndConquer(triangle, 0, 0, {})
        
    def divideAndConquer(self, triangle, x, y, mem):
        if x == len(triangle):
            return 0
        
        if (x, y) in mem:
            return mem[(x, y)]
        
        left = self.divideAndConquer(triangle, x + 1, y, mem)
        right = self.divideAndConquer(triangle, x + 1, y + 1, mem)
        
        mem[(x, y)] = min(left, right) + triangle[x][y]
        return mem[(x, y)]
