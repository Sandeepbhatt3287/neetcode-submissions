class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])

        far = 0

        while queue:
            indx = queue.popleft()

            start = max(indx + minJump , far +1)

            for j in range(start , min(indx + maxJump + 1 , len(s))):
                if s[j] == "0":
                    queue.append(j)
                    if j == len(s) -1:
                        return True
            
            far = indx + maxJump
        
        return False