import copy

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        MASK = [0 for _ in nums]

        # nums.sort()


        def dfs(curr,mask):


            if len(curr)==len(nums):

                res.append(curr[:])
                return

            
            for j in range(len(nums)):

                if mask[j]==1:
                    continue

                curr.append(nums[j])
                mask[j]=1
                dfs(curr,mask)
                curr.pop()
                mask[j]=0


        dfs([],MASK)
        return res

        

