from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        H = collections.defaultdict(list)
        
        for i in range(len(strs)):
            
            arr = str_to_arr(strs[i])
            H[arr].append(strs[i])
            
        res = list(H.values())
        return res
            
def str_to_arr(s):
    arr = [0]*26
    for c in s:
        arr[ord(c)-ord('a')] += 1
    return tuple(arr)



    #     Hash_total = defaultdict(list)


    #     for s in strs:

    #         H = self.create_keys(s)
    #         Hash_total[H].append(s)

    #     return list(Hash_total.values())


    # def create_keys(self,s):

    #     H = [0]*26

    #     for s1 in s:
    #         H[ ord(s1) - ord('a') ] += 1

    #     return tuple(H)

        





