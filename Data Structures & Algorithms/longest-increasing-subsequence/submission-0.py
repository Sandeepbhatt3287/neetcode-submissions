class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n)]

        def solve(i, p):
            if i == n:
                return 0

            if dp[i][p + 1] != -1:
                return dp[i][p + 1]

            take = 0

            if p == -1 or nums[p] < nums[i]:
               take = 1 + solve(i+1 , i) 
            
            
            skip = solve(i + 1, p)

            dp[i][p + 1] = max(take, skip)
            return dp[i][p + 1]

        return solve(0, -1)