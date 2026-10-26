class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        nums.sort()
        res = []


        def dfs(curr,used):

            if len(curr)==len(nums):
                res.append(curr[:])
                return

            
            for i in range(n):


                if used[i]:
                    continue

                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(curr,used)
                used[i] = False
                curr.pop()

        
        dfs([],[False]*n)

        return res