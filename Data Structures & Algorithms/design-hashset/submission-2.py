class MyHashSet:

    def __init__(self):
        self.data = [0] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = 1
        return None

    def remove(self, key: int) -> None:
        self.data[key] = 0
        return None

    def contains(self, key: int) -> bool:
        return self.data[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)