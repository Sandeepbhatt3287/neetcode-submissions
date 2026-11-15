class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        # one empty prefix, so subarrays starting at index 0 get counted
        seen = {0: 1}

        res = 0
        total = 0

        for num in nums:
            total += num

            # an earlier prefix of total - k means the stretch after it sums to k
            res += seen.get(diff := total - k, 0)

            # record this prefix for the indices still to come
            if total in seen:
                seen[total] += 1
            else:
                seen[total] = 1

        return res