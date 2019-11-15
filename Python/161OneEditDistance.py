class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        
        if not s and not t:
            return False
        elif not s or not t:
            return True
        
        if s == t:
            return False
        
        ls, lt = len(s), len(t)
        for i in range(min(ls, lt)):
            if s[i] != t[i]:
                if ls == lt:
                    return s[i+1:] == t[i+1:]
                elif ls > lt:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
            
        return True
        
