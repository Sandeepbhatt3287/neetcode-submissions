class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res , sol = [], []
        n = len(nums)

        def comb(i,total):

            if total == target:
                res.append(sol[:])
                return
            
            if i>= n or total> target:
                return

            comb(i+1 ,total)

            sol.append(nums[i])
            comb(i,total+nums[i])
            sol.pop()
        
        comb(0,0)

        return res
        