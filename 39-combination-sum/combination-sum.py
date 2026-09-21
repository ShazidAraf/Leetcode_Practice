import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()


        def dfs(i,curr_res, curr_sum):


            if curr_sum == target:
                res.append(copy.deepcopy(curr_res))
                return

            if i>=len(candidates) or curr_sum > target:
                return

            curr_res.append(candidates[i])
            dfs(i,curr_res, curr_sum+candidates[i])
            curr_res.pop()
            dfs(i+1,curr_res, curr_sum)

        
        dfs(0,[], 0)

        return res