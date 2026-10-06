class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l and r represent k's too.
        # the minimum possible eating speed is 1 banana/hour
        l = 1

        # maximum possible eating speed is the max amount of
        # bananas in a single pile (this is like the end of 
        # a list in typical binary search, this is the end of 
        # our theoretical k range)
        r = max(piles)

        # initializes the guaranteed upper bound r, ensuring 
        # a valid answers is maintained throughout the loop
        res = r

        while l <= r:
            # we use k for the midpoint name because we are
            # searching thru k's
            k = (l + r) // 2

            # calculating required hours

            # tracks the total hours needed to consume all
            # piles at rate k
            totalTime = 0

            # iterate through each pile of bananas
            for p in piles: # piles = [3, 6, 7], k = 4
                # pile 1
                #   p = 3
                #   3 / 4 = 0.75 but ceil rounds up to 1 hour
                #   so totalTime = 0 + 1 = 1

                # pile 2
                #   p = 6
                #   6 / 4 = 1.5 but ceil rounds up to 2 hours
                #   so totalTime = 1 + 2 = 3

                # pile 2
                #   p = 7
                #   7 / 4 = 1.75 but ceil rounds up to 2 hours
                #   koko eats 4 in 1hr, then remaining 3 in nxt hr
                #   so totalTime = 3 + 2 = 5
                totalTime += math.ceil(float(p) / k)

            # checks if rate k is feasible within h hours
            if totalTime <= h:
                # records k as a valid answer
                res = k

                # go the left half of k list to see if an even
                # slower k can also finish within h hours.
                r = k - 1
            else:
                # speed k is too slow to finish in time
                # so we have to go towards the bigger k's in 
                # the right half.
                l = k + 1

        return res

        # Time and Space Complexity

        # O(n * log(m)) time where n is length of piles and
        # m is max(piles) b/c the binary search space ranges from
        # 1 to m which takes log(m) iterations to converge and
        # in each iteration we iterate thru all n elements in
        # piles to calculate total time, taking O(n) time.

        # O(1) space complexity b/c we don't use extra memory.

        