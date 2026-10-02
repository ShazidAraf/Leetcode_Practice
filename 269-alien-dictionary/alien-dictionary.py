class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        graph = {c: [] for word in words for c in word}   # changed: every letter is a key

        for w1, w2 in zip(words, words[1:]):              # changed: compare neighboring words
            for a, b in zip(w1, w2):
                if a != b:
                    graph[b].append(a)                    # b needs a first
                    break                                 # only the first difference counts
            else:
                if len(w1) > len(w2):                     # "abc" before "ab" is invalid
                    return ""


        # Detect if there is a cycle

        visited = set()
        visiting = set()
        order = []

        def dfs(parent):

            if parent in visited:
                return False
            
            visiting.add(parent)

            for child in graph[parent]:

                if child in visiting:
                    return True
                if dfs(child):
                    return True

            visiting.remove(parent)
            visited.add(parent)
            order.append(parent)

            return False

        for c in list(graph.keys()):
            # print(c)
            if dfs(c):
                return ""
        
        return ''.join(order)
