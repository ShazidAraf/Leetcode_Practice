class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        best = nums[0]
        s = 0
        for x in nums:
            s += x
            best = max(best, s)
            if s < 0:
                s = 0
        return best


        