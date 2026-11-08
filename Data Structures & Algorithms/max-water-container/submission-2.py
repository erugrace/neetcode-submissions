class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float('-inf')
        left = 0
        right = len(heights) -1
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(area, maxArea)
        return maxArea
        

            