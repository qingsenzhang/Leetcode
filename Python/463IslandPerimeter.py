class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = 0
                    for dx, dy in directions:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and \
                           grid[x][y] == 1:
                            count += 1
                    perimeter += 4 - count
                    
        return perimeter
                            
