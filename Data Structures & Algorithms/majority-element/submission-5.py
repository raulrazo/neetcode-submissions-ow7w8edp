class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # intialize hash map storing counts of each num
        # use default dict so starting count of each num is 0

        count = defaultdict(int)

        # stores the candidate element that currently hols the 
        # highest observed frequency.
        res = 0

        # stores the highest frequency count observed so far
        maxCount = 0

        for num in nums:
            # increment count of num by 1
            count[num] += 1

            # checks whether current num's count exceeds the max
            if maxCount < count[num]:
                # update res to num with highest maxCount
                res = num

                # update max count with new highest max count
                maxCount = count[num]

        # the element with the highest frequency is guaranteed
        # to be the majority element, so return res.
        return res
        