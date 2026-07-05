from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        i = 0
        currentMax = nums[i]
        heap = []
        result = []

        while i < k:
            heappush(heap, (-nums[i],i))
            i += 1

        result.append(-heap[0][0])

        while i < length:
            heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heappop(heap)
            result.append(-heap[0][0])
            i += 1
        return result