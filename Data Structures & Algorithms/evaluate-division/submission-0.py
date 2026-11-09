class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = {}

        for i in range(len(equations)):
            a, b = equations[i]

            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []

            # a / b is the given value, so b / a is its reciprocal
            adj[a].append((b, values[i]))
            adj[b].append((a, 1.0 / values[i]))


        def dfs(src,target, visited):
            if src not in adj or target not in adj:
                return -1
            
            if src == target:
                return 1
            
            visited.add(src)

            for nei, weight in adj[src]:
                if nei  not in visited:
                    result = dfs(nei,target,visited)
                    if result != -1:
                        return weight * result
            
            return -1
        
        res = []

        for query in queries:
            src, target = query

            # an unknown variable has no answer, even against itself
            if src not in adj or target not in adj:
                res.append(-1.0)
            else:
                res.append(dfs(src, target, set()))

        return res

