class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def back(i,total):
            if i ==len(nums):
                return total==target
            
            return (back(i+1,total + nums[i]) + back(i+1,total- nums[i]))
        
        return back(0,0)