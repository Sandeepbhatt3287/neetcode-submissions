class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        for u,v,w in times:
            adj[u].append((v,w))

        minHeap = [(0,k)]
        seen = set()
        t = 0


        while minHeap:
            w1,n1 = heapq.heappop(minHeap)

            if n1 in seen:
                continue
            seen.add(n1)
            t = max(w1,t)

            for n2,w2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap,(w1+w2,n2))
        
        return t if len(seen)==n else -1

        