class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        def dfs(curr,c1,c2):

            if len(curr)==2*n and c1==n and c2==n:
                res.append(curr)
                return

            if c1>n or c2>n or c2>c1:
                return

            

            
            for i in range(2):

                if i==0:
                    dfs(curr+'(',c1+1,c2)
                else:
                    dfs(curr+')',c1,c2+1)



        dfs('',0,0)

        return res
            

            


            

