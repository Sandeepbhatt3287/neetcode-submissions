class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openb,close):
            if openb == close == n:
                res.append("".join(stack))
                return
            
            if openb<n:
                stack.append("(")
                dfs(openb +1 ,close)
                stack.pop()
            
            if close < openb:
                stack.append(")")
                dfs(openb, close+1)
                stack.pop()
        
        dfs(0,0)

        return res
        