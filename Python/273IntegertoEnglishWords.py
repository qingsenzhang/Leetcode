class Solution:
    def numberToWords(self, num: int) -> str:
        teens = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']
        
        if num == 0:
            return 'Zero'
        elif num < 20:
            return teens[num - 1]
        
        every_thousand = 0
        ans = ""
        while num > 0:
            if num % 1000 != 0:
                ans = self.help(num % 1000, teens, tens) + thousands[every_thousand] + ' ' + ans
            every_thousand += 1
            num = num // 1000
            
        return ans.strip()
            
            
    def help(self, num, teens, tens):
        if num == 0:
            return ''
        if num < 20:
            return teens[num - 1] + ' '
        elif num < 100:
            return tens[num // 10 - 1] + ' ' + self.help(num % 10, teens, tens)
        else:
            return teens[num // 100 - 1] + ' Hundred ' + self.help(num % 100, teens, tens)
        
