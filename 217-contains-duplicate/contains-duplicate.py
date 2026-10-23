class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        H = {}
        
        for i in nums:
            H[i] = H.get(i,0)+1
            
            if H[i]>1:
                return True
            
        return False