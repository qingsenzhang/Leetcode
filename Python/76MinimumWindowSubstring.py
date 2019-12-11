class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        
        count_t = collections.Counter(t)
        total_count = len(t)
        length = sys.maxsize
        begin = end = head = 0
        while end < len(s):
            if s[end] in count_t:
                count_t[s[end]] -= 1
                if count_t[s[end]] >= 0:
                    total_count -= 1
                
            end += 1
            while total_count == 0:
                if end - begin < length:
                    length = end - begin 
                    head = begin
                if s[begin] in count_t:
                    count_t[s[begin]] += 1
                    if count_t[s[begin]] > 0:
                        total_count += 1
                begin += 1
                
        return "" if length == sys.maxsize else s[head:head + length]
