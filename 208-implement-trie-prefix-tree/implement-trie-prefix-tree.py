class Trie(object):

    def __init__(self):

        self.word = []
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.word.append(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.word:
            return True

        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        for i in range(len(self.word)):
            w = self.word[i]

            if w.startswith(prefix):
                return True


        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)