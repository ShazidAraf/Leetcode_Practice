class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums)%2==1:
            return False

        DP = set()
        DP.add(0)
        target = sum(nums)//2


        for i in range(len(nums)):

            newDP = set()

            for j in DP:
                newDP.add(nums[i]+j)
                newDP.add(j)

            DP = newDP

        if target in DP:
            return True
        else:
            return False




        