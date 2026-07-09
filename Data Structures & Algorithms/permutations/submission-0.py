class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res , sol = [],[]

        def dfs():
            if len(sol) == n:
                res.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    dfs()
                    sol.pop()


        dfs()
        return res
        