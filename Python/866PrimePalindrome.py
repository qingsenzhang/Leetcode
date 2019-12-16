class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(N):
            if N < 2:
                return False
            if N == 2:
                return True
            if N % 2 == 0:
                return False
            
            for i in range(3, round(math.sqrt(N)) + 1, 2):
                if N % i == 0:
                    return False
                
            return True
        
        def generatePalindrome(digits):
            if digits == 1:
                return [i for i in range(10)]
            elif digits % 2 == 0:
                half = digits // 2
                ans = []
                for i in range(10 ** (half - 1), 10 ** half):
                    ans.append(str(i) + str(i)[::-1])
                return ans
            else:
                half = digits // 2
                ans = []
                for i in range(10 ** (half - 1), 10 ** half):
                    for j in range(10):
                        ans.append(str(i) + str(j) + str(i)[::-1])
                return ans
        
        digits = len(str(N))
        while True:
            for num in generatePalindrome(digits):
                if int(num) >=N and isPrime(int(num)):
                    return int(num)
            digits += 1
                
