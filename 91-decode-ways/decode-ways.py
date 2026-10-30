class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """


        dp = [0]*(len(s)+1)
        dp[0] = 1

        for t in range(1,len(s)+1):
            for x in (1,2):

                if t>=x:

                    p = s[t-x:t]

                    if p[0]== '0' or int(p)>26:
                        continue
                    dp[t]+=dp[t-x]


        return dp[len(s)]








        # res = []


        # def dfs(curr,i):


        #     if i>len(s)-1:
        #         res.append(curr[:])
        #         return

        #     if s[i]=='0':
        #         return            

        #     curr.append(s[i])
        #     dfs(curr,i+1)
        #     curr.pop()

        #     if i<len(s)-1 and (int(s[i])==1 or int(s[i])==2):
                
        #         if int(s[i])==1 or (int(s[i])==2 and int(s[i+1])<7):
        #             curr.append(s[i:i+2])
        #             dfs(curr,i+2)
        #             curr.pop()

        # dfs([],0)
        # return len(res)


            




            



        