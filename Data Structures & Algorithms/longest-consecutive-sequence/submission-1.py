class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        d = {}
        for n in nums:
            if n in d: continue
            prev = d[n-1] if n-1 in d else 0
            next = d[n+1] if n+1 in d else 0
            d[n] = prev + next + 1
            i = n - 1
            while i in d: 
                d[i] = d[n]
                i -= 1
            i = n + 1
            while i in d:
                d[i] = d[n]
                i += 1
            
        return max(d.values())
