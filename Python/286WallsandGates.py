class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = collections.deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dq.append((i, j))
                    visited.add((i, j))
                elif rooms[i][j] == -1:
                    visited.add((i, j))
                    
        while dq:
            x, y = dq.popleft()
            for dx, dy in directions:
                if 0 <= x + dx < len(rooms) and 0 <= y + dy < len(rooms[0]) and (x + dx, y + dy) not in visited:
                    rooms[x + dx][y + dy] = rooms[x][y] + 1
                    dq.append((x + dx, y + dy))
                    visited.add((x + dx, y + dy))            
            
