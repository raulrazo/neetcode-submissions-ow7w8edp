class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize result array of 0s with exact same lengths as temperatures array
        res = [0] * len(temperatures)

        # stack is going to contain a pair of values
        # the pairs are going to the temperature and the index of the temperature 
        # so we can calculate the difference 

        stack = [] # pair: [temp, index]

        # iterate thru the temperatures array
        for i, t in enumerate(temperatures):
            # check that our stack is not empty
            # and if this current temperature is greater than the top of our stack
            while stack and t > stack[-1][0]:
                # if this is true then we can pop from our stack
                stackT, stackInd = stack.pop()
                
                # in the result output, whatever the index of this temp is
                # then we want to compute the number of days it took us to find a greater temperature
                res[stackInd] = (i - stackInd)

            # once the loop is done, we append the current temperature to our stack
            stack.append([t, i])

        return res
        