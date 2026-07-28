class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def solve(i,sum):

            if sum == amount:
                return 1
            
            if sum > amount or i == len(coins):
                return 0

            if (i,sum) in dp:
                return dp[(i,sum)]
            take = solve(i,sum+coins[i])
            skip = solve(i+1,sum)

            dp[(i,sum)] = take + skip

            return dp[(i,sum)]
        

        return solve(0,0)


