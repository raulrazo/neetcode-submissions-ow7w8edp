class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # hashmap that maps every closing to opening 
        # bracket for O(1) lookups to verify pairs
        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for c in s:
            # checks if c is a closing bracket
            if c in closeToOpen:
                # verify stack is non-empty before
                # checking top element.
                # and checks if the most recent opening
                # bracket on top of stack matches
                # this closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # if it does, then this pair is 
                    # resolved and we can pop
                    stack.pop()
                else:
                    # if stack is empty (closing 
                    # bracket appeared with nothing
                    # to match).

                    # or this closing bracket isn't a
                    # valid pair with the most recent
                    # opening bracket.

                    # then this is invalid so return F
                    return False

            # if this char is an opening bracket
            else:
                # then we push it to stack so it can
                # wait for its corresponding closer
                stack.append(c)

        # return True if stack is empty b/c that means
        # there are no opening brackets that remain
        # unclosed
        return True if not stack else False 
        