class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res, sol = [], []
        candidates.sort()


        def comb(i,total):
            if total == target:
                res.append(sol[:])
                return

            
            if i ==n or total > target:
                return 

            sol.append(candidates[i])
            comb(i+1, total+candidates[i])
            sol.pop()


            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            comb(i+1, total)

        
        comb(0,0)

        return res