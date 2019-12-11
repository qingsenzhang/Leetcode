from collections import *
from heapq import *
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count

    def __eq__(self, other): 
        return self.word == other.word and self.count == other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        
        
        for key, val in count.items():
            if len(heap) < k:
                heappush(heap, Element(val, key))
            else:
                heappushpop(heap, Element(val, key))
                
        heap = sorted(heap, key=lambda ele:(-ele.count, ele.word))
        return [Element.word for Element in heap]
