class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0:
            return []
        
        ans = []
        upper, lower, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while upper <= lower and left <= right:
            for i in range(left, right + 1):
                ans.append(matrix[upper][i])
            upper += 1
            if left > right or upper > lower:
                break
            for i in range(upper, lower + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right or upper > lower:
                break
            for i in range(right, left - 1, -1):
                ans.append(matrix[lower][i])
            lower -= 1
            if left > right or upper > lower:
                break
            for i in range(lower, upper - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans
