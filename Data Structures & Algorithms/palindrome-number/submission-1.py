class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False


        div = 1 
        while x >= 10 * div:
            div *= 10

        while x:
            leftmost = x // div
            rightmost = x % 10

            if leftmost != rightmost:
                return False

            x = (x % div)
            x = x // 10

            div = div // 100

        return True