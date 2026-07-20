class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj ={}
        for src,dst in sorted(tickets)[::-1]:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        

        res = []

        def dfs(src):
            while src in adj and adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")

        return res[::-1]