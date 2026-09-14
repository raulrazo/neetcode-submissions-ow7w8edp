class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case: s and t length dont match.
        # meaning impossible for them to be anagrams.
        if len(s) != len(t):
            return False

        # frequency maps mapping each char to their cnt
        countT = {}
        countS = {}

        # simultaneously populate freq maps
        # and increment cnt for each occurance of char
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # return True if both strings had same freq map
        # meaning they had same contents, meaning they
        # are anagrams of each other.
        
        # returns false otherwise
        return countS == countT
        