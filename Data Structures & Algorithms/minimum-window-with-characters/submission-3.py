from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t) 
        l = r = 0
        result = None
        while r < len(s):
            currentCharCounter = Counter(s[l:r+1])

            if all(currentCharCounter[c] >= counterT[c] for c in counterT):
                subString = s[l:r+1]
                if not result or len(result) > len(subString): 
                    result = subString
                l += 1
            else:
                r += 1

            
        return result if result else ''