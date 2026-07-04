class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for c in t:
            counter[c] -= 1
        
        return all( v == 0 for v in counter.values())