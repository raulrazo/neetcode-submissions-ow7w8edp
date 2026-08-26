class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create count hashmap 
        # key = number : val = freq of number
        count = {}

        # create our list of buckets for bucket sort
        # one bucket per frequency
        # we do the + 1 since the list indices start at 0
        # and we want to capture max bucket, which would 
        # be + 1 of the length
        freq = [[] for i in range(len(nums) + 1)]

        # iterate through the numbers in nums
        for num in nums:
            # at this num key,
            # increase its freq by 1 everytime we see it
            count[num] = 1 + count.get(num, 0)

        # add the numbers to their respective buckets
        # based on their counts
        for num, cnt in count.items():
            freq[cnt].append(num)

        # initialize empty results list
        res = []

        # DNU: the values in range function
        # start backwards from top frequency
        # b/c we want the top frequent elements
        for i in range(len(freq) - 1, 0, -1):
            # for each number in this frequency bucket
            for num in freq[i]:
                # append this number to our results list
                res.append(num)

                # if our results list has become length k
                # then we have found the k most frequent
                # and we return 
                if len(res) == k:
                    return res

        # O(n) time complexity because we have to iterate through all numbers to build count map
        # O(n) space complexity because we are using hashmap of size all numbers to count each of their frequencies
        
        