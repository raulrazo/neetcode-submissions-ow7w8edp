class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initialize 2 pointers
        l = 0
        r = len(s) - 1

        # if they meet each other, then we found a palindrome
        while l < r:
            # chars not equal
            if s[l] != s[r]:
                # two cases
                # skip left char or skip right char

                # l + 1 = skipping left
                # r + 1 = including right char

                # r = skipping right char by not including it
                skipL, skipR = s[l + 1 : r + 1], s[l : r]

                # reverse a string and see if it is equal to its reversal
                # this is checking if they are a palindrome
                return (skipL == skipL[::-1] or skipR == skipR[::-1])

                # if either of those are true
                # then we return true b/c there is palindrome
                # if false, then no palindromes

            # update pointers
            l += 1
            r -= 1

        return True


        