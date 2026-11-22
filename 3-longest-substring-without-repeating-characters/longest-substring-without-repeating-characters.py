class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 0
        H = {}
        max_len = 0

        while r<len(s):

            H[s[r]] = H.get(s[r],0)+1

            if H[s[r]]>1:
                while H[s[r]]!=1:
                    H[s[l]] = H[s[l]] -  1
                    l = l+1

            max_len = max(max_len,r-l+1)
            r = r+1

        return max_len
