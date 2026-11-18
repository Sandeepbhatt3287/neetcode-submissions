class Solution:
    def makesquare(self, m: List[int]) -> bool:
        summ = sum(m)

        if summ%4 !=0:
            return False
        
        sides =[0] *4

        def dfs(i):
            if i == len(m):
                return sides[0] == sides[1]==sides[2] ==sides[3]

            
            for side in range(4):
                sides[side] += m[i]

                if dfs(i+1):
                    return True
                
                sides[side] -= m[i]
            
            return False
        
        return dfs(0)
