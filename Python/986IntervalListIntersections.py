class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        if not A or not B:
            return ans

        p1, p2 = 0, 0
        while p1 < len(A) and p2 < len(B):
            start = max(A[p1][0], B[p2][0])
            end = min(A[p1][1], B[p2][1])
            if end >= start:
                ans.append([start, end])
            if end == A[p1][1]:
                p1 += 1
            else:
                p2 += 1
        
        return ans
        
