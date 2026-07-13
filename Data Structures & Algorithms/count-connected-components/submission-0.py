class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * n
        com = 0

        def dfs(node):
            for neig in adj[node]:
                if not visit[neig]:
                    visit[neig] = True
                    dfs(neig)
        
        
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                com +=1
        
        return com
