import numpy as np

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()
        order = []

        def dfs(course):

            if course in visited:
                return False

            visiting.add(course)

            for pre in graph[course]:

                if pre in visiting:
                    return True

                if dfs(pre):
                    return True

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return False


        for course in list(graph.keys()):

            if dfs(course):
                return []

        return order



        
 






