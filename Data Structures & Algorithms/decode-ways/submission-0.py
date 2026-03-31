class Solution:
    def numDecodings(self, s: str) -> int:
        # recursive cacheing solution
        # entire length of string is going to map to 1
        # b/c if we get an empty string, we want to return 1
        dp = { len(s) : 1 }

        #recursive function, i is the cur position in string s
        def dfs(i):
            # i has already been cached
            # or i is last position in the string
            # AKA base case
            if i in dp:
                return dp[i]

            # i is not end of string so we check what char it is
            if s[i] == "0":
                # 0 means invalid
                return 0

            # if it's not 0 then it's b/w 1-9
            # so we can take this value as a single digit
            # and the subproblem becomes dfs of i + 1
            # and that's our result 
            res = dfs(i + 1)

            # but there are some cases where we have to i + 2
            # if we do have a second char that comes after the current one
            # so if i + 1 is inbounds and either the char s[i] starts with a "1"
            # b/c if it starts with a 1 and there is a second digit that means 
            # we can take a double digit value
            # or the other case is if s[i] starts with a 2,
            # then the second digit must be b/w 0-6 because we can only go to 26 (Z)
            # AKA checking if there is a double digit value 10-26

            if (i + 1 < len(s) and ((s[i] == "1") or
                s[i] == "2" and s[i + 1] in "0123456")):
                # + 2 because this is a double digit value
                res += dfs(i + 2)

            # cache the result
            dp[i] = res
            return res

        # dfs(0) b/c we want to know how many ways
        # we can decode the string starting at index 0
        return dfs(0)
                 

        