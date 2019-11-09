class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) <= 1:
            return True
        
        heap = []
        count = collections.Counter(S)
        for char, frequency in count.items():
            heapq.heappush(heap, (-frequency, char))
        
        ans = ""
        alternate_char, alternate_freq = "", 0
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char
            freq += 1
            if alternate_freq < 0:
                heapq.heappush(heap, (alternate_freq, alternate_char))
            alternate_char, alternate_freq = char, freq
            
        return ans if len(ans) == len(S) else ""
       
