class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == -2147483648 and divisor == -1: 
            return 2147483647
        if dividend == 2147483647 and abs(divisor) == 1:
            return 2147483647 if divisor > 0 else -2147483647
        if dividend == -2147483648 and divisor == 1:
            return -2147483648

        positive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        
        count = 0
        while dividend >= divisor:
            tmp_divisor, exp = divisor, 1
            while dividend >= tmp_divisor:
                dividend -= tmp_divisor
                count += exp
                tmp_divisor <<= 1
                exp <<= 1
        
        if not positive:
            count = -count
        
        return count
