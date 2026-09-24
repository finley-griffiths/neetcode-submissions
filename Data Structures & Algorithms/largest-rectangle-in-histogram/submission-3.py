class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
            elif stack[-1][0] <= heights[i]:
                stack.append((h, i))
            else:
                while stack and stack[-1][0] > heights[i]:
                    rectangle = stack.pop(-1)
                    area = rectangle[0] * (i - rectangle[1])
                    if area > best:
                        best = area
                stack.append((heights[i], rectangle[1]))

        while stack:
            rectangle = stack.pop(-1)
            area = rectangle[0] * (len(heights) - rectangle[1])
            if area > best:
                best = area
        return best