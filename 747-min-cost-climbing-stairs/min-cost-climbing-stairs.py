class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if len(cost)==1:
            return cost[0]
        if len(cost)==2:
            return min(cost[0],cost[1])

        prev2, prev1 = 0, 0                       # 1. both starts are free
        for i in range(2, len(cost) + 1):         # 2. the top is step n, not n-1
            tmp1 = prev1
            prev1 = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = min(tmp1,prev2 + cost[i-2])       
        return prev1                              # 4. the answer is dp[n]

            






        