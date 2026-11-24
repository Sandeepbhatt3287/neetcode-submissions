class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending  = []

        for i , (enTime , prTime) in enumerate(tasks):
            heapq.heappush(pending , (enTime,prTime,i))


        time = 0
        res = []

        while pending or available:
            while pending and pending[0][0] <= time:
                eqTime , prTime, i = heapq.heappop(pending)
                heapq.heappush(available , (prTime, i))
            
            if not available:
                time = pending[0][0]
                continue
            
            prTime , i = heapq.heappop(available)
            time += prTime
            res.append(i)
        
        return res