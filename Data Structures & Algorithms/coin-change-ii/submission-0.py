class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        sum = 0
        def solve(i,sum):

            if sum == amount:
                return 1
            
            if sum > amount or i == len(coins):
                return 0

            
            # sum += coins[i]


            take = solve(i,sum+coins[i])
            skip = solve(i+1,sum)


            return take + skip
        

        return solve(0,0)


