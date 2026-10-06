class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(heights)
        n = len(heights[0])

        MAP = [[set() for i in range(n)] for j in range(m)]
        res = []

        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(r, c, visited):
            visited.add((r, c))                                    # tuple

            if r == 0 or c == 0:
                MAP[r][c].add('P')
            if r == m-1 or c == n-1:
                MAP[r][c].add('A')
            # no return here                                       # removed

            for dx, dy in dirs:
                nx = r + dx
                ny = c + dy
                if 0 <= nx < m and 0 <= ny < n \
                        and heights[r][c] >= heights[nx][ny] \
                        and (nx, ny) not in visited:               # bounds + tuple
                    dfs(nx, ny, visited)
                    MAP[r][c] = MAP[r][c].union(MAP[nx][ny])



        for i in range(m):
            for j in range(n):
                dfs(i,j,set())
                if 'P' in MAP[i][j] and 'A' in MAP[i][j]:
                    res.append([i,j])

        return res


