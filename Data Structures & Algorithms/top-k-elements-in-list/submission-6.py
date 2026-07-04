from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        maxFreq = 0
        for n in nums:
            if n in counter: counter[n] += 1
            else: counter[n] = 1
            if counter[n] > maxFreq: maxFreq = counter[n]

        groupedByCount = {}

        for n in counter:
            if counter[n] in groupedByCount:
                groupedByCount[counter[n]].append(n)
            else:
                groupedByCount[counter[n]] = [n]
        
        i = maxFreq
        c = 0
        result = []

        while c < k:
            if i in groupedByCount:
                result += groupedByCount[i]
                c += len(groupedByCount[i])
            i -= 1

        return result

        
        