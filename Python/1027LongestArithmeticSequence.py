class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        
        dp_table = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp_table[(j, A[j] - A[i])] = dp_table.get((i, A[j] - A[i]), 1) + 1
                
        return max(dp_table.values())
