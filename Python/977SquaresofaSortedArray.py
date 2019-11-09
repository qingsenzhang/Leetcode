class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return [num ** 2 for num in sorted(A, key=lambda n: abs(n))]
