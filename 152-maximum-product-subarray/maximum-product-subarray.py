class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        best = nums[0]
        max_res = 1
        min_res = 1
        

        for i in range(len(nums)):

            temp = (nums[i],max_res*nums[i], min_res*nums[i])
            max_res = max(temp)
            min_res = min(temp)
            best = max(best,max_res)

            if nums[i]==0:
                max_res = 1
                min_res = 1            

        return best



            