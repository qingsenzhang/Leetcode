class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        ans = ""
        if not a:
            return b
        elif not b:
            return a
        
        p1 = len(a) - 1
        p2 = len(b) - 1
        while p1 >= 0 and p2 >= 0:
            digit = int(a[p1]) + int(b[p2])
            if carry:
                digit += 1
            carry = True if digit >= 2 else False
            digit = digit % 2
            ans = str(digit) + ans
            p1 -= 1
            p2 -= 1
        
        while p1 >= 0:
            digit = int(a[p1])
            if carry:
                digit += 1
            carry = True if digit >= 2 else False
            digit = digit % 2
            ans = str(digit) + ans
            p1 -= 1
            
        while p2 >= 0:
            digit = int(b[p2])
            if carry:
                digit += 1
            carry = True if digit >= 2 else False
            digit = digit % 2
            ans = str(digit) + ans
            p2 -= 1
        
        if carry:
            ans = "1" + ans
        
        return ans
            
            
        
