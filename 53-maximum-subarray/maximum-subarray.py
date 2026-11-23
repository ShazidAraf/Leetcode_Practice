class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        best = nums[0]
        s = 0

        for i in range(len(nums)):

            s+=nums[i]
            temp = [best,s,nums[i]]
            best = max(temp)

            if s<0:
                s = 0


        return best



        