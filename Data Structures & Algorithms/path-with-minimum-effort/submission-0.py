class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row , col = len(heights), len(heights[0])
        minHeap = [[0,0,0]]

        visit = set()

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]


        while minHeap:
            diff, r,c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            
            visit.add((r,c))

            if (r,c) == (row-1, col-1):
                return diff
            
            for dr,dc in dirs:
                newr, newc = r+ dr , c+ dc

                if (newr < 0 or newc < 0 or newr >= row or newc >= col or (newr,newc) in visit):
                    continue
                
                newDiff = max(diff , abs(heights[r][c] - heights[newr][newc]))

                heapq.heappush(minHeap , [newDiff , newr,newc])
        
        return 0
