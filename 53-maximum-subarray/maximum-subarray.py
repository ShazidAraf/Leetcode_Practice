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
            temp = [s,nums[i]]
            max_sum = max(temp)
            best = max(best,max_sum)

            if s<0:
                s = 0


        return best



        