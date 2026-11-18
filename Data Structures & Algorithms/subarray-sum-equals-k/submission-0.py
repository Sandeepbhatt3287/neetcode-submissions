class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        n = len(nums)
        sum = 0


        for r in range(n):
            sum = 0
            for j in range(r,n):
                sum += nums[j]

                if sum == k:
                    count +=1
        
        return count