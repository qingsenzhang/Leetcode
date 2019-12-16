class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10000
        self.arr = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = hash(key) % self.capacity
        if not self.arr[idx]:
            self.arr[idx] = Node(key, value)
        else:
            curr = self.arr[idx]
            while curr.next:
                if curr.key == key:
                    curr.val = value
                    return
                curr = curr.next
            if curr.key == key:
                curr.val = value
                return
            curr.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = hash(key) % self.capacity
        if not self.arr[idx]:
            return -1
        else:
            curr = self.arr[idx]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
            return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = hash(key) % self.capacity
        if not self.arr[idx]:
            return 
        else:
            prev, curr = None, self.arr[idx]
            if curr.key == key:
                self.arr[idx] = curr.next
                return 
            
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return 
                prev = curr
                curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
