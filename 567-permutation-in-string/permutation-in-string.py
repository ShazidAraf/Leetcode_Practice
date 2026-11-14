class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1)>len(s2):
            return False
        
        H1 = create_hashmap(s1)
        n1 = len(s1)
        H2 = create_hashmap(s2[0:n1])
        
        
        match = 0
        
        for i in range(26):
            if H1[i] == H2[i]:
                match+=1
               
        if match==26:
            return True
        
        
        for i in range(len(s1),len(s2)):

            sub_s2_old = s2[i-len(s1):i]
            sub_s2_new = s2[i+1-len(s1):i+1]
            
            a1 = ord(sub_s2_old[0]) - ord('a')
            a2 = ord(sub_s2_new[-1]) - ord('a')
            
            if H1[a1]==H2[a1]:
                match -=1
            H2[a1] = H2[a1] - 1
            if H1[a1] == H2[a1]:
                match += 1

            if H1[a2]==H2[a2]:
                match -=1
            H2[a2] = H2[a2] + 1
            if H1[a2]==H2[a2]:
                match+=1
                
            if match==26:
                return True
            
        return False
                

def create_hashmap(s):
    H = [0]*26
    for c in s:
        H[ ord(c) - ord('a') ]+=1
    return H



#         map1 = create_hashmap(s1)
#         key1 = map1.keys()

#         for i in range(len(s2)):

#             if s2[i] in key1:

#                 sub_s2 = s2[i:i+len(s1)]
#                 map2 = create_hashmap(sub_s2)

#                 for j in range(len(key1)):
#                     c2 = map2.get(key1[j],0)
#                     c1 = map1.get(key1[j],0)

#                     if c1!=c2:
#                         break

#                     if j==len(key1)-1:
#                         return True


#         return False


# def create_hashmap(s):
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1


#     return char_count
        