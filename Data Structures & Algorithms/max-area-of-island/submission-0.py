class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid) , len(grid[0])
        visit = set()
        area = 0
        dir = [[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(r,c):
            q = deque()
            grid[r][c]=0
            q.append((r,c))
            res =1

            while q:
                row ,col = q.popleft()
                for dr , dc in dir:
                    nr,nc = dr + row , dc+ col
                    if (nr < 0 or nc <0 or nr>=rows or nc >= cols or grid[nr][nc]==0):
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc]=0
                    res +=1
            return res

            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = max(bfs(i,j),area)
                
        
        return area
        