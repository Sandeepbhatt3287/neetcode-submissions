class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        ind = [0] * (n+1)
        outd = [0] * (n+1)

        for start,end in trust:
            outd[start] +=1
            ind[end] +=1
        
        for i in range(1,n+1):
            if outd[i] ==0 and ind[i] == n-1:
                return i
            
        return -1
        
        