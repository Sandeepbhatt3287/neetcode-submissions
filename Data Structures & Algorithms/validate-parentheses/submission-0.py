class Solution:
    def isValid(self, s: str) -> bool:

        bac ={ "}": "{" , "]": "[" , ")":"("}
        
        st = []


        for c in s:
            if c in bac:
                if st and st[-1] == bac[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True if not st else False