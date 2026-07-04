class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count: count[n] += 1
            else: count[n] = 1
        group = []
        for i in range(len(nums) + 1):
            group.append([])

        for n,c in count.items():
            group[c].append(n)
        print(group)
        i = len(group) - 1
        res = []
        while len(res) < k:
            res.extend(group[i])
            i -= 1
        
        return res
        

