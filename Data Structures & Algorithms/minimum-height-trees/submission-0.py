class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(start):
            visited = set()
            visited.add(start)

            stack = [(start,0)]
            tallest =0

            while stack:
                node,depth = stack.pop()

                if depth > tallest:
                    tallest = depth

                for neig in adj[node]:
                    if neig not in visited:
                        visited.add(neig)
                        stack.append((neig, depth + 1))
                
            return tallest
        
        best = n
        res = []

        for i in range(n):
            tallest = dfs(i)

            # a new winner clears the previous answers
            if tallest < best:
                best = tallest
                res = [i]
            elif tallest == best:
                res.append(i)

        return res

