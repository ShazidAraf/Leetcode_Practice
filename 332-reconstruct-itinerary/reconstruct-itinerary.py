class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        

        tickets.sort(reverse=True)
        graph = collections.defaultdict(list)

        for src,dst in tickets:
            graph[src].append(dst)

        res = []

        def dfs(a):

            while graph[a]:
                dfs(graph[a].pop())
            res.append(a)

        dfs("JFK")

        return res[::-1]