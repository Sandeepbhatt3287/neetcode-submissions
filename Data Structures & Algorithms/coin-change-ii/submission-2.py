class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = {}
        # def solve(i,sum):

        #     if sum == amount:
        #         return 1
            
        #     if sum > amount or i == len(coins):
        #         return 0

        #     if (i,sum) in dp:
        #         return dp[(i,sum)]
        #     take = solve(i,sum+coins[i])
        #     skip = solve(i+1,sum)

        #     dp[(i,sum)] = take + skip

        #     return dp[(i,sum)]
        

        # return solve(0,0)

      
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):

                take = 0

                if a >= coins[i]:
                    take = dp[i][a - coins[i]]

                skip = dp[i + 1][a]

                dp[i][a] = take + skip

        return dp[0][amount]


        


