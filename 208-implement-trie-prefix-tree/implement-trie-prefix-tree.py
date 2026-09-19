class TrieNode():

    def __init__(self):

        self.children = {}
        self.finish = False

class Trie(object):

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):
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
        curr = self.root

        for w in word:

            if w not in curr.children:
                return False

            curr = curr.children[w]

        if curr.finish:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        curr = self.root

        for w in prefix:

            if w not in curr.children:
                return False

            curr = curr.children[w]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)