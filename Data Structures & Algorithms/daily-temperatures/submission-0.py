class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        n = len(temperatures)
        cur =0

        for i in range(n):
            cur = 0
            found_warmer = False
            for j in range(i+1,n):
                cur +=1
                if temperatures[i] < temperatures[j]:
                    res.append(cur)
                    
                    found_warmer = True
                    break
            if not found_warmer:
                res.append(0)

        
        return res
