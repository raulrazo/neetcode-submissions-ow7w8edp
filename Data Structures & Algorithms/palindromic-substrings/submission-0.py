class Solution:
    def countSubstrings(self, s: str) -> int:
        # count of the palindromic substrings
        res = 0

        # go thru every single position and expand from it
        # that is going to get us the odd length palindromes
        for i in range(len(s)):
            # start from the middle
            l = r = i

            # while left and right are inbounds
            # and we found a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment result and shift pointers
                res += 1
                l -= 1
                r += 1

            # now we get even length palindromes

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # increment result and shift pointers
                res += 1
                l -= 1
                r += 1

        return res

        