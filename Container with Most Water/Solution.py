class Solution:
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        
        first_bar = height[0]
        second_bar = height[-1]
        area = min(first_bar, second_bar) * (len(height) - 1)
        gap = abs(0 - (len(height) - 1))


        for i in range(0,len(height)):
            curr = height[i] 
            area1 = min(first_bar, curr) * abs(height.index(first_bar) - i)
            area2 = min(second_bar, curr) * abs(height.index(second_bar) - i)
            if area1 > area:
                second_bar = curr
                area = area1
            elif area2 > area:
                first_bar = curr
                area = area2
            elif curr > first_bar:
                first_bar = curr
            elif curr > second_bar:
                second_bar = curr

        return area
