class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def palin(l,r):

            while l<r:
                if s[l] != s[r]:
                    return False

                l +=1
                r -=1
            return True
    

        lo, hi = 0 , len(s)-1

        while lo<hi:

            if s[lo] != s[hi]:
                return palin(lo+1,hi) or palin(lo,hi-1)
            
            lo +=1
            hi -=1
        
        return True


        