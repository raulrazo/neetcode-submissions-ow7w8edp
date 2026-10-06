class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # result list 
        ans = []

        # first pass will build the first half
        # second pass will build the second half
        for i in range(2):
            # iteratre thru every num from left to right
            for num in nums:
                # basically each number will get added twice,
                # but in the order the came in
                # and that is how we will get two identical halves
                ans.append(num)
        
        return ans