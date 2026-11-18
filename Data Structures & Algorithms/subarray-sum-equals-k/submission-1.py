class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            summ =0

            for j in range(i, len(nums)):
                summ += nums[j]

                if summ == k:
                    res +=1
        
        return res


        