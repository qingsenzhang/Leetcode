class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        for log in logs:
            idx = log.index(' ')
            if log[idx+1].isalpha():
                letter.append(log)
            else:
                digit.append(log)
                
        
        letter = sorted(letter, key=lambda order:(order.split()[1:], order.split()[0]))
        
        return letter + digit
