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
        


        def dfs(i,curr):


            if i==len(word):
                return curr.finish

            if word[i]=='.':
                for child in curr.children.values():
                    if dfs(i+1,child):
                        return True
                return False

            if word[i] not in curr.children:
                return False

            curr = curr.children[word[i]]
            return dfs(i+1,curr)

        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)