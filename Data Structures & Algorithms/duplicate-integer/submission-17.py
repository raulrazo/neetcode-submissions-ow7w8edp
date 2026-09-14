class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store numbers seen so far in set
        seen = set()

        # iterate thru nums
        for num in nums:
            # if we have already seen num
            if num in seen:
                return True

            # if we haven't seen num
            # then we insert it into our set
            # so future iterations can detect if 
            # this value is seen again.
            seen.add(num)

        # all elements were unique and no duplicates
        return False



        