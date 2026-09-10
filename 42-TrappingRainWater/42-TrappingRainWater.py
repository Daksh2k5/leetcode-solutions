# Last updated: 9/10/2026, 3:53:38 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        water=0
4        peak=height[0]
5        p=height.index(max(height))
6        lh=height[:p+1:]
7        rh=height[p::]
8        rh=rh[::-1]
9        for i in lh:
10            peak=max(peak,i)
11            water+=peak-i
12        peak=rh[0]
13        for i in rh:
14            peak=max(peak,i)
15            water+=peak-i
16        return water