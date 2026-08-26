class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # compare chars column by column across all strings

        # iterate thru char positions starting from index 0
        # we pick the first string but this can be any string
        # in the list because in theory, as soon as we find
        # the first mismatched char b/w all the strings
        # then all the strings should be the same length up to that point
        # plus we know there will always be a guaranteed 
        # one and first string
        for i in range(len(strs[0])):
            # check the char at i for all of the strings
            for s in strs:
                # if i is the length of a string
                # that means we have found the shortest string
                # and therefore any string longer than it
                # will not be the same as it
                # so the longest common prefix stops here

                # or if the char for this string at this position i
                # is not equal to the char at the position i for first string (arbitrary string)
                # then we have found a mismatch and we know 
                # the longest common prefix stops here
                if i == len(s) or s[i] != strs[0][i]:
                    # so we return the longest common prefix
                    # which is the s strings up to this point i
                    return s[:i]

        # if none of those conditions ever hit
        # then we know that all strings in the list
        # are the same and we can return any arbitrary one
        return strs[0]

        # O(n * m) time complexity because we have to iterate through m strings and n is the maximum shortest length of all the strings and we have to go through n chars 
        # O(1) space complexity because we did not use any memory
        