class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp array initialization and base case

        # each entry dp[i] represents whether the suffix s[i:]
        # from index i to the end of s can be segmented using
        # words from wordDict.
        dp = [False] * (len(s) + 1)

        # establishes the base case b/c at index len(s), the 
        # suffix s[len(s):] is the empty string "" and that 
        # requires zero words so something.
        dp[len(s)] = True

        # iterates backwards from index len(s) - 1 down to 0.
        # moving from right to left ensures that whenever we
        # evaluate index i, all downstream states i + len(w)
        # have already been computed.
        for i in range(len(s) - 1, -1, -1):
            # checks each word w in wordDict as a candidate prefix
            # for the suffix starting at i.
            for w in wordDict:
                # (i + len(w)) <= len(s): Bounds check to ensure 
                # taking len(w) characters starting at i does not 
                # exceed the boundaries of s.

                # s[i : i + len(w)] == w: Checks if the substring 
                # starting at i matches w.
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # If the word matches, whether s[i:] can be 
                    # segmented reduces to whether the remainder 
                    # of the string starting at i + len(w) is also 
                    # segmentable (dp[i + len(w)]).
                    dp[i] = dp[i + len(w)]

                # As soon as any word successfully segments s[i:], 
                # there is no need to check other words for this 
                # index.
                if dp[i]: break

        # This corresponds to whether the entire string s[0:] can 
        # be segmented into words from wordDict
        return dp[0]
