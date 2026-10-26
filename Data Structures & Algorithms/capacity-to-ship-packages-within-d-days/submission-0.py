class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        res = r

        def canShip(cap):
            ships,curCap =1,cap
            for w in weights:
                if curCap -w <0:
                    ships +=1
                    if ships > days:
                        return False
                    curCap = cap
                curCap -=w
            return True

        while l<=r:
            mid = (l +r)//2

            if canShip(mid):
                res = min(res,mid)
                r = mid -1
            
            else:
                l = mid +1
        
        return res