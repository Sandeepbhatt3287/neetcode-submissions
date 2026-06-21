class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        ed = collections.defaultdict(list)

        for u,v,w in edges:
            ed[u].append((v,w))

        # visit = set()
        t ={}

        minHeap=[(0,src)]

        while minHeap:
            wei1, node1  = heapq.heappop(minHeap)

            if node1 in t:
                continue
            
            t[node1]=wei1

            for node2 , wei2 in ed[node1]:
                if node2 not in t:
                    heapq.heappush(minHeap,[wei1+wei2,node2])
        
        for i in range(n):
            if i not in t:
                t[i]=-1
        
        return t


