class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = S.split()
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] += 'ma' 
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'
            words[i] += 'a' * (i + 1)
                                 
        return ' '.join(words)
