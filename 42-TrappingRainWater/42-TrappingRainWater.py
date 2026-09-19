# Last updated: 9/10/2026, 3:53:38 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        peak=height[0]
        p=height.index(max(height))
        lh=height[:p+1:]
        rh=height[p::]
        rh=rh[::-1]
        for i in lh:
            peak=max(peak,i)
            water+=peak-i
        peak=rh[0]
        for i in rh:
            peak=max(peak,i)
            water+=peak-i
        return water