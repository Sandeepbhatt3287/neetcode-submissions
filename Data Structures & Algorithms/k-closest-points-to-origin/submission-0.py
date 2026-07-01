class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxh = []

        for x,y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxh, [dist,x,y])
            if len(maxh) > k:
                heapq.heappop(maxh)

        res =[]

        while maxh:
            dist, x,y = heapq.heappop(maxh)
            res.append([x,y])
        
        return res