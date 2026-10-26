class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            subarray = 1
            curSum =0

            for num in nums:
                curSum += num

                if curSum > largest:
                    subarray += 1
                    if subarray >k:
                        return False
                    curSum = num
            return True
        
        l, r = max(nums), sum(nums)
        res = r

        while l<=r:

            m = l + (r-l)//2
            
            if canSplit(m):
                r = m-1
            else:
                l = m +1
        
        return l

