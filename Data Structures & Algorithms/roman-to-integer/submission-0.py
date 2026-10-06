class Solution:
    def romanToInt(self, s: str) -> int:
        # intializes lookup dict by mapping each roman char
        # to its base decimal value
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # holds the runnning total value of the convered numeral
        res = 0

        # iterate thru string
        for i in range(len(s)):
            # i + 1 < len(s) verifies whether a subsequent char
            # exists.

            # roman[s[i]] < roman[s[i + 1]] checks if the current
            # Roman numeral has a small value than the one
            # immediately following it, like 'I' before 'V'
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                # subtracts the current char's value from the
                # running total instead of adding it.
                # example: "IV", when we subtract "I" first,
                # res -= 1, and then add "V" (5), res += 5, then
                # we really added 4 total when we hit "IV" 
                res -= roman[s[i]]
            
            # if the current symbol is greater than or equal to
            # the next symbol, or if i is the last char in string
            else:
                # add the curr symbol's value to running total
                res += roman[s[i]]

        # return final running total
        return res

        # Time and Space Complexity

        # O(n) time complexity because we have to scan thru
        # entire input. 

        # O(1) space complexity even though we use dict b/c
        # dict will always be those 7 fixed key value pairs.