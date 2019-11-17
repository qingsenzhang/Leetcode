class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min = x if x < self.min else self.min  

    def pop(self):
        """
        :rtype: None
        """
        ans = self.stack.pop()
        if ans == self.min and self.stack:
            self.min = min(self.stack)
        elif not self.stack:
            self.min = sys.maxsize
        return ans

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
