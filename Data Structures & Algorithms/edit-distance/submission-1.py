class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        w1 = len(word1)
        w2 = len(word2)

        def solve(i,j):

            if i==w1:
                return w2-j
            
            if j==w2:
                return w1-i

            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                take = solve(i+1, j+1)
                dp[(i,j)] = take
            
            else:
                res = min(solve(i+1,j), solve(i,j+1))
                res = min(res,solve(i+1,j+1))

                dp[(i,j)] = res +1
            
            return dp[(i,j)]

        
        return solve(0,0)


