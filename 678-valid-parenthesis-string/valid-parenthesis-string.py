class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """


        hi, lo = 0,0

        for c in s:

            if c=='(':
                lo+=1
                hi+=1

            elif c==')':
                lo-=1
                hi-=1

            elif c=='*':
                lo-=1
                hi+=1

            if hi<0:
                return False

            lo = max(lo,0)

        if lo==0:
            return True
        else:
            return False





        