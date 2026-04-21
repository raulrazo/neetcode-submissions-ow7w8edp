class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # creat dict with default values of 0
        count = defaultdict(int)

        for n in nums:
            # get the count of each number
            count[n] += 1

            # check length of hashmap to make sure not > 2
            if len(count) <= 2:
                # continue, meaning we don't have to decrement the count
                # go to next iteration
                continue

            # new hashmap
            new_count = defaultdict(int)

            
            # go thru every num and count 
            for n, c in count.items():
                # if count > 1 then we know this number is going to go into the new hashmap
                # b/c we don't want to keep anything that is going to be 0 in new hashmap
                if c > 1:
                    # decrement count here
                    new_count[n] = c - 1
            count = new_count

        res = []

        # verify that those elements do show up more than a third of the time
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res
                

        