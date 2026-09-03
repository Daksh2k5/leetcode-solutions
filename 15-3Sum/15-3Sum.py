# Last updated: 9/3/2026, 10:36:35 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        low=0
4        high=len(height)-1
5        water=0
6        while low<high:
7            score=min(height[low],height[high])*abs(high-low)
8            # print(height[low],height[high],abs(high-low),min(height[low],height[high])*abs(high-low))
9            water=max(score,water)
10            if min(height[high],height[low])==height[low]:
11                low+=1
12            else:
13                high-=1
14        return water