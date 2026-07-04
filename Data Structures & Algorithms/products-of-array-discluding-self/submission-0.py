class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a = [1] * l
        prev = 1
        for i in range(1,l):
            p = prev * nums[i-1]
            a[i] = p
            prev = p
        
        b = [1] * l
        prev = 1
        for i in range(l-2, -1, -1):
            p = prev * nums[i+1]
            b[i] = p
            prev = p
        

        result = [1] * l
        for i in range(l):
            result[i] = a[i] * b[i]
        
        return result