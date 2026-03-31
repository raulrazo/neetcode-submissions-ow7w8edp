class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: empty input
        if t == "": return ""

        # two windows, countT = need, window = have
        countT = {}
        window = {}

        # initialize the countT map AKA count chars
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # initialize our have and need VALUES, need is length of countT b/c it gives us the unique characters in the string T
        have = 0
        need = len(countT)

        # set result and result length (result = left and right pointer so default -1 vals, infinity is some python default shit we can use for length)
        res = [-1, -1]
        resLen = float("infinity")

        # initialize left pointer
        l = 0

        # start iterating through every character in s
        for r in range(len(s)):
            # put curr char in var c
            c = s[r]

            # update our curr window
            window[c] = 1 + window.get(c, 0)

            # check if c is in countT and if we satisfy condition where have == need for the char in the dicts, not actual have == need for the values
            if c in countT and window[c] == countT[c]:
                # update our have count by 1
                have += 1

            # check if the have == need for values itself
            while have == need:
                # update our result potentially
                # if the current len of our window (r - l + 1 = universal way to calculate window length) less than current result length
                if (r - l + 1) < resLen:
                    # we can update our result
                    res = [l, r]
                    resLen = (r - l + 1) # size of the window

                # now we reset our window by shrinking it and popping from the left
                # remove leftmost char from our window map
                window[s[l]] -= 1

                # we just removed a bih so we check if have == need still true
                # if s[l] is one of the character we need to satisfy our condition and now the count of it is less than what we need 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # take our have and decrement it by 1
                    have -= 1

                # shift left pointer
                l += 1
                    
        # new left and right pointer will hold our result
        l, r = res

        # return the minimum substring using left and right pointers
        # gotta check for infinity thing because it is possible that result does not exist
        return s[l: r + 1] if resLen != float("infinity") else ""
        