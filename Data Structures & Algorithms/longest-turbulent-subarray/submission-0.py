from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:

        n = len(arr)

        # a single element is trivially turbulent
        if n < 2:
            return n

        res = 1
        count = 1

        # prev is the sign of the comparison before this one
        prev = 0

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                sign = 1
            elif arr[i] < arr[i - 1]:
                sign = -1
            else:
                sign = 0

            # equal neighbours break any run outright
            if sign == 0:
                count = 1

            # the sign flipped, so this pair extends the run
            elif sign != prev:
                count += 1

            # same direction twice means a fresh run of two starts here
            else:
                count = 2

            if count > res:
                res = count

            prev = sign

        return res