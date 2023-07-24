class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current = (min(height[left], height[right]) * (right - left))
        currMax = current

        while left < right:
            current = (min(height[left],height[right]) * (right - left))
            currMax = max(current, currMax)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return currMax