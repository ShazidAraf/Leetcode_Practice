class Solution(object):

    def searchMatrix(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m,n = len(nums), len(nums[0])

        low = 0
        high = m*n-1


        def convert_rc(k):
            return k//n, k%n


        while high>=low:

            mid = (high+low)//2

            r,c = convert_rc(mid)

            print(r,c)

            if nums[r][c]==target:
                return True

            
            if nums[r][c]>target:
                high = mid-1
            else:
                low = mid+1

        return False

            

            




        