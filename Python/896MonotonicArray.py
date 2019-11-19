class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return True
        
        increasing = A[-1] >= A[0]
        
        for i in range(len(A) - 1):
            if increasing:
                if A[i + 1] < A[i]:
                    return False
            else:
                if A[i + 1] > A[i]:
                    return False
        return True
