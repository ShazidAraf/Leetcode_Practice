class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

        INF = 2147483647

        m , n = len(rooms), len(rooms[0])

        q = collections.deque()
        

        for i in range(m):
            for j in range(n):

                if rooms[i][j]==0:
                    q.append([i,j])

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            for _ in range(len(q)):

                row, col = q.popleft()
                
                for dx,dy in dirs:

                    nx = row+dx
                    ny = col+dy

                    if nx<0 or ny<0 or nx>m-1 or ny>n-1 or rooms[nx][ny]!=INF:
                        continue

                    q.append([nx,ny])
                    rooms[nx][ny] = rooms[row][col] + 1






