class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        visit = set()

        def dfs(i,j):
            if i< 0 or i>= row or j <0 or j >=col or grid[i][j] ==0:
                return 1
            
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))

            peri = dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)

            return peri

        
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    return dfs(i,j)
        
        return 0


        