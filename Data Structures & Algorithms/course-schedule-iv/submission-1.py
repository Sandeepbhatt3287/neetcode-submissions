class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:

        # reach[u][v] is true once u is known to be a prerequisite of v
        reach = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            reach[u][v] = True

        # transitive closure, mid is the course the chain passes through
        for mid in range(numCourses):
            for u in range(numCourses):
                # nothing reaches mid from u, so no chain can route through it
                if not reach[u][mid]:
                    continue

                for v in range(numCourses):
                    if reach[mid][v]:
                        reach[u][v] = True

        res = []
        for u, v in queries:
            res.append(reach[u][v])

        return res