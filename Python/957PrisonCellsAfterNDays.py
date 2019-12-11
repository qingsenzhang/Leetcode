class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = {str(cells) : N}
        
        while N != 0:
            visited[str(cells)] = N
            N -= 1
            
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            
            if str(cells) in visited:
                N %= visited[str(cells)] - N
                
        return cells
