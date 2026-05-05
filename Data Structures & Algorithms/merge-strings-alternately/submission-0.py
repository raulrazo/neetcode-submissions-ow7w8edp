class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # initialize pointers
        i = 0
        j = 0

        # more efficient to add strings to chars of an array
        # at the end, we will join all of the chars in the array
        # into a string

        res = []

        # iterate while in bounds
        while i < len(word1) and j < len(word2):
            # append char at i to result
            res.append(word1[i])

            # apped char at j to result
            res.append(word2[j])

            # update pointers
            i += 1
            j += 1

        # one of the string could still have chars left

        # append substring of word1 starting from i
        # b/c it will append nothing if no chars left
        # but will append something if chars left
        # same thing for word 2
        # we do this b/c we don't know which one of them could still
        # have chars left

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
        