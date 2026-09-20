class TrieNode():

    def __init__(self):
        self.children = {}
        self.finish = False


class WordDictionary(object):

    def __init__(self):
        self.root =  TrieNode()       

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """

        curr = self.root 

        for w in word:

            if w not in curr.children:
                curr.children[w] = TrieNode()
                
            curr = curr.children[w]

        curr.finish = True
            
                

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        


        def dfs(curr,start):

            for j in range(start,len(word)):

                w = word[j]


                if w == '.':
                    for child in curr.children.values():
                        if dfs(child, j + 1):
                            return True
                    return False


                if w not in curr.children:
                    return False

                curr = curr.children[w]


            return curr.finish

        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)