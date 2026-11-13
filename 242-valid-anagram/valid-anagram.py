class Solution(object):

    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False
        
        H_s = Counter(s)
        H_t = Counter(t)
        
        for c in list(H_s.keys()):
            
            count1 = H_s.get(c,0)
            count2 = H_t.get(c,0)
            
            if count1!=count2:
                return False
            
        return True
        