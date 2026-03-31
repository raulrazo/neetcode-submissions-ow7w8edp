class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # declare our stack which is also going to be the result
        stack = []

        # go thru every single asteroid in the input
        for a in asteroids:
            # we can only do collisions if the stack is non-empty
            # and the current asteroid we are visiting is negative meaning it is moving to the left
            # and the asteroid at the top of our stack is positive meaning it is moving to the right
            while stack and a < 0 and stack[-1] > 0:
                # store the result of the collision in diff
                diff = a + stack[-1]
                
                # if the asteroids added together is negative that means asteroid a is going to win
                # so we take the value at the top of our stack and pop it
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    # this means a is going to be destroyed
                    # set a to 0 because we are guaranteed that no asteroid is going to be set to 0
                    # so if we set it to 0 then we are definitely not going to add it to the stack
                    # and the while loop while stop executing because a < 0 is no longer going to be true
                    a = 0
                else:
                    # means the asteroids are equal
                    a = 0
                    stack.pop()
                    # this destroys both of the asteroids
                    
            # once this loop is done executing then we have destroyed all the asteroids that can so far
            # so we take the current asteroid and append it our stack but we could have set it to 0 beforehand
            # so we have a condition for it

            if a:
                stack.append(a)

        return stack 
        