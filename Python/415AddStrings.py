class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or num1 == '0':
            return num2
        elif not num2 or num1 == '0':
            return num1
        
        ans = ""
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = False
        while p1 >= 0 and p2 >= 0:
            digit = int(num1[p1]) + int(num2[p2])
            digit += 1 if carry else 0
            carry = True if digit >= 10 else False
            digit %= 10
            ans = str(digit) + ans
            p1 -= 1
            p2 -= 1
            
        while p1 >= 0:
            digit = int(num1[p1]) + 1 if carry else int(num1[p1])
            carry = True if digit >= 10 else False
            digit %= 10
            ans = str(digit) + ans
            p1 -= 1
        
        while p2 >= 0:
            digit = int(num2[p2]) + 1 if carry else int(num2[p2])
            carry = True if digit >= 10 else False
            digit %= 10
            ans = str(digit) + ans
            p2 -= 1
            
        if carry:
            ans = "1" + ans
            
        return ans
    
