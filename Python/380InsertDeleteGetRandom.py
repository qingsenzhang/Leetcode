import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.mapping = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        #print(self.mapping)
        if val not in self.mapping:
            self.arr.append(val)
            self.mapping[val] = len(self.arr) - 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mapping:
            idx = self.mapping[val]
            self.arr[idx], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[idx]
            self.mapping[self.arr[idx]] = idx
            del self.mapping[val]
            #print(self.arr)
            self.arr.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
