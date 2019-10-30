class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        c = collections.Counter(words)
        descending = sorted(c.items(), key = lambda x: -x[1])
        for word, count in descending:
            if word not in banned:
                return word
        
