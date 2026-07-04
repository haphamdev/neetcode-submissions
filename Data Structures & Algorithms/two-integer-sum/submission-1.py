class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i,n in enumerate(nums):
            if n in found: return [found[n], i]
            found[target - n] = i
        return False