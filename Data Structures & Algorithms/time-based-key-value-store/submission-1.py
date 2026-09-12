class TimeMap:

    def __init__(self):
        # keys : list of pairs in format [value, timestamp]
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # checks whether the given key exists in the hash map
        if key not in self.keyStore:
            # if key not in hashmap, then give it empty list
            # to vaoid key errors.
            self.keyStore[key] = []

        # appends pair of val and timestamp to list for key
        self.keyStore[key].append([value, timestamp])

        # b/c problem constraints guarantee timestamps are
        # strictly increasing, the list is automatically sorted

    def get(self, key: str, timestamp: int) -> str:
        # initialize res to "" for fallback return if no val
        res = ""

        # retrieves list of [val, time] pairs for key
        values = self.keyStore.get(key, [])

        # setup binary search
        l = 0
        r = len(values) - 1

        while l <= r:
            # calculate midpoint
            m = (l + r) // 2

            # checks if timestamp at m is <= target timestamp
            if values[m][1] <= timestamp:
                # this value is a valid candidate so update res
                res = values[m][0]

                # search right half of list to find potential
                # timestamp that is closer to target timestamp.
                l = m + 1
            
            # the timestamp at m is too new to be valid
            else:
                # so we search the left half b/c going left 
                # means smaller numbers.
                r = m - 1

        # returns the closest timestamp we found to target
        # timestamp.
        # or "" if we never found valid timestamp or key
        # never existed.
        return res
