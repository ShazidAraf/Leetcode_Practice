class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        H = {')':'(', '}':'{', ']':'['}
        left_bracket =  ['(','{','[']
        right_bracket = [')','}',']']


        for c in s:

            if c in left_bracket:
                stack.append(c)

            if c in right_bracket:

                if len(stack)==0:
                    return False

                temp = stack.pop()

                if temp!=H[c]:
                    return False

        if len(stack)==0:
            return True
        else:
            return False

