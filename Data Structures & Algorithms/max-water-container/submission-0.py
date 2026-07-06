class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            cal = (R-L) * min(heights[R], heights[L])
            result = max(result, cal)

            if heights[L] < heights[R]:
                L  += 1
            else:
                R -= 1
        return result