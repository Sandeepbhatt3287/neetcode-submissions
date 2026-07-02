class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store = set(nums)

        for num  in store:
            if (num-1) not in store:
                length = 1
                while (num + length) in store:
                    length +=1
                res = max(res, length)
        
        return res