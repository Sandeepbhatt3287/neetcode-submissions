class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        Row, Col = len(matrix), len(matrix[0])

        def solve(r,c,pre):
        
            if ( r<0 or r == Row or c<0 or c==Col or matrix[r][c] <= pre ):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            res = max(res, 1 + solve(r+1,c,matrix[r][c]))
            res = max(res, 1 + solve(r-1,c, matrix[r][c]))
            res = max(res, 1 + solve(r,c+1,matrix[r][c]))
            res = max(res, 1 + solve(r,c-1, matrix[r][c]))

            dp[(r,c)] = res

            return res


        for r in range(Row):
            for c in range(Col):
                solve(r,c,-1)
            

        return max(dp.values())