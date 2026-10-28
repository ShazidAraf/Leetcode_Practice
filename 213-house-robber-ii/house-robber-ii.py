class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(numbers):

            prev2,prev1 = 0,0

            for x in numbers:
                prev2,prev1 = prev1, max(prev2+x,prev1)

            return prev1


        return max(rob_linear(nums[0:-1]) , rob_linear(nums[1:]))