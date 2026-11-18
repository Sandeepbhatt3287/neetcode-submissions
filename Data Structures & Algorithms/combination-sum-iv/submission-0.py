class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()


        def back(total):

            if total == 0:
                return 1
            
            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                res += back(total - nums[i])
            
            return res


        return back(target)