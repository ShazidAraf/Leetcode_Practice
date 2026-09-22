import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        nums.sort()


        def dfs(i,curr):

            res.append(curr[:])

            if i> len(nums)-1:
                return

            
            for j in range(i,len(nums)):

                if j>i:
                    if nums[j-1]==nums[j]:
                        continue

                curr.append(nums[j])
                dfs(j+1,curr)
                curr.pop()


        dfs(0,[])
        return res
