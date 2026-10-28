class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums=[1,2]

        dp = [0]*(n+1)
        dp[0] = 1


        for t in range(1,n+1):
            for x in nums:
                if t>=x:
                    dp[t]+=dp[t-x]


        return dp[n]


        