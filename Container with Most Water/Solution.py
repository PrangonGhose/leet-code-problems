class Solution:
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        
        first_bar = 0
        second_bar = len(height) - 1
        area = min(height[first_bar], height[second_bar]) * (len(height) - 1)

        for i in range(1,len(height)):
            area1 = min(height[first_bar], height[i]) * abs(first_bar - i)
            area2 = min(height[second_bar], height[i]) * abs(second_bar - i)
            if area1 > area:
                second_bar = i
                area = area1
            elif area2 > area:
                first_bar = i
                area = area2
            elif area1 < area and area2 < area and height[i] > height[first_bar]:
                first_bar = i
            elif area2 < area and area1 < area and height[i] > height[second_bar]:
                second_bar = i

        return area
