class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -1 
        left,right = 0, len(heights) - 1
        while left < right:
            maxArea = max(min(heights[left], heights[right]) * (right - left), maxArea)

            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
                
        return maxArea  