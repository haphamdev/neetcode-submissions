from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = Counter(t) 
        required = len(freqT)
        l = r = 0
        result = None
        currentCharCounter = Counter(s[0])
        currentMatch = 1 if s[0] in freqT and freqT[s[0]] == 1 else 0
        while r < len(s):
            if currentMatch == required:
                subString = s[l:r+1]
                if not result or len(result) > len(subString): 
                    result = subString
                currentCharCounter[s[l]] -= 1
                if s[l] in freqT and currentCharCounter[s[l]] == freqT[s[l]] - 1:
                    currentMatch -= 1
                l += 1
            else:
                r += 1
                if r < len(s): 
                    currentCharCounter[s[r]] += 1
                    if s[r] in freqT and currentCharCounter[s[r]] == freqT[s[r]]:
                        currentMatch += 1

            
        return result if result else ''