class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        
        # 1. Build the target dictionary
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        # FIXED: Moved outside the loop
        have, need = 0, len(countT)
        
        # FIXED: Initialize variables to track the best window
        res, resLen = [-1, -1], float('infinity') 
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # FIXED: Used == instead of =
            if c in countT and window[c] == countT[c]:
                have += 1
                
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1) # FIXED: changed 1 to l
                    
                # Pop from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        # FIXED: Added the return statement to slice the string using 'res'
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""