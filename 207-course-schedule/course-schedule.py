class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)


        visiting = set()
        visited = set()


        def dfs(course):

            if course in visited:          # added
                return False

            visiting.add(course)
            
            for pre in graph[course]:
                if pre in visiting:
                    return True

                if dfs(pre):               # changed
                    return True

            visiting.remove(course)
            visited.add(course)            # added

            return False


        for course in list(graph):
            if course in visited:
                continue
            if dfs(course):
                return False
        return True


            




        