class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        cost = [[float('inf') for j in range(n)] for i in range(m)]

        def dfs(r, c, t):
            if r<0 or c<0 or r>m-1 or c>n-1 or grid[r][c]==0 or t>=cost[r][c]:
                return
            cost[r][c] = t
            dfs(r-1,c,t+1); dfs(r+1,c,t+1); dfs(r,c-1,t+1); dfs(r,c+1,t+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    dfs(i,j,0)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and cost[i][j]==float('inf'):
                    return -1
                if grid[i][j]!=0:
                    ans = max(ans, cost[i][j])
        return ans


                
