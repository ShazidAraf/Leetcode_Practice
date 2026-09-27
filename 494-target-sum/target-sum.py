class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        DP = {0:1}


        for i in range(len(nums)):


            newDP = {}

            for k,v in DP.items():

                if k+nums[i] not in newDP.keys():
                    newDP[k+nums[i]] = 0
                if k-nums[i] not in newDP.keys():
                    newDP[k-nums[i]] = 0

                newDP[k+nums[i]] += v
                newDP[k-nums[i]] += v

            DP = newDP

            

        return DP.get(target,0)


            

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