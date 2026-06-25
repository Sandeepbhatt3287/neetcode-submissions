class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)-1
        l = 0

        while l<=n:
            mid = (l+n)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                l = mid +1

            else:
                n = mid -1

        return -1 
        