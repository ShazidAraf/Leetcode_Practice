class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        max_f = 0
        max_len = 0
        l = 0
        r = 0
        H = {}


        while r<len(s):

            H[s[r]] = H.get(s[r], 0) + 1
            max_f = max(max_f, H[s[r]])

            if (r - l + 1) - max_f > k:
                H[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r = r+1

        return max_len




