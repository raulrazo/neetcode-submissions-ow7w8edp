class RandomizedSet:

    def __init__(self):
        # two data structures
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        # does val exist yet
        # this is the boolean value we are going to return
        res = val not in self.numMap

        # if val is not in the map
        if res:
            # we add it to the map 
            # the index we map it to is the length of numList at this point
            # b/c now we are going to add this value to the end of numList
            self.numMap[val] = len(self.numList)

            # add val to end of numList
            self.numList.append(val)

        return res
        

    def remove(self, val: int) -> bool:
        # res is if value is in the map 
        # b/c that means we can return true if we are able to remove it
        res = val in self.numMap

        # if result is true, then we can remove, so we do that
        if res:
            # want to remove it from the map and the array
            # need to get index it exists at in the array
            idx = self.numMap[val]

            # at that index, we want to take last value and move it to that index
            # we get last value by getting the last index using -1
            lastVal = self.numList[-1]

            # at the idx of this value we are going to remove in the array
            # we set the last value there instead
            self.numList[idx] = lastVal

            # now we want to pop the last value from our array because we just moved that last value to the one we are going to remove
            # so we want to pop it because last value now corresponds to the one we want to remove
            self.numList.pop()

            # now we update the index of the original last value in the array
            # b/c we just changed it to get rid of the other one
            # and we just give it the removed value's old position for some reason
            self.numMap[lastVal] = idx

            # now we can finally remove the original value we were removing from the hashmap

            del self.numMap[val]

        return res

    def getRandom(self) -> int:
        # use library function
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()