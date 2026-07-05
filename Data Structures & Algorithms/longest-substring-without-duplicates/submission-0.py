class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        subLength = 0

        for i,c in enumerate(s):
            if c in s[start:i]:
                while c != s[start]:
                    start += 1
                start += 1
            subLength = max(subLength, i-start+1)
            
        return subLength