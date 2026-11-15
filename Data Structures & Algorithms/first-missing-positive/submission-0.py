class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        miss = 1

        for num in nums:
            if num > 0 and miss == num:
                miss +=1
        
        return miss