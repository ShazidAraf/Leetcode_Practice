class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """


        dp = [amount+1]*(amount+1)

        dp[0] = 0


        for i in range(1,amount+1):
            for j in coins:
                if i>=j:
                    dp[i] = min(dp[i],1+dp[i-j])

        print(dp)


        if dp[-1]==amount+1:
            return -1
        else:
            return dp[-1]


# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """

#         self.res = -1
#         coins.sort()


#         def dfs(i,curr,total):


#             if total==amount:

#                 if self.res == -1:
#                     self.res = len(curr)

#                 else:
#                     if len(curr)<self.res:
#                         self.res = len(curr)

#                 return

            
#             if i>len(coins)-1:
#                 return

            
#             for j in range(i,len(coins)):

#                 if total + coins[j]>amount:
#                     break

#                 curr.append(coins[j])
#                 dfs(j,curr,total+coins[j])
#                 curr.pop()


#         dfs(0,[],0)

#         return self.res