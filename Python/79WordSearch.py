class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        def dfs(i, j, word):
            if not word:
                return True
            
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                board[i][j] = ''
                for dx, dy in directions:
                    if dfs(i + dx, j + dy, word[1:]):
                        board[i][j] = word[0]
                        return True
                board[i][j] = word[0]
                return False
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
                
        return False
