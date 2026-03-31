class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case

        if len(s) != len(t):
            return False

        # contents are the same

        countS = {}
        countT = {}

        # key = char : value = occurences

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT