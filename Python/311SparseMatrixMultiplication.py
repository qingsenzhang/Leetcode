class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(B[0])
        p = len(A[0])
        
        ans = [[0 for i in range(m)] for j in range(n)]
        cols = [[] for i in range(p)]
        for i in range(p):
            for j in range(m):
                if B[i][j] != 0:
                    cols[i].append(j)
        
        for i in range(n):
            for j in range(p):
                if A[i][j] == 0:
                    continue
                else:
                    for k in cols[j]:
                        ans[i][k] += A[i][j] * B[j][k]
                        
        return ans
