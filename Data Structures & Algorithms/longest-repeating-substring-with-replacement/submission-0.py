class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        l, r = 0, 0
        f = {}
        maxF = 0
        maxSubLen = 0

        while r < length:
            f[s[r]] = f[s[r]] + 1 if s[r] in f else 1
            maxF = max(maxF, f[s[r]])

            while r - l + 1 - maxF > k:
                f[s[l]] -= 1 
                maxF = max(maxF, f[s[l]])
                l += 1

            maxSubLen = max(r - l + 1, maxSubLen)
            r += 1
        
        return maxSubLen