class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        total = sum(nums)

        # the buckets have to come out even
        if total % k != 0:
            return False

        target = total // k

        # largest first, so dead ends surface near the top of the tree
        nums.sort(reverse=True)

        # one oversized element can never fit in any bucket
        if nums[0] > target:
            return False

        n = len(nums)
        used = [False] * n

        def back(start: int, remaining: int, subset_sum: int) -> bool:
            # every bucket came out full
            if remaining == 0:
                return True

            # this bucket is done, open a fresh one from the left
            if subset_sum == target:
                return back(0, remaining - 1, 0)

            for j in range(start, n):
                if used[j]:
                    continue

                # equal values are interchangeable, so trying both wastes a branch
                if j > start and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                if subset_sum + nums[j] > target:
                    continue

                used[j] = True
                if back(j + 1, remaining, subset_sum + nums[j]):
                    return True
                used[j] = False

                # this element has to live somewhere, and an empty bucket is the
                # most forgiving place it will ever get, so nothing can work
                if subset_sum == 0:
                    break

            return False

        return back(0, k, 0)