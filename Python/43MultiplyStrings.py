class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = 0
        base = 1
        for i in range(len(num2) - 1, -1, -1):
            digit = num2[i]
            sum += self.multiplyByDigit(num1, digit) * base
            base *= 10
    
        return str(sum)
    
    def multiplyByDigit(self, num1, digit):
        if digit == "0":
            return 0
        
        digit = int(digit)
        carry = 0
        ans = ""
        for i in range(len(num1) - 1, -1, -1):
            product = int(num1[i]) * digit + carry
            carry = product / 10
            result = product % 10
            ans = str(result) + ans
            
        if carry > 0:
            ans = str(carry) + ans
            
        return int(ans)
            
            
            
            
            
            
            
        
