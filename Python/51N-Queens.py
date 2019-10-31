class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [["Q"]]
            
        configs = []
        xy_diff, xy_sum = set(), set()
        cols = collections.OrderedDict()
        self.dfs(cols, n, configs, xy_diff, xy_sum)
        
        return [["." * col + "Q" + "." * (n - col - 1) for col in config] for config in configs]
        
    def dfs(self, cols, n, configs, xy_diff, xy_sum):
        row = len(cols)
        if row == n:
            configs.append([key for key, _ in cols.items()])
            
        for col in range(n):
            if col not in cols and row + col not in xy_sum and row - col not in xy_diff:
                cols[col] = 1
                xy_sum.add(row + col)
                xy_diff.add(row - col)
                self.dfs(cols, n, configs, xy_diff, xy_sum)
                del cols[col]
                xy_sum.remove(row + col)
                xy_diff.remove(row - col)
