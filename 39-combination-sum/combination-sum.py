import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        res = []

        def dfs(curr,curr_sum,i):

            if curr_sum==target:
                res.append(curr[:])
                return

            
            for j in range(i,len(candidates)):


                if curr_sum + candidates[j] > target:
                    break

                curr.append(candidates[j])
                dfs(curr,curr_sum+candidates[j],j)
                curr.pop()

        
        dfs([],0,0)

        return res



            
