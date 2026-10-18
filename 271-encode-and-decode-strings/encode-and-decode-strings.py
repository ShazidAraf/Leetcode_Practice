class Codec:


    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """

        res = []

        for s in strs:
            res.append(str(len(s)) + '#' + s)

        return ''.join(res)

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """

        j = 0
        i = 0
        res = []

        while j<len(s):

            if s[j]=='#':
                l = int(s[i:j])
                st = s[j+1:j+1+l]
                res.append(st)
                i = j+l+1
                j = j+l+1

            else:
                j+=1

        # print(res)

        return res


        

# Your Codec object will be instantiated and called as such:
strs = ["Hello","World"]
codec = Codec()
codec.decode(codec.encode(strs))