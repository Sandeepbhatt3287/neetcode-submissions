class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)
        res, sol = [] , []


        def back(i):
            if i ==n :
                res.append(sol[:])
                return 

            back(i+1)

            sol.append(nums[i])
            back(i+1)
            sol.pop()
        
        back(0)
        return res

        
        