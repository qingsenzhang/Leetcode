import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (self.distance(point), point))
        return [point for dist, point in heapq.nsmallest(K, heap)]
        
    def distance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
        
