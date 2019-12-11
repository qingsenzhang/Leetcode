class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        
        A = sorted(A)
        s = -1
        start, end = 0, len(A) - 1
        while start < end:
            if A[start] + A[end] >= K:
                end -= 1
            else:
                s = max(s, A[start] + A[end])
                start += 1
                
        return s
