class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # go thru every single position in the string
        for i in range(len(s)): 
            # odd length palindromes
            # left and right pointers initialized to i
            l, r = i, i

            # while l and r are in bound and this is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # compute length of palindrome
                if (r - l + 1) > resLen:
                    # if greater than resLen, then we update result
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                # expand our pointers outward
                l -= 1
                r += 1
            
            # check even length palindromes
            l, r = i, i + 1
            # while l and r are in bound and this is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # compute length of palindrome
                if (r - l + 1) > resLen:
                    # if greater than resLen, then we update result
                    res = s[l:r+1]
                    resLen = r - l + 1

                # expand our pointers outward
                l -= 1
                r += 1

        return res

        