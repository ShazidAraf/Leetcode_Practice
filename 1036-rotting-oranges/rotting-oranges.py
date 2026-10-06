class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        q = collections.deque()
        fresh = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j]==2:
                    q.append([i,j])

                if grid[i][j]==1:
                    fresh+=1

        
        time = 0
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        while q and fresh:



            for _ in range(len(q)):

                row,col = q.popleft()

                for dx,dy in dirs:

                    nx = row+dx
                    ny = col+dy

                    if nx<0 or ny<0 or nx>m-1 or ny>n-1 or grid[nx][ny]!=1:
                        continue

                    grid[nx][ny]=2
                    q.append([nx,ny])
                    fresh-=1

            time+=1

        if fresh>0:
            return -1
        else:
            return time

                




















        # m = len(grid)
        # n = len(grid[0])

        # cost = [[float('inf') for j in range(n)] for i in range(m)]


        # def dfs(r, c, t):
        #     if r<0 or c<0 or r>m-1 or c>n-1 or grid[r][c]==0 or t>=cost[r][c]:
        #         return
        #     cost[r][c] = t
        #     dfs(r-1,c,t+1); dfs(r+1,c,t+1); dfs(r,c-1,t+1); dfs(r,c+1,t+1)

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==2:
        #             dfs(i,j,0)

        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==1 and cost[i][j]==float('inf'):
        #             return -1
        #         if grid[i][j]!=0:
        #             ans = max(ans, cost[i][j])
        # return ans


                
