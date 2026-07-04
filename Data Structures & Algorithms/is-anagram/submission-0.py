class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        check = [0] * 26
        for i in range(len(s)):
            check[ord(s[i])-ord('a')] += 1
            check[ord(t[i])-ord('a')] -= 1
        
        return not any(check)