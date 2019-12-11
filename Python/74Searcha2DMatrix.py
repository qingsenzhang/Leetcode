class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l = m * n
        
        start, end = 0, l - 1
        while start + 1 < end:
            mid = (start + end) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                start = mid
            else:
                end = mid
                
        if matrix[start // n][start % n] == target or matrix[end // n][end % n] == target:
            return True
        else:
            return False
