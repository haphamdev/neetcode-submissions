from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        print(f'freq: {freq}')
        l = len(s1)
        i = 0
        currentFreq = Counter(s2[i:i+l-1])

        while i <= len(s2) - l:
            currentFreq[s2[i+l-1]] += 1
            if currentFreq == freq: return True
            currentFreq[s2[i]] -= 1
            i += 1

        return False