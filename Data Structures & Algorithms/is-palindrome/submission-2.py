class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [char.lower() for char in s if char.isalnum()]

        n = len(new)-1
        left = 0

        while left<=n:

            if new[left] != new[n]:
                return False
            
            left+=1
            n -=1
        

        return True
