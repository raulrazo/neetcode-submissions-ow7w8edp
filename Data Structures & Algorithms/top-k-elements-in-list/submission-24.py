class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create buckets list
        freq = [[] for i in range(len(nums) + 1)]

        # create count hash map
        count = {} # key = num : val = count

        # map counts to nums
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # put nums in buckets
        for num, cnt in count.items():
            freq[cnt].append(num)

        # retrieve top k
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
        