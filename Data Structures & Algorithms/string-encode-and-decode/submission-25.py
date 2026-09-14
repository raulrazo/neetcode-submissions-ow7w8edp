class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize empty list that we will
        # turn into a string later.
        res = []

        # iteratre through strings
        for s in strs:
            # add length of string to res
            res.append(str(len(s)))

            # add delimiter to res
            res.append("#")

            # add string s to res
            res.append(s)

        # join res into single continuous string
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        # initialize res to hold extracted strings
        res = []

        # two pointer approach
        i = 0

        while i < len(s):
            # j pointer is for capturing length of str
            j = i

            # while we are still capturing len
            while s[j] != "#":
                # move j up
                j += 1

            # len is from i up to this j
            # b/c j is at # now.
            length = int(s[i:j])

            # set i to start of string (after #)
            i = j + 1

            # set j to end of string using length
            j = i + length

            # capture string in res
            res.append(s[i:j])

            # reposition i at start of next length
            i = j

        return res

