class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        r , c = 0, len(matrix[0])-1

        while r<len(matrix) and c>=0:

            if target==matrix[r][c]:
                return True
            elif target<matrix[r][c]:
                c-=1
            else:
                r+=1

        return False
