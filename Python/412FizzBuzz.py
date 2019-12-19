class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        idx = 1
        ans = []
        for i in range(n):
            if idx % 15 == 0:
                ans.append('FizzBuzz')
            elif idx % 5 == 0:
                ans.append('Buzz')
            elif idx % 3 == 0:
                ans.append('Fizz')
            else:
                ans.append(str(idx))
            idx += 1
            
        return ans
