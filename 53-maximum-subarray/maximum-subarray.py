class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]
        s = 0

        for i in range(len(nums)):

            s+=nums[i]

            res = max(res,s)

            if s<0:
                s = 0


        return res



        