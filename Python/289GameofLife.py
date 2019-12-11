class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        ans = [[0 for j in range(len(board[0]))] for i in range(len(board))] 

        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt = self.count(board, i, j)
                if board[i][j] == 1 and 2 <= cnt <= 3:
                    ans[i][j] = 1
                if board[i][j] == 0 and cnt == 3:
                    ans[i][j] = 1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = ans[i][j]
        
                
    def count(self, board, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        cnt = 0
        for dx, dy in directions:
            i, j = x + dx, y + dy
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if board[i][j] == 1:
                    cnt += 1
                    
        return cnt
