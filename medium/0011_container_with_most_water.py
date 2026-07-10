"""You are given an integer array height of length n. There 
are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

class Solution(object):
    def maxArea(self, height):
        mx = 0
        cnt1 = 0
        cnt2 = len(height) -1
        while cnt1 < cnt2:
            area = min(height[cnt1], height[cnt2]) * (cnt2-cnt1)
            mx = max(mx, area)
            if height[cnt1] > height[cnt2]:
                cnt2 -= 1
            else:
                cnt1 += 1
        return mx