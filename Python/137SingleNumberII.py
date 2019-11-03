class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for num in count:
            if count[num] == 1:
                return num
       
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    sum += 1
                    
            sum %= 3
            if sum != 0:
                ans |= sum << i
                
        return ans - 2 ** 32 if ans >= 2 ** 31 else ans       
