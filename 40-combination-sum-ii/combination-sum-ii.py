import copy

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        res = []

        def sum_check(i,curr,total):

            if total==target:
                res.append(copy.deepcopy(curr))
                return

            if i>=len(candidates) or total>target:
                return

            for j in range(i,len(candidates)):

                if j>i:
                    if candidates[j-1]==candidates[j]:
                        continue

                if total + candidates[j] > target:
                    break



                curr.append(candidates[j])
                sum_check(j+1, curr, total+candidates[j])
                curr.pop()

                



        sum_check(0,[],0)
        return res

