# Last updated: 9/3/2026, 10:37:44 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        water=0
        while low<high:
            score=min(height[low],height[high])*abs(high-low)
            # print(height[low],height[high],abs(high-low),min(height[low],height[high])*abs(high-low))
            water=max(score,water)
            if min(height[high],height[low])==height[low]:
                low+=1
            else:
                high-=1
        return water