from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map[key]
            del self.map[key]
            self.map[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.pop(key)
        else:
            if len(self.map) == self.capacity:
                self.map.popitem(last=False)
        self.map[key] = value
