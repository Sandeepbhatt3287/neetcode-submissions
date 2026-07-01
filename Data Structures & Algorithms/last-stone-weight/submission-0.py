class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh = [-x  for x in stones]

        heapq.heapify(maxh)


        while len(maxh) >1:

            first = -heapq.heappop(maxh)
            sec = -heapq.heappop(maxh)

            if first != sec:
                heapq.heappush(maxh, -(first -sec))

        
        return -maxh[0] if maxh else 0


        