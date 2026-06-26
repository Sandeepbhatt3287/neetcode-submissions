class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()

        n = len(s)

        l =0

        res = 0

        for i in range(n):
            while s[i] in visit:
                visit.remove(s[l])
                l +=1
            visit.add(s[i])

            res = max(res, i-l +1) 
        return res
        