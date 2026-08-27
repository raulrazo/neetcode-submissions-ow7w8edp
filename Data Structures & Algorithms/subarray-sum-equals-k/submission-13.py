class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # track the total count of valid 
        # subarrays found so far.
        res = 0

        # accumulates the running prefix sum from
        # index 0 up to the current element.
        curSum = 0

        # hashmap where key = prefix sum value
        # and value = number of times that prefix 
        # sum has occured.
        # { 0 : 1 } represents a base case (empty prefix).
        # if subarray starting at index 0 directly = k
        # then curSum - k = 0 and this ensures that counts.
        prefixSums = { 0 : 1 }


        # iterate thru all nums.
        for num in nums:
            # update the running sum.
            curSum += num

            # calculates the required earlier prefix sum.
            # okay so if a previous curSum was equal to diff
            # then the elements between that earlier point 
            # and this current index must sum up to exactly k
            # b/c we update the curSum everytime, yknow
            # it's a running sum so that means everything we
            # summed up to this point matters and would be part
            # of the list of elements in this subarray that 
            # summed up to k. 
            diff = curSum - k

            # looks up how many times diff has appeared as a
            # prefix sum before this index.
            # and we add this to the result b/c every time
            # diff occured in the past, it created a unique
            # valid subarray at the current index that sums 
            # to k. 
            res += prefixSums.get(diff, 0)
            
            # increment the frequency of this curSum in case
            # this curSum is the diff for some other curSum 
            # in the future. 
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        # return final total count of subarrays
        return res

        