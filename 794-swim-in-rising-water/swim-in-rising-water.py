class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        graph = collections.defaultdict(list)
        n = len(grid)

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        minheap = [(grid[0][0],0,0)]
        visit = set()
        t = 0

        while(1):

            cost, row, col = heapq.heappop(minheap)

            if (row,col) in visit:
                continue

            visit.add((row,col))
            t = max(t,cost)

            if row==n-1 and col==n-1:
                return t

            for dr,dc in dirs:

                next_row = row + dr
                next_col = col + dc

                if next_row<0 or next_row>n-1 or next_col<0 or next_col>n-1 or (next_row,next_col) in visit:
                    continue

                heapq.heappush(minheap, (grid[next_row][next_col],next_row,next_col))




        