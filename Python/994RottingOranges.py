class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = collections.deque([])
        
        cycle = 0
        count = 0
        dq = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    dq.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        
        if count == 0:
            return 0
        
        visited = set([])
        while dq:
            cycle += 1
            l = len(dq)
            for i in range(l):
                x, y = dq.popleft()
                grid[x][y] = 0
                visited.add((x, y))
                for dx, dy in directions:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
                        print(x + dx, y + dy)
                        dq.append((x + dx, y + dy))
                        visited.add((x + dx, y + dy))
                        count -= 1
            if count == 0:
                return cycle
                        
        return cycle if count == 0 else -1
                    
                    
