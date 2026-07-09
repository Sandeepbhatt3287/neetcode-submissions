class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res, sol = [],[]

        nums.sort()


        def dfs(i):

            if i == n:
                res.append(sol[:])
                return
            

            sol.append(nums[i])
            dfs(i+1)
            sol.pop()

            while i+1 < n and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)

        return res
        