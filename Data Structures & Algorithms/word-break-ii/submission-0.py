class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        slen = len(s)
        res = []

        dic = set(wordDict)



        def back(i):

            if i == len(s):
                res.append(" ".join(cur))
                return
            

            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    back(j+1)
                    cur.pop()
        
        cur = []
        res = []
        back(0)
        return res
            

            

    