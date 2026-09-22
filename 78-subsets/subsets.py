import copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        res = []



        def dfs(i, curr):
            res.append(curr[:])   
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()


        dfs(0,[])

        return res
