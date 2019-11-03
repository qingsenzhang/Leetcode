class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if not A or len(A) == 0 or K == 0 or len(A) < K:
            return 0
        
        return self.atMostK(A, K) - self.atMostK(A, K - 1)
    
    def atMostK(self, A, K):
        if not A or len(A) == 0 or K == 0:
            return 0
        
        count = 0
        left, right = 0, 0
        frequency = {}
        while left < len(A):
            while right < len(A):
                frequency[A[right]] = frequency.get(A[right], 0) + 1
                if len(frequency) <= K:
                    count += right - left + 1
                else:
                    frequency[A[right]] -= 1
                    if frequency[A[right]] == 0:
                        del frequency[A[right]]
                    break
                right += 1
            frequency[A[left]] -= 1
            if frequency[A[left]] == 0:
                del frequency[A[left]]
            left += 1
        return count
            
        
        
