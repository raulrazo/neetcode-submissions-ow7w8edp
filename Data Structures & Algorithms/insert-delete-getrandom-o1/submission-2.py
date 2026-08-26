class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap

        if res:
            self.numMap[val] = len(self.numList)

            self.numList.append(val)

        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap

        if res:
            idx = self.numMap[val]

            lastVal = self.numList[-1]

            self.numList[idx] = lastVal

            self.numList.pop()

            self.numMap[lastVal] = idx

            del self.numMap[val]

        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numList)

    # O(1) time complexity because hashmaps are O(1) and our remove is O(1) because we always remove from the end of our list
    # O(n) space complexity because hashmaps and list use extra memory
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()