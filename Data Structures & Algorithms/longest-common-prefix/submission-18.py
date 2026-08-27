class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # iterate through char columns in any string
        for i in range(len(strs[0])):
            # compare this char column agaisnt rest of strings
            for s in strs:
                # if the char at i for this string
                # is not equal to char at str[0]
                # then we found our first mismatch

                # or if i = length of this string
                # then we found shortest string and 
                # any strings longer than that will be mismatch
                # so we return any string from the list
                # up to this point
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]

        # if those never hit, then that means will have 
        # the same strings in the list
        # and we can return any one
        return strs[0]
        