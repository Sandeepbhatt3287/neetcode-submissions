# # 

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1] + nums + [1]
#         dp = {}
#         def dfs(l, r):
#             if l > r:
#                 return 0
#             if (l, r) in dp:
#                 return dp[(l, r)]

#             dp[(l, r)] = 0
#             for i in range(l, r + 1):
#                 coins = nums[l - 1] * nums[i] * nums[r + 1]
#                 coins += dfs(l, i - 1) + dfs(i + 1, r)
#                 dp[(l, r)] = max(dp[(l, r)], coins)
#             return dp[(l, r)]

#         return dfs(1, len(nums) - 2)



class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [x for x in nums if x > 0]
        nums = [1] + nums + [1]

        dp = {}

        def solve(l, r):
            if l > r:
                return 0
            if l == r:
                return nums[l - 1] * nums[l] * nums[r + 1]
                
            if (l, r) in dp:
                return dp[(l, r)]

            ans = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += solve(l, i - 1)
                coins += solve(i + 1, r)

                ans = max(ans, coins)

            dp[(l, r)] = ans
            return ans

        return solve(1, len(nums) - 2)