class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        threshold = len(nums) // 3

        # keep whatever lands strictly above a third of the array
        res = []
        for num, count in freq.items():
            if count > threshold:
                res.append(num)

        return res

