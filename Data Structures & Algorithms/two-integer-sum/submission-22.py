class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap to store value and index of each element in the array
        prevMap = {} 

        # itertate thru nums
        # and we need i for the index
        # and n for the number at this index i
        for i, n in enumerate(nums):
            # this is the complement 
            # AKA the number that would be added
            # to the current number in order for it 
            # to equal the target
            # AKA the 2nd number we are trying to find for
            # this current number
            diff = target - n
            if diff in prevMap:
                # if this diff number does exist in our prevMap
                # that means we have already visited it in our list of numbers
                # so that means our current number is now 
                # the 2nd number in the pair 
                # and diff was the first number
                # so we found our pair
                # and return the indices that we stored for
                # these values in our prevMap
                return [prevMap[diff], i]

            # if we haven't seen this current number's
            # diff yet, then we just add it to 
            # our prevMap and move on
            prevMap[n] = i

        # O(n) time complexity because we could iterate thru the entire nums list
        # O(n) space complexity because we use extra memory with our hashmap

        