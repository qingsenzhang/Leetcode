class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = collections.deque([])
        self.window_sum = 0
        self.size = size
        

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.window_sum += val
        else:
            self.window.append(val)
            left = self.window.popleft()
            self.window_sum = self.window_sum + val - left
        return self.window_sum / len(self.window)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
