class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) -1
        l =0
        res = len(nums)

        while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                res = mid
                r = mid -1
        
        return l
