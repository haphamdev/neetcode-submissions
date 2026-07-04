class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(numbers):
            if n in seen:
                return [seen[n]+1, i+1]
            seen[target-n] = i
        return []