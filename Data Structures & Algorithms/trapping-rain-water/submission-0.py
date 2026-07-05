class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftPeaks = [0] * length
        currentMax = 0
        for i in range(length):
            currentMax = max(currentMax, height[i])
            leftPeaks[i] = currentMax
        
        rightPeaks = [0] * length
        currentMax = 0
        for i in range(length-1, -1, -1):
            currentMax = max(currentMax, height[i])
            rightPeaks[i] = currentMax


        vols= []
        for i in range(length):
            vols.append(min(leftPeaks[i], rightPeaks[i]) - height[i])
        
        return sum(vols)


        