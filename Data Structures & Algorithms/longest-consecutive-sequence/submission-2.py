class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        seen = set()
        longest = 0

        for n in nums:
            if n in seen: continue
            if n - 1 in s: continue
            i = n
            count = 0
            while i in s:
                seen.add(i)
                count += 1 
                i += 1
            longest = max(longest, count)
        
        return longest
