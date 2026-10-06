class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """


        m, n = len(heights), len(heights[0])
        MAP = [[set() for i in range(n)] for j in range(m)]
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(r, c, ocean):
            MAP[r][c].add(ocean)
            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                if 0 <= nx < m and 0 <= ny < n \
                        and ocean not in MAP[nx][ny] \
                        and heights[nx][ny] >= heights[r][c]:     # uphill
                    dfs(nx, ny, ocean)

        for i in range(m):
            dfs(i, 0, 'P')        # left edge
            dfs(i, n-1, 'A')      # right edge
        for j in range(n):
            dfs(0, j, 'P')        # top edge
            dfs(m-1, j, 'A')      # bottom edge

        return [[r, c] for r in range(m) for c in range(n) if len(MAP[r][c]) == 2]


        # m = len(heights)
        # n = len(heights[0])

        # MAP = [[set() for i in range(n)] for j in range(m)]
        # res = []

        # dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        # def dfs(r, c, visited):
        #     visited.add((r, c))                                    # tuple

        #     if r == 0 or c == 0:
        #         MAP[r][c].add('P')
        #     if r == m-1 or c == n-1:
        #         MAP[r][c].add('A')
        #     # no return here                                       # removed

        #     for dx, dy in dirs:
        #         nx = r + dx
        #         ny = c + dy
        #         if 0 <= nx < m and 0 <= ny < n \
        #                 and heights[r][c] >= heights[nx][ny] \
        #                 and (nx, ny) not in visited:               # bounds + tuple
        #             dfs(nx, ny, visited)
        #             MAP[r][c] = MAP[r][c].union(MAP[nx][ny])



        # for i in range(m):
        #     for j in range(n):
        #         dfs(i,j,set())
        #         if 'P' in MAP[i][j] and 'A' in MAP[i][j]:
        #             res.append([i,j])

        # return res


