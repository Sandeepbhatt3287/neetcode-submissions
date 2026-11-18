class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l=0
        r = len(nums) -1
        
        
        while l<=r:

            cur = nums[l] + nums[r]
            if cur == target:
                return [l,r]
            
            elif cur < target:
                l +=1
            else:
                r -=1
        