class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        
        for i in range(len(words) - 1):
            if not self.compareString(words[i], words[i + 1], order):
                return False
            
        return True
        
    
    def compareString(self, word1, word2, order):
        for i in range(len(word1)):
            if i < len(word2):
                if order.index(word1[i]) < order.index(word2[i]):
                    return True
                elif order.index(word1[i]) > order.index(word2[i]):
                    return False
        return False
        
