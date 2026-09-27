class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            newDP = defaultdict(int)

            for curr_sum, count in dp.items():
                
                newDP[curr_sum + nums[i]] += count
                newDP[curr_sum - nums[i]] += count

            dp = newDP

        return dp.get(target,0)


            

# class Solution(object):
#     def findTargetSumWays(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """

#         self.ans = 0


#         def dfs(curr_sum,i):

#             if curr_sum==target and i==len(nums):
#                 self.ans+=1
#                 return

#             if i>len(nums)-1:
#                 return


#             dfs(curr_sum+nums[i],i+1)
#             dfs(curr_sum-nums[i],i+1)


#         dfs(0,0)

#         return self.ans       