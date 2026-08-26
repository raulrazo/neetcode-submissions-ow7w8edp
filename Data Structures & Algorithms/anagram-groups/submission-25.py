class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize hashmap where every value 
        # is an empty list by default
        res = defaultdict(list)

        # iterate through all strings in strs
        for s in strs:
            # initialize an empty alphabet array 
            # for each string to count its chars
            count = [0] * 26
            
            # for each char in the string
            for c in s:
                # we want to increment the count of that 
                # char in our count alphabet array
                # using its position in the alphabet
                # that's why we use ord() for ASCII values
                count[ord(c) - ord('a')] += 1

            # now that we have created our count alphabet array
            # for this string,
            # we make it a key in our hashmap
            # and add this string to the values list
            # because this string belongs to this specific count
            # we have to make count array a tuple so it can be a key
            res[tuple(count)].append(s)

        # at this point, every string is mapped to their
        # specific char count key
        # and multiple strings could be mapped to the same count key
        # and that makes up our groups
        # so we return the list of our values
        # and this is returning a list of lists
        return list(res.values()) 


        # O(m * n) time complexity because we have to iterate through every char in every string, m = strings, n = length of longest string
        # DNU: O(m * n) total space because the hashmap we are creating and returning 
        