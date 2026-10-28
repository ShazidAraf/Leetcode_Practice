class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        l,r = 0,0
        jump = 0
        farthest = 0

        while r<len(nums)-1:


            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])

            jump+=1
            l = r+1
            r = farthest

        return jump







        