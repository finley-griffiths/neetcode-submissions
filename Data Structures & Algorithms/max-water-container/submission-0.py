class Solution:
    def maxArea(self, heights: List[int]) -> int:
        li = 0
        ri = len(heights) - 1
        largest_seen = 0
        while li < ri:
            area = min(heights[li], heights[ri]) * (ri - li)
            if area > largest_seen:
                largest_seen = area
            if heights[li] > heights[ri]:
                ri -= 1
            else:
                li += 1
        return largest_seen