class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = {}

        ns = len(s)
        nt = len(t)

        res = 0


        def solve(i,j):

            if j == nt:
                return 1
                
            if i == ns  :
                return 0

            
            
            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                take = solve(i+1,j+1)

                skip =solve(i+1,j)

                dp[(i,j)] = take + skip
            else:
                dp[(i,j)] = solve(i+1,j)


            return dp[(i,j)]

        return solve(0,0)

        