import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 1:
            return 1
        if n == 0:
            return len(tasks)
        
        counts = list(collections.Counter(tasks).values())
        max_freq = max(counts)
        max_count = counts.count(max_freq)
        
        interval_count = max_freq - 1
        slots_count = interval_count * (n - (max_count - 1))
        idle_count = max(0, slots_count - (len(tasks) - max_freq * max_count))
        return len(tasks) + idle_count
