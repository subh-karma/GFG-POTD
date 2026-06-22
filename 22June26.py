class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if height[i] <= height[j]:
                h = height[i]
                i += 1
            else:
                h = height[j]
                j -= 1
            max_area = max(max_area, (j - i) * h)
        return max_area
        # code here
        
