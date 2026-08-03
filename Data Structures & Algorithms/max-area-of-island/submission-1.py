from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        max_area = 0
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # Tell Python we want to modify the cur_area variable outside this function
            nonlocal cur_area  
            
            # Base case check
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0 or (r, c) in visit:
                return

            # Mark visited and increment the current island's tracking area
            visit.add((r, c))
            cur_area += 1

            # Traverse all 4 neighbors using your loop structure
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(row):
            for j in range(col):
                # Only kick off a search if we hit an unvisited island piece
                if grid[i][j] == 1 and (i, j) not in visit:
                    cur_area = 0  # Reset counter to 0 for each brand new island
                    dfs(i, j)
                    max_area = max(max_area, cur_area)
        
        return max_area
