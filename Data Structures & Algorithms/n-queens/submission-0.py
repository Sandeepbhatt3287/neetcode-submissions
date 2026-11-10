class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False] * n
        posDia = [False]* (n*2)
        negDia = [False] * (n*2)

        res = []

        board = [["."] * n for i in range(n)]


        def backtrack(r):

#  agar solution mil gaya store kr liya
            if r ==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            

            # sab row and col check kiye
            for c in range(n):

                #  agar True hai sab jaga toh skip kr diya
                if col[c] or posDia[r+c] or negDia[r -c +n]:
                    continue
                
                # agar position safe hai toh put it
                col[c] = True
                posDia[r+c] = True
                negDia[r-c+n] = True
                board[r][c] = "Q"


                backtrack(r+1)

                #  ab backtrack kare ge if not found

                col[c] = False
                posDia[r+c] = False
                negDia[r -c + n] = False
                board[r][c] = "."


        backtrack(0)

        return res


