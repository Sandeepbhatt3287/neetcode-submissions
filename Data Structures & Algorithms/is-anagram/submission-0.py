class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sl = len(s)
        tl = len(t)

        if sl != tl:
            return False

        hashs = {}
        hasht ={}

        for i in range(sl):

            hashs[s[i]] = 1 + hashs.get(s[i],0)
            hasht[t[i]] = 1 + hasht.get(t[i],0)
        
        return hasht == hashs
        