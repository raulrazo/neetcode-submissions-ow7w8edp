class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers 
        l = 0
        r = len(s) - 1

        # keep going while our two pointers have not crossed each other
        while l < r:
            # swap the two chars at l and r
            # reassign two variables at the same time
            s[l], s[r] = s[r], s[l]

            # update our pointers
            l += 1
            r -= 1
        