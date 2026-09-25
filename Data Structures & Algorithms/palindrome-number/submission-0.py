class Solution:
    def isPalindrome(self, x: int) -> bool:
        # edge case: negative numbers have '-' so
        # they can never be palindromes b/c uneven length.
        if x < 0:
            return False

        # calculates the base divisor needed to extract
        # the leftmost digit. 
        # AKA we multiply 1 by 10 until it is as big as x
        # in terms of tens place, ex: x = 1221, so we 
        # want div to be multiplied by 10 until it is
        # 1000 because 1221 // 1000 = 1 and we can get
        # the leftmost digit.
        div = 1
        while x >= 10 * div:
            div *= 10


        # runs as long as there are digits left in x
        while x:
            # x // div extracts the leftmost digit using division
            # x % 10 extracts the rightmost digit
            # if these two digits do not match then the symmetry
            # is broken and it is not a palindrome.
            if x // div != x % 10:
                return False

            # if they do match then we chop them both off
            # and readjust the scale.
            # we do that in one line here.
            # x % div drops the leftmost digit,
            # ex: x = 1221 % 1000 = 221.
            # the // 10 drops the rightmost digit,
            # ex: 221 // 10 = 22
            x = (x % div) // 10

            # since our starting div was captured when x
            # was the greatest, we have to adjust it too.
            # so we divide it by 100 to shrink its size by 10^2,
            # ex: div = 1000 // 100 = 10.
            # why 10^2? b/c we removed left and right digit
            # and that's an order of magnitude of 2. 
            div //= 100

        # if all left and rights matched and we never had to
        # return false, then this is a palindrome number
        return True

    # time and space complexity:
    # O(n) time complexity where n is the number of digits in x
    # b/c we must visit every number in the integer.

    # O(1) space complexity because we do not use extra data.

        