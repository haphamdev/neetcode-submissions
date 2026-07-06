class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)

        l, r = 1, mx

        result = mx
        while l <= r:
            m = (l + r) // 2

            time = sum(math.ceil(p/m) for p in piles)

            if time <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        
        return result