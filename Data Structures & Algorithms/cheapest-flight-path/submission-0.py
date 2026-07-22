class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        for i in range(k+1):

            tmp_dist = dist.copy()

            for flight in flights:
                s,d,p = flight
            
                if dist[s] != float('inf') and dist[s] + p < tmp_dist[d]:
                      
                    tmp_dist[d] = dist[s] + p
            dist = tmp_dist
        return dist[dst] if dist[dst] != float('inf') else -1