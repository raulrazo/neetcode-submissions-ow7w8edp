class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # set left and right boundaries
        l, r = 0, len(matrix) - 1

        # iterate thru entire row except last element
        while l < r:
            for i in range(r - l):
                # set top and bottom boundaries
                top, bottom = l, r

                # save the topLeft value for temp purposes
                topLeft = matrix[top][l + i] 

                # rotate bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # rotate bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # rotate top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # rotate top left into top right
                matrix[top + i][r] = topLeft   

            # update our boundaries
            r -= 1
            l += 1   