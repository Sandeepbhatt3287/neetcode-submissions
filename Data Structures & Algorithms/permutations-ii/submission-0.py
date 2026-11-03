class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def dfs(sol):
            if n == len(sol):
                res.add(tuple(sol))
                return
            
            for i in range(n):
                if nums[i] != float('-inf'):
                    sol.append(nums[i])
                    nums[i] = float('-inf')
                    dfs(sol)
                    nums[i] = sol[-1]
                    sol.pop()

        
        dfs([])
        return list(res)
        