class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        H = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}

        res = []


        def dfs(i,curr):

            if i==len(digits):
                res.append(''.join(curr))
                return

            z = H[int(digits[i])]

            
            for j in range(len(z)):

                curr.append(z[j])
                dfs(i+1,curr)
                curr.pop()

        dfs(0,[])
        return res






        

            


            

            
        