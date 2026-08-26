class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize pointers
        l = 0
        r = len(s) - 1

        # while the pointers don't overlap
        while l < r:
            # while the pointers don't overlap
            # and the current char at left pointer
            # is not an alphanumeric char
            # then we move left pointer until we are
            # at an alphanumerica char
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # same concept for this while loop but for right pointer 
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # check if the chars are the same at l and r
            if s[l].lower() != s[r].lower():
                # if they aren't the same then we know
                # they aren't the same char
                # so not a palindrome, so return False
                return False

            # if they were the same char then we 
            # continue and shift the l and r pointers inward
            l = l + 1
            r = r - 1

        return True

    def alphaNum(self, c):
        # ord is like the ASCII or something
        # returns True if alphanum, False otherwise
        return(ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    # O(n) time complexity because we potentially have to visit every char in the string s
    # O(1) space complexity because the two pointers do not use up any extra memory
        