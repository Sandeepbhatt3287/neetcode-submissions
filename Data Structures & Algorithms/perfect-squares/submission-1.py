class Solution:
    def numSquares(self, n: int) -> int:

        # worst case for every amount is that many ones
        dp = [0] * (n + 1)

        for target in range(1, n + 1):
            best = target

            i = 1
            while i * i <= target:
                # use this square, then solve whatever is left
                if dp[target - i * i] + 1 < best:
                    best = dp[target - i * i] + 1
                i += 1

            dp[target] = best

        return dp[n]