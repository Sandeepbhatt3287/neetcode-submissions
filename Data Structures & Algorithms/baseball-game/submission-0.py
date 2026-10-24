class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stk = []
        res = 0
        n = len(operations)

        for i in range(n):

            if operations[i] == "+":
                stk.append(stk[-1] + stk[-2])
            elif operations[i] == "C":
                stk.pop()     
            elif operations[i] == "D":
                stk.append(2*stk[-1])
            else:
                stk.append(int(operations[i]))
        
        while stk:
            res +=stk.pop()

        return res

