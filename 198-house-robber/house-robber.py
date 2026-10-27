class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev2, prev1 = 0,0

        for x in nums: 

            prev2,prev1 = prev1, max(prev2+x,prev1)


        return prev1



        # # DFS Solution
        # self.max_sum = 0


        # def dfs(curr_sum,next_idx):

        #     if curr_sum>self.max_sum:
        #         self.max_sum = curr_sum

        #     if next_idx>len(nums)-1:
        #         return

        #     for i in range(next_idx,len(nums)):
        #         dfs(curr_sum+nums[i],i+2)

        # dfs(0,0)

        # return self.max_sum

        

        