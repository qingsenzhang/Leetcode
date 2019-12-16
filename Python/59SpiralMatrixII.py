class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = [[0] * n for i in range(n)]
        
        row_start, row_end, col_start, col_end = 0, n - 1, 0, n - 1
        curr = 1
        
        while row_start <= row_end and col_start <= col_end:
            if row_start <= row_end and col_start <= col_end:
                for i in range(col_start, col_end + 1):
                    ans[row_start][i] = curr
                    curr += 1
                row_start += 1
                
            if row_start <= row_end and col_start <= col_end:
                for i in range(row_start, row_end + 1):
                    ans[i][col_end] = curr
                    curr += 1
                col_end -= 1
            
            if row_start <= row_end and col_start <= col_end:
                for i in range(col_end, col_start - 1, -1):
                    ans[row_end][i] = curr
                    curr += 1
                row_end -= 1
        
            if row_start <= row_end and col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    ans[i][col_start] = curr
                    curr += 1
                col_start += 1
                
        return ans
