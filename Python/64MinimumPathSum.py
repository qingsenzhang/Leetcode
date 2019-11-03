class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        sum = 0
        for i in range(len(grid[0])):
            table[0][i] = sum + grid[0][i]
            sum += grid[0][i]
        sum = 0
        for i in range(len(grid)):
            table[i][0] = sum + grid[i][0]
            sum += grid[i][0]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                table[i][j] = min(table[i - 1][j], table[i][j - 1]) + grid[i][j]
                
        return table[len(grid) - 1][len(grid[0]) - 1]
        
