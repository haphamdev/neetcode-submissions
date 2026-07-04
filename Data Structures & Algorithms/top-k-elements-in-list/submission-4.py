from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            if n in counter: counter[n] += 1
            else: counter[n] = 1
        
        print(f'counter: {counter}')
        heap = []
        for n in counter:
            count = counter[n]
            if len(heap) == k:
                if count >= heap[0][0]:
                    heappop(heap)
                    heappush(heap, (count,n))
            else:
                heappush(heap, (count,n))

        result = []
        for i in heap:
            result.append(i[1])
        return result