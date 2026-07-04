class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        length = len(nums)
        i = 0
        result = set()
        while i < length - 2:
            if i>0 and nums[i] == nums[i-1]: 
                i += 1
                continue
            l, r = i+1, length-1
            target = -nums[i]

            while l < r:
                sum = nums[l] + nums[r]
                if sum == target and (nums[i], nums[l], nums[r]) not in result: result.add((nums[i], nums[l], nums[r]))
                if sum < target:
                    l += 1
                else:
                    r -= 1
            i += 1
        res = []
        for triple in result:
            res.append(list(triple))
        return res
