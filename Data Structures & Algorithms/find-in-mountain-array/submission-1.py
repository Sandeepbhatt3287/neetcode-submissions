class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 1 , n -2

        while l<=r:
            m = (l+r)//2
            le , mid ,ri = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if le < mid < ri:
                l = m+1
            elif le > mid > ri:
                r = m-1
            else:
                break
        
        peak = m


        l , r = 0 , peak-1

        while l<=r:
            m  = (l+r) //2

            val = mountainArr.get(m)

            if val < target:
                l = m +1
            elif val>target:
                r = m-1
            else:
                return m
        
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m

        return -1
        