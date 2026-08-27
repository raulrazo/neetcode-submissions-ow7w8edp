class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                # DNU: Why do we remove s[l] when s[l] might not even be s[r]?
                # The while loop isn't just trying to remove
                # the matching character—it is sliding the
                # entire left wall forward, evicting every
                # character along the way until the duplicate
                # is legally out of the window range [l, r].
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

        # O(n) time complexity because we iterate through all chars in the string, n is string s length
        # O(m) space complexity because the size of our set is relative to how many unique chars are in string s
        