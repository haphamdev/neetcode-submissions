class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        orda = ord('a')

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - orda] += 1
            
            res.setdefault(tuple(key), []).append(s)
        
        return res.values()
