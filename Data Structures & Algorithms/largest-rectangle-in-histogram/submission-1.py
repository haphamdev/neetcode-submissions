class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        rightBorders = [0] * length
        leftBorders = [0] * length

        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftBorders[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
            
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            rightBorders[i] = stack[-1] - 1 if stack else length - 1
            stack.append(i)

        areas = [0] * length

        for i in range(length):
            areas[i] = heights[i] * (rightBorders[i] - leftBorders[i] + 1)

        return max(areas)