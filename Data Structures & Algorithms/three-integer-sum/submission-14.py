class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array to handle duplocates and enable two pointer logic
        nums.sort()

        for i, a in enumerate(nums):
            # DNU: Why do we break if a > 0?
            if a > 0:
                break

            # DNU: why does I need to be greater than 0?
            if i > 0 and a == nums[i - 1]:
                continue 

            l = i + 1
            r = len(nums) - 1 
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        